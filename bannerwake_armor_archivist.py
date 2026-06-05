#!/usr/bin/env python3
"""
Bannerwake Armor Archivist v3
==============================
External data + visual archive builder for Mount & Blade II: Bannerlord armor items.
Target: Bannerlord beta v1.4.5 + War Sails/NavalDLC v1.2.5 (private Bannerwake overhaul).

What it does:
  - Scans one or more Bannerlord module folders for XML <Item> records.
  - Extracts armor, shield, and horse-armor data.
  - Detects UseTeamColor support with multi-pass heuristics.
  - Generates:
      catalog/armor_catalog.csv
      catalog/armor_catalog.json
      catalog/capture_queue.json
      catalog/capture_queue.tsv        (consumed by the in-game AutoCapture module)
      reports/archive_summary.md
      reports/armor_by_module.md
      reports/armor_by_culture.md
      reports/recolor_candidates.md
      reports/armor_missing_screenshots.md
      gallery/armor_gallery.html       (self-contained, filterable, dark-themed)

No Bannerlord DLLs required. Python 3.10+ recommended. Zero third-party packages.

Changes from v2 (ChatGPT build):
  - Overhauled XML scan: iterates all <Item> children correctly; handles Bannerlord's
    nested ItemComponent/Armor/Weapon/Flags structure without missing items.
  - UseTeamColor detection is a proper 3-pass check (flags node, root attrs, XML text).
  - Slot inference is priority-ordered and handles Shoulder/Cape properly.
  - Faction colour-hint matching uses culture field first, then text scan.
  - Duplicate handling: same item_id from same module+xml is deduplicated;
    cross-module duplication is KEPT (intentional: mods often override vanilla items).
  - HTML gallery: cards now show all screenshot views; screenshot viewer cycles
    front/side/back on click; cards highlight recolor priority visually.
  - Capture queue TSV now includes a 'resume_from' index comment and is
    written atomically (write-then-rename) so a crash never produces a corrupt queue.
  - link-screenshots command prints a progress bar and verifies file count before writing.
  - export-autocapture merges directly from armor_catalog.json so you can
    re-export without re-scanning.
  - All file writes use write-then-rename (atomic) to prevent half-written files.
  - New 'stats' command: quick summary printed to stdout, no file I/O.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html as _html
import json
import os
import re
import shutil
import sys
import tempfile
import traceback
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

ARMOR_TYPES = {
    "HeadArmor", "BodyArmor", "Cape", "Shoulder",
    "HandArmor", "LegArmor", "HorseHarness", "HorseArmor", "Shield",
}

SLOT_ORDER: Dict[str, int] = {
    "HeadArmor": 10, "BodyArmor": 20, "Cape": 30, "Shoulder": 31,
    "HandArmor": 40, "LegArmor": 50, "HorseHarness": 60, "HorseArmor": 61,
    "Shield": 70, "UnknownArmor": 99,
}

# XML sub-directories we never need to parse for item data
SKIP_DIR_KEYWORDS = {
    "languages", "language", "voice", "voices", "music", "sound", "sounds",
    "atmospheres", "prefabs", "gui", "particles", "shaders", "physics",
}

# Bannerwake faction colour palette (XML implementation colours)
FACTION_COLORS: Dict[str, Tuple[str, str]] = {
    "sturgia":   ("FF1C2A50", "FF949CCC"),
    "vlandia":   ("FF5C2017", "FFECBA44"),
    "battania":  ("FF2D3F1D", "FFBFCBB0"),
    "aserai":    ("FF965228", "FF4F2212"),
    "khuzait":   ("FF468C7C", "FFCCBB89"),
    "empire":    ("owner-dependent", "purple/gold variants"),
    "nord":      ("FF202931", "FFb7623c"),
    "pirate":    ("tar-black/charcoal", "dead sea-brown/corroded iron"),
}

# Words that anchor a text scan to a faction bucket
FACTION_KEYWORDS: Dict[str, List[str]] = {
    "sturgia":  ["sturgia", "sturgian"],
    "vlandia":  ["vlandia", "vlandian", "swadian"],
    "battania": ["battania", "battanian", "battan"],
    "aserai":   ["aserai", "mamluk", "arab", "maml"],
    "khuzait":  ["khuzait", "steppe", "mongol", "nomad"],
    "empire":   ["empire", "imperial", "legionary"],
    "nord":     ["nord", "nordic", "norseman", "norse", "viking"],
    "pirate":   ["pirate", "raider", "sea_raider", "corsair", "buccaneer", "black_keel"],
}

KNOWN_VANILLA_MODULES = {
    "native", "sandbox", "sandboxcore", "storymode", "custombattle", "navaldlc",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def now_stamp() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[1] if "}" in tag else tag

def norm_key(s: Optional[str]) -> str:
    if not s:
        return ""
    return re.sub(r"[^a-z0-9]+", "_", s.lower().strip()).strip("_")

def clean_display_name(raw: Optional[str]) -> str:
    """Strip Bannerlord's {=abc123} text-ID prefix."""
    if not raw:
        return ""
    return re.sub(r"^\{=[^}]+\}", "", raw).strip()

def boolish(value: Optional[str]) -> Optional[bool]:
    if value is None:
        return None
    v = value.strip().lower()
    if v in {"true", "1", "yes"}:
        return True
    if v in {"false", "0", "no"}:
        return False
    return None

def nblanked(value: Optional[str]) -> str:
    return "" if value is None else str(value)

def safe_rel(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")

def atomic_write_text(path: Path, text: str, encoding: str = "utf-8") -> None:
    """Write text atomically: write to a temp file then rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp_bw_")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(text)
        shutil.move(tmp, str(path))
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

def progress_bar(done: int, total: int, width: int = 40) -> str:
    if total == 0:
        return "[----------] 0/0"
    frac = done / total
    filled = int(frac * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {done}/{total} ({frac*100:.0f}%)"

# ---------------------------------------------------------------------------
# Module discovery
# ---------------------------------------------------------------------------

def discover_modules(
    roots: List[Path],
    include_modules: List[str],
    exclude_modules: List[str],
) -> List[Path]:
    include_norm = {norm_key(x) for x in include_modules if x.strip()}
    exclude_norm = {norm_key(x) for x in exclude_modules if x.strip()}
    found: Dict[str, Path] = {}

    for root in roots:
        if not root.exists():
            print(f"  [WARN] Modules root not found: {root}", file=sys.stderr)
            continue

        candidates: List[Path] = []
        if (root / "SubModule.xml").exists():
            candidates.append(root)
        else:
            try:
                for child in sorted(root.iterdir()):
                    if child.is_dir() and (child / "SubModule.xml").exists():
                        candidates.append(child)
            except PermissionError as exc:
                print(f"  [WARN] Permission denied: {root} — {exc}", file=sys.stderr)

        for mod_path in candidates:
            mod_key = norm_key(mod_path.name)
            if mod_key in exclude_norm:
                continue
            if include_norm:
                if mod_key not in include_norm and mod_path.name.lower() not in {
                    x.lower() for x in include_modules
                }:
                    continue
            found[mod_key] = mod_path

    return [found[k] for k in sorted(found.keys())]

def should_skip_xml(xml_path: Path) -> bool:
    parts_lower = {p.lower() for p in xml_path.parts}
    if parts_lower & SKIP_DIR_KEYWORDS:
        return True
    name = xml_path.name.lower()
    return any(kw in name for kw in ("language", "strings", "voice", "text", "gui_"))

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class ArmorRecord:
    item_id: str
    display_name_raw: str = ""
    display_name_clean: str = ""
    source_module: str = ""
    source_xml: str = ""

    # Classification
    item_type: str = ""
    slot: str = ""
    culture: str = ""

    # Mesh / material
    mesh: str = ""
    body_mesh: str = ""
    holster_mesh: str = ""
    multi_mesh: str = ""
    material: str = ""
    material_type: str = ""
    physics_material: str = ""

    # Item stats
    weight: str = ""
    value: str = ""
    difficulty: str = ""
    appearance: str = ""
    tier: str = ""
    modifier_group: str = ""
    item_usage: str = ""
    is_merchandise: str = ""

    # Flags
    use_team_color: str = "UNKNOWN"
    civilian: str = ""
    multiplayer_item: str = ""
    cannot_be_picked_up: str = ""
    has_flags_node: str = ""
    raw_flag_names: str = ""

    # Armor values
    head_armor: str = ""
    body_armor: str = ""
    arm_armor: str = ""
    leg_armor: str = ""
    horse_armor: str = ""
    shield_hit_points: str = ""
    covers_body: str = ""
    covers_legs: str = ""

    # Bannerwake analysis
    visual_bucket: str = ""
    bannerwake_faction_colors: str = ""
    bannerwake_recolor_needed: str = "UNKNOWN"
    recolor_reason: str = ""

    # Screenshots (filled by ScreenshotLinker)
    screenshot_front: str = ""
    screenshot_side: str = ""
    screenshot_back: str = ""
    screenshot_detail: str = ""

    notes: str = ""

    def sort_key(self) -> Tuple[str, int, str]:
        return (
            self.source_module.lower(),
            SLOT_ORDER.get(self.slot, 999),
            self.item_id.lower(),
        )

# ---------------------------------------------------------------------------
# XML scanner
# ---------------------------------------------------------------------------

class BannerlordXmlScanner:
    def __init__(
        self,
        module_paths: List[Path],
        out_dir: Path,
        include_all_xml: bool = False,
    ):
        self.module_paths = module_paths
        self.out_dir = out_dir
        self.include_all_xml = include_all_xml
        self.errors: List[str] = []
        self.records: List[ArmorRecord] = []

    # ------------------------------------------------------------------ scan

    def scan(self) -> List[ArmorRecord]:
        print(f"\n[SCAN] {len(self.module_paths)} module(s) to scan...")
        for i, mod_path in enumerate(self.module_paths, 1):
            print(f"  [{i}/{len(self.module_paths)}] {mod_path.name}")
            self._scan_module(mod_path)

        # Deduplicate: keep first occurrence per (module, item_id, source_xml).
        # Cross-module duplicates are intentionally KEPT — mods override vanilla.
        seen: Dict[Tuple[str, str, str], ArmorRecord] = {}
        for r in self.records:
            key = (r.source_module, r.item_id, r.source_xml)
            if key not in seen:
                seen[key] = r
        self.records = sorted(seen.values(), key=lambda r: r.sort_key())
        print(f"\n[SCAN] Total armor/shield records: {len(self.records)}")
        if self.errors:
            print(f"[SCAN] XML parse errors: {len(self.errors)} (see reports/archive_summary.md)")
        return self.records

    def _scan_module(self, module_path: Path) -> None:
        xml_files = [
            p for p in module_path.rglob("*.xml")
            if not (should_skip_xml(p) and not self.include_all_xml)
        ]
        found = 0
        for xml_path in xml_files:
            before = len(self.records)
            self._scan_xml(module_path, xml_path)
            found += len(self.records) - before
        print(f"       {len(xml_files)} XML files → {found} records")

    def _scan_xml(self, module_path: Path, xml_path: Path) -> None:
        try:
            tree = ET.parse(str(xml_path))
            root = tree.getroot()
        except ET.ParseError as exc:
            self.errors.append(f"XML parse: {xml_path} :: {exc}")
            return
        except Exception as exc:
            self.errors.append(f"File error: {xml_path} :: {exc}")
            return

        # Bannerlord item XMLs have a root like <Items> with <Item> children,
        # but sometimes items are nested further. We iterate the whole tree.
        for elem in root.iter():
            if strip_ns(elem.tag) == "Item":
                rec = self._parse_item(module_path, xml_path, elem)
                if rec is not None:
                    self.records.append(rec)

    # -------------------------------------------------------------- item parse

    def _parse_item(
        self,
        module_path: Path,
        xml_path: Path,
        item: ET.Element,
    ) -> Optional[ArmorRecord]:
        attrs = item.attrib
        item_id = attrs.get("id") or attrs.get("ID") or attrs.get("Id")
        if not item_id:
            return None

        item_type = (
            attrs.get("Type") or attrs.get("type") or
            attrs.get("subtype") or ""
        )

        # Collect sub-elements
        armor_elem: Optional[ET.Element] = None
        weapon_elem: Optional[ET.Element] = None
        flags_elem: Optional[ET.Element] = None
        flag_names: List[str] = []
        extra: Dict[str, str] = {}  # mesh/material attrs from nested nodes

        for child in item.iter():
            tag = strip_ns(child.tag)
            if tag == "Armor":
                armor_elem = child
            elif tag == "Weapon":
                weapon_elem = child
            elif tag == "Flags" or tag == "ItemFlags":
                flags_elem = child
                for k, v in child.attrib.items():
                    b = boolish(v)
                    if b is True:
                        flag_names.append(k)
            # Accumulate mesh/material attrs from any nested node
            for k, v in child.attrib.items():
                if k.lower() in {
                    "mesh", "body_mesh", "holster_mesh", "multi_mesh",
                    "material", "material_type", "physics_material",
                    "modifier_group", "item_usage",
                }:
                    extra.setdefault(k, v)

        # Detect shields: weapon items with shield weapon_class
        is_shield = False
        if weapon_elem is not None:
            wc = (
                weapon_elem.attrib.get("weapon_class", "") or
                weapon_elem.attrib.get("WeaponClass", "")
            ).lower()
            is_shield = "shield" in wc or "shield" in item_type.lower()

        # Filter: must be armor-type or shield
        armor_attrs = armor_elem.attrib if armor_elem is not None else {}
        if armor_elem is None and not is_shield:
            if item_type not in ARMOR_TYPES:
                return None

        slot = self._infer_slot(item_type, attrs, armor_attrs, is_shield)
        if slot == "UnknownArmor" and not is_shield and not armor_elem:
            return None

        use_team_color = self._detect_team_color(
            attrs, flags_elem, flag_names, item
        )
        culture = (
            attrs.get("culture", "") or attrs.get("Culture", "")
        ).replace("Culture.", "")

        bucket, faction_colors, recolor, reason = self._classify(
            item_id=item_id,
            name=attrs.get("name", ""),
            source_module=module_path.name,
            culture=culture,
            item_type=item_type,
            use_team_color=use_team_color,
        )

        def ga(key: str) -> str:
            return attrs.get(key) or attrs.get(key.lower()) or ""

        def ae(key: str) -> str:
            return armor_attrs.get(key, "") or extra.get(key, "")

        return ArmorRecord(
            item_id=item_id,
            display_name_raw=ga("name"),
            display_name_clean=clean_display_name(ga("name")),
            source_module=module_path.name,
            source_xml=safe_rel(xml_path, module_path),
            item_type=item_type,
            slot=slot,
            culture=culture,
            mesh=ga("mesh") or extra.get("mesh", ""),
            body_mesh=ga("body_mesh") or extra.get("body_mesh", ""),
            holster_mesh=ga("holster_mesh") or extra.get("holster_mesh", ""),
            multi_mesh=ga("multi_mesh") or extra.get("multi_mesh", ""),
            material=ga("material") or extra.get("material", ""),
            material_type=ae("material_type"),
            physics_material=ga("physics_material") or extra.get("physics_material", ""),
            weight=nblanked(ga("weight")),
            value=nblanked(ga("value")),
            difficulty=nblanked(ga("difficulty")),
            appearance=nblanked(ga("appearance")),
            tier=nblanked(ga("tier") or ga("Tier")),
            modifier_group=ga("modifier_group") or extra.get("modifier_group", ""),
            item_usage=ga("item_usage") or extra.get("item_usage", ""),
            is_merchandise=nblanked(ga("is_merchandise")),
            use_team_color=use_team_color,
            civilian="true" if "Civilian" in flag_names else nblanked(ga("civilian")),
            multiplayer_item="true" if "MultiplayerItem" in flag_names else nblanked(ga("multiplayer_item")),
            cannot_be_picked_up="true" if "CannotBePickedUp" in flag_names else "",
            has_flags_node="true" if flags_elem is not None else "false",
            raw_flag_names=";".join(sorted(set(flag_names))),
            head_armor=nblanked(ae("head_armor")),
            body_armor=nblanked(ae("body_armor")),
            arm_armor=nblanked(ae("arm_armor")),
            leg_armor=nblanked(ae("leg_armor")),
            horse_armor=nblanked(ae("horse_armor")),
            shield_hit_points=nblanked(
                (weapon_elem.attrib.get("hit_points") if weapon_elem is not None else None)
                or extra.get("hit_points", "")
            ),
            covers_body=nblanked(ae("covers_body")),
            covers_legs=nblanked(ae("covers_legs")),
            visual_bucket=bucket,
            bannerwake_faction_colors=faction_colors,
            bannerwake_recolor_needed=recolor,
            recolor_reason=reason,
        )

    # ------------------------------------------------------------ slot inference

    def _infer_slot(
        self,
        item_type: str,
        attrs: Dict[str, str],
        armor_attrs: Dict[str, str],
        is_shield: bool,
    ) -> str:
        if is_shield:
            return "Shield"
        # Exact type match takes priority
        if item_type in ARMOR_TYPES:
            return "Cape" if item_type == "Shoulder" else item_type
        # Infer from armor stat values (most reliable secondary signal)
        ha = armor_attrs.get("head_armor", "")
        ba = armor_attrs.get("body_armor", "")
        aa = armor_attrs.get("arm_armor", "")
        la = armor_attrs.get("leg_armor", "")
        hoa = armor_attrs.get("horse_armor", "")
        if hoa:
            return "HorseArmor"
        if ha and not ba:
            return "HeadArmor"
        if ba:
            return "BodyArmor"
        if aa and not ba:
            return "HandArmor"
        if la and not ba:
            return "LegArmor"
        # Last resort: keyword scan on id+name+mesh
        text = " ".join([
            attrs.get("id", ""),
            attrs.get("name", ""),
            attrs.get("mesh", ""),
            attrs.get("body_mesh", ""),
        ]).lower()
        for kw, slot in [
            ("helmet", "HeadArmor"), ("helm", "HeadArmor"),
            ("coif", "HeadArmor"), ("cap", "HeadArmor"),
            ("boot", "LegArmor"), ("shoe", "LegArmor"), ("leg_", "LegArmor"),
            ("greave", "LegArmor"), ("sabatons", "LegArmor"),
            ("glove", "HandArmor"), ("gauntlet", "HandArmor"), ("hand_", "HandArmor"),
            ("cape", "Cape"), ("cloak", "Cape"), ("shoulder", "Cape"), ("mantle", "Cape"),
            ("lamellar", "BodyArmor"), ("mail", "BodyArmor"), ("robe", "BodyArmor"),
            ("tunic", "BodyArmor"), ("gambeson", "BodyArmor"), ("armor", "BodyArmor"),
            ("armour", "BodyArmor"), ("hauberk", "BodyArmor"),
        ]:
            if kw in text:
                return slot
        return "UnknownArmor"

    # --------------------------------------------------------- UseTeamColor detection

    def _detect_team_color(
        self,
        attrs: Dict[str, str],
        flags_elem: Optional[ET.Element],
        flag_names: List[str],
        item: ET.Element,
    ) -> str:
        # Pass 1: explicit flag in <Flags> node
        if "UseTeamColor" in flag_names:
            return "true"
        # Pass 2: top-level item attribute variants
        for k, v in attrs.items():
            if k.lower() in {"use_team_color", "useteamcolor", "use_tableau"}:
                b = boolish(v)
                if b is True:
                    return "true"
                if b is False:
                    return "false"
        # Pass 3: inside <Flags> node as attribute with boolean value
        if flags_elem is not None:
            for k, v in flags_elem.attrib.items():
                if "teamcolor" in k.lower() or "useteam" in k.lower():
                    b = boolish(v)
                    if b is True:
                        return "true"
                    if b is False:
                        return "false"
        # Pass 4: heuristic full-text scan (NavalDLC items sometimes store this differently)
        xml_text = ET.tostring(item, encoding="unicode").lower()
        if any(kw in xml_text for kw in ("useteamcolor", "use_team_color", "teamcolor", "bannercolor")):
            return "LIKELY"
        return "UNKNOWN"

    # --------------------------------------------------------- Bannerwake classification

    def _classify(
        self,
        item_id: str,
        name: str,
        source_module: str,
        culture: str,
        item_type: str,
        use_team_color: str,
    ) -> Tuple[str, str, str, str]:
        # Build search text from all identifiers
        text = norm_key(" ".join([item_id, name, source_module, culture, item_type]))

        # Culture field is authoritative; fall back to text scan
        bucket = "generic"
        culture_norm = norm_key(culture)

        # Check culture field first (most reliable)
        for faction, keywords in FACTION_KEYWORDS.items():
            if any(kw == culture_norm or kw in culture_norm for kw in keywords):
                bucket = faction
                break

        # Fall back to full-text scan if culture was empty or unrecognized
        if bucket == "generic":
            for faction, keywords in FACTION_KEYWORDS.items():
                if any(kw in text for kw in keywords):
                    bucket = faction
                    break

        # Pirate/Black Keel override: only for generic/nord/sturgia base buckets
        if bucket in {"generic", "nord", "sturgia"}:
            pirate_kw = FACTION_KEYWORDS["pirate"]
            if any(kw in text for kw in pirate_kw):
                bucket = "pirate"

        # Build color hint string
        if bucket in FACTION_COLORS:
            c1, c2 = FACTION_COLORS[bucket]
            faction_colors = f"{bucket}: {c1} / {c2}"
        else:
            faction_colors = ""

        # Determine recolor need
        reasons: List[str] = []
        if use_team_color == "true":
            recolor = "maybe_not"
            reasons.append(
                "UseTeamColor confirmed — dynamic color likely works. "
                "Test in-game before creating bw_ texture variant."
            )
        elif use_team_color == "LIKELY":
            recolor = "verify"
            reasons.append(
                "Dynamic color clue found in XML but not proven via explicit flag. "
                "Verify in-engine before deciding on bw_ variant."
            )
        else:
            recolor = "likely"
            reasons.append(
                "No UseTeamColor flag found — "
                "likely needs bw_ material/texture variant if faction-coloured."
            )

        if bucket == "pirate":
            recolor = "heavy"
            reasons.append(
                "Pirate/sea asset — candidate for Black Keel dark "
                "salt-weathered palette (tar black / charcoal / corroded iron)."
            )
        if bucket == "empire":
            reasons.append(
                "Empire tree: verify which sub-faction owns this item. "
                "Northern/Southern/Western Empire each need a distinct palette."
            )
        if norm_key(source_module) not in KNOWN_VANILLA_MODULES:
            reasons.append(
                f"External mod asset ({source_module}): "
                "verify permission/private-use notes and texture quality before use."
            )

        return bucket, faction_colors, recolor, " ".join(reasons)

# ---------------------------------------------------------------------------
# Screenshot linker
# ---------------------------------------------------------------------------

class ScreenshotLinker:
    def __init__(self, screenshot_roots: List[Path], out_dir: Path):
        self.out_dir = out_dir
        self.index: Dict[str, List[Path]] = {}
        for root in screenshot_roots:
            if root.exists():
                self._index_root(root)

    def _index_root(self, root: Path) -> None:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
                key = norm_key(path.stem)
                self.index.setdefault(key, []).append(path)

    def attach(self, records: List[ArmorRecord]) -> None:
        for r in records:
            candidates = self._find_candidates(r.item_id)
            views = self._classify_views(r.item_id, candidates)
            r.screenshot_front  = self._rel(views.get("front"))
            r.screenshot_side   = self._rel(views.get("side"))
            r.screenshot_back   = self._rel(views.get("back"))
            r.screenshot_detail = self._rel(views.get("detail"))

    def _find_candidates(self, item_id: str) -> List[Path]:
        needle = norm_key(item_id)
        result: List[Path] = []
        for key, paths in self.index.items():
            # Exact or starts-with match on normalised key
            if key == needle or key.startswith(needle + "_") or ("_" + needle + "_") in ("_" + key + "_"):
                result.extend(paths)
        return sorted(set(result), key=lambda p: str(p).lower())

    def _classify_views(
        self, item_id: str, paths: List[Path]
    ) -> Dict[str, Path]:
        views: Dict[str, Path] = {}
        for p in paths:
            k = norm_key(p.stem)
            if "front" in k and "front" not in views:
                views["front"] = p
            elif "side" in k and "side" not in views:
                views["side"] = p
            elif "back" in k and "back" not in views:
                views["back"] = p
            elif ("detail" in k or "close" in k) and "detail" not in views:
                views["detail"] = p
        # Fallback: first image → front
        if paths and "front" not in views:
            views["front"] = paths[0]
        return views

    def _rel(self, path: Optional[Path]) -> str:
        if not path:
            return ""
        return safe_rel(path, self.out_dir)

# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_csv(records: List[ArmorRecord], path: Path) -> None:
    fields = list(asdict(ArmorRecord(item_id="")).keys())
    lines = [",".join(fields)]
    for r in records:
        d = asdict(r)
        lines.append(",".join(
            '"' + str(d.get(f, "")).replace('"', '""') + '"'
            for f in fields
        ))
    atomic_write_text(path, "\n".join(lines), encoding="utf-8-sig")


def write_json(records: List[ArmorRecord], path: Path) -> None:
    atomic_write_text(
        path,
        json.dumps([asdict(r) for r in records], ensure_ascii=False, indent=2),
    )


def write_capture_queue_json(
    records: List[ArmorRecord], path: Path, views: List[str]
) -> None:
    queue = []
    for idx, r in enumerate(records, 1):
        base = norm_key(r.slot or "armor")
        queue.append({
            "order": idx,
            "item_id": r.item_id,
            "display_name": r.display_name_clean or r.display_name_raw,
            "source_module": r.source_module,
            "slot": r.slot,
            "culture": r.culture,
            "mesh": r.mesh or r.body_mesh,
            "views": {v: f"{base}__{r.item_id}__{v}.png" for v in views},
        })
    atomic_write_text(path, json.dumps(queue, ensure_ascii=False, indent=2))


def write_capture_queue_tsv(
    queue_json_path: Path,
    out_tsv: Path,
    views: List[str],
    limit: int = 0,
    slots: Optional[List[str]] = None,
    start_index: int = 1,
) -> int:
    """
    Writes the TSV consumed by the in-game BannerwakeArmorAutoCapture module.
    Returns the number of rows written.
    """
    data = json.loads(queue_json_path.read_text(encoding="utf-8"))
    allowed_slots = {norm_key(x) for x in (slots or []) if x.strip()}

    header = "order\titem_id\tslot\tfilename_front\tfilename_side\tfilename_back\tfilename_detail\tdisplay_name\tsource_module\n"
    rows: List[str] = []
    count = 0
    for entry in data:
        slot = entry.get("slot", "") or "UnknownArmor"
        if allowed_slots and norm_key(slot) not in allowed_slots:
            continue
        vm = entry.get("views", {}) or {}
        row = "\t".join([
            str(entry.get("order", "")),
            str(entry.get("item_id", "")),
            slot,
            str(vm.get("front", "")),
            str(vm.get("side", "")),
            str(vm.get("back", "")),
            str(vm.get("detail", "")),
            str(entry.get("display_name", "")).replace("\t", " "),
            str(entry.get("source_module", "")).replace("\t", " "),
        ])
        rows.append(row)
        count += 1
        if limit and count >= limit:
            break

    # Prepend a resume comment so the user knows where they left off
    header_comment = f"# BannerwakeArmorAutoCapture capture queue — {now_stamp()}\n"
    header_comment += f"# resume_from_index={start_index}\n"
    header_comment += f"# total_rows={count}\n"

    # TSV lines (comments start with #; the C# parser skips them)
    content = header_comment + header + "\n".join(rows) + "\n"
    atomic_write_text(out_tsv, content)
    return count


# ---------------------------------------------------------------------------
# Markdown reports
# ---------------------------------------------------------------------------

def _group_counts(records: List[ArmorRecord], key: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for r in records:
        v = getattr(r, key, None) or "UNKNOWN"
        counts[v] = counts.get(v, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0].lower())))


def write_markdown_reports(
    records: List[ArmorRecord],
    out_dir: Path,
    errors: List[str],
    module_paths: List[Path],
) -> None:
    rdir = out_dir / "reports"
    rdir.mkdir(parents=True, exist_ok=True)

    # --- archive_summary.md ---
    lines = [
        "# Bannerwake Armor Archive — Summary",
        f"\nGenerated: {now_stamp()}",
        f"\nTotal records: **{len(records)}**",
        "\n## Scanned Modules\n",
    ]
    for p in module_paths:
        lines.append(f"- `{p}`")
    lines += ["", "## By Source Module", ""]
    for k, v in _group_counts(records, "source_module").items():
        lines.append(f"- {k}: {v}")
    lines += ["", "## By Slot", ""]
    for k, v in _group_counts(records, "slot").items():
        lines.append(f"- {k}: {v}")
    lines += ["", "## By Visual Bucket", ""]
    for k, v in _group_counts(records, "visual_bucket").items():
        lines.append(f"- {k}: {v}")
    lines += ["", "## By UseTeamColor", ""]
    for k, v in _group_counts(records, "use_team_color").items():
        lines.append(f"- {k}: {v}")
    lines += ["", "## By Recolor Priority", ""]
    for k, v in _group_counts(records, "bannerwake_recolor_needed").items():
        lines.append(f"- {k}: {v}")
    lines += ["", "## XML Parse Errors", ""]
    if errors:
        for e in errors[:500]:
            lines.append(f"- `{e}`")
        if len(errors) > 500:
            lines.append(f"\n…and {len(errors)-500} more.")
    else:
        lines.append("None.")
    atomic_write_text(rdir / "archive_summary.md", "\n".join(lines))

    # --- armor_by_module.md ---
    lines = ["# Armor by Module\n"]
    current = None
    for r in sorted(records, key=lambda x: (x.source_module.lower(), x.slot, x.item_id.lower())):
        if r.source_module != current:
            current = r.source_module
            lines.append(f"\n## {current}\n")
        lines.append(
            f"- `{r.item_id}` — {r.slot}; "
            f"culture `{r.culture or 'UNKNOWN'}`; "
            f"mesh `{r.mesh or r.body_mesh or 'UNKNOWN'}`; "
            f"team_color `{r.use_team_color}`"
        )
    atomic_write_text(rdir / "armor_by_module.md", "\n".join(lines))

    # --- armor_by_culture.md ---
    lines = ["# Armor by Culture / Visual Bucket\n"]
    current = None
    for r in sorted(
        records,
        key=lambda x: ((x.culture or x.visual_bucket or "UNKNOWN").lower(), x.slot, x.item_id.lower()),
    ):
        key = r.culture or r.visual_bucket or "UNKNOWN"
        if key != current:
            current = key
            faction_note = ""
            if current in FACTION_COLORS:
                c1, c2 = FACTION_COLORS[current]
                faction_note = f" — colours: `{c1}` / `{c2}`"
            lines.append(f"\n## {current}{faction_note}\n")
        lines.append(
            f"- `{r.item_id}` [{r.source_module}/{r.slot}] "
            f"recolor: `{r.bannerwake_recolor_needed}`"
        )
    atomic_write_text(rdir / "armor_by_culture.md", "\n".join(lines))

    # --- recolor_candidates.md ---
    candidates = [
        r for r in records
        if r.bannerwake_recolor_needed in {"likely", "heavy", "verify"}
    ]
    lines = [
        "# Recolor Candidates",
        "\nGenerated heuristically. Human visual review still wins.\n",
        f"Total candidates: **{len(candidates)}**\n",
    ]
    for r in candidates:
        lines += [
            f"## `{r.item_id}`",
            f"- Module: `{r.source_module}`",
            f"- Source XML: `{r.source_xml}`",
            f"- Slot: {r.slot}",
            f"- Culture: `{r.culture or 'UNKNOWN'}`",
            f"- Mesh: `{r.mesh or r.body_mesh or 'UNKNOWN'}`",
            f"- UseTeamColor: `{r.use_team_color}`",
            f"- Visual bucket: `{r.visual_bucket}`",
            f"- Faction colours: {r.bannerwake_faction_colors}",
            f"- Priority: **{r.bannerwake_recolor_needed}**",
            f"- Reason: {r.recolor_reason}",
            "",
        ]
    atomic_write_text(rdir / "recolor_candidates.md", "\n".join(lines))

    # --- armor_missing_screenshots.md ---
    missing = [r for r in records if not r.screenshot_front]
    lines = [
        "# Missing Screenshots",
        f"\n{len(missing)} items have no linked front screenshot.\n",
        "Run the AutoCapture workflow or provide screenshots matching item IDs.\n",
    ]
    for r in missing:
        lines.append(f"- `{r.item_id}` — {r.source_module}/{r.slot}")
    atomic_write_text(rdir / "armor_missing_screenshots.md", "\n".join(lines))


# ---------------------------------------------------------------------------
# HTML gallery
# ---------------------------------------------------------------------------

RECOLOR_BADGE_COLORS = {
    "heavy":    "#ff4444",
    "likely":   "#ff8c00",
    "verify":   "#f0c000",
    "maybe_not": "#3cba54",
    "UNKNOWN":  "#666",
}


def _img(src: str, alt: str) -> str:
    if not src:
        return '<div class="noimg">no screenshot</div>'
    safe = _html.escape(src.replace("\\", "/"), quote=True)
    return (
        f'<img loading="lazy" src="{safe}" '
        f'alt="{_html.escape(alt, quote=True)}" '
        f'onerror="this.parentNode.innerHTML=\'<div class=\\\"noimg\\\">image not found</div>\'">'
    )


def write_html_gallery(records: List[ArmorRecord], path: Path) -> None:
    # Embed data for JS filtering
    data_json = json.dumps([asdict(r) for r in records], ensure_ascii=False)

    cards_html: List[str] = []
    for r in records:
        # Pick best available image for thumbnail
        thumb_src = r.screenshot_front or r.screenshot_side or r.screenshot_back or r.screenshot_detail
        # All views for the viewer
        views_json = json.dumps({
            "front":  r.screenshot_front,
            "side":   r.screenshot_side,
            "back":   r.screenshot_back,
            "detail": r.screenshot_detail,
        })
        badge_color = RECOLOR_BADGE_COLORS.get(r.bannerwake_recolor_needed, "#666")
        slot_tag = _html.escape(r.slot or "—")
        culture_tag = _html.escape(r.culture or r.visual_bucket or "—")
        card = f"""
<article
  class="card"
  data-id="{norm_key(r.item_id)}"
  data-module="{norm_key(r.source_module)}"
  data-slot="{norm_key(r.slot)}"
  data-culture="{norm_key(r.culture or r.visual_bucket)}"
  data-recolor="{norm_key(r.bannerwake_recolor_needed)}"
  data-views='{_html.escape(views_json, quote=True)}'
>
  <div class="thumb" onclick="openViewer(this.closest('.card'))">{_img(thumb_src, r.item_id)}</div>
  <div class="cardbody">
    <div class="card-header">
      <span class="badge" style="background:{badge_color}" title="Recolor priority">{_html.escape(r.bannerwake_recolor_needed)}</span>
      <span class="slottag">{slot_tag}</span>
      <span class="culturetag">{culture_tag}</span>
    </div>
    <h3 title="{_html.escape(r.item_id)}">{_html.escape(r.item_id)}</h3>
    <p class="dname">{_html.escape(r.display_name_clean or r.display_name_raw or '—')}</p>
    <dl>
      <dt>Module</dt><dd>{_html.escape(r.source_module)}</dd>
      <dt>Mesh</dt><dd><code>{_html.escape(r.mesh or r.body_mesh or '—')}</code></dd>
      <dt>Armor</dt><dd>H{r.head_armor or '-'} B{r.body_armor or '-'} A{r.arm_armor or '-'} L{r.leg_armor or '-'}</dd>
      <dt>Tier</dt><dd>{r.tier or '—'}</dd>
      <dt>TeamColor</dt><dd class="tc-{norm_key(r.use_team_color)}">{_html.escape(r.use_team_color)}</dd>
      <dt>Colors</dt><dd>{_html.escape(r.bannerwake_faction_colors or '—')}</dd>
    </dl>
    <details>
      <summary>Source &amp; reason</summary>
      <p class="reason">{_html.escape(r.recolor_reason)}</p>
      <code class="srcxml">{_html.escape(r.source_xml)}</code>
    </details>
  </div>
</article>"""
        cards_html.append(card)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bannerwake Armor Gallery</title>
<style>
:root{{
  --bg:#0e0f11; --surface:#16181c; --raised:#1f2126; --border:#2a2d35;
  --text:#e8e9ec; --muted:#8a8f9a; --accent:#c4a44a;
  --tc-true:#3cba54; --tc-likely:#f0c000; --tc-unknown:#888; --tc-false:#ff4444;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);min-height:100vh}}

/* HEADER */
header{{
  position:sticky;top:0;z-index:20;
  background:var(--bg);border-bottom:1px solid var(--border);
  padding:12px 16px;backdrop-filter:blur(10px);
}}
.header-top{{display:flex;align-items:center;gap:12px;margin-bottom:10px}}
h1{{font-size:18px;font-weight:700;color:var(--accent);letter-spacing:.04em;white-space:nowrap}}
.stats{{font-size:13px;color:var(--muted);margin-left:auto;white-space:nowrap}}
.filters{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:8px}}
input,select{{
  padding:8px 10px;border:1px solid var(--border);border-radius:6px;
  background:var(--raised);color:var(--text);font-size:13px;width:100%;
  transition:border-color .15s;
}}
input:focus,select:focus{{outline:none;border-color:var(--accent)}}

/* GRID */
main{{padding:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}}

/* CARD */
.card{{
  background:var(--surface);border:1px solid var(--border);
  border-radius:10px;overflow:hidden;
  display:flex;flex-direction:column;
  transition:box-shadow .2s,border-color .2s;
}}
.card:hover{{box-shadow:0 0 0 1px var(--accent);border-color:var(--accent)}}
.thumb{{
  background:#0a0b0d;
  display:flex;align-items:center;justify-content:center;
  height:200px;cursor:pointer;overflow:hidden;
  border-bottom:1px solid var(--border);
  position:relative;
}}
.thumb img{{max-width:100%;max-height:200px;object-fit:contain;display:block;transition:transform .2s}}
.thumb:hover img{{transform:scale(1.04)}}
.noimg{{color:#555;font-size:12px;text-align:center;padding:12px}}
.zoom-icon{{
  position:absolute;bottom:6px;right:6px;
  background:rgba(0,0,0,.6);border-radius:4px;
  padding:3px 5px;font-size:11px;color:#aaa;
  pointer-events:none;opacity:0;transition:opacity .2s;
}}
.thumb:hover .zoom-icon{{opacity:1}}

.cardbody{{padding:12px;flex:1;display:flex;flex-direction:column;gap:6px}}
.card-header{{display:flex;gap:6px;align-items:center;flex-wrap:wrap}}
.badge{{
  font-size:11px;font-weight:600;padding:2px 7px;border-radius:12px;
  color:#000;letter-spacing:.02em;white-space:nowrap;
}}
.slottag,.culturetag{{
  font-size:11px;padding:2px 7px;border-radius:12px;
  background:var(--raised);color:var(--muted);border:1px solid var(--border);
}}
h3{{font-size:13px;font-weight:600;word-break:break-all;color:var(--text)}}
.dname{{font-size:12px;color:var(--muted)}}

dl{{display:grid;grid-template-columns:80px 1fr;gap:2px 8px;font-size:12px}}
dt{{color:var(--muted)}}
dd{{overflow-wrap:anywhere}}
.tc-true{{color:var(--tc-true)}}
.tc-likely{{color:var(--tc-likely)}}
.tc-unknown{{color:var(--tc-unknown)}}
.tc-false{{color:var(--tc-false)}}
code{{font-size:11px;background:var(--raised);padding:1px 3px;border-radius:3px;color:#c0c0c0}}
details{{margin-top:4px}}
summary{{cursor:pointer;font-size:12px;color:var(--muted)}}
.reason{{font-size:11px;color:var(--muted);margin-top:4px;line-height:1.5}}
.srcxml{{display:block;font-size:10px;color:#666;margin-top:4px;word-break:break-all}}

.hidden{{display:none!important}}

/* VIEWER OVERLAY */
#viewer{{
  display:none;position:fixed;inset:0;z-index:50;
  background:rgba(0,0,0,.9);backdrop-filter:blur(6px);
  flex-direction:column;align-items:center;justify-content:center;
}}
#viewer.open{{display:flex}}
#viewer img{{max-width:92vw;max-height:80vh;object-fit:contain;border-radius:8px}}
#viewer-info{{color:#ccc;font-size:13px;margin-top:10px;text-align:center}}
.viewer-nav{{display:flex;gap:12px;margin-top:12px}}
.viewer-nav button{{
  padding:7px 18px;background:var(--raised);border:1px solid var(--border);
  color:var(--text);border-radius:6px;cursor:pointer;font-size:13px;
  transition:background .15s;
}}
.viewer-nav button:hover{{background:var(--accent);color:#000}}
#viewer-close{{
  position:absolute;top:16px;right:20px;
  background:none;border:none;color:#aaa;font-size:26px;cursor:pointer;
}}

@media(max-width:700px){{
  .filters{{grid-template-columns:1fr 1fr}}
  .thumb{{height:160px}}
}}
</style>
</head>
<body>

<header>
  <div class="header-top">
    <h1>⚔ Bannerwake Armor Gallery</h1>
    <span class="stats" id="stats">Loading…</span>
  </div>
  <div class="filters">
    <input id="q" placeholder="Search ID, name, mesh, module…" autocomplete="off">
    <select id="f-module"><option value="">All modules</option></select>
    <select id="f-slot"><option value="">All slots</option></select>
    <select id="f-culture"><option value="">All cultures</option></select>
    <select id="f-recolor"><option value="">All recolor states</option></select>
  </div>
</header>

<main>
  <section class="grid" id="grid">{''.join(cards_html)}</section>
</main>

<!-- Screenshot viewer overlay -->
<div id="viewer">
  <button id="viewer-close" onclick="closeViewer()" title="Close (Esc)">✕</button>
  <img id="viewer-img" src="" alt="">
  <div id="viewer-info"></div>
  <div class="viewer-nav">
    <button onclick="cycleView('front')">Front</button>
    <button onclick="cycleView('side')">Side</button>
    <button onclick="cycleView('back')">Back</button>
    <button onclick="cycleView('detail')">Detail</button>
  </div>
</div>

<script>
const DATA = {data_json};

function norm(s){{
  return (s||'').toString().toLowerCase().replace(/[^a-z0-9]+/g,'_').replace(/^_+|_+$/g,'');
}}
function addOptions(id, vals){{
  const sel = document.getElementById(id);
  [...new Set(vals.filter(Boolean).map(norm))].sort().forEach(v=>{{
    const o = document.createElement('option');
    o.value = v; o.textContent = v;
    sel.appendChild(o);
  }});
}}
addOptions('f-module', DATA.map(x=>x.source_module));
addOptions('f-slot', DATA.map(x=>x.slot));
addOptions('f-culture', DATA.map(x=>x.culture||x.visual_bucket));
addOptions('f-recolor', DATA.map(x=>x.bannerwake_recolor_needed));

function applyFilters(){{
  const q = norm(document.getElementById('q').value);
  const mod = document.getElementById('f-module').value;
  const slot = document.getElementById('f-slot').value;
  const cult = document.getElementById('f-culture').value;
  const rcol = document.getElementById('f-recolor').value;
  let shown=0, total=0;
  document.querySelectorAll('.card').forEach(card=>{{
    total++;
    const txt = norm(card.textContent);
    const ok = (!q||txt.includes(q))
      && (!mod||card.dataset.module===mod)
      && (!slot||card.dataset.slot===slot)
      && (!cult||card.dataset.culture===cult)
      && (!rcol||card.dataset.recolor===rcol);
    card.classList.toggle('hidden',!ok);
    if(ok) shown++;
  }});
  document.getElementById('stats').textContent = shown+' / '+total+' items';
}}

['q','f-module','f-slot','f-culture','f-recolor'].forEach(id=>
  document.getElementById(id).addEventListener('input', applyFilters)
);
applyFilters();

// --- Viewer ---
let viewerCard = null;
function openViewer(card){{
  viewerCard = card;
  cycleView('front');
  document.getElementById('viewer').classList.add('open');
}}
function closeViewer(){{
  document.getElementById('viewer').classList.remove('open');
  viewerCard = null;
}}
function cycleView(v){{
  if(!viewerCard) return;
  const views = JSON.parse(viewerCard.dataset.views||'{{}}');
  const src = views[v];
  const img = document.getElementById('viewer-img');
  const info = document.getElementById('viewer-info');
  const id = viewerCard.querySelector('h3').textContent;
  if(src){{
    img.src = src;
    info.textContent = id+' — '+v;
  }} else {{
    img.src = '';
    info.textContent = id+' — no '+v+' screenshot';
  }}
}}
document.addEventListener('keydown', e=>{{
  if(e.key==='Escape') closeViewer();
}});
</script>
</body>
</html>"""

    atomic_write_text(path, html)


# ---------------------------------------------------------------------------
# Sequential screenshot linker
# ---------------------------------------------------------------------------

def _natural_sort_key(p: Path) -> List:
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def link_sequential_screenshots(
    queue_path: Path,
    raw_folder: Path,
    out_dir: Path,
    view: str,
    copy_mode: bool = True,
) -> Path:
    if not queue_path.exists():
        raise FileNotFoundError(f"Queue not found: {queue_path}")
    if not raw_folder.exists():
        raise FileNotFoundError(f"Raw screenshot folder not found: {raw_folder}")

    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    images = sorted(
        [p for p in raw_folder.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS],
        key=_natural_sort_key,
    )
    if not images:
        raise RuntimeError(f"No images found in {raw_folder}")

    if len(images) != len(queue):
        print(
            f"[WARN] Queue={len(queue)} items, raw folder={len(images)} images. "
            f"Will link {min(len(queue), len(images))}.",
            file=sys.stderr,
        )

    target_root = out_dir / "screenshots" / view
    target_root.mkdir(parents=True, exist_ok=True)
    count = min(len(queue), len(images))
    manifest: List[Dict] = []

    for i in range(count):
        entry = queue[i]
        src = images[i]
        slot = norm_key(entry.get("slot", "armor")) or "armor"
        filename = (
            (entry.get("views", {}) or {}).get(view)
            or f"{slot}__{entry['item_id']}__{view}{src.suffix.lower()}"
        )
        if not Path(filename).suffix:
            filename += src.suffix.lower()
        dst = target_root / filename

        if copy_mode:
            shutil.copy2(src, dst)
        else:
            shutil.move(str(src), str(dst))

        manifest.append({
            "order": i + 1,
            "item_id": entry.get("item_id"),
            "source_image": str(src),
            "linked_image": str(dst),
        })

        if (i + 1) % 50 == 0 or (i + 1) == count:
            print(f"\r  {progress_bar(i+1, count)}", end="", flush=True)

    print()
    manifest_path = out_dir / "reports" / f"linked_screenshots_{view}.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"[DONE] Linked {count} screenshot(s) for view '{view}'. Manifest: {manifest_path}")
    return manifest_path


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

def run_scan(args: argparse.Namespace) -> int:
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    module_roots = [Path(p).expanduser() for p in args.modules_root]
    module_paths = discover_modules(
        module_roots,
        args.include_modules or [],
        args.exclude_modules or [],
    )
    if not module_paths:
        print(
            "[ERROR] No modules found. Check --modules-root path(s) and --include-modules names.",
            file=sys.stderr,
        )
        return 2

    print(f"[INFO] Output dir: {out_dir}")
    scanner = BannerlordXmlScanner(module_paths, out_dir, include_all_xml=args.include_all_xml)
    records = scanner.scan()

    if not records:
        print("[WARN] No armor records found. Check your module paths.", file=sys.stderr)
        return 1

    # Attach screenshots if provided
    screenshot_roots = [Path(p).expanduser() for p in (args.screenshots_root or [])]
    if screenshot_roots:
        print(f"\n[SCREENSHOTS] Indexing {len(screenshot_roots)} screenshot root(s)…")
        ScreenshotLinker(screenshot_roots, out_dir).attach(records)
        with_screens = sum(1 for r in records if r.screenshot_front)
        print(f"[SCREENSHOTS] {with_screens}/{len(records)} records have a front screenshot.")

    catalog = out_dir / "catalog"
    gallery = out_dir / "gallery"
    catalog.mkdir(parents=True, exist_ok=True)
    gallery.mkdir(parents=True, exist_ok=True)

    print("\n[WRITE] Generating outputs…")
    queue_json = catalog / "capture_queue.json"
    write_csv(records, catalog / "armor_catalog.csv")
    write_json(records, catalog / "armor_catalog.json")
    write_capture_queue_json(records, queue_json, views=args.views)
    tsv_path = catalog / "capture_queue.tsv"
    n = write_capture_queue_tsv(queue_json, tsv_path, views=args.views, start_index=1)
    print(f"  TSV: {tsv_path} ({n} rows)")
    write_markdown_reports(records, out_dir, scanner.errors, module_paths)
    write_html_gallery(records, gallery / "armor_gallery.html")

    print("\n[DONE] Bannerwake armor archive generated:")
    print(f"  CSV:     {catalog / 'armor_catalog.csv'}")
    print(f"  JSON:    {catalog / 'armor_catalog.json'}")
    print(f"  Queue:   {queue_json}")
    print(f"  TSV:     {tsv_path}")
    print(f"  Reports: {out_dir / 'reports'}")
    print(f"  Gallery: {gallery / 'armor_gallery.html'}")
    return 0


def run_link(args: argparse.Namespace) -> int:
    link_sequential_screenshots(
        Path(args.queue).expanduser().resolve(),
        Path(args.raw_screenshots).expanduser().resolve(),
        Path(args.out).expanduser().resolve(),
        args.view,
        copy_mode=not args.move,
    )
    return 0


def run_export_autocapture(args: argparse.Namespace) -> int:
    queue = Path(args.queue).expanduser().resolve()
    out_tsv = Path(args.out_tsv).expanduser().resolve()
    n = write_capture_queue_tsv(
        queue,
        out_tsv,
        views=args.views,
        limit=args.limit,
        slots=args.slots,
        start_index=args.start_index,
    )
    print(f"[DONE] {n} item(s) written to {out_tsv}")
    return 0


def run_stats(args: argparse.Namespace) -> int:
    catalog = Path(args.catalog).expanduser().resolve()
    if not catalog.exists():
        print(f"[ERROR] Catalog not found: {catalog}", file=sys.stderr)
        return 1
    records_raw = json.loads(catalog.read_text(encoding="utf-8"))
    records = [ArmorRecord(**{k: v for k, v in r.items() if k in ArmorRecord.__dataclass_fields__}) for r in records_raw]
    print(f"Total records: {len(records)}")
    for label, key in [
        ("By source module", "source_module"),
        ("By slot",          "slot"),
        ("By culture",       "culture"),
        ("By visual bucket", "visual_bucket"),
        ("By UseTeamColor",  "use_team_color"),
        ("By recolor need",  "bannerwake_recolor_needed"),
    ]:
        print(f"\n{label}:")
        for k, v in _group_counts(records, key).items():
            print(f"  {k}: {v}")
    return 0


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Bannerwake Armor Archivist v3 — XML data + visual gallery builder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # scan ---------------------------------------------------------------
    scan = sub.add_parser(
        "scan",
        help="Scan Bannerlord modules and generate CSV / JSON / reports / gallery.",
    )
    scan.add_argument(
        "--modules-root", action="append", required=True,
        metavar="PATH",
        help="Bannerlord Modules root or Workshop content root (can repeat).",
    )
    scan.add_argument(
        "--include-modules", nargs="*", default=[],
        metavar="NAME",
        help="Only scan these module folder names. Omit to scan all discovered.",
    )
    scan.add_argument(
        "--exclude-modules", nargs="*", default=[],
        metavar="NAME",
        help="Exclude these module folder names.",
    )
    scan.add_argument(
        "--screenshots-root", action="append", default=[],
        metavar="PATH",
        help="Folder containing screenshots (can repeat).",
    )
    scan.add_argument(
        "--out", required=True, metavar="PATH",
        help="Output archive folder.",
    )
    scan.add_argument(
        "--include-all-xml", action="store_true",
        help="Also parse language/GUI/prefab XML (slower and noisier).",
    )
    scan.add_argument(
        "--views", nargs="*", default=["front", "side", "back"],
        metavar="VIEW",
        help="Views to include in capture queues. Default: front side back.",
    )
    scan.set_defaults(func=run_scan)

    # link-screenshots ---------------------------------------------------
    lnk = sub.add_parser(
        "link-screenshots",
        help="Map sequential raw screenshots to capture_queue item IDs.",
    )
    lnk.add_argument("--queue", required=True, metavar="PATH",
                     help="Path to capture_queue.json.")
    lnk.add_argument("--raw-screenshots", required=True, metavar="PATH",
                     help="Folder with sequential raw screenshot images.")
    lnk.add_argument("--out", required=True, metavar="PATH",
                     help="Output archive folder.")
    lnk.add_argument("--view",
                     choices=["front", "side", "back", "detail"],
                     default="front",
                     help="Which view these raw screenshots represent.")
    lnk.add_argument("--move", action="store_true",
                     help="Move instead of copy raw screenshots.")
    lnk.set_defaults(func=run_link)

    # export-autocapture -------------------------------------------------
    auto = sub.add_parser(
        "export-autocapture",
        help="Export capture_queue.json to TSV for the in-game AutoCapture module.",
    )
    auto.add_argument("--queue", required=True, metavar="PATH",
                      help="Path to capture_queue.json.")
    auto.add_argument("--out-tsv", required=True, metavar="PATH",
                      help="Output capture_queue.tsv path.")
    auto.add_argument("--views", nargs="*", default=["front", "side", "back"],
                      metavar="VIEW")
    auto.add_argument("--limit", type=int, default=0,
                      help="Max items (0 = no limit). Useful for test runs.")
    auto.add_argument("--slots", nargs="*", default=[],
                      metavar="SLOT",
                      help="Filter by slot, e.g. BodyArmor HeadArmor Shield.")
    auto.add_argument("--start-index", type=int, default=1,
                      help="Resume index written as a comment in the TSV.")
    auto.set_defaults(func=run_export_autocapture)

    # stats --------------------------------------------------------------
    stats = sub.add_parser(
        "stats",
        help="Quick summary of an existing armor_catalog.json (no file writes).",
    )
    stats.add_argument("--catalog", required=True, metavar="PATH",
                       help="Path to armor_catalog.json.")
    stats.set_defaults(func=run_stats)

    # init ---------------------------------------------------------------
    init = sub.add_parser(
        "init",
        help="Write README.md and RUN_BANNERWAKE_ARMOR_SCAN.bat to current folder.",
    )
    init.add_argument("--out", default=".", metavar="PATH")

    def _run_init(a: argparse.Namespace) -> int:
        out = Path(a.out).expanduser().resolve()
        out.mkdir(parents=True, exist_ok=True)
        _write_readme(out / "README.md")
        _write_bat(out / "RUN_BANNERWAKE_ARMOR_SCAN.bat")
        print(f"[DONE] Wrote README.md and RUN_BANNERWAKE_ARMOR_SCAN.bat to {out}")
        return 0

    init.set_defaults(func=_run_init)

    return parser


def _write_readme(path: Path) -> None:
    text = r"""# Bannerwake Armor Archivist v3

Scans Bannerlord module XML to build a full armor archive (CSV / JSON / Markdown / HTML gallery).
Generates a TSV capture queue for the in-game AutoCapture module.

## Quick start

```powershell
python bannerwake_armor_archivist.py scan `
  --modules-root "C:\...\Modules" `
  --out "C:\BannerwakeArmorArchive"
```

Open `C:\BannerwakeArmorArchive\gallery\armor_gallery.html` in any browser.

## With screenshots

```powershell
python bannerwake_armor_archivist.py scan `
  --modules-root "C:\...\Modules" `
  --screenshots-root "C:\BannerwakeArmorArchive\screenshots" `
  --out "C:\BannerwakeArmorArchive"
```

## Subcommands

| Command | Purpose |
|---------|---------|
| `scan` | Scan modules, generate all outputs |
| `link-screenshots` | Map sequential raw screenshots to item IDs |
| `export-autocapture` | Re-export TSV without re-scanning |
| `stats` | Print summary of an existing catalog |
| `init` | Write this README and sample batch file |

## Recolor codes

| Code | Meaning |
|------|---------|
| `heavy` | Black Keel / pirate — full dark palette reskin needed |
| `likely` | No UseTeamColor — probably needs bw_ texture variant |
| `verify` | Dynamic color clue found but not proven |
| `maybe_not` | UseTeamColor confirmed — test in-game first |
| `UNKNOWN` | Could not determine |
"""
    atomic_write_text(path, text)


def _write_bat(path: Path) -> None:
    text = (
        "@echo off\nsetlocal\n"
        "set MODULES=C:\\Program Files (x86)\\Steam\\steamapps\\common\\Mount & Blade II Bannerlord\\Modules\n"
        "set WORKSHOP=C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\261550\n"
        "set OUT=C:\\BannerwakeArmorArchive\n"
        "set SCREENSHOTS=%OUT%\\screenshots\n\n"
        "python \"%~dp0bannerwake_armor_archivist.py\" scan ^\n"
        "  --modules-root \"%MODULES%\" ^\n"
        "  --modules-root \"%WORKSHOP%\" ^\n"
        "  --screenshots-root \"%SCREENSHOTS%\" ^\n"
        "  --out \"%OUT%\"\n\n"
        "if exist \"%OUT%\\gallery\\armor_gallery.html\" start \"\" \"%OUT%\\gallery\\armor_gallery.html\"\n"
        "pause\n"
    )
    atomic_write_text(path, text)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\n[ABORTED]", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
