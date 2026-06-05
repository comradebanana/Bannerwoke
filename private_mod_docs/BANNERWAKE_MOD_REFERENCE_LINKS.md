# Bannerwake Mod Reference Links

Research date: 2026-06-03.

Use these as research references unless explicitly marked as a likely dependency. Bannerwake's design rule still stands: study implementations, asset permissions, and behavior patterns, then build integrated Bannerwake systems instead of stacking unrelated overhaul dependencies.

## Immediate Corrections

- Swadian Armoury is not Nexus `1778`. The correct Nexus page is `2349`: https://www.nexusmods.com/mountandblade2bannerlord/mods/2349
- Nexus `1778` is Hallow Plate Armor: https://www.nexusmods.com/mountandblade2bannerlord/mods/1778
- Steam `3622146187`, previously unidentified in the notes, is More Battle Shouts: https://steamcommunity.com/sharedfiles/filedetails/?id=3622146187
- `CalradiaRisingArmory` is selected in local launcher data, but the module folder was missing in the local game `Modules` folder during the audit. Its current public home appears to be Steam/ModDB, not Nexus:
  - Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3469351983
  - ModDB: https://www.moddb.com/mods/calradia-rising-armory/downloads

## Mentioned Mods

| Mod | Best current link | Status | Bannerwake use |
| --- | --- | --- | --- |
| Open Source Armory | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/2829 | Mentioned asset source | Primary armor/weapon/shield pool. Use as requirement/reference; do not blindly auto-assign gear. |
| Swadian Armoury | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/2349 | Mentioned asset source, corrected ID | Vlandian late-medieval armor reference. Nexus is preferred over Steam because the Steam page is older. |
| Hallow Plate Armor | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/1778 | Mistakenly cited as Swadian Armoury | Optional separate armor reference only. Do not treat this as Swadian Armoury. |
| Terra Armarium - Medieval Arsenal Pack | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/8764 | Mentioned asset source | Vlandian/Empire weapon variety: vouges, crossbows, shields. Strong visual fit. |
| Fire Swords Polearms and Axes | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/4547 | Mentioned fire reference | Melee fire visuals for Undying Flame. Note page says its own fire arrows were removed; keep fire arrows separate. |
| Fire Arrows | Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3542272439 | Mentioned fire reference | Fire arrow volleys, burning damage, deployment/crafting concepts. Treat as research-only until tested because Steam page shows warning text despite recent updates. |
| Siege Engines Extended | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/8958 | Mentioned siege reference | Siege variety, siege HP/AI, faction-differentiated siege capability. |
| Adventurer | Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3172213744 | Mentioned encounter reference | Tavern notices, hero approaches, street encounters. Study interaction pattern, not tone. |
| Titles | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/9794 | Mentioned title reference | Culture/fief/status title logic for Seajarls, Groveseers, Vrak lieutenants, etc. |
| Champion's Relics / Tournaments Enhanced | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/8777 | Mentioned relic reference | Culture-appropriate legendary item assignment; Bannerwake relics should be authored, not random drops. |
| Horde Kingdom | Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3676690880 | Mentioned faction-behavior reference | Fiefless kingdom and sack-without-claim logic for Black Keel/Nord/raider behavior. |
| Immersive Storms | Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3626222686 | Mentioned weather reference | Regional storm effects, morale/speed pressure, War Sails weather atmosphere. |
| Esoteric Knowledge | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/9372 | Mentioned progression reference | Earned/passive progression philosophy. Not a dependency. |
| AI Influence / AI Diplomacy | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/9711 | Mentioned AI/NPC reference | Reaction hooks and NPC memory ideas. Avoid AI-generated dialogue for Bannerwake canon. |
| Special Troops Plus | Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2875905594 | Mentioned special-troop reference | Exclusive high-tier units outside ordinary recruitment pools. |
| More Battle Shouts | Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3622146187 | Previously unidentified Steam ID | Battle audio/voice atmosphere reference. Nice-to-have, not core. |
| Calradia at War / CustomSpawns | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/411 | Mentioned spawn/API reference | Custom party and spawn architecture. Also inspect source: https://github.com/CustomSpawnsTeam/CustomSpawns |
| No More Idle Minor Factions | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/9564 | Mentioned engine-fix reference | Confirms Diathma drift/home-settlement problem. Bannerwake must assign homes in XML/C# and monitor runtime drift. |
| Religions | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/3015 | Mentioned devotion reference | Old but still useful architecture reference for settlement/character devotion concepts. |
| Diplomacy | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/832 | Mentioned diplomacy reference | Messengers, war exhaustion, alliances, civil-war/secession ideas. Reference, not dependency. |
| WarAndAiTweaks - Overhaul | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/8427 | Mentioned war-AI candidate | Coalition logic, marshal logic, war fatigue, narrative war declarations. Verify before copying any assumptions. |
| Bellum Civile | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/10609 | Mentioned civil-war candidate | Internal faction politics, rebellious intent, rebel factions, succession. Very relevant to Sturgia/Empire/Aserai fracture systems. |
| Realistic Battle Mod | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/791 | Mentioned combat reference | Formation AI, armor/weapon behavior, RBM War Sails submod. Use carefully because it can reshape combat too broadly. |
| DynaCulture | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/639 | Mentioned culture-spread reference | Old but conceptually useful for devotion/culture influence spreading from settlements. |
| Cultural Identity | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/9675 | Mentioned equipment/culture reference | Lord culture equipment, settlement conversion, notables. Strong Phase 7 visual-identity reference. |
| Banner Kings | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/3826 | Mentioned, do-not-depend warning | Study religion/economy/court ideas only. Do not use as a dependency because it collides with custom troop/faction systems. |
| Tales from the Age of Men | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/7748 | Mentioned Shroud asset reference | Dark faction armor inspiration/private-use texture study. Verify permissions before anything public. |
| Party AI Overhaul and Commands | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/493 | Mentioned Woodsmen AI reference | Old/outdated, but historically relevant for Harmony party behavior targeting. Prefer newer Party AI Controls for current research. |

## New Recommendations To Research

| Mod | Link | Why Bannerwake should study it |
| --- | --- | --- |
| Harmony | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/2006 | Core patching library. Any serious C# behavior patching will touch Harmony-style architecture. |
| ButterLib | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/2018 | Common utility layer, logging/crash/reporting patterns, and dependency ecosystem reference. |
| UIExtenderEx | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/2102 | Reference for custom UI/prefab extension if Bannerwake adds debug panels, faction-state UI, or special event screens. |
| Mod Configuration Menu | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/612 | Reference for dev/debug toggles, event cadence settings, and playtest-only knobs. |
| Bannerlord Software Extender / BLSE | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/1 | Study as tooling/launcher support. Do not require it unless Bannerwake truly needs extender-level behavior. |
| Better Exception Window | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/404 | Strong playtest tool. Bannerwake will need excellent crash surfaces once state machines, factions, and NavalDLC hooks stack up. |
| Troop Editor | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/9245 | Current, active troop-tree prototyping tool. Useful for quickly testing Bannerwake faction equipment/tiers before XML finalization. |
| My Little Warband | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/3164 | Good older reference for custom troop-tree export/import and gear restriction logic. Steam version is older/unofficial; Nexus preferred. |
| Party AI Controls | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/6218 | Newer current reference for clan/party behavior, composition templates, raiding toggles, and map-party commands. Better research target than old Party AI Overhaul. |
| Improved Garrisons | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/688 | Garrison training, recruitment, guard parties, settlement defense AI. Relevant for Black Keel Hvalvik, Last Legion castles, and Vrak garrisons. |
| Fourberie | Nexus: https://www.nexusmods.com/mountandblade2bannerlord/mods/2969 | Cunning/rogue systems, criminal play, schemes, bandit integration. Highly relevant to Shroud, Hidden Hand, Lake Rats, and Vrak underworld pressure. |

## Practical Link Preference

- Prefer Nexus for framework mods, C# libraries, and anything Claude Code may inspect manually.
- Prefer Steam only when the mod exists only on Steam or the Steam page is clearly the living/current version.
- Do not mix Nexus and Steam versions of the same dependency stack in one test profile unless intentionally testing load-order and duplicate-module behavior.
- For private asset use, still record permission terms and source version. Private use is not the same thing as permission to redistribute.
