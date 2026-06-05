
--------------------------------------------------------------------------------
SECTION 9h: EXTRACTED NPC ROSTER — VANILLA + WAR SAILS
--------------------------------------------------------------------------------

Extraction scope:
- Vanilla files used: SandBox/ModuleData/lords.xml, SandBox/ModuleData/heroes.xml, SandBox/ModuleData/spclans.xml, SandBox/ModuleData/spkingdoms.xml, SandBox/ModuleData/settlements.xml.
- War Sails local module is named NavalDLC. Files used: NavalDLC/ModuleData/naval_lords.xml, heroes.xml, clans.xml, kingdoms.xml, settlements.xml.
- Requested SandBoxCore lords.xml/nobles.xml and WarSails/ModuleData/lords.xml do not exist in this install; equivalent records are in SandBox and NavalDLC.
- Scope is named NPCCharacter records with occupation="Lord" and is_hero="true", joined to Hero, clan, kingdom, and settlement XML.
- Pregnancy state: no pregnancy/is_pregnant/pregnant XML attributes were found in extracted lord records.

Counts: 453 named lord NPCCharacter records; 397 vanilla/SandBox; 56 War Sails/NavalDLC; 82 noble clans; 0 duplicate NPC IDs across source modules.

Priority flags and corrections:
STURGIAN priority confirmations:
- Kostoroving: confirmed. XML members: Rolan, Dakhila, Forim, Chastimir.
- Ormidoving: confirmed. XML members: Isvan, Valkava, Zaverena, Vizhduna, Yorig, Tyaska, Svedorn, Izdenka.
- Vezhoving: confirmed. XML members: Ratagost, Yachana, Milanka, Velina, Bovan, Vashorki, Vitomira.
- Togaroving: confirmed. XML members: Vyldur, Dracha, Lashonek, Zheneva, Alvar, Zorina.
- Kuloving: confirmed. XML members: Olek the Old, Varra, Olek, Siga, Apolanea, Urik, Idrun, Rozhivol.
  - Name correction: active Olek is named 'Olek' in XML; 'Olek the Old' is dead_lord_2_1. No literal 'Olek the Young' string was found.
- Gundaroving: CORRECTION NEEDED missing/renamed: Tenir, Vyldur. XML members: Raganvad, Asta, Simir, Mimir, Valla, Vidar, Lilizha, Andruta, Luda, Teta.
  - Name correction: XML has Vidar as Raganvad's uncle (lord_2_13, with the comment 'Raganvad uncle. Decent, loyal, not very thoughtful'). It has no active Gundaroving 'Vyldur' or 'Young Tenir' record.
- Vagiroving: confirmed. XML members: Godun, Erta, Lek, Svana, Osven.
- Bovan traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind).
- Zorina pregnancy state: no pregnancy/is_pregnant attribute found in the XML hero or NPCCharacter records; Bannerlord XML here lists family links only.
  - Zorina [lord_2_24_1, SandBox, Togaroving]: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating).
NORD/NORDVYG priority confirmations:
- Throsniring (clan_nord_1): leader Halthdar; members Volbjorn the Hungry, Ilrika, Halthdar, Jarminja, Mjalrik, Sidunric, Thyrsif, Orvi, Gunjadrid, Yfinja, Morgunja, Valmua; holdings Thronderlag, Skarthness Castle.
- Kjolding (clan_nord_2): leader Grykka; members Grykka, Gautgar, Iridrun, Heimkir, Agrynja, Dyfa; holdings Gretysfjord, Tharklif Castle.
- Orthling (clan_nord_3): leader Asgotha; members Asgotha, Vulthir, Kjarvon, Aelfeyja, Njasnir; holdings Hvalvik, Hakarshus Castle.
- Skylfing (clan_nord_4): leader Gornlautir; members Gornlautir, Gulsyf, Alrika, Stohrith, Kautas, Alsa, Svorni, Bjolablum; holdings Hargard, Haugr Castle.
- Gauting (clan_nord_5): leader Horgar; members Horgar, Skathja, Bjorgir, Hralsa, Yngvar, Vystrun; holdings Agilting Castle.
- Rungniring (clan_nord_6): leader Gafnir; members Gafnir, Vitharsura, Karlek, Ulvirinja, Olvira; holdings Ykerslund Castle.
- Huldring (clan_nord_7): leader Murin; members Unjort, Tovsja, Gudrinja, Svalsa, Orthogar, Liljan, Murin; holdings Ulikshorn Castle.
- Dvarroving (clan_nord_8): leader Toverik; members Toverik, Hvana; holdings Brunmark Castle.
- Visduring (clan_nord_9): leader Dagvi; members Dagvi, Drivana, Otfar, Anle, Triven; holdings Fimbulgard Castle.
- Halthdar Throsniring confirmed: lord_7_1, clan Throsniring, traits Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive).
BATTANIAN priority confirmations:
- Taorse: found in fen Eingal (lord_5_21_2, SandBox); culture Battania; traits Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset).
- Culharn: found in fen Uvain (lord_5_9, SandBox); culture Battania; traits Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive).
- Brighan: found in fen Eingal (lord_5_17_1, SandBox); culture Battania; traits Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating).
- Melidir: found in fen Uvain (lord_5_5, SandBox); culture Battania; traits Generosity +1 (Generous); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset).
- Alcaea: found in fen Uvain (lord_5_6, SandBox); culture Empire; traits Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset).
- Grovebound sub-faction XML check: no Grovebound clan/faction roster XML was found in vanilla SandBox/SandBoxCore or NavalDLC ModuleData. Taorse and Culharn appear as active Battanian clan members, not as removed-to-Grovebound entries.
- Brighan pregnancy state: no pregnancy/is_pregnant attribute found in XML.
TWO-VYLDUR disambiguation:
- Vyldur: lord_2_17, clan Togaroving, source SandBox, traits Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind), settlements Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC].
- CORRECTION NEEDED: expected two Vyldurs, found 1. Active XML confirms Vyldur Togaroving only; Gundaroving uses Vidar as Raganvad's uncle.
Frozen pregnancies:
- No XML attributes matching pregnancy/is_pregnant/pregnant were found on extracted lord Hero or NPCCharacter records. Zorina and Brighan are not marked pregnant in these XML files.

Discrepancy notes:
Discrepancy source: compared against task priority claims and the local source design file at C:\Users\korom\Downloads\BANNERWAKE_DESIGN.txt.
CORRECTION NEEDED: the local source design file contains SECTION 9d, but no literal SECTION 9e/9f/9g headings were found; later discrepancy checks should use the latest full design if those sections live elsewhere.
Design cross-check: 'Vyldur' was not found inside the local SECTION 9d excerpt; priority confirmation below is therefore XML-first.
Design cross-check: 'Zorina' was not found inside the local SECTION 9d excerpt; priority confirmation below is therefore XML-first.
Design cross-check: 'Brighan' was not found inside the local SECTION 9d excerpt; priority confirmation below is therefore XML-first.
Design cross-check: 'Taorse' was not found inside the local SECTION 9d excerpt; priority confirmation below is therefore XML-first.
Design cross-check: 'Culharn' was not found inside the local SECTION 9d excerpt; priority confirmation below is therefore XML-first.
Design cross-check: 'Halthdar' was not found inside the local SECTION 9d excerpt; priority confirmation below is therefore XML-first.

Roster:

## Northern Empire

### Argoros (id clan_empire_north_2; culture Empire; home town_EN1; owner Manteos)
  Clan XML note: Aristocratic clan - head of west empire Patriarch 1_1 - Clearcos Lady - Very high sense of
                 decorum Heir 21 - Equally strong sense of entitlement "The Osticoi are one of the oldest
                 families in the Empire, and the wealthiest. They have always resented it when the Emperor
                 is chosen from another dynasty.
Veneranda Argoros (Argoros)
  ID/Source: lord_1_1_3 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: ironic
  Note: none listed
  Family: spouse Andros
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Phalarisa Argoros (Argoros)
  ID/Source: lord_1_1_4 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Belithor
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Presciana Argoros (Argoros)
  ID/Source: lord_1_1_5 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Manteos, mother Phenoria; siblings Adrichea, Maurentios, Sora
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Adrichea Argoros (Argoros)
  ID/Source: lord_1_1_6 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: softspoken
  Note: none listed
  Family: parents father Manteos, mother Phenoria; siblings Maurentios, Presciana, Sora
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Andros Argoros (Argoros)
  ID/Source: lord_1_22 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: Andros. Heir clan 2. Generally benevolent
  Family: none listed
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Manteos Argoros (Argoros)
  ID/Source: lord_1_3 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Phenoria; children Adrichea, Maurentios, Presciana, Sora
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Sora Argoros (Argoros)
  ID/Source: lord_1_32 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: Sora, Matthis' daughter. Honorable, a bit moralistic, conscientious ruler
  Family: parents father Manteos, mother Phenoria; siblings Adrichea, Maurentios, Presciana
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Phenoria Argoros (Argoros)
  ID/Source: lord_1_4 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Phenoria, matriarch of clan 2,
  Family: spouse Manteos; children Adrichea, Maurentios, Presciana, Sora
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Belithor Argoros (Argoros)
  ID/Source: lord_1_42 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: clan 2 lieutenant. Mathhis cousin. Ferocious, dedicated to the clan. One eyed
  Family: none listed
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]
Maurentios Argoros (Argoros)
  ID/Source: lord_1_422 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Maurentios, younger son of Neretzes
  Family: parents father Manteos, mother Phenoria; siblings Adrichea, Presciana, Sora
  Settlement: Ataconia Castle [castle_EN6, castle, NavalDLC], Epicrotea [town_EN1, town, NavalDLC]

### Chonis (id clan_empire_north_6; culture Empire; home castle_EN2; owner Nicasor)
Justina Chonis (Chonis)
  ID/Source: lord_1_1_15 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: none listed
  Family: spouse Olypos; children Leontia
  Settlement: Lochana Castle [castle_EN2, castle, NavalDLC]
Leontia Chonis (Chonis)
  ID/Source: lord_1_1_16 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: parents father Olypos, mother Justina
  Settlement: Lochana Castle [castle_EN2, castle, NavalDLC]
Nicasor Chonis (Chonis)
  ID/Source: lord_1_51 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Nicasor. Gruff but very competent fanatic, lucon's faction. One eyed
  Family: none listed
  Settlement: Lochana Castle [castle_EN2, castle, NavalDLC]
Olypos Chonis (Chonis)
  ID/Source: lord_1_67 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Olypos, older. Genuine republican, military-oriented Cicero
  Family: children Leontia
  Settlement: Lochana Castle [castle_EN2, castle, NavalDLC]

### Dolentos (id clan_empire_north_5; culture Empire; home town_EN5; owner Gyphor)
Tyliana Dolentos (Dolentos)
  ID/Source: lord_1_1_14 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Gyphor
  Settlement: Myzea [town_EN5, town, NavalDLC]
Variasis Dolentos (Dolentos)
  ID/Source: lord_1_1_17 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Unreliable, rather unpleasant member of the clan
  Family: none listed
  Settlement: Myzea [town_EN5, town, NavalDLC]
Gyphor Dolentos (Dolentos)
  ID/Source: lord_1_50 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Gyphor. Calm, lucon's faction
  Note: Gyphor. Calm, lucon's faction
  Family: none listed
  Settlement: Myzea [town_EN5, town, NavalDLC]
Lantanor Dolentos (Dolentos)
  ID/Source: lord_1_66 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Lantanor, opportunist. Somewhat like Primus. Gyphor's more aggressive cousin
  Family: none listed
  Settlement: Myzea [town_EN5, town, NavalDLC]

### Impestores (id clan_empire_north_4; culture Empire; home town_EN6; owner Encurion)
  Clan XML note: Unsympathetic: close-minded Patriarch (1_5) is imperial blowhard Heir 23 - is younger
                 imperial blowhard Lieutenant
Epipheria Impestores (Impestores)
  ID/Source: lord_1_1_12 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Epipheria is a noblewoman of the Impestores, a clan noted for their fanatical loyalty to the
        aristocratic, oligarchic wing of the Senate and their personal eccentricities. Unlike most of the
        women of the oligarchs, who tend to be conservative, she trained as a warrior. At the outbreak of
        the civil war, she took some of her family's famed wealth to raise her own warband to fight the
        'tyrant' Rhagaea and the 'upstart' Garios in the name of senatorial supremacy.
  Note: Encurion's cousin
  Family: none listed
  Settlement: Amprela [town_EN6, town, NavalDLC]
Agnathea Impestores (Impestores)
  ID/Source: lord_1_1_13 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Miron
  Settlement: Amprela [town_EN6, town, NavalDLC]
Encurion Impestores (Impestores)
  ID/Source: lord_1_20 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Impestores, Lucon's faction. Different personalities but fanatic oligarchs
  Note: Leader of Impestores. Ruthless aristocrat
  Family: none listed
  Settlement: Amprela [town_EN6, town, NavalDLC]
Miron Impestores (Impestores)
  ID/Source: lord_1_64 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: Miron, eccentric stoic. Lucon
  Family: none listed
  Settlement: Amprela [town_EN6, town, NavalDLC]

### Neretzes (id clan_empire_north_3; culture Empire; home town_EN3; owner Penton)
  Clan XML note: Sympathetic: O Philosophical clan? Views Osticos as most likely to restore republic
                 Patriarch 1_3, stoic - Stenecos Heir 22 Lieutenant - loyal Volorias MINOR FACTION: POSITIVE
                 ties to lost legion "The Argoroi hold to the ideals of the republic, and would probably
                 like to see the Emperor made subject to the Senate. They are known for long speeches in the
                 Senate on honor and virtue. Stenecos is a dour man, who expects much of himself and much of
                 others. But they are known for being trustworthy, and diligent in their execution of
                 warfare against the Empire's enemies."
Rhoda Neretzes (Neretzes)
  ID/Source: lord_1_1_10 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: none listed
  Family: parents father Chason, mother Eodisia; siblings Amaliana
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Amaliana Neretzes (Neretzes)
  ID/Source: lord_1_1_11 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: parents father Chason, mother Eodisia; siblings Rhoda
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Hylasiana Neretzes (Neretzes)
  ID/Source: lord_1_1_7 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Penton; children Apolytea, Chalia, Phadon
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Apolytea Neretzes (Neretzes)
  ID/Source: lord_1_1_8 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: parents father Penton, mother Hylasiana; siblings Chalia, Phadon
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Eodisia Neretzes (Neretzes)
  ID/Source: lord_1_1_9 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Chason; children Amaliana, Rhoda
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Chalia Neretzes (Neretzes)
  ID/Source: lord_1_33 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Chalia, Neretzes' daughter. Clan 3 daughter. Much more astute than her parents.
  Family: parents father Penton, mother Hylasiana; siblings Apolytea, Phadon
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Chason Neretzes (Neretzes)
  ID/Source: lord_1_43 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Chason. clan 3 lieutenant. Foul tempered
  Family: children Amaliana, Rhoda
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Penton Neretzes (Neretzes)
  ID/Source: lord_1_5 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Penton Neretzes was the son of the old emperor, Drosios Neretzes, killed at the Battle of Pendraic.
        Emperors' sons usually inherited the diadem, but that was custom, not law, and the Senate chose the
        general Arenicos instead. Most emperors would then have discretely eliminated such a potential
        challenger, but Arenicos took a calculated risk in the interest of imperial unity, and kept Penton
        alive. The Neretzes family traditionally were part of the oligarchic faction of the Empire and
        Penton now backs Lucon in the civil war.
  Note: Clan 3 patriarch Penton Neretzes is imperial blowhard, part of aristocratic imperial faction
  Note: USED TO DERIVE SKILLS
  Family: children Apolytea, Chalia, Phadon
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]
Phadon Neretzes (Neretzes)
  ID/Source: lord_1_6 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Alena, Penton's wife, removed
  Note: USED TO DERIVE SKILLS
  Family: parents father Penton, mother Hylasiana; siblings Apolytea, Chalia
  Settlement: Varagos Castle [castle_EN1, castle, NavalDLC], Gaos Castle [castle_EN4, castle, NavalDLC], Saneopa [town_EN3, town, NavalDLC]

### Osticos (id clan_empire_north_1; culture Empire; home town_EN2; owner Lucon)
  Clan XML note: <Faction id="freemen" initial_posX="136.0" initial_posY="504.0" label_color="714833"
                 color="714833" color2="FFFF66FF" alternative_color="FFFF66FF" alternative_color2="714833"
                 culture="Culture.vlandia"
                 default_party_template="PartyTemplate.kingdom_hero_party_eleftheroi_template"
                 encounterbackgroundmesh="gui_bg_lord_empire" settlement_banner_mesh="encounter_flag_f"
                 is_minor_faction="true" is_outlaw="true" is_nomad="true" name="Freemen of the Marshes">
                 </Faction>
  Clan XML note: Aristocratic starting kingdom
Lucon Osticos (Osticos)
  ID/Source: lord_1_1 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: The northern third of the Empire is ruled by Lucon, who represents a long-standing oligarchic trend
        in imperial politics. It holds that strict adherence to imperial law is the best guarantee that the
        empire will not become a tyranny. Oligarchs like Lucon also tend to believe that only landowners can
        have the extensive education, experience in government, and stake in property to really understand
        and appreciate the law, and thus the Senate should be supreme.
  Note: EMPIRE: empire horsemean armor, legionary mail, imperial_mail_over_leather,
        imperial_lamellar_over_leather, imperial_mail_vest, imperial_lamellar
  Note: Male noble: imperial robes
  Note: Female noble: empire_dress
  Note: Sturgia: leather and iron plate armor
  Note: Sturgia nobleman: heavy nordic tunic
  Note: Sturgia noblewoman: laced dress
  Note: Vlandia: Vlandia chainmail, hauberk
  Note: Vlandia nobleman: long woolen tunic
  Note: Battania: Battania dress (#3)
  Note: Aserai warrior: Brass lamellar over mail
  Note: Aserai nobleman: Tassled southern robes, aserai tunic waistcoat
  Note: Aserai noblewoman: Fine southern dress, layered robe
  Note: Khuzait warrior: Khuzait lamellar strapped
  Note: Khuzait nobleman: Eastern silk clothing
  Note: ANCESTORS END
  Family: spouse Zerosica; children Ascyron, Zoana
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Susada Osticos (Osticos)
  ID/Source: lord_1_1_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Arcor
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Decantia Osticos (Osticos)
  ID/Source: lord_1_1_2 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Ascyron
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Zerosica Osticos (Osticos)
  ID/Source: lord_1_2 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Lucon's wife. Traditional matriarch, benevolent
  Note: USED TO DERIVE SKILLS
  Note: PERSONALITY/REPUTATION
  Family: spouse Lucon; children Ascyron, Zoana
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Ascyron Osticos (Osticos)
  ID/Source: lord_1_21 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: earnest
  Note: Lords 1-20 are clan patriarchs and their wives/>
  Note: Lords 21-30 are marriageable heirs/>
  Note: Ascyron, Lucon's heir, Sulla type. More enthusiastic than father. Switch with Apys?
  Family: parents father Lucon, mother Zerosica; siblings Zoana
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Zoana Osticos (Osticos)
  ID/Source: lord_1_31 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Lords 31-40 are marriageable daughters Combatants are: Ira, Rhagaea's daughter
  Family: parents father Lucon, mother Zerosica; siblings Ascyron
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Arcor Osticos (Osticos)
  ID/Source: lord_1_41 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: Lords 41-50 lieutenants, uncles and others of the clans
  Note: clan 1 lieutenant. Lucon's cousin. Far more ruthless than the clan leader
  Family: spouse Susada; children Arion
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]
Arion Osticos (Osticos)
  ID/Source: lord_1_411 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: none listed
  Family: parents father Arcor
  Settlement: Atrion Castle [castle_EN5, castle, NavalDLC], Mecalovea Castle [castle_EN9, castle, NavalDLC], Diathma [town_EN2, town, NavalDLC], Argoron [town_EN4, town, NavalDLC]

### Phalentes (id clan_empire_north_7; culture Empire; home castle_EN7; owner Tasynor)
Tasynor Phalentes (Phalentes)
  ID/Source: lord_1_58 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Tasynor, Lucon's faction. Smug, privileged, self-righteous
  Family: none listed
  Settlement: Epinosa Castle [castle_EN7, castle, NavalDLC]
Panalea Phalentes (Phalentes)
  ID/Source: lord_1_70 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Panalea, Heiress. Husband a general for Garios, he spoke up for her. Senate vote did not recognize
        her right to inherit
  Family: none listed
  Settlement: Epinosa Castle [castle_EN7, castle, NavalDLC]
Nesthys Phalentes (Phalentes)
  ID/Source: lord_NE7_u / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Nesthys, quiet strategist
  Family: none listed
  Settlement: Epinosa Castle [castle_EN7, castle, NavalDLC]

### Serapides (id clan_empire_north_9; culture Empire; home castle_EN3; owner Porphalios)
Vamina Serapides (Serapides)
  ID/Source: lord_NE9_d / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: parents father Porphalios; siblings Aesos
  Settlement: Rhesos Castle [castle_EN3, castle, NavalDLC]
Porphalios Serapides (Serapides)
  ID/Source: lord_NE9_l / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Serapides, latter-day Scipios. Angry that moment of glory has passed
  Family: children Aesos, Vamina
  Settlement: Rhesos Castle [castle_EN3, castle, NavalDLC]
Aesos Serapides (Serapides)
  ID/Source: lord_NE9_s / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Silasos, wishes to rebuild the clan
  Family: parents father Porphalios; siblings Vamina
  Settlement: Rhesos Castle [castle_EN3, castle, NavalDLC]

### Vatatzes (id clan_empire_north_8; culture Empire; home castle_EN8; owner Maritzios)
Seranor Vatatzes (Vatatzes)
  ID/Source: lord_1_56 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: spouse Germana; children Rustica
  Settlement: Syratos Castle [castle_EN8, castle, NavalDLC]
Germana Vatatzes (Vatatzes)
  ID/Source: lord_1_56_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: spouse Seranor; children Rustica
  Settlement: Syratos Castle [castle_EN8, castle, NavalDLC]
Theavisos Vatatzes (Vatatzes)
  ID/Source: lord_NE8_c1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Theavisos, dissolute heir. (I like to have these as commented lines separating skill traits from
        personality traits)
  Family: parents father Maritzios, mother Pradentia; siblings Lucala
  Settlement: Syratos Castle [castle_EN8, castle, NavalDLC]
Lucala Vatatzes (Vatatzes)
  ID/Source: lord_NE8_c2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Maritzios, mother Pradentia; siblings Theavisos
  Settlement: Syratos Castle [castle_EN8, castle, NavalDLC]
Maritzios Vatatzes (Vatatzes)
  ID/Source: lord_NE8_l / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Vatatzes clan. Non-ideological but served with Lucon
  Family: spouse Pradentia; children Lucala, Theavisos
  Settlement: Syratos Castle [castle_EN8, castle, NavalDLC]
Pradentia Vatatzes (Vatatzes)
  ID/Source: lord_NE8_s / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: spouse Maritzios; children Lucala, Theavisos
  Settlement: Syratos Castle [castle_EN8, castle, NavalDLC]

## Western Empire

### Comnos (id clan_empire_west_1; culture Empire; home town_EW2; owner Garios)
  Clan XML note: Populist starting kingdom - WEST
Tadeos Comnos (Comnos)
  ID/Source: lord_1_24 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: garios's son or nephew, traits not set. younger than father. Switch face with someone else
  Family: none listed
  Settlement: Onica Castle [castle_EW3, castle, NavalDLC], Zeonica [town_EW2, town, NavalDLC], Jalmarys [town_EW3, town, NavalDLC]
Nadea Comnos (Comnos)
  ID/Source: lord_1_34 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Nadea, Gario's daughter. Huntress.
  Family: parents father Garios, mother Vendelia
  Settlement: Onica Castle [castle_EW3, castle, NavalDLC], Zeonica [town_EW2, town, NavalDLC], Jalmarys [town_EW3, town, NavalDLC]
Nemos Comnos (Comnos)
  ID/Source: lord_1_44 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: Nemos. clan 4 lieutenant for gario. dedicated to gario. stern
  Family: none listed
  Settlement: Onica Castle [castle_EW3, castle, NavalDLC], Zeonica [town_EW2, town, NavalDLC], Jalmarys [town_EW3, town, NavalDLC]
Garios Comnos (Comnos)
  ID/Source: lord_1_7 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: The western third of the Empire is ruled by Garios, a charismatic general who represents a
        longstanding populist trend in imperial politics. He is deeply loved by his soldiers, both for his
        solid record in winning battles and for his insistence that his veterans be compensated in land
        afterwards. He often demands that the 'people' should settle key issues, but in practice this
        usually means an assembly of his soldiers, where his veterans can be counted on to shut down
        opposition.
  Note: USED TO DERIVE SKILLS
  Note: PERSONALITY/REPUTATION
  Family: spouse Vendelia; children Nadea, Thephilos
  Settlement: Onica Castle [castle_EW3, castle, NavalDLC], Zeonica [town_EW2, town, NavalDLC], Jalmarys [town_EW3, town, NavalDLC]
Thephilos Comnos (Comnos)
  ID/Source: lord_1_75 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: parents father Garios
  Settlement: Onica Castle [castle_EW3, castle, NavalDLC], Zeonica [town_EW2, town, NavalDLC], Jalmarys [town_EW3, town, NavalDLC]
Vendelia Comnos (Comnos)
  ID/Source: lord_1_8 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Vendelia, somewhat bitter, feels she is taken for granted by Gario, accepts her marriage as a duty
  Note: USED TO DERIVE SKILLS
  Note: PERSONALITY/REPUTATION
  Family: spouse Garios; children Nadea
  Settlement: Onica Castle [castle_EW3, castle, NavalDLC], Zeonica [town_EW2, town, NavalDLC], Jalmarys [town_EW3, town, NavalDLC]

### Corenios (id clan_empire_west_7; culture Empire; home castle_EW5; owner Achios)
Achios Corenios (Corenios)
  ID/Source: lord_1_53 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: ironic
  Note: Achios. A talent for dealing with common soldiers, but ruthless. Napoleon/Trotsky type. Garios
        faction
  Family: none listed
  Settlement: Veron Castle [castle_EW5, castle, NavalDLC]
Ovagos Corenios (Corenios)
  ID/Source: lord_1_73 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Popilia
  Settlement: Veron Castle [castle_EW5, castle, NavalDLC]
Popilia Corenios (Corenios)
  ID/Source: lord_1_73_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Ovagos
  Settlement: Veron Castle [castle_EW5, castle, NavalDLC]

### Dionicos (id clan_empire_west_3; culture Empire; home town_EW1; owner Crotor)
  Clan XML note: Fully unsympathetic clan - terrorizes their valley Apokos, Father - debauched, based on
                 Alexius Apokaukos, master schemer Heir 25 - charismatic psychopath Heiress leads armies -
                 equally charismatic psychopath MINOR FACTION: POSITIVE ties to Hidden Ones
Crotor Dionicos (Dionicos)
  ID/Source: lord_1_11 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Crotor's family, the house of Dionicos, has taken charge of the empire's northwestern defenses for
        generations. The clan's leaders are more likely to keep the company of border raiders and scouts
        than senators in the capital. Crotor has backed Garios in the civil war, largely due to his innate
        sense of loyalty to a fellow comrade-in-arms.
  Note: crotor, patriarch clan 5, akritic border guards />
  Family: spouse Lysica; children Casinon, Meritor, Phaea
  Settlement: Thractorae Castle [castle_EW4, castle, NavalDLC], Lageta [town_EW1, town, NavalDLC]
Casinon Dionicos (Dionicos)
  ID/Source: lord_1_111 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: none listed
  Family: parents father Crotor, mother Lysica; siblings Meritor, Phaea
  Settlement: Thractorae Castle [castle_EW4, castle, NavalDLC], Lageta [town_EW1, town, NavalDLC]
Lysica Dionicos (Dionicos)
  ID/Source: lord_1_12 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Lysica is the wife of Crotor, a frontier lord in the western empire. Like many noblewomen in the
        border countries, she learned to ride, shoot, and lead men, often taking the lead in defending clan
        lands when her husband is away.
  Note: Lysica Dionikos, dutiful frontier nobility. Fighter
  Family: spouse Crotor; children Casinon, Meritor, Phaea
  Settlement: Thractorae Castle [castle_EW4, castle, NavalDLC], Lageta [town_EW1, town, NavalDLC]
Meritor Dionicos (Dionicos)
  ID/Source: lord_1_26 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Dionicos heir - border lords, also cautious tactician
  Family: parents father Crotor, mother Lysica; siblings Casinon, Phaea
  Settlement: Thractorae Castle [castle_EW4, castle, NavalDLC], Lageta [town_EW1, town, NavalDLC]
Phaea Dionicos (Dionicos)
  ID/Source: lord_1_36 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Phaea is a noblewoman of the house of Dionicos, traditional wardens of the empire's frontier with
        Battania. Like her mother, Lysica, she has trained to fight and to lead men in battle, so that the
        frontiers can still be defended when the clan patriarchs are away at war.
  Note: Phaea. Dionikos daughter. Mother is also combatant
  Note: COMBATANT
  Family: parents father Crotor, mother Lysica; siblings Casinon, Meritor
  Settlement: Thractorae Castle [castle_EW4, castle, NavalDLC], Lageta [town_EW1, town, NavalDLC]

### Elaches (id clan_empire_west_4; culture Empire; home town_EW5; owner Tynops)
  Clan XML note: Sympathetic - Border guards - many sacrifices but much sense of entitlement Ancestor was
                 Asurai emir Draw on Akritic ballads
Tynops Elaches (Elaches)
  ID/Source: lord_1_40 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: Tynops Enaches. Goodnatured, garios faction.
  Family: spouse Catella
  Settlement: Thorios Castle [castle_EW2, castle, NavalDLC], Amitatys [town_EW5, town, NavalDLC]
Catella Elaches (Elaches)
  ID/Source: lord_1_40_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Tynops's wife.
  Family: spouse Tynops
  Settlement: Thorios Castle [castle_EW2, castle, NavalDLC], Amitatys [town_EW5, town, NavalDLC]
Milos Elaches (Elaches)
  ID/Source: lord_1_46 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: clanless empire lords
  Note: Moralist
  Family: children Seorgys
  Settlement: Thorios Castle [castle_EW2, castle, NavalDLC], Amitatys [town_EW5, town, NavalDLC]
Seorgys Elaches (Elaches)
  ID/Source: lord_1_46_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Young populist, had ambitions but also genuinely compassionate
  Family: parents father Milos
  Settlement: Thorios Castle [castle_EW2, castle, NavalDLC], Amitatys [town_EW5, town, NavalDLC]

### Lonalion (id clan_empire_west_5; culture Empire; home town_EW6; owner Desporion)
Desporion Lonalion (Lonalion)
  ID/Source: lord_1_45 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: Lonalion clan, backs Lucon. Fierce, rather cruel warriors.
  Note: Desporion - Ibn tughluq type. honorable, but easily infuriated. Formerly clan 5 uncle. Garios
  Family: spouse Agnala; children Nereida, Phostor
  Settlement: Rhotae [town_EW6, town, NavalDLC]
Agnala Lonalion (Lonalion)
  ID/Source: lord_1_45_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Desporion; children Nereida, Phostor
  Settlement: Rhotae [town_EW6, town, NavalDLC]
Phostor Lonalion (Lonalion)
  ID/Source: lord_1_45_2 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: parents father Desporion, mother Agnala; siblings Nereida
  Settlement: Rhotae [town_EW6, town, NavalDLC]
Nereida Lonalion (Lonalion)
  ID/Source: lord_1_45_3 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Desporion, mother Agnala; siblings Phostor
  Settlement: Rhotae [town_EW6, town, NavalDLC]
Altenos Lonalion (Lonalion)
  ID/Source: lord_1_57 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Altenos. Younger enthusiast, less thoughtful than others. Garios faction
  Family: spouse Sophalia; children Jephalia
  Settlement: Rhotae [town_EW6, town, NavalDLC]
Sophalia Lonalion (Lonalion)
  ID/Source: lord_1_57_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: spouse Altenos; children Jephalia
  Settlement: Rhotae [town_EW6, town, NavalDLC]
Jephalia Lonalion (Lonalion)
  ID/Source: lord_1_57_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: TWO-YEAR OLD
  Family: parents father Altenos, mother Sophalia
  Settlement: Rhotae [town_EW6, town, NavalDLC]

### Maneolis (id clan_empire_west_8; culture Empire; home castle_EW6; owner Vipon)
Vipon Maneolis (Maneolis)
  ID/Source: lord_1_71 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Maneolis clan, West 8. Vipon. Cruel. Ambitious
  Family: none listed
  Settlement: Hertogea Castle [castle_EW6, castle, NavalDLC]
Icratia Maneolis (Maneolis)
  ID/Source: lord_WE8_c / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: none listed
  Settlement: Hertogea Castle [castle_EW6, castle, NavalDLC]
Varmyros Maneolis (Maneolis)
  ID/Source: lord_WE8_u / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Placeholder face
  Family: none listed
  Settlement: Hertogea Castle [castle_EW6, castle, NavalDLC]

### Palladios (id clan_empire_west_9; culture Empire; home castle_EW7; owner Vincantios)
Vincantios Palladios (Palladios)
  ID/Source: lord_WE9_l / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Vincantios, somewhat dull clan leader and his much sharper sister
  Note: Placeholder face value
  Note: Leader of the clan
  Family: none listed
  Settlement: Oristocorys Castle [castle_EW7, castle, NavalDLC]
Euresa Palladios (Palladios)
  ID/Source: lord_WE9_u / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Political driver of the clan, genuine populist
  Family: spouse Torvasis
  Settlement: Oristocorys Castle [castle_EW7, castle, NavalDLC]
Torvasis Palladios (Palladios)
  ID/Source: lord_WE9_u2 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: husband of Euresa, much older, honest but not much else
  Family: spouse Euresa
  Settlement: Oristocorys Castle [castle_EW7, castle, NavalDLC]

### Sorados (id clan_empire_west_6; culture Empire; home castle_EW8; owner Saratis)
Saratis Sorados (Sorados)
  ID/Source: lord_1_52 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Saratis. Clever, but does not like to fight. Garios
  Family: spouse Minarvina; children Megarita
  Settlement: Gersegos Castle [castle_EW8, castle, NavalDLC]
Minarvina Sorados (Sorados)
  ID/Source: lord_1_52_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Saratis; children Megarita
  Settlement: Gersegos Castle [castle_EW8, castle, NavalDLC]
Megarita Sorados (Sorados)
  ID/Source: lord_1_52_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: TEENAGER
  Family: parents father Saratis, mother Minarvina
  Settlement: Gersegos Castle [castle_EW8, castle, NavalDLC]
Sejaron Sorados (Sorados)
  ID/Source: lord_1_62 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Sejaron. Outward veneer of professionalism, ruthless ambition beneath. Garios
  Family: spouse Arytha
  Settlement: Gersegos Castle [castle_EW8, castle, NavalDLC]
Arytha Sorados (Sorados)
  ID/Source: lord_1_62_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Sejaron's wife. Gracious but equally devious
  Family: spouse Sejaron
  Settlement: Gersegos Castle [castle_EW8, castle, NavalDLC]

### Varros (id clan_empire_west_2; culture Empire; home town_EW4; owner Apys)
Melkea Varros (Varros)
  ID/Source: lord_1_10 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Melkea, wife of Apys Varros. Equally amoral.
  Family: spouse Apys; children Eronyx, Jastion
  Settlement: Garontor Castle [castle_EW1, castle, NavalDLC], Ortysia [town_EW4, town, NavalDLC]
Jastion Varros (Varros)
  ID/Source: lord_1_23 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Heir clan 3, Neretzes. Shallow like his father, good voice though
  Family: parents father Apys, mother Melkea; siblings Eronyx
  Settlement: Garontor Castle [castle_EW1, castle, NavalDLC], Ortysia [town_EW4, town, NavalDLC]
Eronyx Varros (Varros)
  ID/Source: lord_1_25 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: earnest
  Note: Apys Varros heir - charismatic psychopath
  Family: parents father Apys, mother Melkea; siblings Jastion
  Settlement: Garontor Castle [castle_EW1, castle, NavalDLC], Ortysia [town_EW4, town, NavalDLC]
Amenon Varros (Varros)
  ID/Source: lord_1_35 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: Face key needs redoing, repurposed from female
  Note: Amenon, Apys's dutiful lieutenant.
  Family: none listed
  Settlement: Garontor Castle [castle_EW1, castle, NavalDLC], Ortysia [town_EW4, town, NavalDLC]
Apys Varros (Varros)
  ID/Source: lord_1_9 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor -1 (Cautious); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Apys Varros was one of the most notoriously debauched, unscrupulous, and wealthy members of the old
        imperial Senate. But he made an early alliance with Garios, in whom he recognized a rising star.
        Garios provided the fame, Apys provided the money. And even if the populist general ever puts one of
        his land redistribution schemes into practice, few doubt that Apys would find a way to emerge even
        richer than before.
  Family: spouse Melkea; children Eronyx, Jastion
  Settlement: Garontor Castle [castle_EW1, castle, NavalDLC], Ortysia [town_EW4, town, NavalDLC]

## Southern Empire

### Avlonos (id clan_empire_south_7; culture Empire; home castle_ES3; owner Serandon)
Serandon Avlonos (Avlonos)
  ID/Source: lord_1_55 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Serandon, humanitarian. rhagaea
  Family: spouse Megethia
  Settlement: Melion Castle [castle_ES3, castle, NavalDLC]
Megethia Avlonos (Avlonos)
  ID/Source: lord_1_55_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: spouse Serandon
  Settlement: Melion Castle [castle_ES3, castle, NavalDLC]
Niphon Avlonos (Avlonos)
  ID/Source: lord_1_69 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Niphon. Attentive, political, deceptive
  Family: spouse Areliana; children Dorathila
  Settlement: Melion Castle [castle_ES3, castle, NavalDLC]
Areliana Avlonos (Avlonos)
  ID/Source: lord_1_69_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: spouse Niphon; children Dorathila
  Settlement: Melion Castle [castle_ES3, castle, NavalDLC]
Dorathila Avlonos (Avlonos)
  ID/Source: lord_1_69_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Niphon, mother Areliana
  Settlement: Melion Castle [castle_ES3, castle, NavalDLC]

### Hongeros (id clan_empire_south_4; culture Empire; home town_ES2; owner Turiados)
  Clan XML note: Hongeros - Turiados is a genuine autocrat. 'I would rather be ruled by the well-fed than
                 the hungry, by one satisfied thief than a hundred frustrated thieves.'
Turiados Hongeros (Hongeros)
  ID/Source: lord_1_30 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: turiados, devious but means well. Rhagaea
  Family: spouse Justina; children Callinia, Synesios
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Justina Hongeros (Hongeros)
  ID/Source: lord_1_30_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Turiados; children Callinia, Synesios
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Callinia Hongeros (Hongeros)
  ID/Source: lord_1_30_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Turiados, mother Justina; siblings Synesios
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Synesios Hongeros (Hongeros)
  ID/Source: lord_1_30_3 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Turiados, mother Justina; siblings Callinia
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Obron Hongeros (Hongeros)
  ID/Source: lord_1_49 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: clan 9 lieutenant. Oros cousin. Selfish and narrow-minded, timid
  Family: spouse Tristania; children Gordiana
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Tristania Hongeros (Hongeros)
  ID/Source: lord_1_49_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: ironic
  Note: none listed
  Family: spouse Obron; children Gordiana
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Gordiana Hongeros (Hongeros)
  ID/Source: lord_1_49_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: TEENAGER
  Family: parents father Obron, mother Tristania
  Settlement: Vostrum [town_ES2, town, NavalDLC]
Rustica Hongeros (Hongeros)
  ID/Source: lord_1_56_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Seranor, mother Germana
  Settlement: Vostrum [town_ES2, town, NavalDLC]

### Julios (id clan_empire_south_5; culture Empire; home town_ES7; owner Baranor)
Baranor Julios (Julios)
  ID/Source: lord_1_63 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Baranor. former guard captain for the emperor. rhagaea. Head of clan 5
  Family: spouse Valaria; children Comatasa, Elidilea
  Settlement: Corenia Castle [castle_ES2, castle, NavalDLC], Syronea [town_ES7, town, NavalDLC]
Valaria Julios (Julios)
  ID/Source: lord_1_63_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Baranor; children Comatasa, Elidilea
  Settlement: Corenia Castle [castle_ES2, castle, NavalDLC], Syronea [town_ES7, town, NavalDLC]
Comatasa Julios (Julios)
  ID/Source: lord_1_63_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Baranor, mother Valaria; siblings Elidilea
  Settlement: Corenia Castle [castle_ES2, castle, NavalDLC], Syronea [town_ES7, town, NavalDLC]
Elidilea Julios (Julios)
  ID/Source: lord_1_63_3 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Baranor, mother Valaria; siblings Comatasa
  Settlement: Corenia Castle [castle_ES2, castle, NavalDLC], Syronea [town_ES7, town, NavalDLC]
Zachanis Julios (Julios)
  ID/Source: lord_1_74 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Zena
  Settlement: Corenia Castle [castle_ES2, castle, NavalDLC], Syronea [town_ES7, town, NavalDLC]
Zena Julios (Julios)
  ID/Source: lord_1_74_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Zachanis
  Settlement: Corenia Castle [castle_ES2, castle, NavalDLC], Syronea [town_ES7, town, NavalDLC]

### Leonipardes (id clan_empire_south_2; culture Empire; home town_ES3; owner Pharon)
  Clan XML note: Head of clan - Queen, niece of the emperor, raised abroad, blood of the Padishah as well
                 Queen's consort - of imperial birth, charismatic but vindictive, Queen's lieutenant -
                 Queen's younger brother and sister - goodnatured
  Clan XML note: Leonipardes- Plutocratic Patriarch #15 - Old-school aristocrat, doing something he finds
                 distasteful to maintain his family's position Cunning, pragmatist heir "The empire is beset
                 on all sides, it defeat its foes, it must absorb them."
Pharon Leonipardes (Leonipardes)
  ID/Source: lord_1_15 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Pharon is patriarch of the Leonipardes, an imperial house that owns vast estates on the hot plains
        of the south. The family has traditionally taken the welfare of its tenants seriously, but expects
        total loyalty from them. He has little to do with the Senate and the politics of the capital.
        Dynastic inheritance seems to him the natural order of things, so he has leaned towards Rhagaea in
        the civil wars.
  Family: spouse Martira; children Helea, Temion, Zeno
  Settlement: Poros [town_ES3, town, NavalDLC]
Zeno Leonipardes (Leonipardes)
  ID/Source: lord_1_155 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Placeholder face
  Family: parents father Pharon, mother Martira; siblings Helea, Temion
  Settlement: Poros [town_ES3, town, NavalDLC]
Martira Leonipardes (Leonipardes)
  ID/Source: lord_1_16 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Martira, sister of Destor, somewhat withdrawn
  Family: spouse Pharon; children Helea, Temion, Zeno
  Settlement: Poros [town_ES3, town, NavalDLC]
Temion Leonipardes (Leonipardes)
  ID/Source: lord_1_28 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Leonipardes heir. Cunning, aggressive, somewhat devious
  Family: parents father Pharon, mother Martira; siblings Helea, Zeno
  Settlement: Poros [town_ES3, town, NavalDLC]
Helea Leonipardes (Leonipardes)
  ID/Source: lord_1_38 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: leonipardes's daughter
  Family: parents father Pharon, mother Martira; siblings Temion, Zeno
  Settlement: Poros [town_ES3, town, NavalDLC]
Joron Leonipardes (Leonipardes)
  ID/Source: lord_1_48 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Leonipardes lieutenant. brave, good-natured, not especially thoughtful.
  Family: spouse Alympia; children Anea, Nonesos
  Settlement: Poros [town_ES3, town, NavalDLC]
Alympia Leonipardes (Leonipardes)
  ID/Source: lord_1_48_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: spouse Joron; children Anea, Nonesos
  Settlement: Poros [town_ES3, town, NavalDLC]
Anea Leonipardes (Leonipardes)
  ID/Source: lord_1_48_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: parents father Joron, mother Alympia; siblings Nonesos
  Settlement: Poros [town_ES3, town, NavalDLC]
Nonesos Leonipardes (Leonipardes)
  ID/Source: lord_1_48_3 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: none listed
  Family: parents father Joron, mother Alympia; siblings Anea
  Settlement: Poros [town_ES3, town, NavalDLC]

### Mestricaros (id clan_empire_south_3; culture Empire; home town_ES1; owner Oros)
  Clan XML note: Mestricaros - Long list of grievances against other large families, sided with Pathros by
                 default Uncle - Cunning, frustrated
Oros Mestricaros (Mestricaros)
  ID/Source: lord_1_17 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Oros Patriarch of Mestrikaros, clan 9, a lord who nurses his grievances
  Note: -Opportunist
  Family: spouse Jathea; children Debana, Honoratus, Sanion
  Settlement: Odrysa Castle [castle_ES1, castle, NavalDLC], Lavenia Castle [castle_ES4, castle, NavalDLC], Danustica [town_ES1, town, NavalDLC]
Honoratus Mestricaros (Mestricaros)
  ID/Source: lord_1_177 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: -Opportunist
  Family: parents father Oros, mother Jathea; siblings Debana, Sanion
  Settlement: Odrysa Castle [castle_ES1, castle, NavalDLC], Lavenia Castle [castle_ES4, castle, NavalDLC], Danustica [town_ES1, town, NavalDLC]
Jathea Mestricaros (Mestricaros)
  ID/Source: lord_1_18 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Hythea, wealthy and somewhat garish />
  Note: NONCOMBATANT
  Family: spouse Oros; children Debana, Honoratus, Sanion
  Settlement: Odrysa Castle [castle_ES1, castle, NavalDLC], Lavenia Castle [castle_ES4, castle, NavalDLC], Danustica [town_ES1, town, NavalDLC]
Sanion Mestricaros (Mestricaros)
  ID/Source: lord_1_29 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Sanion - heir to clan 9. Knight-errant type
  Family: parents father Oros, mother Jathea; siblings Debana, Honoratus
  Settlement: Odrysa Castle [castle_ES1, castle, NavalDLC], Lavenia Castle [castle_ES4, castle, NavalDLC], Danustica [town_ES1, town, NavalDLC]
Debana Mestricaros (Mestricaros)
  ID/Source: lord_1_39 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: ironic
  Note: clan 9 daughter. Debana Mestrikaros. Conventional but a bit off />
  Family: parents father Oros, mother Jathea; siblings Honoratus, Sanion
  Settlement: Odrysa Castle [castle_ES1, castle, NavalDLC], Lavenia Castle [castle_ES4, castle, NavalDLC], Danustica [town_ES1, town, NavalDLC]

### Pethros (id clan_empire_south_1; culture Empire; home town_ES4; owner Rhagaea)
  Clan XML note: Monarchist starting kingdom
Rhagaea Pethros (Pethros)
  ID/Source: lord_1_14 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: The southern third of the Empire is ruled by Rhagaea, widow of the murdered emperor. For her,
        politics is personal: all men want their families to inherit what they have, and if you loved
        Arenicos then you will support the rights of his heirs. Arenicos was indeed loved, and also there
        are some Calradians who believe that the endless squabbling and civil wars can only be overcome by a
        king, or, if necessary, by a queen.
  Note: voice changed to softspoken, Nov2022
  Note: Rhagaea needs to be at least in her mid-40s, as she has a grown daughter. She needs to be
        attractive, with searching eyes.
  Family: children Ira
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Patyr Pethros (Pethros)
  ID/Source: lord_1_27 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Verina; children Eutropios, Vasilia
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Verina Pethros (Pethros)
  ID/Source: lord_1_27_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: spouse Patyr; children Eutropios, Vasilia
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Eutropios Pethros (Pethros)
  ID/Source: lord_1_27_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: parents father Patyr, mother Verina; siblings Vasilia
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Vasilia Pethros (Pethros)
  ID/Source: lord_1_27_3 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Patyr's younger daughter
  Family: parents father Patyr, mother Verina; siblings Eutropios
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Ira Pethros (Pethros)
  ID/Source: lord_1_37 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Ira is the daughter of Rhagaea, one of the three claimants to the imperial throne, and the slain
        emperor Arenicos. At one point, her father appeared to be grooming her as his heir. But though she
        took well to military campaigns, she also displayed a wild side unbecoming of imperial dignity,
        carousing in taverns with other young aristocrats and even appearing in the arenas as a gladiator.
        She is Rhagaea's heir-apparent, but her mother makes no secret of wishing to find her a responsible
        consort to ensure the continuity of the dynasty.
  Note: rhagaea's daughter, impetuous. Ira must be very young, as her mother is 40
  Family: parents mother Rhagaea
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Ulbos Pethros (Pethros)
  ID/Source: lord_1_47 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: clan 7 lieutenant. ulbos, rhagaea ally, fanatic partisan
  Family: spouse Mina; children Casyrea, Colambea
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Mina Pethros (Pethros)
  ID/Source: lord_1_47_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Ulbos; children Casyrea, Colambea
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Casyrea Pethros (Pethros)
  ID/Source: lord_1_47_2 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: TEENAGER, NO TRAITS OR SKILLS FOR UNDER-18s
  Family: parents father Ulbos, mother Mina; siblings Colambea
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]
Colambea Pethros (Pethros)
  ID/Source: lord_1_47_3 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: TEENAGER, NO TRAITS OR SKILLS FOR UNDER-18s
  Family: parents father Ulbos, mother Mina; siblings Casyrea
  Settlement: Sestadaim Castle [castle_ES6, castle, NavalDLC], Chanopsis Castle [castle_ES8, castle, NavalDLC], Lycaron [town_ES4, town, NavalDLC], Onira [town_ES5, town, NavalDLC]

### Prienicos (id clan_empire_south_8; culture Empire; home castle_ES5; owner Abalytos)
Abalytos Prienicos (Prienicos)
  ID/Source: lord_1_72 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Abalytos. Loves to campaign
  Family: spouse Viviana
  Settlement: Morenia Castle [castle_ES5, castle, NavalDLC]
Viviana Prienicos (Prienicos)
  ID/Source: lord_1_72_1 / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Abalytos
  Settlement: Morenia Castle [castle_ES5, castle, NavalDLC]
Itaria Prienicos (Prienicos)
  ID/Source: lord_SE8_c / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: eager warrior
  Family: none listed
  Settlement: Morenia Castle [castle_ES5, castle, NavalDLC]

### Vetranis (id clan_empire_south_9; culture Empire; home castle_ES7; owner Satros)
Pagarios Vetranis (Vetranis)
  ID/Source: lord_SE9_c1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: anxious to rehabilitate the family name
  Family: parents father Satros, mother Jonna; siblings Diasca
  Settlement: Jogurys Castle [castle_ES7, castle, NavalDLC]
Diasca Vetranis (Vetranis)
  ID/Source: lord_SE9_c2 / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Diasca, genuine monarchist. I like to have these as commented lines separating skill traits from
        personality traits
  Family: parents father Satros, mother Jonna; siblings Pagarios
  Settlement: Jogurys Castle [castle_ES7, castle, NavalDLC]
Satros Vetranis (Vetranis)
  ID/Source: lord_SE9_l / SandBox
  Culture: Empire
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: somewhat bitter child of a traitor, rehabilitated and loyal to Rhagaea
  Family: spouse Jonna; children Diasca, Pagarios
  Settlement: Jogurys Castle [castle_ES7, castle, NavalDLC]
Jonna Vetranis (Vetranis)
  ID/Source: lord_SE9_s / SandBox
  Culture: Empire
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Satros; children Diasca, Pagarios
  Settlement: Jogurys Castle [castle_ES7, castle, NavalDLC]

### Vizartos (id clan_empire_south_6; culture Empire; home town_ES6; owner Sichanis)
Sichanis Vizartos (Vizartos)
  ID/Source: lord_1_54 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: sichanis, rather quiet schemer. rhagaea. Cruel
  Family: spouse Constalia
  Settlement: Phycaon [town_ES6, town, NavalDLC]
Constalia Vizartos (Vizartos)
  ID/Source: lord_1_54_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Sichanis
  Settlement: Phycaon [town_ES6, town, NavalDLC]
Tharos Vizartos (Vizartos)
  ID/Source: lord_1_68 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Dynon. Humorless altruist.
  Note: Tharos. Rather vicious, unsubtle
  Family: spouse Silvina
  Settlement: Phycaon [town_ES6, town, NavalDLC]
Silvina Vizartos (Vizartos)
  ID/Source: lord_1_68_1 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: spouse Tharos
  Settlement: Phycaon [town_ES6, town, NavalDLC]

## Sturgia

### Gundaroving (id clan_sturgia_1; culture Sturgia; home town_S1; owner Raganvad)
  Clan XML note: STURGIA Jomsvikings
Raganvad Gundaroving (Gundaroving)
  ID/Source: lord_2_1 / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: The current Grand Prince of Sturgia is Raganvad. Harsh and uncompromising, he believes that it is
        the right of the prince to command the boyars in all things, not just in making war. For the time
        being they obey him, not least for his ability to call on the kinsmen of his mother, a Nordic
        princess with ties to the fearsome Skolderbroda mercenary company.
  Note: Ragenvad, Hardrada type
  Family: spouse Asta; children Mimir, Simir, Valla
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Valla Gundaroving (Gundaroving)
  ID/Source: lord_2_10 / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: sturgian heiresses. Raganvar's daughter, ambitious like father
  Family: parents father Raganvad, mother Asta; siblings Mimir, Simir
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Vidar Gundaroving (Gundaroving)
  ID/Source: lord_2_13 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: sturgian lieutenants
  Note: Raganvad uncle. Decent, loyal, not very thoughtful
  Family: children Andruta, Lilizha, Luda, Teta
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Lilizha Gundaroving (Gundaroving)
  ID/Source: lord_2_13_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Vidar; siblings Andruta, Luda, Teta
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Andruta Gundaroving (Gundaroving)
  ID/Source: lord_2_13_2 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Vidar; siblings Lilizha, Luda, Teta
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Luda Gundaroving (Gundaroving)
  ID/Source: lord_2_13_3 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: TEENAGER, NO SKILLS OR TRAITS YET
  Family: parents father Vidar; siblings Andruta, Lilizha, Teta
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Teta Gundaroving (Gundaroving)
  ID/Source: lord_2_13_4 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: TEENAGER, NO SKILLS OR TRAITS YET
  Family: parents father Vidar; siblings Andruta, Lilizha, Luda
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Asta Gundaroving (Gundaroving)
  ID/Source: lord_2_2 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Asta, queenly ideal
  Family: spouse Raganvad; children Mimir, Simir, Valla
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Simir Gundaroving (Gundaroving)
  ID/Source: lord_2_7 / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: earnest
  Note: sturgian heirs
  Note: Simir, Raganvar's son. Cold
  Family: parents father Raganvad, mother Asta; siblings Mimir, Valla
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]
Mimir Gundaroving (Gundaroving)
  ID/Source: lord_2_7_1 / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: earnest
  Note: none listed
  Family: parents father Raganvad, mother Asta; siblings Simir, Valla
  Settlement: Mazhadan Castle [castle_S2, castle, NavalDLC], Nevyansk Castle [castle_S3, castle, NavalDLC], Varcheg [town_S1, town, NavalDLC], Balgard [town_S2, town, NavalDLC]

### Isyaroving (id clan_sturgia_6; culture Sturgia; home town_S6; owner Fafen)
Fafen Isyaroving (Isyaroving)
  ID/Source: lord_2_18 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: independent sturgian lord. Fafen. Cold and calculating
  Family: spouse Zorika
  Settlement: Sibir [town_S6, town, NavalDLC]
Zorika Isyaroving (Isyaroving)
  ID/Source: lord_2_18_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: ironic
  Note: none listed
  Family: spouse Fafen
  Settlement: Sibir [town_S6, town, NavalDLC]
Galden Isyaroving (Isyaroving)
  ID/Source: lord_2_23 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: independent sturgian lord. Galden. Smart but a bit cowardly. Does not exert himself
  Family: children Zlatka
  Settlement: Sibir [town_S6, town, NavalDLC]
Zlatka Isyaroving (Isyaroving)
  ID/Source: lord_2_23_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents father Galden
  Settlement: Sibir [town_S6, town, NavalDLC]

### Kostoroving (id clan_sturgia_9; culture Sturgia; home castle_S4; owner Rolan)
  Clan XML note: Kostaroving, dominated by a matriarch allied to Olek
Forim Kostoroving (Kostoroving)
  ID/Source: lord_S9_c / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: milder than his parents
  Family: parents father Rolan
  Settlement: Kranirog Castle [castle_S4, castle, NavalDLC]
Rolan Kostoroving (Kostoroving)
  ID/Source: lord_S9_l / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents mother Dakhila; children Forim
  Settlement: Kranirog Castle [castle_S4, castle, NavalDLC]
Dakhila Kostoroving (Kostoroving)
  ID/Source: lord_S9_m / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Stern matriarch
  Family: children Rolan
  Settlement: Kranirog Castle [castle_S4, castle, NavalDLC]
Chastimir Kostoroving (Kostoroving)
  ID/Source: lord_S9_u / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: obediant enforcer of dakhila's will
  Family: none listed
  Settlement: Kranirog Castle [castle_S4, castle, NavalDLC]

### Kuloving (id clan_sturgia_2; culture Sturgia; home town_S3; owner Olek)
  Clan XML note: Ruling clan, centralizing, Patriarch: Raganvad, Ivan/Hardrada type, minimal sense of humor
                 Heir: Simir, ambitious but treated coldly by father, wants to prove self
Olek the Old Kuloving (Kuloving)
  ID/Source: dead_lord_2_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Olek the Old was boyar of the Kuloving, the fiercest and most conservative of the Sturgian noble
        houses. He fell at the battle of Pendraic, leading from the front - as many say Raganvad should have
        done.
  Note: ANCESTORS - GO ON TOP BECAUSE MUST BE SCANNED FIRST
  Note: Father of Olek, Siga and Varra
  Family: children Olek, Siga, Varra
  Settlement: Omor [town_S3, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Varra Kuloving (Kuloving)
  ID/Source: dead_lord_2_2 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Varra was a noblewoman of the Kuloving. She died under mysterious circumstances the year after the
        battle of Pendraic.
  Note: Sister of Olek and Siga
  Family: parents father Olek the Old; siblings Olek, Siga
  Settlement: Omor [town_S3, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Idrun Kuloving (Kuloving)
  ID/Source: lord_2_11 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: Olek's daughter, very conventional maiden
  Family: parents father Olek; siblings Rozhivol, Urik
  Settlement: Omor [town_S3, town, NavalDLC]
Rozhivol Kuloving (Kuloving)
  ID/Source: lord_2_111 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: parents father Olek; siblings Idrun, Urik
  Settlement: Omor [town_S3, town, NavalDLC]
Olek Kuloving (Kuloving)
  ID/Source: lord_2_3 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: curt
  Note: Olek is patriarch of the Kuloving, one of the oldest of the Sturgian clans, which never really
        accepted the idea of the monarchy. He believes the boyars should be lords in their own lands. He is
        famed for once telling the prince, 'Every wound I suffer in battle under your banner is like my
        wife's caress, but every denar I pay to your treasury in tax is like an arrow in my gut.' He is
        older now, and keeps his counsel, but few believe that his resentment of princely authority has in
        any way diminished.
  Family: parents father Olek the Old; children Idrun, Rozhivol, Urik; siblings Siga, Varra
  Settlement: Omor [town_S3, town, NavalDLC]
Siga Kuloving (Kuloving)
  ID/Source: lord_2_4 / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Siga, his sister, older shieldmaiden. Archetype of humorless, honor-obsessed
  Family: parents father Olek the Old; children Apolanea; siblings Olek, Varra
  Settlement: Omor [town_S3, town, NavalDLC]
Apolanea Kuloving (Kuloving)
  ID/Source: lord_2_4_1 / SandBox
  Culture: Sturgia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents mother Siga
  Settlement: Omor [town_S3, town, NavalDLC]
Urik Kuloving (Kuloving)
  ID/Source: lord_2_8 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: Urik, Olek's son. Much like his father, but more aggressive and deceitful
  Family: parents father Olek; siblings Idrun, Rozhivol
  Settlement: Omor [town_S3, town, NavalDLC]

### Ormidoving (id clan_sturgia_4; culture Sturgia; home town_S4; owner Yorig)
  Clan XML note: Based on Icelandish explorers - independent forging outward Patriarch: Havyn Heir: Lek
                 Uncle: Rategost - Mystic Heiress: Svana - heiress, leads armies
Isvan Ormidoving (Ormidoving)
  ID/Source: lord_2_14 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Olek's cousin - classic hotheaded warrior
  Family: spouse Valkava; children Vizhduna, Zaverena
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Valkava Ormidoving (Ormidoving)
  ID/Source: lord_2_14_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: spouse Isvan; children Vizhduna, Zaverena
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Zaverena Ormidoving (Ormidoving)
  ID/Source: lord_2_14_2 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents father Isvan, mother Valkava; siblings Vizhduna
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Vizhduna Ormidoving (Ormidoving)
  ID/Source: lord_2_14_3 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: TEENAGER, NO SKILLS OR TRAITS YET
  Family: parents father Isvan, mother Valkava; siblings Zaverena
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Yorig Ormidoving (Ormidoving)
  ID/Source: lord_2_16 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: independent sturgian lord. Yorig. Enthusiastic raider
  Family: spouse Tyaska
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Tyaska Ormidoving (Ormidoving)
  ID/Source: lord_2_16_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Yorig
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Svedorn Ormidoving (Ormidoving)
  ID/Source: lord_2_21 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: independent sturgian lord. Svedorn. Generous, honest, emotional
  Family: spouse Izdenka
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]
Izdenka Ormidoving (Ormidoving)
  ID/Source: lord_2_21_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Svedorn
  Settlement: Vladiv Castle [castle_S8, castle, NavalDLC], Varnovapol [town_S4, town, NavalDLC]

### Togaroving (id clan_sturgia_5; culture Sturgia; home town_S7; owner Vyldur)
Vyldur Togaroving (Togaroving)
  ID/Source: lord_2_17 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: independent sturgian lord. Vyldur. Fairly gentle, as warlords go
  Family: spouse Dracha
  Settlement: Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC]
Dracha Togaroving (Togaroving)
  ID/Source: lord_2_17_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: none listed
  Family: spouse Vyldur
  Settlement: Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC]
Lashonek Togaroving (Togaroving)
  ID/Source: lord_2_22 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: independent sturgian lord. Lashonek. Wise, pessimistic
  Family: spouse Zheneva
  Settlement: Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC]
Zheneva Togaroving (Togaroving)
  ID/Source: lord_2_22_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Lashonek's wife, former shield-maiden
  Family: spouse Lashonek
  Settlement: Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC]
Alvar Togaroving (Togaroving)
  ID/Source: lord_2_24 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Zorina
  Settlement: Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC]
Zorina Togaroving (Togaroving)
  ID/Source: lord_2_24_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Alvar
  Settlement: Ustokol Castle [castle_S1, castle, NavalDLC], Revyl [town_S7, town, NavalDLC]

### Ubroving (id clan_sturgia_8; culture Sturgia; home castle_S6; owner Tovir)
Tovir Ubroving (Ubroving)
  ID/Source: lord_2_20 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Sturgia 8, Ubroving, Tovir. Brave and headstrong
  Family: spouse Kisha
  Settlement: Takor Castle [castle_S6, castle, NavalDLC]
Kisha Ubroving (Ubroving)
  ID/Source: lord_2_20_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Tovir
  Settlement: Takor Castle [castle_S6, castle, NavalDLC]
Galyk Ubroving (Ubroving)
  ID/Source: lord_S8_u / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Older, cautious, much better suited to governor
  Family: none listed
  Settlement: Takor Castle [castle_S6, castle, NavalDLC]

### Vagiroving (id clan_sturgia_3; culture Sturgia; home town_S5; owner Godun)
  Clan XML note: Old Believers, ties to Jomsvikings Patriarch - Olek old, ferocious Heir - Urik, fierce but
                 high-spirited
Svana Vagiroving (Vagiroving)
  ID/Source: lord_2_12 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Svana, shieldmaiden
  Family: parents father Godun, mother Erta; siblings Lek, Osven
  Settlement: Urikskala Castle [castle_S7, castle, NavalDLC], Tyal [town_S5, town, NavalDLC]
Osven Vagiroving (Vagiroving)
  ID/Source: lord_2_121 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Godun, mother Erta; siblings Lek, Svana
  Settlement: Urikskala Castle [castle_S7, castle, NavalDLC], Tyal [town_S5, town, NavalDLC]
Godun Vagiroving (Vagiroving)
  ID/Source: lord_2_5 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Godun is lord of the Vagiroving, one of the younger houses of the Sturgians. His people have always
        been as interested in trade as they have been in war, although Godun himself is everything a prince
        might want: cooperative, prompt to pay his feudal dues, quick to respond to his liege's calls to
        arms. Yet Raganvad has never fully trusted him, because it is hard to imagine a Vagiroving without
        his own long-term plan for personal aggrandizement.
  Note: Godun, lord of clan 3, the more outward looking of the three voice="Male, northern accent, older,
        authoritative and competent"
  Family: spouse Erta; children Lek, Osven, Svana
  Settlement: Urikskala Castle [castle_S7, castle, NavalDLC], Tyal [town_S5, town, NavalDLC]
Erta Vagiroving (Vagiroving)
  ID/Source: lord_2_6 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Erta, matriarch of clan 3
  Family: spouse Godun; children Lek, Osven, Svana
  Settlement: Urikskala Castle [castle_S7, castle, NavalDLC], Tyal [town_S5, town, NavalDLC]
Lek Vagiroving (Vagiroving)
  ID/Source: lord_2_9 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Lek, heir to faction 3
  Family: parents father Godun, mother Erta; siblings Osven, Svana
  Settlement: Urikskala Castle [castle_S7, castle, NavalDLC], Tyal [town_S5, town, NavalDLC]

### Vezhoving (id clan_sturgia_7; culture Sturgia; home castle_S5; owner Vashorki)
Ratagost Vezhoving (Vezhoving)
  ID/Source: lord_2_15 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: Rategost, mystical. Cautious and kind.
  Family: children Bovan, Milanka, Velina, Yachana
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]
Yachana Vezhoving (Vezhoving)
  ID/Source: lord_2_15_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Ratagost; siblings Bovan, Milanka, Velina
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]
Milanka Vezhoving (Vezhoving)
  ID/Source: lord_2_15_2 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Ratagost; siblings Bovan, Velina, Yachana
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]
Velina Vezhoving (Vezhoving)
  ID/Source: lord_2_15_3 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: parents father Ratagost; siblings Bovan, Milanka, Yachana
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]
Bovan Vezhoving (Vezhoving)
  ID/Source: lord_2_15_4 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Ratagost; siblings Milanka, Velina, Yachana
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]
Vashorki Vezhoving (Vezhoving)
  ID/Source: lord_2_19 / SandBox
  Culture: Sturgia
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor -1 (Cautious); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: independent sturgian lord. Vashorki. Generally held to be despicable
  Family: spouse Vitomira
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]
Vitomira Vezhoving (Vezhoving)
  ID/Source: lord_2_19_1 / SandBox
  Culture: Sturgia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Vashorki
  Settlement: Ov Castle [castle_S5, castle, NavalDLC]

## Aserai

### Banu Arbas (id clan_aserai_5; culture Aserai; home town_A7; owner Iyalas)
Iyalas Banu Arbas (Banu Arbas)
  ID/Source: lord_3_17 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: Iyalas, mild and generally goodnatured
  Family: spouse Shaima; children Sanit
  Settlement: Askar [town_A7, town, NavalDLC]
Shaima Banu Arbas (Banu Arbas)
  ID/Source: lord_3_17_1 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: spouse Iyalas; children Sanit
  Settlement: Askar [town_A7, town, NavalDLC]
Sanit Banu Arbas (Banu Arbas)
  ID/Source: lord_3_17_2 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Iyalas, mother Shaima
  Settlement: Askar [town_A7, town, NavalDLC]
Ukhai Banu Arbas (Banu Arbas)
  ID/Source: lord_3_21 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Ukhai, true believer in whatever cause he gravitates to, not much given to independent thought
  Family: spouse Ashisa
  Settlement: Askar [town_A7, town, NavalDLC]
Ashisa Banu Arbas (Banu Arbas)
  ID/Source: lord_3_21_1 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Ukhai
  Settlement: Askar [town_A7, town, NavalDLC]

### Banu Atij (id clan_aserai_6; culture Aserai; home town_A8; owner Talas)
Talas Banu Atij (Banu Atij)
  ID/Source: lord_3_18 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Talas, abrasive but generally benevolent
  Family: children Farzana, Hafisa, Jalfar, Zuad
  Settlement: Qasira [town_A8, town, NavalDLC]
Farzana Banu Atij (Banu Atij)
  ID/Source: lord_3_18_1 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Talas; siblings Hafisa, Jalfar, Zuad
  Settlement: Qasira [town_A8, town, NavalDLC]
Hafisa Banu Atij (Banu Atij)
  ID/Source: lord_3_18_2 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents father Talas; siblings Farzana, Jalfar, Zuad
  Settlement: Qasira [town_A8, town, NavalDLC]
Zuad Banu Atij (Banu Atij)
  ID/Source: lord_3_18_3 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Talas' daughter, combatant
  Family: parents father Talas; siblings Farzana, Hafisa, Jalfar
  Settlement: Qasira [town_A8, town, NavalDLC]
Jalfar Banu Atij (Banu Atij)
  ID/Source: lord_3_18_4 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: AGE 7
  Family: parents father Talas; siblings Farzana, Hafisa, Zuad
  Settlement: Qasira [town_A8, town, NavalDLC]

### Banu Habbab (id clan_aserai_8; culture Aserai; home castle_A8; owner Hashan)
Hashan Banu Habbab (Banu Habbab)
  ID/Source: lord_3_22 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: Hashan, gallant
  Family: spouse Yamina; children Hajara, Suna, Zanuwa
  Settlement: Tamnuh Castle [castle_A8, castle, NavalDLC]
Yamina Banu Habbab (Banu Habbab)
  ID/Source: lord_3_22_1 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Hashan; children Hajara, Suna, Zanuwa
  Settlement: Tamnuh Castle [castle_A8, castle, NavalDLC]
Suna Banu Habbab (Banu Habbab)
  ID/Source: lord_3_22_2 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: ironic
  Note: none listed
  Family: parents father Hashan, mother Yamina; siblings Hajara, Zanuwa
  Settlement: Tamnuh Castle [castle_A8, castle, NavalDLC]
Zanuwa Banu Habbab (Banu Habbab)
  ID/Source: lord_3_22_3 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Hashan, mother Yamina; siblings Hajara, Suna
  Settlement: Tamnuh Castle [castle_A8, castle, NavalDLC]
Hajara Banu Habbab (Banu Habbab)
  ID/Source: lord_3_22_4 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Hashan, mother Yamina; siblings Suna, Zanuwa
  Settlement: Tamnuh Castle [castle_A8, castle, NavalDLC]

### Banu Hulyan (id clan_aserai_1; culture Aserai; home town_A1; owner Unqid)
  Clan XML note: ASURAI Jawwal, Ghilman0 The Asuri, three tribes who all trace their lineage to the ancient
                 patriarch Asur, were nomads who were established as a client kingdom to guard the Empire's
                 south, essentially being paid to protect caravans instead of raid them. As the empire
                 contracts they have made themselves independent, and indeed have pressed claims of marriage
                 to the imperial throne itself. The leaders of the Banu Hulyan claim the title of Sultan of
                 the Asuri. They are the richest of the clans in the south, masters of the key passes
                 between the lake and the outer desert, and are seen by other tribes as haughty and amoral.
                 They are close to the Ghulam, a group of warrior slaves that has converted itself to a
                 mercenary military order. The Banu Sarran are recently settled bedouin, who seized the Banu
                 Hulyan's holdings in the outer oases but were eventually accepted as clients and vassals.
                 They are thought of as upstarts by the others, a reputation which they in fact relish. They
                 celebrate their nomadic past with carefully poems on their success in battle over the other
                 tribes, or in seducing the other tribes' daughters. This does not endear them to other
                 Asuris. They maintain close ties with the Jawwal, a clan of outcasts who still keep the
                 nomadic lifestyle. The Banu Qild are known as a dour ascetics, looking down from their
                 desert fastnesses with disapproval on both the wealthy Banu Hulyan and the poor and roguish
                 Banu Sarran. They answer readily enough to the Banu Hulyan's summons for war, but have also
                 made hints that they may some day attempt to seize the sultanate to cleanse the Asuri lands
                 from corruption. The Ghulam are an order of warrior-slaves. They originated as the
                 bodyguard of an imperial noble who tried - and failed - to subdue the desert frontier, but
                 during the chaos that preceded the establishment of the Asuri state they set themselves up
                 as independent mercenaries. They purchase new recruits from slave markets across the
                 empire, putting them through a rigorous course of training before initiating them into the
                 order.
  Clan XML note: Quraysh-like clan, established and mercantile
Unqid Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_1 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: The current Sultan of Aserai is Unqid. He wears his authority lightly, preferring to charm rather
        than to coerce, always deferring to the laws of the Banu Asera in his judgments. But there are some
        who say that Unqid is remiss in his duty to administer justice, allowing the wealthiest clans - such
        as his own - to use bribes and clever legal arguments to oppress the others.
  Note: Unqid. Cautious, pragmatic, generous. A trader by temperament
  Family: spouse Jinda; children Anidha, Dhiyul
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]
Anidha Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_10 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: aserai heiresses
  Note: unqidh the merchant's daughter, conventional
  Family: parents father Unqid, mother Jinda; siblings Dhiyul
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]
Nuqar Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_13 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Nuqar, warrior, devious but clever
  Family: spouse Sira; children Razana
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]
Sira Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_13_1 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Nuqar's wife
  Family: spouse Nuqar; children Razana
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]
Razana Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_13_2 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Nuqar, mother Sira
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]
Jinda Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_2 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Jinda. Fierce, and retains strong grudges
  Family: spouse Unqid; children Anidha, Dhiyul
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]
Dhiyul Banu Hulyan (Banu Hulyan)
  ID/Source: lord_3_7 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Heirs, 3_7 to 3_9
  Note: Dhiyul, decent but impulsive rich youth. Not especially martial
  Family: parents father Unqid, mother Jinda; siblings Anidha
  Settlement: Tubilis Castle [castle_A1, castle, NavalDLC], Quyaz [town_A1, town, NavalDLC], Sanala [town_A6, town, NavalDLC]

### Banu Qaraz (id clan_aserai_4; culture Aserai; home town_A3; owner Suruq)
Thamza Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_14 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Thamza, somewhat grizzled fighter, aware of his role keeping youth of clan out of danger
  Family: spouse Sasaitha
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]
Sasaitha Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_14_1 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Thamza's confidante and wife
  Family: spouse Thamza
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]
Ghuzid Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_15 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Ghuzid, Qild clan attack dog
  Family: spouse Shimra; children Bushila
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]
Shimra Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_15_1 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Ghuzid; children Bushila
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]
Bushila Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_15_2 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: AGE 5
  Family: parents father Ghuzid, mother Shimra
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]
Suruq Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_16 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Suruq, cautious but deadly when cornered. Politically ambitious. Chooses words carefully
  Family: spouse Farina
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]
Farina Banu Qaraz (Banu Qaraz)
  ID/Source: lord_3_16_1 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Suruq
  Settlement: Jamayeh Castle [castle_A5, castle, NavalDLC], Iyakis [town_A3, town, NavalDLC]

### Banu Qild (id clan_aserai_3; culture Aserai; home town_A5; owner Tais)
  Clan XML note: Jahaliya poet boaster POSITIVE ties to Jawal
  Clan XML note: Ascetics
Manan Banu Qild (Banu Qild)
  ID/Source: lord_3_12 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Manan, moralist but curious about solving ills of the world
  Family: parents father Tais, mother Ruma; siblings Haqan, Usair
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Karith Banu Qild (Banu Qild)
  ID/Source: lord_3_20 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: Karith, misanthropic
  Family: spouse Judira; children Azina
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Judira Banu Qild (Banu Qild)
  ID/Source: lord_3_20_1 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Karith; children Azina
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Azina Banu Qild (Banu Qild)
  ID/Source: lord_3_20_2 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: TEENAGER, NO SKILLS OR TRAITS
  Family: parents father Karith, mother Judira
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Tais Banu Qild (Banu Qild)
  ID/Source: lord_3_5 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Banu Qild, a proud ascetic clan
  Note: Tais al-Qildi, harsh patriarch
  Family: spouse Ruma; children Haqan, Manan, Usair
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Haqan Banu Qild (Banu Qild)
  ID/Source: lord_3_51 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: parents father Tais, mother Ruma; siblings Manan, Usair
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Ruma Banu Qild (Banu Qild)
  ID/Source: lord_3_6 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Ruma, fierce, shames lords who do not uphold honor. Zeinab al-Ghazali type
  Family: spouse Tais; children Haqan, Manan, Usair
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]
Usair Banu Qild (Banu Qild)
  ID/Source: lord_3_9 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: earnest
  Note: Usair al-Qildi, much younger than his father. Smart, friendly zealot. fanatically devoted to values
        of the Faction. Friendly but capable of turning quickly
  Family: parents father Tais, mother Ruma; siblings Haqan, Manan
  Settlement: Sahel Castle [castle_A2, castle, NavalDLC], Shibal Zumr Castle [castle_A6, castle, NavalDLC], Hubyar [town_A5, town, NavalDLC]

### Banu Ruwaid (id clan_aserai_9; culture Aserai; home castle_A9; owner Aqar)
Dhila Banu Ruwaid (Banu Ruwaid)
  ID/Source: lord_A9_c / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Aqar, mother Thiqa
  Settlement: Barihal Castle [castle_A9, castle, NavalDLC]
Aqar Banu Ruwaid (Banu Ruwaid)
  ID/Source: lord_A9_l / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Banu Ruwaid. Patriarch who dominate his clan by fear and the force of his personality.
  Family: spouse Thiqa; children Dhila
  Settlement: Barihal Castle [castle_A9, castle, NavalDLC]
Thiqa Banu Ruwaid (Banu Ruwaid)
  ID/Source: lord_A9_s / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Aqar; children Dhila
  Settlement: Barihal Castle [castle_A9, castle, NavalDLC]
Qaban Banu Ruwaid (Banu Ruwaid)
  ID/Source: lord_A9_u / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Cousin, part of Nimr's generation
  Family: none listed
  Settlement: Barihal Castle [castle_A9, castle, NavalDLC]

### Banu Sarmal (id clan_aserai_7; culture Aserai; home castle_A3; owner Awdhan)
Awdhan Banu Sarmal (Banu Sarmal)
  ID/Source: lord_3_19 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Awdhan, competent warlord.
  Family: spouse Salma; children Sulhana, Zulaika
  Settlement: Ain Baliq Castle [castle_A3, castle, NavalDLC], Uqba Castle [castle_A7, castle, NavalDLC]
Salma Banu Sarmal (Banu Sarmal)
  ID/Source: lord_3_19_1 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Awdhan; children Sulhana, Zulaika
  Settlement: Ain Baliq Castle [castle_A3, castle, NavalDLC], Uqba Castle [castle_A7, castle, NavalDLC]
Zulaika Banu Sarmal (Banu Sarmal)
  ID/Source: lord_3_19_2 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: parents father Awdhan, mother Salma; siblings Sulhana
  Settlement: Ain Baliq Castle [castle_A3, castle, NavalDLC], Uqba Castle [castle_A7, castle, NavalDLC]
Sulhana Banu Sarmal (Banu Sarmal)
  ID/Source: lord_3_19_3 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Awdhan, mother Salma; siblings Zulaika
  Settlement: Ain Baliq Castle [castle_A3, castle, NavalDLC], Uqba Castle [castle_A7, castle, NavalDLC]
Qahin Banu Sarmal (Banu Sarmal)
  ID/Source: lord_3_23 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Sukayna
  Settlement: Ain Baliq Castle [castle_A3, castle, NavalDLC], Uqba Castle [castle_A7, castle, NavalDLC]
Sukayna Banu Sarmal (Banu Sarmal)
  ID/Source: lord_3_23_1 / SandBox
  Culture: Aserai
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: spouse Qahin
  Settlement: Ain Baliq Castle [castle_A3, castle, NavalDLC], Uqba Castle [castle_A7, castle, NavalDLC]

### Banu Sarran (id clan_aserai_2; culture Aserai; home town_A4; owner Adram)
  Clan XML note: Quraysh, also based on Osama Bin Munqidh, fastidious Patriarch, Unqidh, cautious, generous
                 POSITIVE ties to Ghulam
  Clan XML note: Upstart clan, recently settled bedouin
Nimr Banu Sarran (Banu Sarran)
  ID/Source: dead_lord_3_1 / SandBox
  Culture: Aserai
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Nimr was a young warrior of the Banu Sarran who led the Aserai contingent at the battle of Pendraic.
        He was executed by the Banu Qild after seducing a young woman of that clan.
  Note: Nimr
  Family: none listed
  Settlement: Medeni Castle [castle_A4, castle, NavalDLC], Husn Fulq [town_A2, town, NavalDLC], Razih [town_A4, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Arwa Banu Sarran (Banu Sarran)
  ID/Source: lord_3_11 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Arwa, of the sarran. Leads warriors. Somewhat devious and manipulative
  Family: parents father Adram, mother Maraa; siblings Addas, Tariq
  Settlement: Medeni Castle [castle_A4, castle, NavalDLC], Husn Fulq [town_A2, town, NavalDLC], Razih [town_A4, town, NavalDLC]
Adram Banu Sarran (Banu Sarran)
  ID/Source: lord_3_3 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Adram. Like Unqidh, a strong sense of being protector of his clan, but unlike the former aggressive
  Family: spouse Maraa; children Addas, Arwa, Tariq
  Settlement: Medeni Castle [castle_A4, castle, NavalDLC], Husn Fulq [town_A2, town, NavalDLC], Razih [town_A4, town, NavalDLC]
Tariq Banu Sarran (Banu Sarran)
  ID/Source: lord_3_3_1 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: parents father Adram, mother Maraa; siblings Addas, Arwa
  Settlement: Medeni Castle [castle_A4, castle, NavalDLC], Husn Fulq [town_A2, town, NavalDLC], Razih [town_A4, town, NavalDLC]
Maraa Banu Sarran (Banu Sarran)
  ID/Source: lord_3_4 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Maraa - patroness
  Family: spouse Adram; children Addas, Arwa, Tariq
  Settlement: Medeni Castle [castle_A4, castle, NavalDLC], Husn Fulq [town_A2, town, NavalDLC], Razih [town_A4, town, NavalDLC]
Addas Banu Sarran (Banu Sarran)
  ID/Source: lord_3_8 / SandBox
  Culture: Aserai
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Addas, models himself on Nimr's daring. Roguish
  Family: parents father Adram, mother Maraa; siblings Arwa, Tariq
  Settlement: Medeni Castle [castle_A4, castle, NavalDLC], Husn Fulq [town_A2, town, NavalDLC], Razih [town_A4, town, NavalDLC]

## Vlandia

### dey Arromanc (id clan_vlandia_3; culture Vlandia; home town_V6; owner Calatild)
  Clan XML note: Patriarch - Rendric. Wealthy, entitled clan. Duc de Berry Rendric of the House of Tir is
                 wealthy and notoriously avaricious, known for squeezing every last denar out of his
                 subjects while neglecting his duty to defend them. His son meanwhile is considered
                 depraved, and is almost as greatly feared as the Sturgian and Battanian raiders who he
                 allows the rampage through the northlands as he pursues his desires. Rendric's daughter
                 Liena is considered the saving grace of the family, who has donned armor and taken on the
                 responsibilities that her male relatives neglect. Heir is Furenhard - depraved and feared
                 Heiress is Liena, leads armies, somewhat feckless Lieutenant -
Silvind dey Arromanc (dey Arromanc)
  ID/Source: lord_4_12 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Silvind, daughter of clan 3 led by the Countess
  Note: COMBATANT FEMALE
  Family: parents father Unthery, mother Calatild; siblings Lasand, Odofled, Thomund
  Settlement: Jaculan [town_V6, town, NavalDLC]
Lasand dey Arromanc (dey Arromanc)
  ID/Source: lord_4_121 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: ironic
  Note: none listed
  Family: parents father Unthery, mother Calatild; siblings Odofled, Silvind, Thomund
  Settlement: Jaculan [town_V6, town, NavalDLC]
Unthery dey Arromanc (dey Arromanc)
  ID/Source: lord_4_5 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Clan 3, headed by Calatild
  Note: Unthery, Younger brother of the countess (currently cousin)
  Family: spouse Calatild; children Lasand, Odofled, Silvind, Thomund
  Settlement: Jaculan [town_V6, town, NavalDLC]
Calatild dey Arromanc (dey Arromanc)
  ID/Source: lord_4_6 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Countess Calatild, leader of clan 3. Rigid
  Note: NONCOMBATANT LEADER
  Family: spouse Unthery; children Lasand, Odofled, Silvind, Thomund
  Settlement: Jaculan [town_V6, town, NavalDLC]
Odofled dey Arromanc (dey Arromanc)
  ID/Source: lord_4_6_1 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Arrogant, but does have authority
  Family: parents father Unthery, mother Calatild; siblings Lasand, Silvind, Thomund
  Settlement: Jaculan [town_V6, town, NavalDLC]
Thomund dey Arromanc (dey Arromanc)
  ID/Source: lord_4_9 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Thomund, heir to clan 3. Hotheaded but loyal to his friends
  Family: parents father Unthery, mother Calatild; siblings Lasand, Odofled, Silvind
  Settlement: Jaculan [town_V6, town, NavalDLC]

### dey Cortain (id clan_vlandia_4; culture Vlandia; home town_V7; owner Ingalther)
  Clan XML note: Calatild was her father's only child, and was named heir of the House of Arromanc in
                 contrary to normal Vlandian custom. The claim to her lands staked by Ingalther of Cortain
                 has allowed her to rally her relatives to her banner, overcoming any objections they might
                 have to a female liege. Patriarch - Untheric, consort of queen Queen - Calatild Heir,
                 Thomund - valiant but hotheaded, conventional Uncle, Hecard Heiress
Ingalther dey Cortain (dey Cortain)
  ID/Source: lord_4_16 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Lords 16-20 - Clan 4, settlements
  Note: Ingalther, William character
  Family: spouse Elbet; children Amalgun, Arthamund, Asela, Mitela
  Settlement: Charas [town_V7, town, NavalDLC]
Mitela dey Cortain (dey Cortain)
  ID/Source: lord_4_16_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: Ingalther's daughter
  Family: parents father Ingalther, mother Elbet; siblings Amalgun, Arthamund, Asela
  Settlement: Charas [town_V7, town, NavalDLC]
Elbet dey Cortain (dey Cortain)
  ID/Source: lord_4_17 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Elbet, matriarch, warmer, but still devoted to aggrandizenment of the clan
  Family: spouse Ingalther; children Amalgun, Arthamund, Asela, Mitela
  Settlement: Charas [town_V7, town, NavalDLC]
Amalgun dey Cortain (dey Cortain)
  ID/Source: lord_4_18 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Amalgun, heir, sadistic, takes things very personally
  Family: parents father Ingalther, mother Elbet; siblings Arthamund, Asela, Mitela
  Settlement: Charas [town_V7, town, NavalDLC]
Arthamund dey Cortain (dey Cortain)
  ID/Source: lord_4_181 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Ingalther, mother Elbet; siblings Amalgun, Asela, Mitela
  Settlement: Charas [town_V7, town, NavalDLC]
Asela dey Cortain (dey Cortain)
  ID/Source: lord_4_19 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Heiress, Asela
  Family: parents father Ingalther, mother Elbet; siblings Amalgun, Arthamund, Mitela
  Settlement: Charas [town_V7, town, NavalDLC]

### dey Folcun (id clan_vlandia_10; culture Vlandia; home castle_V4; owner Ecarand)
Ecarand dey Folcun (dey Folcun)
  ID/Source: lord_4_28 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: Ecarand, rigid but kind.
  Family: children Adalindis, Mauriana
  Settlement: Ormanfard Castle [castle_V4, castle, NavalDLC]
Adalindis dey Folcun (dey Folcun)
  ID/Source: lord_4_28_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: parents father Ecarand; siblings Mauriana
  Settlement: Ormanfard Castle [castle_V4, castle, NavalDLC]
Mauriana dey Folcun (dey Folcun)
  ID/Source: lord_4_28_2 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: ambitious and good at it
  Family: parents father Ecarand; siblings Adalindis
  Settlement: Ormanfard Castle [castle_V4, castle, NavalDLC]

### dey Fortes (id clan_vlandia_7; culture Vlandia; home town_V2; owner Belgir)
Belgir dey Fortes (dey Fortes)
  ID/Source: lord_4_23 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Belgir, bad-tempered
  Family: children Anstruda, Eleduran, Richelda
  Settlement: Verecsand Castle [castle_V8, castle, NavalDLC], Ocs Hall [town_V2, town, NavalDLC]
Richelda dey Fortes (dey Fortes)
  ID/Source: lord_4_23_1 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Belgir's daughter
  Family: parents father Belgir; siblings Anstruda, Eleduran
  Settlement: Verecsand Castle [castle_V8, castle, NavalDLC], Ocs Hall [town_V2, town, NavalDLC]
Anstruda dey Fortes (dey Fortes)
  ID/Source: lord_4_23_2 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Belgir's other daughter
  Family: parents father Belgir; siblings Eleduran, Richelda
  Settlement: Verecsand Castle [castle_V8, castle, NavalDLC], Ocs Hall [town_V2, town, NavalDLC]
Eleduran dey Fortes (dey Fortes)
  ID/Source: lord_4_23_3 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Belgir's son
  Family: parents father Belgir; siblings Anstruda, Richelda
  Settlement: Verecsand Castle [castle_V8, castle, NavalDLC], Ocs Hall [town_V2, town, NavalDLC]

### dey Gunric (id clan_vlandia_5; culture Vlandia; home castle_V5; owner Ospir)
  Clan XML note: Fourth clan Ingalther, lord of the House of Cortain, seized his estate from a much older
                 illegitimate half-brother. His ambition and sense of entitlement is extreme even by
                 Vlandian standards. He has a dynastic claim to Arromanc lands, and has been pressing
                 Derther to disinherit Calatild and award her lands to him. Derthert has of course refused,
                 as this would both start a war with the Arromancs and make Ingalther twice as powerful as
                 the king, but Ingalther nonetheless greatly resents him for it. Ingalther keeps close ties
                 with the Free Company, a notoriously rapacious band of mercenaries whose seaside castle
                 lies near his domains. MINOR FACTIION ties to free company
Ospir dey Gunric (dey Gunric)
  ID/Source: lord_4_21 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Ospir, conventionally martial
  Family: none listed
  Settlement: Tirby Castle [castle_V5, castle, NavalDLC]
Lucand dey Gunric (dey Gunric)
  ID/Source: lord_4_25 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: Lucand, gallant. One-eyed
  Family: spouse Bertliana
  Settlement: Tirby Castle [castle_V5, castle, NavalDLC]
Bertliana dey Gunric (dey Gunric)
  ID/Source: lord_4_25_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Lucand
  Settlement: Tirby Castle [castle_V5, castle, NavalDLC]

### dey Jelind (id clan_vlandia_9; culture Vlandia; home castle_V2; owner Vartin)
Vartin dey Jelind (dey Jelind)
  ID/Source: lord_4_27 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: lord_4_26_1 exists in "Delete Later" region
  Note: Clan 9, Dey Jelind. Vartin, debauched.
  Family: spouse Lietgardis
  Settlement: Hongard Castle [castle_V2, castle, NavalDLC]
Lietgardis dey Jelind (dey Jelind)
  ID/Source: lord_4_27_1 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: none listed
  Family: spouse Vartin
  Settlement: Hongard Castle [castle_V2, castle, NavalDLC]
Urundulf dey Jelind (dey Jelind)
  ID/Source: lord_V9_u / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: softspoken
  Note: none listed
  Family: none listed
  Settlement: Hongard Castle [castle_V2, castle, NavalDLC]

### dey Meroc (id clan_vlandia_1; culture Vlandia; home town_V1; owner Derthert)
  Clan XML note: VLANDIA Brotherhood of the Woods Free Company Vlandian warships first came to the western
                 shores of Calradia as traders. Then, seeing how rich the land was, they decided to take it.
                 First the Empire fought them, then when that failed granted them noble titles and estates
                 to make them into imperial clients, and then - when they rebelled - fought them again. Now
                 they are an independent kingdom, known for steel-forging and their horses, and their
                 armored riders are a constant menace to the Empire's western marches.
Derthert dey Meroc (dey Meroc)
  ID/Source: lord_4_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: The current king of Vlandia is Derthert. In his youth, he dreamt of glorious conquest. In fact he
        spent most of his reign simply putting down revolts, quashing pretenders, and keeping the fractious
        barons in line. When possible, he prefers to rule by arbitration, cajoling his vassals to set aside
        claims to each other's lands and enjoy what they have. But some Vlandians murmur that a warrior
        people deserve a more virile king.
  Note: Vlandians
  Note: Derthert, weary king
  Family: spouse Philenora; children Alary, Amorcon, Elys, Erdurand, Morcon
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Elys dey Meroc (dey Meroc)
  ID/Source: lord_4_10 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Elys, Heiress for clan 1. Decent and thoughtful, a better ruler than her brother
  Family: parents father Derthert, mother Philenora; siblings Alary, Amorcon, Erdurand, Morcon
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Romund dey Meroc (dey Meroc)
  ID/Source: lord_4_13 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Romund, blunt and conventional
  Family: none listed
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Morcon dey Meroc (dey Meroc)
  ID/Source: lord_4_14 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Morcon, cautious and icy. Honest, but takes every advantage in combat
  Family: parents father Derthert, mother Philenora; siblings Alary, Amorcon, Elys, Erdurand
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Amorcon dey Meroc (dey Meroc)
  ID/Source: lord_4_141 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Derthert, mother Philenora; siblings Alary, Elys, Erdurand, Morcon
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Erdurand dey Meroc (dey Meroc)
  ID/Source: lord_4_15 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Endurand, brave but bad-tempered
  Family: parents father Derthert, mother Philenora; siblings Alary, Amorcon, Elys, Morcon
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Philenora dey Meroc (dey Meroc)
  ID/Source: lord_4_2 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: ironic
  Note: Philenora - benevolent
  Family: spouse Derthert; children Alary, Amorcon, Elys, Erdurand, Morcon
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]
Alary dey Meroc (dey Meroc)
  ID/Source: lord_4_7 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Alary, heir to Vlandian clan 1. Skilled and driven, but unimaginative
  Family: parents father Derthert, mother Philenora; siblings Amorcon, Elys, Erdurand, Morcon
  Settlement: Talivel Castle [castle_V7, castle, NavalDLC], Sargot [town_V1, town, NavalDLC], Galend [town_V5, town, NavalDLC]

### dey Molarn (id clan_vlandia_8; culture Vlandia; home town_V8; owner Hecard)
Hecard dey Molarn (dey Molarn)
  ID/Source: lord_4_24 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: curt
  Note: Hecard, martial. Attentive to his men but ruthless
  Family: spouse Adaltrud; children Gudonhelda, Ingunde, Irmgard
  Settlement: Ostican [town_V8, town, NavalDLC]
Adaltrud dey Molarn (dey Molarn)
  ID/Source: lord_4_24_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: softspoken
  Note: none listed
  Family: spouse Hecard; children Gudonhelda, Ingunde, Irmgard
  Settlement: Ostican [town_V8, town, NavalDLC]
Gudonhelda dey Molarn (dey Molarn)
  ID/Source: lord_4_24_2 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: softspoken
  Note: none listed
  Family: parents father Hecard, mother Adaltrud; siblings Ingunde, Irmgard
  Settlement: Ostican [town_V8, town, NavalDLC]
Ingunde dey Molarn (dey Molarn)
  ID/Source: lord_4_24_3 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: parents father Hecard, mother Adaltrud; siblings Gudonhelda, Irmgard
  Settlement: Ostican [town_V8, town, NavalDLC]
Irmgard dey Molarn (dey Molarn)
  ID/Source: lord_4_24_4 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: TEENAGER, NO SKILLS OR TRAITS
  Family: parents father Hecard, mother Adaltrud; siblings Gudonhelda, Ingunde
  Settlement: Ostican [town_V8, town, NavalDLC]
Peric dey Molarn (dey Molarn)
  ID/Source: lord_4_26 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: none listed
  Settlement: Ostican [town_V8, town, NavalDLC]
Reingarda dey Molarn (dey Molarn)
  ID/Source: lord_4_26_1 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: ANCESTORS - characters who are dead when the game begins
  Note: Arenicos
  Note: Siga's sister killed by Raganvad
  Note: Some imperial affair
  Note: Gario's kinsman Pateor killed by Lucon
  Note: make Leonipardes' wife in fact his sister, married by Gario who then cheated on her, went back to
        her brother
  Note: Nimr, slain by the al-Qildis
  Note: new lords added May 2020, to be reordered
  Note: remaining lords go here
  Note: #region Delete Later
  Note: Lord is not in heroes.xml, kept only for backwards save compatibility
  Note: kind but antisocial
  Family: none listed
  Settlement: Ostican [town_V8, town, NavalDLC]

### dey Rothad (id clan_vlandia_11; culture Vlandia; home castle_V1; owner Berican)
Elendara dey Rothad (dey Rothad)
  ID/Source: lord_V11_c1 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Daughter of the clan. Somewhat unsatisfied in her current circumstances
  Family: parents father Berican; siblings Dagunic
  Settlement: Usanc Castle [castle_V1, castle, NavalDLC]
Dagunic dey Rothad (dey Rothad)
  ID/Source: lord_V11_c2 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Heir
  Family: parents father Berican; siblings Elendara
  Settlement: Usanc Castle [castle_V1, castle, NavalDLC]
Berican dey Rothad (dey Rothad)
  ID/Source: lord_V11_l / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Impulsive, generous at times, not especially warlike.
  Family: children Dagunic, Elendara
  Settlement: Usanc Castle [castle_V1, castle, NavalDLC]
Voleric dey Rothad (dey Rothad)
  ID/Source: lord_V11_u / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: His younger brother. Better fighter but somewhat unpleasant
  Family: none listed
  Settlement: Usanc Castle [castle_V1, castle, NavalDLC]

### dey Tihr (id clan_vlandia_2; culture Vlandia; home town_V3; owner Aldric)
  Clan XML note: Derthert - Cunning but weary king, Hugh Capet, trying to retain compassion Derthert, of the
                 House of Meroc, is King of the Vlandians. His subjects regard him as a decent man but a
                 tired one. He is worn down by years of struggle against vassals who swear oaths of fealty
                 only to break them, who see no patch of pasture so worthless, no dynastic claim so
                 unconvincingly traced, that they will not go to war over it. His heir, Alary, retains some
                 of the optimism and vigor of youth, and it's widely believed that he will make a popular
                 king. The House of Meroc thinks of commoners as a counterbalance to the nobles, and have
                 tried to elevate them to offices of authority when possible. Eldest son is XXX. Dissolute,
                 his father;s greatest headache Younger son is Alary, knight-errant, gallant, but loyal to
                 father Heiress is Elyce, like Eleanor of Aquitaine, her father's daughter, determined to
                 play the dynastic game to her best ability Lieutenant - Merteon MINOR FACTION ties to
                 Brotherhood of the Woods
Liena dey Tihr (dey Tihr)
  ID/Source: lord_4_11 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: Liena, Heiress for clan 2. Saving grace of her family
  Note: COMBATANT FEMALE
  Family: parents father Aldric, mother Elthild; siblings Furnhard, Megenhelda
  Settlement: Drapand Castle [castle_V3, castle, NavalDLC], Pravend [town_V3, town, NavalDLC]
Aldric dey Tihr (dey Tihr)
  ID/Source: lord_4_3 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Aldric, patriarch of clan 2. Weak, not especially cruel
  Family: spouse Elthild; children Furnhard, Liena, Megenhelda
  Settlement: Drapand Castle [castle_V3, castle, NavalDLC], Pravend [town_V3, town, NavalDLC]
Megenhelda dey Tihr (dey Tihr)
  ID/Source: lord_4_3_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: none listed
  Family: parents father Aldric, mother Elthild; siblings Furnhard, Liena
  Settlement: Drapand Castle [castle_V3, castle, NavalDLC], Pravend [town_V3, town, NavalDLC]
Elthild dey Tihr (dey Tihr)
  ID/Source: lord_4_4 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: earnest
  Note: Elthild, more astute than husband, but equally unscrupulous
  Family: spouse Aldric; children Furnhard, Liena, Megenhelda
  Settlement: Drapand Castle [castle_V3, castle, NavalDLC], Pravend [town_V3, town, NavalDLC]
Furnhard dey Tihr (dey Tihr)
  ID/Source: lord_4_8 / SandBox
  Culture: Vlandia
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor -1 (Cautious); Mercy -1 (Cruel)
  Voice: ironic
  Note: Furnhard, as debauched as his father
  Family: parents father Aldric, mother Elthild; siblings Liena, Megenhelda
  Settlement: Drapand Castle [castle_V3, castle, NavalDLC], Pravend [town_V3, town, NavalDLC]

### dey Valant (id clan_vlandia_6; culture Vlandia; home town_V9; owner Servic)
Varmund dey Valant (dey Valant)
  ID/Source: lord_4_20 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Varmund, Lieutenant, ruthless and dutiful. Stunningly ugly
  Family: spouse Ingeltrud
  Settlement: Caleus Castle [castle_V6, castle, NavalDLC], Rovalt [town_V9, town, NavalDLC]
Ingeltrud dey Valant (dey Valant)
  ID/Source: lord_4_20_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Varmund
  Settlement: Caleus Castle [castle_V6, castle, NavalDLC], Rovalt [town_V9, town, NavalDLC]
Servic dey Valant (dey Valant)
  ID/Source: lord_4_22 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Servic, charming but dangerous
  Family: spouse Alwith
  Settlement: Caleus Castle [castle_V6, castle, NavalDLC], Rovalt [town_V9, town, NavalDLC]
Alwith dey Valant (dey Valant)
  ID/Source: lord_4_22_1 / SandBox
  Culture: Vlandia
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Servic
  Settlement: Caleus Castle [castle_V6, castle, NavalDLC], Rovalt [town_V9, town, NavalDLC]

## Khuzait

### Arkit (id clan_khuzait_3; culture Khuzait; home town_K4; owner Tulag)
  Clan XML note: The Khergit, or Roan Horses, were one of the first peoples to be subjugated by Urkhun.
                 Although assimilated into his confederacy by force, they proved themselves some of his most
                 valuable warriors, and were rewarded with extensive lands in his new conquests. War however
                 took a heavy toll of the clan's males, and ten years ago the Arkit made a bid for their
                 territories. Mesui, sister of a slain noyan and part of a long tradition of steppe
                 warrior-women, led the Khergit's counter-attack. She continues to rule a clan nervous about
                 its brush with extinction, and resentful of the Urkhunait for doing little to help them.
                 Matriarch - female, widow, very conscious of her clan's brush with extinction Heir: Baybuz
                 Energetic but sometimes weak-willed confessional Valorous, deceitful, generous
Kuyug Arkit (Arkit)
  ID/Source: dead_lord_6_3 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Kuyug was the chief noyan of the Arkit clan of the Khuzaits.
  Family: children Oragur, Tulag, Undul
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Undul Arkit (Arkit)
  ID/Source: dead_lord_6_4 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Undul was a Khuzait noble of the Arkit clan.
  Note: Undul, Arkhit brother killed by Siga
  Family: parents father Kuyug; siblings Oragur, Tulag
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Abagai Arkit (Arkit)
  ID/Source: lord_6_12 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Arkit heiress, rogue princess
  Family: parents father Tulag; siblings Khada, Temun
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
Oragur Arkit (Arkit)
  ID/Source: lord_6_15 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: Khergit lieutenant, removed
  Note: Arkit lieutenant. Ruthless executor of clan will
  Family: spouse Khorijin; parents father Kuyug; children Sechen; siblings Tulag, Undul
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
Khorijin Arkit (Arkit)
  ID/Source: lord_6_15_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: none listed
  Family: spouse Oragur; children Sechen
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
Sechen Arkit (Arkit)
  ID/Source: lord_6_15_2 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: none listed
  Family: parents father Oragur, mother Khorijin
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
Tulag Arkit (Arkit)
  ID/Source: lord_6_5 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Arkit
  Family: parents father Kuyug; children Abagai, Khada, Temun; siblings Oragur, Undul
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
Khada Arkit (Arkit)
  ID/Source: lord_6_51 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Tulag; siblings Abagai, Temun
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]
Temun Arkit (Arkit)
  ID/Source: lord_6_9 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Temun, arkhit heir. Honorable, no tolerance
  Family: parents father Tulag; siblings Abagai, Khada
  Settlement: Usek Castle [castle_K1, castle, NavalDLC], Ortongard [town_K4, town, NavalDLC]

### Baltait (id clan_khuzait_6; culture Khuzait; home castle_K6; owner Ilatar)
Ilatar Baltait (Baltait)
  ID/Source: lord_6_18 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Ilatar, sardonic but impulsive, no particular plan. Dislikes cruelty
  Family: spouse Tilun; children Chagun
  Settlement: Dinar Castle [castle_K6, castle, NavalDLC], Kaysar Castle [castle_K9, castle, NavalDLC]
Tilun Baltait (Baltait)
  ID/Source: lord_6_18_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Ilatar's wife. Keeps him in check
  Family: spouse Ilatar; children Chagun
  Settlement: Dinar Castle [castle_K6, castle, NavalDLC], Kaysar Castle [castle_K9, castle, NavalDLC]
Chagun Baltait (Baltait)
  ID/Source: lord_6_18_2 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: curt
  Note: none listed
  Family: parents father Ilatar, mother Tilun
  Settlement: Dinar Castle [castle_K6, castle, NavalDLC], Kaysar Castle [castle_K9, castle, NavalDLC]
Achaku Baltait (Baltait)
  ID/Source: lord_6_22 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: curt
  Note: Achaku. Harsh
  Family: spouse Eselen
  Settlement: Dinar Castle [castle_K6, castle, NavalDLC], Kaysar Castle [castle_K9, castle, NavalDLC]
Eselen Baltait (Baltait)
  ID/Source: lord_6_22_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Achaku
  Settlement: Dinar Castle [castle_K6, castle, NavalDLC], Kaysar Castle [castle_K9, castle, NavalDLC]

### Harfit (id clan_khuzait_5; culture Khuzait; home town_K6; owner Akrum)
Akrum Harfit (Harfit)
  ID/Source: lord_6_17 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Akrum. Cautious
  Family: spouse Ergene; children Yesum
  Settlement: Odokh [town_K6, town, NavalDLC]
Ergene Harfit (Harfit)
  ID/Source: lord_6_17_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Akrum; children Yesum
  Settlement: Odokh [town_K6, town, NavalDLC]
Yesum Harfit (Harfit)
  ID/Source: lord_6_17_2 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: TEENAGER
  Family: parents father Akrum, mother Ergene
  Settlement: Odokh [town_K6, town, NavalDLC]
Ulman Harfit (Harfit)
  ID/Source: lord_6_21 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Ulman. Martial
  Family: spouse Esachei
  Settlement: Odokh [town_K6, town, NavalDLC]
Esachei Harfit (Harfit)
  ID/Source: lord_6_21_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: spouse Ulman
  Settlement: Odokh [town_K6, town, NavalDLC]

### Khergit (id clan_khuzait_2; culture Khuzait; home town_K1; owner Mesui)
  Clan XML note: The Urkhunait are ruling clan of the Khuzaits, named after the Khagan Urkhun who
                 transformed them from squabbling bands of fierce but undisciplined nomads into a formidable
                 machine of war. The current Khan, Tulag, is cut from this cloth. Grim, humorless, as
                 demanding of his followers as he is of himself, he has an unblemished record on the
                 battlefield. But the Khuzaits are no longer a hungry people, desperate for a iron-handed
                 warlord to lead them to richer pastures, and from the comfort of their palaces many clan
                 leaders are beginning to wonder if they too could serve as Khagan. Patriarch: Tulag.
                 Aescetic. Valorous, Honorable, Cruel, Ungenerous Heir: overawed, Heiress is warrior
Solun Khergit (Khergit)
  ID/Source: dead_lord_6_2 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Solun was the chief noyan of the Khergit and the former husband of Mesui, slain at the battle of
        Pendraic.
  Family: children Esur, Nayantai, Yana
  Settlement: Baltakhand [town_K1, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Yana Khergit (Khergit)
  ID/Source: lord_6_11 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Yana, clan 2 khergit heiress
  Family: parents father Solun, mother Mesui; siblings Esur, Nayantai
  Settlement: Baltakhand [town_K1, town, NavalDLC]
Bagai Khergit (Khergit)
  ID/Source: lord_6_3 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: ironic
  Note: clan 2. Lady Mesui is clan leader
  Note: Bagai is mesui's consort, moderating factor
  Family: none listed
  Settlement: Baltakhand [town_K1, town, NavalDLC]
Mesui Khergit (Khergit)
  ID/Source: lord_6_4 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: curt
  Note: Mesui is leader of the Khergit. Once one of the largest clans in the Khuzait confederacy, they
        suffered many losses during Urkhun Khan's conquests and their lands were subsequently targeted by
        other tribes. Mesui has ruthlessly defended her clan's rights, and frequently complained about the
        injustices suffered by smaller clans that she says have shed blood for the khanate without reaping
        any rewards.
  Note: Lady Mesui, clan leader. Honorable but thoroughly ruthless
  Family: children Esur, Nayantai, Yana
  Settlement: Baltakhand [town_K1, town, NavalDLC]
Esur Khergit (Khergit)
  ID/Source: lord_6_8 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Esur, son of Khergit queen. Brave and generous
  Family: parents father Solun, mother Mesui; siblings Nayantai, Yana
  Settlement: Baltakhand [town_K1, town, NavalDLC]
Nayantai Khergit (Khergit)
  ID/Source: lord_6_81 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Solun, mother Mesui; siblings Esur, Yana
  Settlement: Baltakhand [town_K1, town, NavalDLC]

### Koltit (id clan_khuzait_7; culture Khuzait; home castle_K5; owner Kanujan)
Kanujan Koltit (Koltit)
  ID/Source: lord_6_19 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Kanujan, quiet, honorable, follower
  Family: spouse Sokhatai; children Korte
  Settlement: Khimli Castle [castle_K5, castle, NavalDLC], Simira Castle [castle_K7, castle, NavalDLC]
Sokhatai Koltit (Koltit)
  ID/Source: lord_6_19_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: spouse Kanujan; children Korte
  Settlement: Khimli Castle [castle_K5, castle, NavalDLC], Simira Castle [castle_K7, castle, NavalDLC]
Korte Koltit (Koltit)
  ID/Source: lord_6_19_2 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Kanujan, mother Sokhatai
  Settlement: Khimli Castle [castle_K5, castle, NavalDLC], Simira Castle [castle_K7, castle, NavalDLC]
Kinteg Koltit (Koltit)
  ID/Source: lord_6_23 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Kinteg. Brave and efficient
  Family: none listed
  Settlement: Khimli Castle [castle_K5, castle, NavalDLC], Simira Castle [castle_K7, castle, NavalDLC]

### Oburit (id clan_khuzait_9; culture Khuzait; home castle_K8; owner Gusukan)
Altu Oburit (Oburit)
  ID/Source: lord_K9_c1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents father Gusukan, mother Sevin; siblings Mela
  Settlement: Erzenur Castle [castle_K8, castle, NavalDLC]
Mela Oburit (Oburit)
  ID/Source: lord_K9_c2 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Can lead a caravan if necessary but better suited to administer
  Family: parents father Gusukan, mother Sevin; siblings Altu
  Settlement: Erzenur Castle [castle_K8, castle, NavalDLC]
Gusukan Oburit (Oburit)
  ID/Source: lord_K9_l / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Oburit, more interested in trade than fighting
  Family: spouse Sevin; children Altu, Mela
  Settlement: Erzenur Castle [castle_K8, castle, NavalDLC]
Sevin Oburit (Oburit)
  ID/Source: lord_K9_s / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Gusukan; children Altu, Mela
  Settlement: Erzenur Castle [castle_K8, castle, NavalDLC]

### Tigrit (id clan_khuzait_4; culture Khuzait; home town_K2; owner Hurunag)
  Clan XML note: The Arkit, the Children of the Sky, were formerly the richest and most prestigious of the
                 tribes in the Khuzait homelands, of which Urkhun and his followers were at first merely a
                 humble offshoot. They followed the Khuzait hordes to the west but are not happy about
                 living in the shadow of a less ancient lineage. Their patriarch, the noyan Monchug, models
                 himself on Tulag but is somewhat less competent. Embittered elder tribe Patriarch: Honest,
                 ungenerous, cruel like ascetic Heir: gallant
Hurunag Tigrit (Tigrit)
  ID/Source: lord_6_16 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Hurunag, raging
  Family: spouse Chambui; children Unagen
  Settlement: Akiser Castle [castle_K2, castle, NavalDLC], Akkalat [town_K2, town, NavalDLC]
Chambui Tigrit (Tigrit)
  ID/Source: lord_6_16_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Hurunag; children Unagen
  Settlement: Akiser Castle [castle_K2, castle, NavalDLC], Akkalat [town_K2, town, NavalDLC]
Unagen Tigrit (Tigrit)
  ID/Source: lord_6_16_2 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: parents father Hurunag, mother Chambui
  Settlement: Akiser Castle [castle_K2, castle, NavalDLC], Akkalat [town_K2, town, NavalDLC]
Mehir Tigrit (Tigrit)
  ID/Source: lord_6_24 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: none listed
  Settlement: Akiser Castle [castle_K2, castle, NavalDLC], Akkalat [town_K2, town, NavalDLC]
Suran Tigrit (Tigrit)
  ID/Source: lord_6_6 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: none listed
  Settlement: Akiser Castle [castle_K2, castle, NavalDLC], Akkalat [town_K2, town, NavalDLC]

### Urkhunait (id clan_khuzait_1; culture Khuzait; home town_K3; owner Monchug)
  Clan XML note: KHUZAITS The Khuzaits thundered into the steppes west of Lake Baetiros two generations ago,
                 driving other nomads before them. They and their vassal tribes, the Khergit and the Arkit,
                 seized some of the cities on the fringe of the empire. They grew rich on the caravans from
                 the lands of the Padishah to the east, trading in their yurts for carpeted palaces. But
                 they still lead raids into the heart of the empire, their swift horse archers spreading
                 terror for leagues around their armies. (Minor faction:) The Hawlan are unsubjugated
                 nomads, living on the fringes of the Khuzait's kingdom. Other Khuzait mock them for living
                 only in yurts and smelling like the sheep dung they use for their fuel. They are what the
                 Khuzait used to be, but despite this - or perhaps because of this - the newly rich, newly
                 settled tribes treat them with scorn. Sons of Noyans have even been known to lead
                 expeditions into the deep steppe to hunt them like animals. The Khergit however turned to
                 them in their recent moment of crisis, using them as mercenaries.
Urkhun Urkhunait (Urkhunait)
  ID/Source: dead_lord_6_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: The great Khan Urkhun conquered the eastern frontiers of the Empire and established the Khuzait
        khanate. Most remember him as a hero, though some resent how he curtailed the ancient liberties of
        his people to transform them from nomads into lords of a kingdom.
  Family: none listed
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Monchug Urkhunait (Urkhunait)
  ID/Source: lord_6_1 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Monchug, the current khan of the Khuzaits, looks upon the Empire in its state of disarray and dreams
        of glory, of surpassing his ancestor Urkhun and conquering even deeper into the settled lands. Some
        of the clans have been decimated by the Urkhunids' wars, however, and feel their sacrifices have not
        been properly rewarded. They yearn for a khan who is less interested in glory, and more interested
        in justice.
  Note: Smart and devious
  Family: spouse Anat; children Alijin, Bolat, Bortu, Chaghan
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]
Alijin Urkhunait (Urkhunait)
  ID/Source: lord_6_10 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: heiresses
  Note: Urkhunait heiress. Manipulative, a bit pampered
  Family: parents father Monchug, mother Anat; siblings Bolat, Chaghan
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]
Bolat Urkhunait (Urkhunait)
  ID/Source: lord_6_101 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: none listed
  Family: parents father Monchug, mother Anat; siblings Alijin, Chaghan
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]
Bortu Urkhunait (Urkhunait)
  ID/Source: lord_6_13 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: lieutenants
  Note: Urkhunait lieutenant. Quiet voice of reason
  Family: parents father Monchug
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]
Anat Urkhunait (Urkhunait)
  ID/Source: lord_6_2 / SandBox
  Culture: Khuzait
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Monchug; children Alijin, Bolat, Chaghan
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]
Chaghan Urkhunait (Urkhunait)
  ID/Source: lord_6_7 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Heirs
  Note: Chagan, extremely protective of his family's primacy
  Family: parents father Monchug, mother Anat; siblings Alijin, Bolat
  Settlement: Tepes Castle [castle_K4, castle, NavalDLC], Makeb [town_K3, town, NavalDLC], Chaikand [town_K5, town, NavalDLC]

### Yanserit (id clan_khuzait_8; culture Khuzait; home castle_K3; owner Taslur)
Taslur Yanserit (Yanserit)
  ID/Source: lord_6_20 / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Taslur of the Yanserit. Cruel and clever. Manipulative
  Family: spouse Jigur
  Settlement: Hakkun Castle [castle_K3, castle, NavalDLC]
Jigur Yanserit (Yanserit)
  ID/Source: lord_6_20_1 / SandBox
  Culture: Khuzait
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Taslur
  Settlement: Hakkun Castle [castle_K3, castle, NavalDLC]
Boronchar Yanserit (Yanserit)
  ID/Source: lord_K8_u / SandBox
  Culture: Khuzait
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Earnest but ferocious
  Family: none listed
  Settlement: Hakkun Castle [castle_K3, castle, NavalDLC]

## Battania

### Unknown clan
Eren (Unknown clan)
  ID/Source: main_hero / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: main hero
  Note: <feat id="VlandianBattlePerception" value="10" />
  Note: <feat id="BattanianForestAgility" value="10" />
  Note: <feat id="KhuzaitCavalryAgility" value="10" />
  Note: <feat id="SturgianSnowAgility" value="10" />
  Note: Light Armor
  Note: Medium Armor
  Note: Heavy Armor
  Note: Heaviest Armor
  Note: Make sure to update main_hero riding skill to horse difficulty if you change horse
  Family: none listed
  Settlement: none listed

### fen Caernacht (id clan_battania_8; culture Battania; home castle_B1; owner Maireas)
  Clan XML note: fen Caernacht, resentful clan
Guaran fen Caernacht (fen Caernacht)
  ID/Source: lord_B8_c / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: Son, wants to do other things with the clan
  Family: parents father Rodarac, mother Maireas
  Settlement: Ab Comer Castle [castle_B1, castle, NavalDLC]
Maireas fen Caernacht (fen Caernacht)
  ID/Source: lord_B8_l / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: ironic
  Note: Marein, matriarch of the clan. Ruthless but attentive to others
  Family: spouse Rodarac; children Guaran
  Settlement: Ab Comer Castle [castle_B1, castle, NavalDLC]
Rodarac fen Caernacht (fen Caernacht)
  ID/Source: lord_B8_s / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: Rodarac, red-faced angry warlord
  Family: spouse Maireas; children Guaran
  Settlement: Ab Comer Castle [castle_B1, castle, NavalDLC]

### fen Derngil (id clan_battania_2; culture Battania; home town_B2; owner Ergeon)
Alynneth fen Derngil (fen Derngil)
  ID/Source: lord_5_11 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: Alynneth, Heiress of clan 2, Ergeon's daughter. Mystic.
  Family: parents father Ergeon; siblings Ranaon, Sein
  Settlement: Aster Castle [castle_B7, castle, NavalDLC], Dunglanys [town_B2, town, NavalDLC]
Ergeon fen Derngil (fen Derngil)
  ID/Source: lord_5_3 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Ergeon is head of the fen Derngil and brother of the vanished king Aeril. Although his clan deeply
        resents Caladog, whom they consider a lowborn upstart who probably had something to do with King
        Uthelhain's disappearance, Ergeon insists that his relatives remain loyal to the new king. The fen
        Derngils have always stood for a strong monarchy, and he is loathe to return the Battanians to the
        anarchy that consumed them for much of their history.
  Note: REMOVED: Aireen. Surprisingly gentle and compassionate wife, to whom he is devoted
  Note: Ergeon fen Derngil, submits to Caradog because he recognizes his capacity to lead, cautious
  Family: spouse Nywin; children Alynneth, Ranaon, Sein
  Settlement: Aster Castle [castle_B7, castle, NavalDLC], Dunglanys [town_B2, town, NavalDLC]
Ranaon fen Derngil (fen Derngil)
  ID/Source: lord_5_3_1 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Ergeon's daughter. Committed to the clan, but precocious enough to have independent ideas about her
        father's decisions
  Family: parents father Ergeon; siblings Alynneth, Sein
  Settlement: Aster Castle [castle_B7, castle, NavalDLC], Dunglanys [town_B2, town, NavalDLC]
Ladogual fen Derngil (fen Derngil)
  ID/Source: lord_5_3_2 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Cousin of Ergeon. Risk-averse and devious, but ambitious
  Family: none listed
  Settlement: Aster Castle [castle_B7, castle, NavalDLC], Dunglanys [town_B2, town, NavalDLC]
Nywin fen Derngil (fen Derngil)
  ID/Source: lord_5_4 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: ironic
  Note: Nywin, Ergeon's younger wife. Should have her own lands. Devious, but kind.
  Family: spouse Ergeon
  Settlement: Aster Castle [castle_B7, castle, NavalDLC], Dunglanys [town_B2, town, NavalDLC]
Sein fen Derngil (fen Derngil)
  ID/Source: lord_5_8 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: Sein fen Derngil, heir of Ergeon, gallant
  Family: parents father Ergeon; siblings Alynneth, Ranaon
  Settlement: Aster Castle [castle_B7, castle, NavalDLC], Dunglanys [town_B2, town, NavalDLC]

### fen Eingal (id clan_battania_6; culture Battania; home castle_B3; owner Aradwyr)
Aradwyr fen Eingal (fen Eingal)
  ID/Source: lord_5_17 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Aradwyr, decent but devious. Clever but thinks he is smarter than others, out of touch with
        mainstream
  Family: spouse Brighan
  Settlement: Druimmor Castle [castle_B3, castle, NavalDLC]
Brighan fen Eingal (fen Eingal)
  ID/Source: lord_5_17_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Aradwyr
  Settlement: Druimmor Castle [castle_B3, castle, NavalDLC]
Carfyd fen Eingal (fen Eingal)
  ID/Source: lord_5_21 / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Carfyd. Dour traditionalist.
  Family: spouse Beathag; children Taorse
  Settlement: Druimmor Castle [castle_B3, castle, NavalDLC]
Beathag fen Eingal (fen Eingal)
  ID/Source: lord_5_21_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: spouse Carfyd; children Taorse
  Settlement: Druimmor Castle [castle_B3, castle, NavalDLC]
Taorse fen Eingal (fen Eingal)
  ID/Source: lord_5_21_2 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: parents father Carfyd, mother Beathag
  Settlement: Druimmor Castle [castle_B3, castle, NavalDLC]

### fen Giall (id clan_battania_5; culture Battania; home town_B5; owner Aeron)
Aeron fen Giall (fen Giall)
  ID/Source: lord_5_16 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: Aeron. Impulsive, and likes it that way. Varies between rage and generosity
  Family: spouse Liasin; children Gawen
  Settlement: Pen Cannoc [town_B5, town, NavalDLC]
Liasin fen Giall (fen Giall)
  ID/Source: lord_5_16_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: spouse Aeron; children Gawen
  Settlement: Pen Cannoc [town_B5, town, NavalDLC]
Gawen fen Giall (fen Giall)
  ID/Source: lord_5_16_2 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: teenager
  Family: parents father Aeron, mother Liasin
  Settlement: Pen Cannoc [town_B5, town, NavalDLC]
Siaramus fen Giall (fen Giall)
  ID/Source: lord_5_20 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: Siaramus. Calculating. Wellington type
  Family: none listed
  Settlement: Pen Cannoc [town_B5, town, NavalDLC]

### fen Gruffendoc (id clan_battania_1; culture Battania; home town_B1; owner Caladog)
  Clan XML note: BATTANIA Minors: Wolfskins
Caladog fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_1 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: ironic
  Note: The current High King of Battania is Caladog, a brilliant war captain adopted by the prior king,
        Aeril, who then died in mysterious circumstances. Despite the doubts around his accession, Caladog
        has made himself popular among the lesser clans of the land who admire him, a man of no great
        lineage, for having discomfited the Battanians' traditional clan hierarchy. His clan is the fen
        Gruffendoc, a formerly obscure family now swollen with his comrades-in-arms with whom he has made
        marriage alliances.
  Note: BATTANIANS
  Note: Caladog fen Gruffendoc, ruthless
  Family: children Corein, Mengus, Merag
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]
Corein fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_10 / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: curt
  Note: lords 10-12 - heiresses
  Note: Corein, Caladog's daughter, fierce and haughty
  Note: COMBATANT FEMALE
  Family: parents father Caladog; siblings Mengus, Merag
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]
Muinser fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_13 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: lords 13-15 - lieutenants
  Note: Muinser fen , conventional.
  Family: children Beasag, Rath
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]
Rath fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_131 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Rath, Muinser's son
  Family: parents father Muinser; siblings Beasag
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]
Beasag fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_13_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: Teenager, no skills or traits
  Family: parents father Muinser; siblings Rath
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]
Merag fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_1_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: CHILD, YOUNGER DAUGHTER OF CALADOG
  Family: parents father Caladog; siblings Corein, Mengus
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]
Mengus fen Gruffendoc (fen Gruffendoc)
  ID/Source: lord_5_7 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: earnest
  Note: Mengus fen Gruffendoc, heir of Caladog, under spell of father
  Family: parents father Caladog; siblings Corein, Merag
  Settlement: Rhemtoil Castle [castle_B5, castle, NavalDLC], Uthelaim Castle [castle_B8, castle, NavalDLC], Marunath [town_B1, town, NavalDLC]

### fen Morcar (id clan_battania_7; culture Battania; home castle_B2; owner Pryndor)
Pryndor fen Morcar (fen Morcar)
  ID/Source: lord_5_15 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: curt
  Note: Pryndor fen Uvain, fierce old warlord
  Family: children Beitrin, Branoc, Diarbhain, Floraidh
  Settlement: Llanoc Hen Castle [castle_B2, castle, NavalDLC]
Floraidh fen Morcar (fen Morcar)
  ID/Source: lord_5_15_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel)
  Voice: ironic
  Note: Floraidh, Pryndor's daughter
  Family: parents father Pryndor; siblings Beitrin, Branoc, Diarbhain
  Settlement: Llanoc Hen Castle [castle_B2, castle, NavalDLC]
Beitrin fen Morcar (fen Morcar)
  ID/Source: lord_5_15_2 / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: Beitrin, Pryndor's heir, weak personality, somewhat nasty
  Family: parents father Pryndor; siblings Branoc, Diarbhain, Floraidh
  Settlement: Llanoc Hen Castle [castle_B2, castle, NavalDLC]
Diarbhain fen Morcar (fen Morcar)
  ID/Source: lord_5_15_3 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: ironic
  Note: Teenager
  Family: parents father Pryndor; siblings Beitrin, Branoc, Floraidh
  Settlement: Llanoc Hen Castle [castle_B2, castle, NavalDLC]
Branoc fen Morcar (fen Morcar)
  ID/Source: lord_5_18 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Branoc, straightforward if bombastic
  Family: spouse Seonag; parents father Pryndor; siblings Beitrin, Diarbhain, Floraidh
  Settlement: Llanoc Hen Castle [castle_B2, castle, NavalDLC]
Seonag fen Morcar (fen Morcar)
  ID/Source: lord_5_18_1 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: spouse Branoc
  Settlement: Llanoc Hen Castle [castle_B2, castle, NavalDLC]

### fen Penraic (id clan_battania_4; culture Battania; home town_B4; owner Luichan)
  Clan XML note: Fen Uvain Old house, know they lack the charisma to conquer, prefer to plot to maintain
                 their independence Good ties to Wolfskins Meledir. Patriarch (5_5) - Cautious, deceitful,
                 unctuous, Inactive queen (5_6) Heir - Culharn (5_9) conventional Heiress (5_12) Lieutenant
                 (5_15)
Luichan fen Penraic (fen Penraic)
  ID/Source: lord_5_14 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Luichan, former clan 2, made independent. Decent, somewhat naive
  Family: spouse Eabyr
  Settlement: Flintolg Castle [castle_B6, castle, NavalDLC], Seonon [town_B4, town, NavalDLC]
Eabyr fen Penraic (fen Penraic)
  ID/Source: lord_5_14_1 / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Luichan
  Settlement: Flintolg Castle [castle_B6, castle, NavalDLC], Seonon [town_B4, town, NavalDLC]
Fenagan fen Penraic (fen Penraic)
  ID/Source: lord_5_19 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Fenagan, gallant
  Family: none listed
  Settlement: Flintolg Castle [castle_B6, castle, NavalDLC], Seonon [town_B4, town, NavalDLC]
Fiarad fen Penraic (fen Penraic)
  ID/Source: lord_5_22 / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: none listed
  Settlement: Flintolg Castle [castle_B6, castle, NavalDLC], Seonon [town_B4, town, NavalDLC]

### fen Uvain (id clan_battania_3; culture Battania; home town_B3; owner Melidir)
Wythuin fen Uvain (fen Uvain)
  ID/Source: lord_5_12 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: Wythuin, heiress of clan 3, fen Uvain daughter, conspiratorial
  Family: parents father Melidir, mother Alcaea; siblings Culharn, Eilidh, Tegan
  Settlement: Pendraic Castle [castle_B4, castle, NavalDLC], Car Banseth [town_B3, town, NavalDLC]
Melidir fen Uvain (fen Uvain)
  ID/Source: lord_5_5 / SandBox
  Culture: Battania
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Meledir fen Uvain, unctuous
  Family: spouse Alcaea; children Culharn, Eilidh, Tegan, Wythuin
  Settlement: Pendraic Castle [castle_B4, castle, NavalDLC], Car Banseth [town_B3, town, NavalDLC]
Eilidh fen Uvain (fen Uvain)
  ID/Source: lord_5_5_1 / SandBox
  Culture: Battania
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: parents father Melidir, mother Alcaea; siblings Culharn, Tegan, Wythuin
  Settlement: Pendraic Castle [castle_B4, castle, NavalDLC], Car Banseth [town_B3, town, NavalDLC]
Alcaea fen Uvain (fen Uvain)
  ID/Source: lord_5_6 / SandBox
  Culture: Empire
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: Alcaea, imperial bride
  Family: spouse Melidir; children Culharn, Eilidh, Tegan, Wythuin
  Settlement: Pendraic Castle [castle_B4, castle, NavalDLC], Car Banseth [town_B3, town, NavalDLC]
Culharn fen Uvain (fen Uvain)
  ID/Source: lord_5_9 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Culharn fen Uvain, conventional
  Family: parents father Melidir, mother Alcaea; siblings Eilidh, Tegan, Wythuin
  Settlement: Pendraic Castle [castle_B4, castle, NavalDLC], Car Banseth [town_B3, town, NavalDLC]
Tegan fen Uvain (fen Uvain)
  ID/Source: lord_5_91 / SandBox
  Culture: Battania
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents father Melidir, mother Alcaea; siblings Culharn, Eilidh, Wythuin
  Settlement: Pendraic Castle [castle_B4, castle, NavalDLC], Car Banseth [town_B3, town, NavalDLC]

## Nord

### Dvarroving (id clan_nord_8; culture Nord/Nordvyg; home castle_N4; owner Toverik)
Toverik Dvarroving (Dvarroving)
  ID/Source: lord_7_20 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: spouse Hvana
  Settlement: Brunmark Castle [castle_N4, castle, NavalDLC]
Hvana Dvarroving (Dvarroving)
  ID/Source: lord_7_20_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Toverik
  Settlement: Brunmark Castle [castle_N4, castle, NavalDLC]

### Gauting (id clan_nord_5; culture Nord/Nordvyg; home castle_N1; owner Horgar)
Horgar Gauting (Gauting)
  ID/Source: lord_7_17 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: spouse Skathja
  Settlement: Agilting Castle [castle_N1, castle, NavalDLC]
Skathja Gauting (Gauting)
  ID/Source: lord_7_17_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: curt
  Note: none listed
  Family: spouse Horgar
  Settlement: Agilting Castle [castle_N1, castle, NavalDLC]
Bjorgir Gauting (Gauting)
  ID/Source: lord_7_22 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: spouse Hralsa
  Settlement: Agilting Castle [castle_N1, castle, NavalDLC]
Hralsa Gauting (Gauting)
  ID/Source: lord_7_22_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Bjorgir
  Settlement: Agilting Castle [castle_N1, castle, NavalDLC]
Yngvar Gauting (Gauting)
  ID/Source: lord_7_24 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: children Vystrun
  Settlement: Agilting Castle [castle_N1, castle, NavalDLC]
Vystrun Gauting (Gauting)
  ID/Source: lord_7_24_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents father Yngvar
  Settlement: Agilting Castle [castle_N1, castle, NavalDLC]

### Huldring (id clan_nord_7; culture Nord/Nordvyg; home castle_N9; owner Murin)
Unjort Huldring (Huldring)
  ID/Source: lord_7_15 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: spouse Tovsja; children Gudrinja, Liljan, Orthogar, Svalsa
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]
Tovsja Huldring (Huldring)
  ID/Source: lord_7_15_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: spouse Unjort; children Gudrinja, Liljan, Orthogar, Svalsa
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]
Gudrinja Huldring (Huldring)
  ID/Source: lord_7_15_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Unjort, mother Tovsja; siblings Liljan, Orthogar, Svalsa
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]
Svalsa Huldring (Huldring)
  ID/Source: lord_7_15_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: parents father Unjort, mother Tovsja; siblings Gudrinja, Liljan, Orthogar
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]
Orthogar Huldring (Huldring)
  ID/Source: lord_7_15_4 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Unjort, mother Tovsja; siblings Gudrinja, Liljan, Svalsa
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]
Liljan Huldring (Huldring)
  ID/Source: lord_7_15_5 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: parents father Unjort, mother Tovsja; siblings Gudrinja, Orthogar, Svalsa
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]
Murin Huldring (Huldring)
  ID/Source: lord_7_19 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor -1 (Cautious); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: none listed
  Settlement: Ulikshorn Castle [castle_N9, castle, NavalDLC]

### Kjolding (id clan_nord_2; culture Nord/Nordvyg; home town_N2; owner Grykka)
Grykka Kjolding (Kjolding)
  ID/Source: lord_7_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: Grykka Half-an-Ear came from a poor offshoot of the Kjoldings, and was little thought-of until the
        night that his uncle the jarl and his followers were trapped in their mead-hall by unknown warriors
        and the roof set alight. His hasty confirmation as jarl by the old king Volbjorn, left little doubt
        that he was the culprit, and had been suborned by the ruthless unifier of the Nordvyg. Despite this,
        or perhaps because of it, he is viewed with suspicion by Volbjorn's son and heir Halthdar.
  Family: children Gautgar, Heimkir, Iridrun
  Settlement: Tharklif Castle [castle_N2, castle, NavalDLC], Gretysfjord [town_N2, town, NavalDLC]
Gautgar Kjolding (Kjolding)
  ID/Source: lord_7_3_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: none listed
  Family: parents father Grykka; siblings Heimkir, Iridrun
  Settlement: Tharklif Castle [castle_N2, castle, NavalDLC], Gretysfjord [town_N2, town, NavalDLC]
Iridrun Kjolding (Kjolding)
  ID/Source: lord_7_3_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: softspoken
  Note: none listed
  Family: parents father Grykka; siblings Gautgar, Heimkir
  Settlement: Tharklif Castle [castle_N2, castle, NavalDLC], Gretysfjord [town_N2, town, NavalDLC]
Heimkir Kjolding (Kjolding)
  ID/Source: lord_7_3_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: none listed
  Family: parents father Grykka; siblings Gautgar, Iridrun
  Settlement: Tharklif Castle [castle_N2, castle, NavalDLC], Gretysfjord [town_N2, town, NavalDLC]
Agrynja Kjolding (Kjolding)
  ID/Source: lord_7_4 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: none listed
  Family: children Dyfa
  Settlement: Tharklif Castle [castle_N2, castle, NavalDLC], Gretysfjord [town_N2, town, NavalDLC]
Dyfa Kjolding (Kjolding)
  ID/Source: lord_7_4_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents mother Agrynja
  Settlement: Tharklif Castle [castle_N2, castle, NavalDLC], Gretysfjord [town_N2, town, NavalDLC]

### Orthling (id clan_nord_3; culture Nord/Nordvyg; home town_N3; owner Asgotha)
Asgotha Orthling (Orthling)
  ID/Source: lord_7_5 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: softspoken
  Note: The Orthling led the colonists of Beinland against King Volbjorn during the wars of unification.
        After their defeat they bowed to the inevitable, and offered their chief's daughter, Asgotha, as
        bride to the king's younger and far more popular brother Surnir. But the marriage, despite its
        inauspicious origins, turned out well. Asgotha was a shield maiden, and the couple fought
        side-by-side in battles, up until the day that Surnir was slain in a skirmish with the Sturgians.
        The new king Halthdar has confirmed her as jarl of Beinland, but many of her kinsmen chaff under the
        humiliation of Skylfing rule.
  Family: spouse Vulthir; children Aelfeyja, Kjarvon, Njasnir
  Settlement: Hakarshus Castle [castle_N7, castle, NavalDLC], Hvalvik [town_N1, town, NavalDLC]
Kjarvon Orthling (Orthling)
  ID/Source: lord_7_5_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents father Vulthir, mother Asgotha; siblings Aelfeyja, Njasnir
  Settlement: Hakarshus Castle [castle_N7, castle, NavalDLC], Hvalvik [town_N1, town, NavalDLC]
Aelfeyja Orthling (Orthling)
  ID/Source: lord_7_5_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Vulthir, mother Asgotha; siblings Kjarvon, Njasnir
  Settlement: Hakarshus Castle [castle_N7, castle, NavalDLC], Hvalvik [town_N1, town, NavalDLC]
Njasnir Orthling (Orthling)
  ID/Source: lord_7_5_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Vulthir, mother Asgotha; siblings Aelfeyja, Kjarvon
  Settlement: Hakarshus Castle [castle_N7, castle, NavalDLC], Hvalvik [town_N1, town, NavalDLC]
Vulthir Orthling (Orthling)
  ID/Source: lord_7_6 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Asgotha; children Aelfeyja, Kjarvon, Njasnir
  Settlement: Hakarshus Castle [castle_N7, castle, NavalDLC], Hvalvik [town_N1, town, NavalDLC]

### Rungniring (id clan_nord_6; culture Nord/Nordvyg; home castle_N3; owner Gafnir)
Gafnir Rungniring (Rungniring)
  ID/Source: lord_7_18 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: spouse Vitharsura
  Settlement: Ykerslund Castle [castle_N3, castle, NavalDLC]
Vitharsura Rungniring (Rungniring)
  ID/Source: lord_7_18_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +1 (Merciful/Kind)
  Voice: ironic
  Note: none listed
  Family: spouse Gafnir
  Settlement: Ykerslund Castle [castle_N3, castle, NavalDLC]
Karlek Rungniring (Rungniring)
  ID/Source: lord_7_23 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor -1 (Cautious); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: none listed
  Family: children Olvira, Ulvirinja
  Settlement: Ykerslund Castle [castle_N3, castle, NavalDLC]
Ulvirinja Rungniring (Rungniring)
  ID/Source: lord_7_23_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents mother Karlek; siblings Olvira
  Settlement: Ykerslund Castle [castle_N3, castle, NavalDLC]
Olvira Rungniring (Rungniring)
  ID/Source: lord_7_23_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: none listed
  Family: parents mother Karlek; siblings Ulvirinja
  Settlement: Ykerslund Castle [castle_N3, castle, NavalDLC]

### Skylfing (id clan_nord_4; culture Nord/Nordvyg; home town_N4; owner Gornlautir)
Gornlautir Skylfing (Skylfing)
  ID/Source: lord_7_14 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: spouse Gulsyf; children Alrika, Stohrith
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Gulsyf Skylfing (Skylfing)
  ID/Source: lord_7_14_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating +1 (Ambitious/Calculating)
  Voice: earnest
  Note: none listed
  Family: spouse Gornlautir; children Alrika, Stohrith
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Alrika Skylfing (Skylfing)
  ID/Source: lord_7_14_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents father Gornlautir, mother Gulsyf; siblings Stohrith
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Stohrith Skylfing (Skylfing)
  ID/Source: lord_7_14_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: TEENAGER, NO SKILLS OR TRAITS YET
  Family: parents father Gornlautir, mother Gulsyf; siblings Alrika
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Kautas Skylfing (Skylfing)
  ID/Source: lord_7_16 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: spouse Alsa
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Alsa Skylfing (Skylfing)
  ID/Source: lord_7_16_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind)
  Voice: earnest
  Note: none listed
  Family: spouse Kautas
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Svorni Skylfing (Skylfing)
  ID/Source: lord_7_21 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: ironic
  Note: none listed
  Family: spouse Bjolablum
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]
Bjolablum Skylfing (Skylfing)
  ID/Source: lord_7_21_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Svorni
  Settlement: Haugr Castle [castle_N6, castle, NavalDLC], Hargard [town_N4, town, NavalDLC]

### Throsniring (id clan_nord_1; culture Nord/Nordvyg; home town_N1; owner Halthdar)
Volbjorn the Hungry Throsniring (Throsniring)
  ID/Source: dead_lord_7_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Many over the years have styled themselves King of the Nordvyg, but Volbjorn the Hungry is the first
        for whom it was more than an empty title. As a young man he served the Empire as a mercenary,
        accumulating a huge horde of gold. With it, he returned home to transform his jarldom into a
        kingdom. Some who resisted him were defeated in battle, others were bought, and others found out
        that someone whom they trusted could be bought. It is whispered that, when Volbjorn was on his
        deathbed, he ordered himself sealed alive inside his barrow with his gold, so that greed and sorcery
        could transform him, and he could count it every night.
  Family: spouse Ilrika; children Halthdar
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Ilrika Throsniring (Throsniring)
  ID/Source: dead_lord_7_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: curt
  Note: Ilrika was the wife of Volbjorn the Hungry, first King of the Nordvyg. She was a caretaker of a
        woodland shrine, the keeper of secret rituals, and every bit as ambitious as her husband. When
        Volbjorn died, Ilrika's machinations ensured that her son, Halthdar, had no serious rivals for the
        throne. When his rule was secure, she soon died - or so the royal household claimed. Others say she
        returned to the woods, and some claim to see her wandering on moonless nights, ensuring none dare
        challenge the dynasty.
  Family: spouse Volbjorn the Hungry; children Halthdar
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
  Status: dead/alive="false" in Hero XML
Halthdar Throsniring (Throsniring)
  ID/Source: lord_7_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: Were Halthdar the Golden a petty chieftain or jarl, he would no doubt be beloved of all the warriors
        who followed him into battle and sat at his feast-table afterwards, to be showered with praise and
        rings. But he is a king, in a land that is still unhappy to be a kingdom. He is blamed by his jarls
        for the sins of his father, Volbjorn the Hungry, who created the Nordvyg with blood and trickery,
        and many long to return to the old days when they answered to no one.
  Family: spouse Jarminja; parents father Volbjorn the Hungry, mother Ilrika; children Mjalrik, Sidunric, Thyrsif
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Orvi Throsniring (Throsniring)
  ID/Source: lord_7_13 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: children Gunjadrid, Morgunja, Valmua, Yfinja
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Gunjadrid Throsniring (Throsniring)
  ID/Source: lord_7_13_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Orvi; siblings Morgunja, Valmua, Yfinja
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Yfinja Throsniring (Throsniring)
  ID/Source: lord_7_13_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: parents father Orvi; siblings Gunjadrid, Morgunja, Valmua
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Morgunja Throsniring (Throsniring)
  ID/Source: lord_7_13_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: TEENAGER, NO SKILLS OR TRAITS YET
  Family: parents father Orvi; siblings Gunjadrid, Valmua, Yfinja
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Valmua Throsniring (Throsniring)
  ID/Source: lord_7_13_4 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating -1 (Impulsive)
  Voice: curt
  Note: none listed
  Family: parents father Orvi; siblings Gunjadrid, Morgunja, Yfinja
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Mjalrik Throsniring (Throsniring)
  ID/Source: lord_7_1_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: earnest
  Note: none listed
  Family: parents father Halthdar, mother Jarminja; siblings Sidunric, Thyrsif
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Sidunric Throsniring (Throsniring)
  ID/Source: lord_7_1_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel)
  Voice: earnest
  Note: none listed
  Family: parents father Halthdar, mother Jarminja; siblings Mjalrik, Thyrsif
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Thyrsif Throsniring (Throsniring)
  ID/Source: lord_7_1_3 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy -1 (Cruel); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents father Halthdar, mother Jarminja; siblings Mjalrik, Sidunric
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]
Jarminja Throsniring (Throsniring)
  ID/Source: lord_7_2 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +1 (Honest/Honorable); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset)
  Voice: earnest
  Note: none listed
  Family: spouse Halthdar; children Mjalrik, Sidunric, Thyrsif
  Settlement: Skarthness Castle [castle_N8, castle, NavalDLC], Thronderlag [town_N3, town, NavalDLC]

### Visduring (id clan_nord_9; culture Nord/Nordvyg; home castle_N7; owner Dagvi)
Dagvi Visduring (Visduring)
  ID/Source: lord_7_25 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor -1 (Devious); Valor +0 (Neutral/unset); Mercy +0 (Neutral/unset); Other: Calculating +1 (Ambitious/Calculating)
  Voice: ironic
  Note: none listed
  Family: parents mother Drivana; children Otfar
  Settlement: Fimbulgard Castle [castle_N5, castle, NavalDLC]
Drivana Visduring (Visduring)
  ID/Source: lord_7_25_1 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity -1 (Closefisted); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy +0 (Neutral/unset)
  Voice: curt
  Note: none listed
  Family: children Dagvi
  Settlement: Fimbulgard Castle [castle_N5, castle, NavalDLC]
Otfar Visduring (Visduring)
  ID/Source: lord_7_26 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor +0 (Neutral/unset); Mercy +1 (Merciful/Kind); Other: Calculating -1 (Impulsive)
  Voice: earnest
  Note: none listed
  Family: parents father Dagvi
  Settlement: Fimbulgard Castle [castle_N5, castle, NavalDLC]
Anle Visduring (Visduring)
  ID/Source: lord_7_27 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +0 (Neutral/unset); Honor +0 (Neutral/unset); Valor +1 (Daring); Mercy -1 (Cruel); Other: Calculating -1 (Impulsive)
  Voice: softspoken
  Note: obediant enforcer of dakhila's will
  Family: none listed
  Settlement: Fimbulgard Castle [castle_N5, castle, NavalDLC]
Triven Visduring (Visduring)
  ID/Source: lord_7_28 / NavalDLC
  Culture: Nord/Nordvyg
  Traits: Generosity +1 (Generous); Honor +0 (Neutral/unset); Valor -1 (Cautious); Mercy +0 (Neutral/unset)
  Voice: softspoken
  Note: none listed
  Family: none listed
  Settlement: Fimbulgard Castle [castle_N5, castle, NavalDLC]
