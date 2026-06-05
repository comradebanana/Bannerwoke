# BANNERWAKE CODEX AUDIT

Generated: 2026-06-03
Purpose: high-detail local-file audit and implementation companion for Claude / Claude Code.

This file does not replace `C:\Users\korom\Downloads\BANNERWAKE_DESIGN.txt`.
It patches the practical gaps between the design and the installed Bannerlord
v1.4.5 environment.

## Hard Corrections From User

- Do not add a separate spawn-budget system. Use native party templates, state
  gates, home settlements, naval party logic, and event escalation. The mod does
  not need an extra "spawn budget" abstraction.
- Do not design a lite version of non-Vlandian factions. Every major faction and
  every meaningful sub-faction must receive full-depth treatment. Bannerwake is
  intended to be maximal, insane, immersive, and private.
- Campaign assumption remains NO DEATH, NO BIRTH. No quest, succession, faction
  collapse, or escalation can depend on killing a hero or waiting for heirs.
- Game target is beta branch v1.4.5 as installed locally, with NavalDLC selected.

## Local Install Facts

Game directory:

`C:\Program Files (x86)\Steam\steamapps\common\Mount & Blade II Bannerlord`

Documents directory:

`C:\Users\korom\Documents\Mount and Blade II Bannerlord`

Private mod workspace:

`C:\Users\korom\Documents\MOUNT AND BLADE BANNERLORD PRIVATE MOD`

Design source:

`C:\Users\korom\Downloads\BANNERWAKE_DESIGN.txt`

Installed official module directories:

- `Native`
- `SandBoxCore`
- `BirthAndDeath`
- `CustomBattle`
- `FastMode`
- `Multiplayer`
- `SandBox`
- `StoryMode`
- `NavalDLC`

Selected modules in `LauncherData.xml`:

- `Native` v1.4.5.114824
- `SandBoxCore` v1.4.5.114824
- `BirthAndDeath` v1.4.5.114824
- `CustomBattle` v1.4.5.114824
- `Sandbox` v1.4.5.114824
- `StoryMode` v1.4.5.114824
- `NavalDLC` v1.2.5.114824
- `CalradiaRisingArmory` v1.3.13.0

Important discrepancy:

- `package_info.txt` reports `Environment: PC@v1.3.4` but compile changeset
  `114824`.
- Launcher data and NavalDLC `SubModule.xml` target `v1.4.5.114824`.
- Treat `v1.4.5.114824` as the actual modding target. Record the package-info
  mismatch as a build/install quirk.

Important loader/config discrepancy:

- Launcher data says `CalradiaRisingArmory` is selected, but no folder with that
  ID exists under the local game `Modules` directory. Do not build against it
  until the real module folder is present and inspected.

## Bannerlord File Audit

Deep local file audit:

`C:\Users\korom\Documents\MOUNT AND BLADE BANNERLORD PRIVATE MOD\BANNERWAKE_BANNERLORD_FILE_AUDIT.md`

This is the deliberately noisy Bannerlord file audit requested after the first
pass. It is large on purpose: 77,650 markdown lines, about 3.1 MB, generated
from the local install. It scanned:

- Full game-root file inventory by extension and module.
- Launcher selected modules and versions.
- `package_info.txt`.
- Every official `SubModule.xml` load graph, dependencies, DLL submodules, and
  XML node declarations.
- 3,596 `ModuleData` XML files with root tags, child counts, sizes, and module
  ownership.
- All XML schemas, with special attention to `Factions`, `SPCultures`,
  `Kingdoms`, `Settlements`, `NPCCharacters`, `partyTemplates`, and the
  NavalDLC ship schemas.
- Active NavalDLC settlement data.
- Kingdom, clan/faction, culture, troop, party-template, item, ship, and scene
  inventories.
- 120 DLL paths and sizes.
- 26 high-value DLLs expanded into categorized raw ASCII/UTF-16 string hits.

Most important search anchors inside that audit:

- Filesystem inventory starts at line 13.
- SubModule load graph starts at line 124.
- ModuleData XML inventory starts at line 347.
- XML schema inventory starts at line 1129.
- Active NavalDLC settlement audit starts at line 1638.
- Kingdom/faction audit starts at line 1808.
- Culture audit starts at line 1946.
- NPC/troop audit starts at line 1987.
- Party-template audit starts at line 2297.
- Item XML audit starts at line 2460.
- NavalDLC ship/sea file audit starts at line 3068.
- Scene audit starts at line 3319.
- DLL inventory starts at line 3449.
- Noisy binary string audit starts at line 3574.
- `TaleWorlds.CampaignSystem.dll` string audit starts at line 3578.
- `NavalDLC.dll` string audit starts at line 32719.
- Exact local Bannerwake-relevant term search starts at line 76127.
- Implementation judgement starts at line 77641.

How to use the noisy binary section:

- Treat every binary string hit as a lead, not a public API guarantee.
- Use it to choose what to inspect in dnSpy/ILSpy.
- Verify exact class names, method signatures, access levels, and event
  registration before writing C#.
- Do not discard noisy hits too early. A messy string like `ForceRaid`,
  `CanSpawnPiratePartyInZone`, `ChangeOwnerOfSettlementAction`, or
  `BurnSails` may still point Claude to the correct subsystem.

High-signal judgement from the noisy audit:

- `ChangeOwnerOfSettlementAction` appears repeatedly across campaign and
  NavalDLC binaries. Vrak, Black Keel, Ironjarls, Jawwal oasis expansion,
  Beni Zilal claimant seizures, Undying Flame claimant escalation, and Last
  Legion fort administration should all route settlement mutation through a
  single Bannerwake wrapper around this action.
- `CreateCustomPartyWithPartyTemplate` and `CreateCustomPartyWithTroopRoster`
  appear in both core campaign and NavalDLC string hits. Bannerwake should
  create special event parties through templates/rosters, then let faction
  state control when those templates are eligible.
- `OnMapEventEnd`, `OnMapEventEnded`, `OnPlayerBattleEventEnded`, and
  `CanPartyJoinBattle` appear locally. These are leads for Ghilman-vs-Ghilman
  contract voiding, Vrak defeat/re-emergence, Black Keel aftermaths, Golden
  Boar memory, and post-battle faction-state changes.
- `CanSpawnPiratePartyInZone`, `CreateSeaHoundParty`, `FindAnchorSettlementForParty`,
  `StartSeaRaidMission`, and `OpenNavalBattleMission` appear in NavalDLC string
  hits. Black Keel, Renegati, Lake Rats, and northern/southern pirate baselines
  should be researched against these systems before custom naval spawning is
  written.
- `CreateStormAtPosition`, `StormCreated`, `BurnSails`,
  `CalculateHullFireDamage`, and `CalculateSailFireDamage` appear locally.
  Storm-season logic, Black Keel winter-sea advantage, Vlandian grounded galleys,
  and Undying Flame naval fire can likely hook existing naval/fire systems
  instead of inventing everything from scratch.
- `AddBlockadeVisuals`, `PortStateHelper`, `GetShipyard`,
  `TownShipyardLevel`, `GetSettlementPatrolStatus`,
  `IFleetManagementCampaignBehavior`, and `INavalPatrolPartiesCampaignBehavior`
  appear locally. Port seizure, shipyard UI, blockade presentation, Nord patrol
  state, and Vlandian amphibious war should treat NavalDLC UI/viewmodel behavior
  as a real integration surface.
- `ClanFleetManagementCampaignBehavior`, `NavalDLCClanShipOwnershipModel`,
  `ClanShipOwnershipModel`, and `FishingPartyCampaignBehavior` appear locally.
  Bannerwake should not hand-wave ship ownership. Special factions that own
  ports, patrols, or raiding fleets need a ship ownership policy compatible
  with this model.
- `SyncData` appears in the raw audit. All Bannerwake state machines must be
  save/load-first systems, with repair passes on campaign load.
- StoryMode quest/conspiracy hits are heavy: quest manager events, Empire
  conspiracy, Dragon Banner, Istiana/Arzagos, and anti-/pro-Empire kingdom
  creation strings are present. Any Imperial legitimacy, Last Legion,
  Undying Flame fourth-claimant, or main-quest interference must be tested with
  StoryMode enabled.
- The raw file contains build-agent source path strings for several systems.
  Those are useful breadcrumbs for decompiler search terms even when the class
  or method is internal.

## Highest-Level Praise

Bannerwake's strongest design quality is not the number of factions. It is that
almost every faction has a behavioral identity, not only a visual identity.
Vrak is not just "bandit king"; he damages Vlandian legitimacy, humiliates
specific lords, and changes the incentives of nearby nobles. Black Keel is not
just "strong pirates"; it has a deliberately unresolved wrongness, a regional
naval footprint, and a staged emergence. Grovebound are not just "wild men";
they are built from actual Battanian religious lore and carry legal, social,
and battlefield consequences.

The design also understands Bannerlord's best modding target: the campaign map
as a living state machine. The four-state DORMANT / ACTIVE / ESCALATED / CRISIS
model is exactly the right backbone for a private overhaul because it lets
different factions feel alive without making all of them constantly loud.

Vrak's faction is the clearest example of the document working at full power:
settlement ownership, named vassals, lord reactions, family shame, criminal
logistics, and future re-emergence all point at the same theme. That should be
the quality bar for every other major arc.

## Main Criticism

The design is ambitious enough to survive. The risk is not too much content.
The risk is ambiguity in the implementation contract.

Claude Code needs exact answers to these questions:

- Is this thing a minor faction, a clan, a kingdom, or a pseudo-kingdom?
- Does it use an existing culture or a cloned custom culture?
- Which XML owns the active settlement coordinates?
- Which heroes are normal named lords and which are abstract event actors?
- Which old names are forbidden from appearing in code?
- Which mechanics are flavor and which require C# state?

The notes already contained a few contradictions that would confuse codegen:

- Black Keel was defined and then the same section said Nord slot 2 was open.
- Grovebound had a stray Nord-slot note.
- Akritoi's mercenary list included Ironjarls and then immediately said
  Ironjarls are not mercenaries.
- Vrak text used "killing Vrak" and "when Vrak dies" despite the global NO
  DEATH assumption.
- The "hard cap of 3 named hero leaders" was written too broadly. It applies to
  ordinary minor-faction design, not to custom-kingdom constructs like Vrak or a
  multi-clan Black Keel crisis structure.

Those have been patched in `BANNERWAKE_DESIGN.txt`.

## Active XML Source Of Truth

Core XML surfaces:

- Cultures: `Modules\SandBoxCore\ModuleData\spcultures.xml`
- Vanilla troop trees: `Modules\SandBoxCore\ModuleData\spnpccharacters.xml`
- Kingdoms: `Modules\SandBox\ModuleData\spkingdoms.xml`
- Clans/factions: `Modules\SandBox\ModuleData\spclans.xml`
- Vanilla settlements: `Modules\SandBox\ModuleData\settlements.xml`
- Lords: `Modules\SandBox\ModuleData\lords.xml`
- Heroes: `Modules\SandBox\ModuleData\heroes.xml`
- Items: `Modules\SandBoxCore\ModuleData\items\*.xml`
- Banner icons: `Modules\Native\ModuleData\banner_icons.xml`
- Map icons: `Modules\Native\ModuleData\map_icons.xml`
- Strings: `Modules\Native\ModuleData\module_strings.xml` and module-specific
  `module_strings.xml`

NavalDLC XML surfaces:

- Active NavalDLC settlements: `Modules\NavalDLC\ModuleData\settlements.xml`
- Nord kingdom: `Modules\NavalDLC\ModuleData\kingdoms.xml`
- Nord clans and pirate factions: `Modules\NavalDLC\ModuleData\clans.xml`
- Nord lords: `Modules\NavalDLC\ModuleData\naval_lords.xml`
- Nord and marine troops: `Modules\NavalDLC\ModuleData\naval_characters.xml`
- Naval party templates: `Modules\NavalDLC\ModuleData\naval_partyTemplates.xml`
- Naval cultures: `Modules\NavalDLC\ModuleData\naval_cultures.xml`
- Naval items: `Modules\NavalDLC\ModuleData\items.xml`
- Naval weapons: `Modules\NavalDLC\ModuleData\naval_weapons.xml`
- Ship hulls: `Modules\NavalDLC\ModuleData\ship_hulls.xml`
- Ship slots: `Modules\NavalDLC\ModuleData\ship_slots.xml`
- Ship upgrades: `Modules\NavalDLC\ModuleData\ship_upgrade_pieces.xml`
- Mission ships: `Modules\NavalDLC\ModuleData\mission_ships.xml`
- Ship physics: `Modules\NavalDLC\ModuleData\ship_physics_references.xml`
- Naval scenes: `Modules\NavalDLC\SceneObj\*`

Schema surfaces:

- `XmlSchemas\SPCultures.xsd`
- `XmlSchemas\Kingdoms.xsd`
- `XmlSchemas\Factions.xsd`
- `XmlSchemas\Settlements.xsd`
- `XmlSchemas\NPCCharacters.xsd`
- `XmlSchemas\Heroes.xsd`
- `XmlSchemas\Items.xsd`
- `XmlSchemas\partyTemplates.xsd`
- `XmlSchemas\EquipmentRosters.xsd`
- `XmlSchemas\GameText.xsd`
- `XmlSchemas\ShipHulls.xsd`
- `XmlSchemas\ShipSlots.xsd`
- `XmlSchemas\ShipUpgradePieces.xsd`
- `XmlSchemas\ShipPhysicsReferences.xsd`
- `XmlSchemas\MissionShips.xsd`

## NavalDLC Is Not Optional In This Install

NavalDLC is selected and depends on:

- `Native`
- `SandBoxCore`
- `Sandbox`
- `StoryMode`

NavalDLC `SubModule.xml` requires base version `v1.4.5` and loads:

- `NavalDLC.NavalDLCSubModule`
- `NavalDLC.CustomBattle.NavalDLCCustomBattleSubModule`
- `NavalDLC.View.NavalDLCViewSubModule`
- `NavalDLC.GauntletUI.NavalDLCGauntletUISubModule`

Important: NavalDLC has its own full `Settlements` XML. It repeats base
Calradia settlements with changed map coordinates and adds the Nord homeland.
Because NavalDLC is enabled and loaded after base modules, treat:

`Modules\NavalDLC\ModuleData\settlements.xml`

as the active campaign-map settlement file for this install.

Do not use old SandBox coordinates for Vrak, Hvalvik, Sturgia, Vlandia, or any
navigation logic when NavalDLC is enabled.

## Active Kingdom Colors From Local XML

These are the implementation colors from local XML, not the wiki palette.
Use these for exact XML implementation. The design palette can still remain an
art-direction target when intentionally different.

| Kingdom | ID | Culture | color | color2 | primary banner | secondary banner |
| --- | --- | --- | --- | --- | --- | --- |
| Northern Empire | `empire` | `Culture.empire` | `FF39223F` | `FFDE9953` | `0xff793191` | `0xffFCDE90` |
| Western Empire | `empire_w` | `Culture.empire` | `FF9E5072` | `FFDE9953` | `0xff591645` | `0xffFFAD54` |
| Southern Empire | `empire_s` | `Culture.empire` | `FF9382D0` | `FFDE9953` | `0xff382188` | `0xffDEA940` |
| Sturgia | `sturgia` | `Culture.sturgia` | `FF1C2A50` | `FF949CCC` | `0xff224277` | `0xffCEDAE7` |
| Aserai | `aserai` | `Culture.aserai` | `FF965228` | `FF4F2212` | `0xffB57A1E` | `0xff4E1A13` |
| Vlandia | `vlandia` | `Culture.vlandia` | `FF5C2017` | `FFECBA44` | `0xff8D291A` | `0xffF7BF46` |
| Battania | `battania` | `Culture.battania` | `FF2D3F1D` | `FFBFCBB0` | `0xff284E19` | `0xffB4F0F1` |
| Khuzait | `khuzait` | `Culture.khuzait` | `FF468C7C` | `FFCCBB89` | `0xff429081` | `0xffEFC990` |
| Nord | `nord` | `Culture.nord` | `FF202931` | `FFb7623c` | `0xff202931` | `0xffb7623c` |

## Active Settlement IDs For Bannerwake

Use NavalDLC coordinates.

| Name | ID | Type | Culture | Owner | Position | Prosperity |
| --- | --- | --- | --- | --- | --- | --- |
| Hvalvik | `town_N1` | town | `Culture.nord` | `Faction.clan_nord_3` | `(202.846, 725.805)` | 3100 |
| Hargard | `town_N4` | town | `Culture.nord` | `Faction.clan_nord_4` | `(886.46, 744.819)` | 3100 |
| Galend | `town_V5` | town | `Culture.vlandia` | `Faction.clan_vlandia_1` | `(198.1, 448.996)` | 1900 |
| Jaculan | `town_V6` | town | `Culture.vlandia` | `Faction.clan_vlandia_3` | `(245.971, 428.867)` | 4000 |
| Drapand Castle | `castle_V3` | castle | `Culture.vlandia` | `Faction.clan_vlandia_2` | `(204.432, 541.76)` | 830 |
| Talivel Castle | `castle_V7` | castle | `Culture.vlandia` | `Faction.clan_vlandia_1` | `(292.323, 438.912)` | 770 |
| Hongard Castle | `castle_V2` | castle | `Culture.vlandia` | `Faction.clan_vlandia_9` | `(231.065, 456.48)` | 1020 |
| Rovalt | `town_V9` | town | `Culture.vlandia` | `Faction.clan_vlandia_6` | `(291.39, 564.699)` | 2800 |
| Sargot | `town_V1` | town | `Culture.vlandia` | `Faction.clan_vlandia_1` | `(315.571, 414.116)` | 4500 |
| Ocs Hall | `town_V2` | town | `Culture.vlandia` | `Faction.clan_vlandia_7` | `(290.882, 513.747)` | 4200 |
| Pravend | `town_V3` | town | `Culture.vlandia` | `Faction.clan_vlandia_2` | `(241.947, 512.805)` | 3200 |
| Charas | `town_V7` | town | `Culture.vlandia` | `Faction.clan_vlandia_4` | `(307.81, 376.313)` | 3000 |
| Ostican | `town_V8` | town | `Culture.vlandia` | `Faction.clan_vlandia_8` | `(241.2, 589.995)` | 3900 |
| Dunglanys | `town_B2` | town | `Culture.battania` | `Faction.clan_battania_2` | `(368.936, 514.946)` | 4000 |
| Varcheg | `town_S1` | town | `Culture.sturgia` | `Faction.clan_sturgia_1` | `(518.344, 611.004)` | 3100 |
| Omor | `town_S3` | town | `Culture.sturgia` | `Faction.clan_sturgia_2` | `(560.254, 578.686)` | 3200 |

Vrak's planned Vlandian holdings map cleanly to local IDs:

- `town_V5` Galend: Vrak ruling clan.
- `castle_V3` Drapand Castle: Vrak ruling clan.
- `town_V6` Jaculan: Gurn / Brackfen axis.
- `castle_V2` Hongard Castle: Hund / Brunval axis.
- `castle_V7` Talivel Castle: optional or disputed depending on final Vrak map.

## Active Nord / War Sails Content

The install already contains a real Nord kingdom:

- `Kingdom.nord`
- Name in XML: "Nord"
- Ruler: `Hero.lord_7_1`
- Culture: `Culture.nord`
- Initial war: Nord kingdom is at war with Vlandia in NavalDLC kingdom data.
- Lore text confirms Volbjorn the Hungry and a fragile bond between jarls.

This is extremely useful for Bannerwake. Do not create Nords from scratch.
Build on the existing Nord culture, kingdom, lords, clans, ship hulls, and troop
trees unless a Bannerwake mechanic specifically needs a cloned variant.

Existing NavalDLC Nord clans:

| Clan ID | Name | Home | Owner | Tier |
| --- | --- | --- | --- | --- |
| `clan_nord_1` | Throsniring | `town_N1` | `Hero.lord_7_1` | 6 |
| `clan_nord_2` | Kjolding | `town_N2` | `Hero.lord_7_3` | 5 |
| `clan_nord_3` | Orthling | `town_N3` | `Hero.lord_7_5` | 4 |
| `clan_nord_4` | Skylfing | `town_N4` | `Hero.lord_7_14` | 4 |
| `clan_nord_5` | Gauting | `castle_N1` | `Hero.lord_7_17` | 3 |
| `clan_nord_6` | Rungniring | `castle_N3` | `Hero.lord_7_18` | 3 |
| `clan_nord_7` | Huldring | `castle_N9` | `Hero.lord_7_19` | 4 |
| `clan_nord_8` | Dvarroving | `castle_N4` | `Hero.lord_7_20` | 1 |
| `clan_nord_9` | Visduring | `castle_N7` | `Hero.lord_7_25` | 2 |

Existing NavalDLC pirate factions:

- `northern_pirates`: Sea Raiders. Bandit/outlaw. Home:
  `Settlement.hideout_mountain_12`. Template:
  `PartyTemplate.northern_pirates_template`.
- `southern_pirates`: Corsairs. Bandit/outlaw. Home:
  `Settlement.hideout_forest_4`. Culture: `Culture.southern_pirates`.
  Template: `PartyTemplate.southern_pirates_template`.

Do not confuse these with Black Keel or Renegati:

- Sea Raiders can be a mundane northern-pirate baseline.
- Corsairs can be a mundane southern-pirate baseline.
- Black Keel are the wrong northern crisis entity.
- Renegati are organized Imperial toll authority, not cursed pirates.

## Existing Naval Troop Lines

NavalDLC adds marine branches to core cultures:

- Vlandia: `vlandian_crossbowman` -> `vlandian_marine_t4` ->
  `vlandian_marine_t5`
- Sturgia: `sturgian_warrior` -> `sturgia_marine_t3` ->
  `sturgia_marine_t4` -> `sturgia_marine_t5`
- Battania: `battanian_skirmisher` -> `battanian_marine_t4` ->
  `battanian_marine_t5`
- Aserai: `aserai_skirmisher` -> `aserai_marine_t4` ->
  `aserai_marine_t5`
- Empire: `imperial_infantryman` -> `empire_marine_t3` ->
  `empire_marine_t4` -> `empire_marine_t5`

Nord common tree:

- `nord_youngling` -> `nord_drengr` -> `nord_axe_warrior`
  - -> `nord_boandi` -> `nord_berserkr`
  - -> `nord_hew-bearer` -> `nord_skjaldbrestir`
- `nord_youngling` -> `nord_drengr` -> `nord_spear_warrior`
  - -> `nord_vargr` -> `nord_ulfhednar`
- `nord_youngling` -> `nord_huntsman`
  - -> `nord_freeman_archer` -> `nord_marksman` -> `nord_skathi`

Nord noble tree:

- `nord_ungmann` -> `nord_thegn` -> `nord_jarlsmann` ->
  `nord_hirdmann` -> `nord_huscarl`

All Nord troops have Mariner values, rising from 50 to 100. This means
Bannerwake should treat Nords as natively maritime in actual mechanics, not just
lore.

Existing pirate trees:

- `sea_raiders_bandit` upgrades into Nord axe warrior branches.
- `southern_pirates_bandit` -> `southern_pirates_raider` ->
  `southern_pirates_chief`, with access into Aserai marine tiers.

## Existing Ship Hulls

Key hulls from `ship_hulls.xml`:

| Hull ID | Name | Value | Mission ship |
| --- | --- | ---: | --- |
| `northern_trade_ship` | Knarr | 6000 | `ship_knarr` |
| `northern_light_ship` | Light Longship | 8500 | `ship_lightlongship` |
| `northern_medium_ship` | Longship | 24000 | `ship_longship` |
| `nord_medium_ship` | Drakkar | 50000 | `ship_drakkar` |
| `nord_mediumballista_ship` | Battle Knarr | 26000 | `nord_mediumballista_ship` |
| `sturgia_heavy_ship` | Lodya | 45000 | `ship_sturgianheavylongship` |
| `western_light_ship` | Western Galley | 8000 | `ship_galley` |
| `western_medium_ship` | Cog | 25000 | `ship_cog` |
| `western_trade_ship` | Trade Cog | 13000 | `ship_trade_cog` |
| `vlandia_heavy_ship` | Roundship | 72000 | `ship_roundship` |
| `battanian_light_ship` | Birlinn | 11000 | `ship_catship` |
| `battanian_medium_ship` | Barlinnger | 25500 | `ship_catship_medium` |
| `central_light_ship` | Eastern Galley | 7500 | `ship_meditlight` |
| `eastern_medium_ship` | Sambuk | 26000 | `ship_meditmedium` |
| `eastern_trade_ship` | Dhow | 6000 | `ship_dhow` |
| `eastern_heavy_ship` | Dromakion | 60000 | `ship_lightdromon` |
| `aserai_heavy_ship` | Ghurab | 75000 | `ship_meditheavy` |
| `empire_medium_ship` | Liburna | 28000 | `ship_liburna` |
| `empire_heavy_ship` | Dromon | 80000 | `ship_dromon` |
| `empire_trade_ship` | Corbita | 16000 | `ship_corbita` |
| `khuzait_heavy_ship` | Qalguk | 62000 | `ship_xebec` |

Culture-to-ship availability from NavalDLC XSLT:

- Empire: `empire_heavy_ship`, `empire_medium_ship`, `central_light_ship`,
  `eastern_trade_ship`, `western_light_ship`, `eastern_heavy_ship`,
  `empire_trade_ship`.
- Aserai: `central_light_ship`, `eastern_heavy_ship`, `aserai_heavy_ship`,
  `eastern_medium_ship`, `eastern_trade_ship`.
- Sturgia: `northern_medium_ship`, `northern_light_ship`,
  `sturgia_heavy_ship`, `northern_trade_ship`, `nord_mediumballista_ship`.
- Vlandia: `western_light_ship`, `western_medium_ship`,
  `vlandia_heavy_ship`, `western_trade_ship`, `battanian_medium_ship`.
- Battania: `western_light_ship`, `western_medium_ship`,
  `battanian_light_ship`, `northern_trade_ship`, `western_trade_ship`,
  `battanian_medium_ship`.
- Khuzait: `khuzait_heavy_ship`, `eastern_medium_ship`,
  `eastern_heavy_ship`, `central_light_ship`, `eastern_trade_ship`.
- Nord: `northern_light_ship`, `northern_medium_ship`,
  `nord_medium_ship`, `northern_trade_ship`, `nord_mediumballista_ship`.

Ship upgrade pieces include ballista, fire ballista, fire pot ballista,
grapeshot ballista, fire grapeshot ballista, mangonel placeholder, and ram
families. This is directly useful for Undying Flame naval fire concepts,
Black Keel boarding pressure, and Vlandian invasion ships.

## Useful C# Surface Names Found In Local DLL Strings

Reflection loading hit recursion issues, so this was a string-surface audit, not
a full API signature dump. Claude Code should verify exact signatures by
decompiling the v1.4.5 assemblies before writing final C#.

Campaign system names found:

- `CampaignBehaviorBase`
- `CampaignEvents`
- `CampaignEventDispatcher`
- `OnNewGameCreated`
- `OnGameLoaded`
- `OnSettlementEntered`
- `OnMakePeace`
- `OnKingdomDestroyed`
- `OnVillageRaid`
- `OnMapEventEnd`
- `OnPlayerBattleEventEnded`
- `OnHeroKilled`

Action / world mutation names found:

- `ChangeOwnerOfSettlementAction`
- `ChangeOwnerOfSettlementDetail`
- `ChangeKingdomAction`
- `DestroyKingdomAction`
- `DestroyPartyAction`
- `CreateCustomPartyWithPartyTemplate`
- `CreateCustomPartyWithTroopRoster`
- `CreateNewClanMobileParty`
- `CreateBanditParty`
- `ActivateBanditParty`
- `ApplyForCapturingEnemySettlement`
- `ApplyForRaidingEnemyVillage`
- `StartAlliance`
- `AddAlliance`
- `AddAllianceDecision`
- `CanMakeTradeAgreement`
- `AcceptPeaceOffer`

Clan/faction fields found:

- `IsMinorFaction`
- `InitialHomeSettlement`
- `IsClanTypeMercenary`
- `IsRebelClan`

NavalDLC namespaces and behavior/model names found:

- `TaleWorlds.CampaignSystem.Naval`
- `ClanFleetManagementCampaignBehavior`
- `ClanShipOwnershipModel`
- `FishingPartyCampaignBehavior`
- `NavalDLCManager`
- `NavalDLCEvents`
- `NavalDLCHelpers`
- `NavalStorylineData`
- `NavalStorylineStage`

Naval actions / helpers found:

- `AddShip`
- `AddShipToPlayer`
- `AddShipUpgradePieces`
- `ChangeShipOwnerAction`
- `DestroyShipAction`
- `DiscardShips`
- `DistributeDefeatedPartyShipsAmongWinners`
- `FindAppropriateInitialShipsForMobileParty`
- `CanClanBuyShipFromTown`
- `CanTownCreateShipFromHull`
- `CanPartyTakeShip`
- `CanPartyTradeShip`
- `CanPartyUpgradeShips`
- `CanMainPartySail`
- `CanMainHeroEnterPort`

Naval party / AI names found:

- `CreateSeaHoundParty`
- `CreateMerchantsParty`
- `CreateFishingParty`
- `CreatePatrolParty`
- `CanSpawnPiratePartyInZone`
- `FindAnchorSettlementForParty`
- `DirectMerchantPartyToBase`
- `AdjustMerchantPartySpeed`
- `CalculateDefensivePatrollingScoreForSettlement`
- `CalculateOffensivePatrollingScoreForSettlement`

Naval battle / storm / fire names found:

- `OpenNavalBattleMission`
- `OpenNavalRaidMission`
- `StartSeaRaidMission`
- `IsNavalBattle`
- `IsNavalRaidBattle`
- `IsNavalMapEvent`
- `CalculateMoraleChangeOnShipSunk`
- `CalculateMoraleOnShipsConnected`
- `CalculateOpenSeaAttritionDamageForShip`
- `CanPartyGetDamagedByStorm`
- `CreateStormAtPosition`
- `StormCreated`
- `CalculateWindBoostForParty`
- `BurnShipObject`
- `BurnShipObjective`
- `BurnSails`
- `CalculateHullFireDamage`
- `CalculateSailFireDamage`
- `AttemptBoarding`

Naval AI behavior names found:

- `BehaviorNavalApproachInLine`
- `BehaviorNavalDefendInLine`
- `BehaviorNavalEngageCorrespondingEnemy`
- `BehaviorNavalRamming`
- `BehaviorNavalSkirmish`
- `BehaviorNavalRaidCliffShooting`
- `BehaviorNavalRaidHoldChokePoint`
- `BehaviorNavalRemoveConnection`

Naval view/UI names found:

- `AddBlockadeVisuals`
- `RemoveBlockadeVisuals`
- `CreateBlockadeShipVisual`
- `BlockadeVisualHelper`
- `BlockadePositionScript`
- `OpenManageFleetAction`
- `PortState`
- `PortStateHelper`
- `GetNavalPatrolParty`
- `GetSettlementPatrolStatus`
- `GetShipyard`
- `TownShipyardLevel`
- `IsTownShipyard`
- `IsShipyardEnabled`
- `HasPort`
- `Shipmaster`
- `Shipyard`
- `Mariner`

StoryMode / Dragon Banner names found:

- `AssembleEmpireQuestBehavior`
- `MeetWithArzagosQuest`
- `MeetWithIstianaQuest`
- `SupportKingdomQuest`
- `CreateAntiImperialKingdom`
- `CreateImperialKingdom`
- `AntiEmpireConspiracyBeginsSceneNotificationItem`

Do not assume StoryMode quests are safe to break. If Bannerwake changes the
Empire claimant layer, test with StoryMode enabled because it is selected.

## Recommended Bannerwake Module Shape

Create a module that depends on:

- `Native`
- `SandBoxCore`
- `Sandbox`
- `StoryMode`
- `NavalDLC`

Module folder:

`Modules\Bannerwake`

Suggested structure:

- `SubModule.xml`
- `bin\Win64_Shipping_Client\Bannerwake.dll`
- `ModuleData\bannerwake_cultures.xml`
- `ModuleData\bannerwake_kingdoms.xml`
- `ModuleData\bannerwake_clans.xml`
- `ModuleData\bannerwake_lords.xml`
- `ModuleData\bannerwake_heroes.xml`
- `ModuleData\bannerwake_characters.xml`
- `ModuleData\bannerwake_partyTemplates.xml`
- `ModuleData\bannerwake_items.xml`
- `ModuleData\bannerwake_equipment_sets.xml`
- `ModuleData\bannerwake_bodyproperties.xml`
- `ModuleData\bannerwake_skill_sets.xml`
- `ModuleData\bannerwake_module_strings.xml`
- `ModuleData\bannerwake_dialog_strings.xml`
- `ModuleData\bannerwake_ship_hulls.xml` only if new hulls are truly required.
- `ModuleData\bannerwake_ship_upgrade_pieces.xml` only if existing fire/ram
  pieces are insufficient.

Use `bw_` prefix for all new object IDs:

- `bw_black_keel_deckhand`
- `bw_vrak_bandit_recruit`
- `bw_jomsvikingr_jomskarl`
- `bw_grove_wildling`
- `bw_golden_boar_crossbowman`
- `bw_hidden_hand_enforcer`

Avoid generic IDs like `deckhand`, `captain`, `floki`, `vrak_guard`; collisions
and future confusion are guaranteed.

## C# Architecture Recommendation

Do not put all behavior in one giant campaign behavior. Use small services and
one or two persistence behaviors.

Suggested classes:

- `BannerwakeSubModule`
  - Registers campaign behaviors during game start.
  - Checks that NavalDLC is loaded.
  - Logs target version and module dependency status.

- `BannerwakeCampaignBehavior : CampaignBehaviorBase`
  - Owns save/load via `SyncData`.
  - Stores state enum per sub-faction.
  - Stores timers, event flags, settlement seizure flags, contract memories,
    player karma, and per-faction relationship overrides.

- `BannerwakeFactionRegistry`
  - Central mapping of all XML IDs to typed references.
  - Validates all required kingdoms, clans, cultures, settlements, heroes,
    troops, templates, and ship hulls on campaign start/load.
  - Fails loudly in logs when an ID is missing.

- `BannerwakeStateService`
  - Evaluates DORMANT / ACTIVE / ESCALATED / CRISIS transitions.
  - One state machine per sub-faction. Do not hardcode all logic in one switch.

- `BannerwakeSettlementService`
  - Wraps `ChangeOwnerOfSettlementAction`.
  - Handles garrison injection, culture changes, prosperity damage, loyalty
    changes, and return-to-normal logic.
  - Contains Vrak seizure logic and Black Keel Hvalvik seizure logic.

- `BannerwakeContractService`
  - Mercenary contract state.
  - Jomsvikingr code enforcement.
  - Golden Boar permanent memory.
  - Ghilman "will not fight Ghilman" rule.
  - Akritoi contract / route knowledge unlocks.

- `BannerwakeNavalService`
  - Ship assignment to special parties.
  - Naval threat zones.
  - Port/blockade interactions.
  - Black Keel, Renegati, Lake Rats, Vlandian landings, Nord patrols.

- `BannerwakeTargetingService`
  - Custom party target restrictions.
  - Woodsmen target lords/tax convoys, never villages.
  - Karakhergit target Khuzait caravans/parties specifically.
  - Lake Rats stay around Lake Laconis.
  - Black Keel stay northern with rare alarming exceptions.

- `BannerwakeKarmaService`
  - Honor / cunning / faith / cruelty style axes.
  - Does not replace vanilla traits; it supplements them for Bannerwake dialogue
    and faction reactions.

- `BannerwakeNotificationService`
  - World notifications, rumors, tavern lines, and phase transitions.
  - Keeps the player informed without overexplaining hidden truths.

Persistence:

- Store enum states and important booleans with stable save keys.
- Never store direct object references without re-resolving IDs on load unless
  v1.4.5 serialization examples confirm it is safe.
- Every dynamic faction needs a "repair pass" on load to correct missing parties,
  invalid home settlements, broken ownership, or stale garrisons.

## Faction Implementation Contracts

### Vrak The Foul

Implementation type:

- Custom kingdom / pseudo-kingdom, not ordinary minor faction.
- Four clans: Vrak ruling clan plus three vassal clans.
- Five settlements total per design, using active NavalDLC settlement IDs.
- Vrak never dies. If defeated, he escapes and can re-emerge.

Why not ordinary minor faction:

- Ordinary minor factions cannot naturally own settlements.
- The design requires a kingdom-scale political disruption.
- The design requires multiple clans, vassal behavior, and lord reactions.

Implementation needs:

- Initial hidden/dormant state.
- Crisis event seizes exact settlements with C#.
- Vlandian lord reaction state table.
- Defeat route that scatters armies and stores Vrak re-emergence flag.
- No code path calls hero death.
- All "kill Vrak" text converted to defeat, drive out, capture, rout, expose,
  imprison temporarily, or force escape.

Suggested culture:

- Use `Culture.vlandia` for most Vrak lords and troops unless a custom
  `bw_vrak` culture is needed for recruitment UI. If a custom culture is used,
  clone all necessary civilian/town roles from Vlandia to avoid missing NPCs.

### Black Keel

Implementation type:

- Dormant hidden multi-clan structure that can become pseudo-kingdom or custom
  kingdom at CRISIS.
- Do not model as a single ordinary minor faction if it needs Hrothgar plus a
  captain council plus port ownership.

Culture choice:

- Start with `Culture.nord` for heroes and troop equipment inheritance.
- Create `Culture.bw_black_keel` only if the seized port must produce distinct
  Black Keel recruits through settlement culture mechanics.
- If creating `bw_black_keel`, clone the Nord culture fully: basic troop,
  elite troop, militia, caravans, guards, notables, town NPCs, equipment rosters,
  body properties, names, and shipwright.

Implementation needs:

- Hrothgar hidden until world event.
- Captain clans hidden until escalation.
- Black Keel troop tree independent from ordinary Nord troop tree.
- Seizes Hvalvik (`town_N1`) unless design changes it.
- Garrison inflated intentionally.
- Face/skin wrongness stays Phase 7 art task.
- Never explain the wrongness definitively.
- Rare Imperial-coast appearances should be event-driven, not normal patrols.

### Jomsvikingr

Implementation type:

- Mercenary brotherhood with fixed hall.
- Nord-exclusive player arc.
- Can escalate to independent fortified entity if Nordvyg weakens.

Use existing content:

- Replace vanilla Skolderbroda conceptually, but do not blindly overwrite
  `skolderbrotva` until all references are checked.
- Jomsvikingr need exclusive recruitment from their hall only.

Implementation needs:

- Player membership ranks.
- Contract memory and absolute code enforcement.
- No recruitment without membership.
- No renamed `Skolvard` IDs in code except migration comments.

### Ironjarls

Implementation type:

- Nord internal political faction, not mercenary.
- Active from campaign start.
- Uses Nordvyg weakness thresholds.

Implementation needs:

- Tracks Nord settlement count and major defeats.
- Targets Halthdar tax collectors / supply convoys.
- Does not attack villages as common bandits.
- Can seize a historically meaningful inland Nord settlement at CRISIS.
- De-escalates when Nordvyg recovers.
- Never appears in mercenary contract list.

### Lake Rats

Implementation type:

- Sturgian-adjacent lake threat.
- Region locked to Lake Laconis.
- Hostile salvage/wrecker identity.

Implementation needs:

- False beacon mechanic.
- Wreck aftermath events.
- Lake-only pathing or hard corrective teleport/target restrictions if AI
  wanders.
- Ship / coastal encounter hooks from NavalDLC.
- Accepts fugitives from multiple cultures; do not make roster ethnically pure.

### Woodsmen Of Robynn

Implementation type:

- Vlandian outlaw folk-hero faction.
- Hostile to Vlandian nobility, friendly/neutral to villages.

Implementation needs:

- Targeting override: lords, noble convoys, tax collectors.
- Explicitly suppress village raiding.
- Positive village relationships.
- Forrath remains place name, not faction name.
- No corruption arc.

### Company Of The Golden Boar

Implementation type:

- Hireable Vlandian professional mercenary faction.
- Permanent memory system.

Implementation needs:

- Logs every contract kept/broken.
- Can take contracts against player after betrayal.
- Crossbow superiority must be visible in battle composition.
- If unpaid and strong, land-demand escalation.

### Grovebound

Implementation type:

- Battanian religious militant/seer structure.
- Fighters can be hostile; Groveseers are special neutral/untouchable actors.

Implementation needs:

- Sacred grove anchor near Dunglanys.
- Gathering event only; Gathering Warriors do not enter ordinary spawn pools.
- Ca fal legal taboo: attacking rite-observant Grovebound costs Battanian-wide
  relationship.
- No shield-infantry/ranged-only dilution. Pure aggressive faith.
- Use Dunglanys lore as foundation, not invented external fantasy.

### Karakhergit

Implementation type:

- Khuzait anti-centralization holdout faction.
- Specifically targets Khuzait caravans and parties.

Implementation needs:

- Khuzait-specific hostility.
- Neutral to outsiders unless provoked or allied through war.
- Reclamation event if Khuzait loses territory.
- Can become Khanate of Karak if granted stronghold.

### Dust Speakers

Implementation type:

- Khuzait shamanic intelligence / burial-rite network.
- Mostly non-combat and event-driven.

Implementation needs:

- Burial ground map anchors or invisible event settlements.
- Neutral default.
- Permanent enmity if burial rites are violated.
- Information unlocks about Veil Riders / Shroud should be fragmentary and
  never too early.

### Hidden Hand

Implementation type:

- Imperial regional criminal cell network, not one centralized army.

Implementation needs:

- One cell per major Imperial city or region.
- Proxy quests and merchant/notable manipulation.
- Hostile to Undying Flame.
- Dismantling one cell does not destroy the network.

### Undying Flame

Implementation type:

- Imperial fire cult with devotion spread.
- Can become Fourth Imperial claimant at escalation.

Implementation needs:

- Real fire arrows / fire weapons / burning effects.
- Settlement devotion values.
- Vessel election at escalation.
- Fire identity at every tier.
- No "they are right" simplification. They can identify real corruption and
  still be monstrous.

### Last Legion

Implementation type:

- Imperial loyalist military remnant.
- Occupies forts / toll roads.
- Can reintegrate into a reunified Empire.

Implementation needs:

- Abandoned fort anchors.
- Tax/toll behavior.
- Disciplined heavy infantry.
- Reintegration reward that significantly boosts the Empire faction.

### Akritoi

Implementation type:

- Imperial frontier cavalry mercenaries.
- Hireable mercenary; no intelligence-network angle.

Implementation needs:

- Frontier route knowledge as quest reward.
- Cavalry-only identity.
- Available to Imperial-adjacent kingdoms.
- Discovery event within first 30 days.

### Jawwal

Implementation type:

- Aserai Bedouin tribute confederacy.

Implementation needs:

- Caravan tribute checks in desert/highland routes.
- Poetry dialogue on capture/encounter.
- Oasis expansion if Aserai collapses militarily.
- Neutral to paid travelers, hostile to unpaid caravans.

### Ghilman

Implementation type:

- Aserai elite mercenary slave-soldiers.

Implementation needs:

- Contract loyalty while paid.
- Absolute no Ghilman-vs-Ghilman battle rule.
- Pre-battle / pre-targeting detection that voids contract before conflict.
- No exceptions.

### Beni Zilal

Implementation type:

- Aserai traditionalist claimant faction.

Implementation needs:

- Escalates from military losses and instability, not death.
- Tax redirection events.
- Claimant declaration if Aserai throne looks weak.
- Distinct old-line armor and elder guard.

### Renegati

Implementation type:

- Cross-regional Imperial naval toll authority.
- Businesslike, southern, organized.

Implementation needs:

- Boarding/toll encounters.
- Receipt/paper-trail flavor.
- Tribute arrangement de-escalation.
- Distinct from Corsairs and Black Keel.

### Shroud

Implementation type:

- Late-game hidden conspiracy / ancient-civilization advance agents.
- Do not overexpose early.

Implementation needs:

- Fragment system.
- Contradictory clues.
- Physical parties only late.
- No definitive origin reveal.
- Visual wrongness Phase 7 asset plan must strip Tolkien-specific symbols if
  private assets are used.

## Non-Vlandian Depth Gap Fill

The current Vlandian/Vrak material is the deepest political layer. Other major
factions need comparable consequences, not equal word count.

Sturgia needs:

- Boyar Council variables tied to lost settlements, failed campaigns, caravan
  disruption, and Nord pressure.
- Lake Laconis as a living naval/economic region, not just a place Lake Rats
  spawn.
- Raganvad pressure events after losses: boyars withhold troops, demand shorter
  campaigns, or redirect armies defensively.
- Varangian/Nord tension that is visible but not a copy of Ironjarls.
- If the third Sturgian sub-faction remains open, keep it open. Depth can come
  from Boyar Council mechanics and Lake Rats until the right concept appears.

Battania needs:

- Sacred-site data table: Dunglanys, grove outside Dunglanys, key villages,
  old forest routes.
- Caladog political reactions to Grovebound events.
- Groveseer travel events in non-Battanian cities.
- Consequences for burning or occupying Battanian sacred territory.
- Terrain-based AI preference: avoid open plains, prefer forest/broken ground.

Khuzait needs:

- Clan-cohesion variable separate from generic military strength.
- Karakhergit raids should hit Khuzait legitimacy, not only economy.
- Dust Speaker information should make Khuzait feel older than Monchug's state.
- Naval weakness should matter strategically: Khuzaits can use ferries/rivers
  but should not become a sea power.

Empire needs:

- Claimant legitimacy variables for all three Empire factions.
- Hidden Hand cells should interact with all three courts differently.
- Undying Flame devotion should spread unevenly by city corruption, war damage,
  and claimant weakness.
- Last Legion should be a possible stabilizer or threat depending on legitimacy.
- Akritoi should make the frontier feel watched.

Aserai needs:

- Caravan economy should feed army strength over 60-ish in-game days as the
  design states.
- Jawwal tribute should affect safe passage and local prices.
- Ghilman contract rules should create dramatic battlefield non-events.
- Beni Zilal should be an internal legitimacy threat, not a random rebel clan.

Nordvyg needs:

- Halthdar strength variable.
- Ironjarl restlessness variable.
- Jomsvikingr independence threshold.
- Black Keel northern-sea dread variable.
- The existing Nord clans should react differently to all three pressures.

## XML Design Warnings

`Factions.xsd` requires `initial_home_settlement`. Missing or invalid homes are
not safe. Every new faction/clan should have one in XML, then C# should verify
and repair on load.

Do not create custom cultures lightly. A culture is not just a name/color. It
contains default party templates, militia, rebels, vassal rewards, civilian NPCs,
guards, notables, equipment rosters, body properties, name lists, and sometimes
naval fields. A half-filled culture will break settlement UI, recruitment, or
spawn logic.

Rule of thumb:

- If a faction uses normal settlement recruitment and owns a settlement long
  term, consider a complete cloned culture.
- If a faction only has custom parties, custom troops, and event spawns, use an
  existing culture and custom party templates.

Settlement ownership changes should always be done through a service that:

- Checks the settlement exists.
- Checks current owner and logs mismatch.
- Changes owner through the correct action.
- Injects or adjusts garrison.
- Updates culture only if deliberately intended.
- Repairs militia/recruitment templates if culture changed.
- Sends player/world notifications.

## What Claude Code Should Do First

1. Create the Bannerwake module skeleton with hard dependency on NavalDLC.
2. Add a state behavior that saves/loads empty state for every sub-faction.
3. Add registry validation for all local IDs listed in this audit.
4. Add no-op daily/evaluation hooks and log output.
5. Add XML for one harmless test faction or test party only.
6. Boot a new campaign and verify no XML load errors.
7. Implement Vrak or Black Keel only after the skeleton can save/load and repair
   state safely.

The first milestone is not "Vrak works." The first milestone is "Bannerwake can
load, save, reload, validate IDs, and do nothing without corrupting a campaign."

## No-Go List

- No code path that kills Vrak, Hrothgar, Floki, Derthert, Halthdar, or any
  required state-machine hero.
- No separate spawn-budget system unless the user explicitly reverses the
  correction.
- No Ironjarls in hireable mercenary lists.
- No Skolvard IDs except deprecated migration comments.
- No Black Keel definitive origin explanation.
- No Khuzait sea-power escalation.
- No ordinary minor faction owning a settlement without C# support.
- No custom culture unless all required culture roles are filled.
- No reliance on wiki colors over local XML for implementation.
- No building against missing `CalradiaRisingArmory` until its module folder is
  found and inspected.
