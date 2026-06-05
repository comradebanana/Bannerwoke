# Bannerwake Hostile Evidence Cleanup - 2026-06-05

This note records the correction pass against:

- `C:\Users\korom\Downloads\BANNERWAKE_DESIGN.txt`
- `C:\Users\korom\Downloads\BANNERWAKE_LORDS.txt`
- `C:\Users\korom\Documents\MOUNT AND BLADE BANNERLORD PRIVATE MOD\BANNERWAKE_ALL_NPC_AND_DIALOGUE_REFERENCE_FOR_CLAUDE.md`
- Local Bannerlord beta v1.4.5 files under `C:\Program Files (x86)\Steam\steamapps\common\Mount & Blade II Bannerlord`

Treat the design and lords documents as corrected working sources after this pass. Treat the reference file and local XML as hard evidence for vanilla and War Sails NPC facts.

## Hard Locks

- No extracted lord Hero or NPCCharacter record has a pregnancy marker. Zorina and Brighan are not XML-confirmed pregnant.
- Taorse [lord_5_21_2] is an active fen Eingal noble, age 18, female, softspoken, honorable, daughter of Carfyd and Beathag. She is not the Grovebound elder.
- Branoc [lord_5_18] is an active fen Morcar noble, spouse of Seonag and son of Pryndor. Do not use him as a Grovebound leader name.
- Aldric [lord_4_3] is vanilla dey Tihr. Do not use him as the Company of the Golden Boar leader.
- Hongard Castle [castle_V2] is dey Jelind/Vartin's starting holding. Vrak seizing it displaces Vartin.
- Vrak's seizure damages four Vlandian clans directly: dey Meroc, dey Tihr, dey Jelind, and dey Arromanc.
- Sunor/town_V4 and Wrexand are not active local v1.4.5 settlement facts for this design pass.
- Vrak's kingdom is named Mortia. Do not resurrect the old placeholder kingdom name.

## Ghosts Removed

- Grovebound elder ghosts: Taorse and Branoc were removed from Grovebound roles. Torcarn/Brenach are Bannerwake-invented names for those roles.
- Golden Boar ghost: Aldric was removed as sub-faction leader. Baldric is the Bannerwake-invented leader name.
- Vlandian family ghosts removed or fenced as non-XML: Beswinda, Ulgaric, Sigatruda, Sicard, Thavin, Turvald, Choric, Vilmarand, Athafled, Arigun, Isigund, Aldric dey Valant, and Brun dey Tihr.
- Brun dey Tihr is now explicitly a Bannerwake-invented retainer/survivor, not an XML lord.
- Chastimir [lord_S9_u] is now the real fourth Kostoroving member, not a pending unnamed placeholder.
- Kanujan [lord_6_19] was removed from the Nord Visduring roster. He is Khuzait Koltit. Triven [lord_7_28] and Anle [lord_7_27] are the Visduring enforcement pair carrying the reused "obediant enforcer of dakhila's will" XML note.
- Compact roster rows were normalized to use `Voice:` labels so future scripts do not borrow the next character's voice.

## Verification Results

- `BANNERWAKE_LORDS.txt`: 174 lord blocks checked against `lords.xml` and `naval_lords.xml`; 0 name, ID, age, or voice mismatches.
- `BANNERWAKE_LORDS.txt`: settlement labels and clan headers checked against local XML; 0 mismatches.
- `BANNERWAKE_DESIGN.txt`: settlement labels and clan headers checked against local XML; 0 mismatches.
- `BANNERWAKE_DESIGN.txt`: explicit lord-ID mentions checked against local XML; 32 mentions, 0 mismatches.
- Bracketed game-looking IDs in the design and lords documents checked against local `ModuleData` ID registry: 1,192 checked; 0 real missing IDs. One prose false positive was "Vlandian lord."
- High-risk stale phrase sweep found no active hits for the deprecated kingdom name, fake pregnancy, Grovebound misassignments, Golden Boar Aldric, Wrexand, pending Kostoroving placeholder, or Kanujan-in-Visduring contamination.

## Rules For Claude / Claude Code

- If an NPC is XML-confirmed, cite the reference ID and do not change age, clan, family, kingdom, or voice without a deliberate Bannerwake event.
- If an NPC is Bannerwake-invented, label them as Bannerwake-invented and do not assign a vanilla lord_id.
- XML comments are useful flavor evidence, not family-law evidence. Do not infer spouse, child, heir, or vassal status from comment proximity alone.
- Do not treat sample dialogue as vanilla dialogue unless a vanilla string ID is cited. The reference gives voice/persona/tag/state material, not bespoke per-lord transcripts.
- No separate spawn-budget layer. Use native party templates, state gates, homes, naval logic, and escalation.
- No "lite" pass for non-Vlandian factions.
