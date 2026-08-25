# Research Registry

Do not place unverified historical claims in this file. Cite sources when research begins and mark uncertainty as `ASSUMPTION`.

## 1836 Ottoman Setup

## Population & Demographics

## States & Provinces

## Agriculture & Resources

- **R-04/R-05 — Ottoman resource-potential audit:** [`docs/research/R04_ottoman_resource_potential.md`](docs/research/R04_ottoman_resource_potential.md). Arable/agriculture and mineral/oil matrices were completed together, approved, and used in I-02 via Community State Framework state-level complete-key overrides. **COMPLETE AND USED IN I-02; TIGER CLEAN; RUNTIME SMOKE TEST PENDING.**

## Starting Buildings

- **R-06 — 1836 Ottoman starting economy audit:** [`docs/research/R06_ottoman_starting_economy_audit.md`](docs/research/R06_ottoman_starting_economy_audit.md). All 30 TUR region-states and all authored starting-building categories checked against vanilla 1.13.11; final proposal contains 12 state packages / 29 atomic building edits. **COMPLETE AND USED IN I-03; INITIAL RUNTIME SMOKE TEST SUBSTANTIALLY COMPLETED; FINAL/EXTENDED VALIDATION PENDING.** The user called the deliverable R-05, but the established roadmap reserves R-05 for minerals/oil and R-06 for the establishment inventory.

## Economy & Finance

- **R-19 — Ottoman companies/institutions inventory:** [`docs/research/R19_ottoman_companies_institutions_inventory.md`](docs/research/R19_ottoman_companies_institutions_inventory.md). Four named candidates were duplicate-checked against installed vanilla 1.13.11 companies, JEs, events, modifiers, technologies, laws and buildings. Vanilla already has Tersâne-i Âmire, Ottoman Tobacco Régie, Allatini Mills, Chemins de fer Orientaux and Turkish Petroleum. I-14 v1 roster: Şirket-i Hayriye as a port company; Bank-ı Osmanî-i Şahane as event/decision/modifier only. Memleket Sandıkları are not a company; Düyun-u Umumiye must not become a prosperity company because the Régie already covers the tobacco-monopoly slice. **COMPLETE AND USED IN I-14 `77397d5`.** The exact contract is [`docs/research/I14_ottoman_company_institution_proposal.md`](docs/research/I14_ottoman_company_institution_proposal.md); implementation dossier [`docs/implementation/I14_ottoman_company_institution_flavor.md`](docs/implementation/I14_ottoman_company_institution_flavor.md). Tiger clean for I-14; runtime pending.

## Ottoman Debt

- **R-19 companion finding:** Düyun-u Umumiye is not an I-14 company. Vanilla `company_ottoman_tobacco_regie` already represents the 1883 Régie tobacco monopoly created under the Public Debt Administration. A named OPDA constraint JE belongs to later debt/capitulations work (R-16 already marked that design **LATER**). See [`docs/research/R19_ottoman_companies_institutions_inventory.md`](docs/research/R19_ottoman_companies_institutions_inventory.md).

## Capitulations

- **I-16 Baltalimanı:** vanilla 1.13.11 has no Baltalimanı treaty. Implemented as a 1838 sign/refuse event creating a one-way `trade_privilege` (TUR grantor, GBR receiver), not DLC-gated `no_tariffs` / `foreign_investment_rights`. See [`docs/research/I16_ottoman_diplomatic_opening_proposal.md`](docs/research/I16_ottoman_diplomatic_opening_proposal.md) and [`docs/implementation/I16_ottoman_diplomatic_opening.md`](docs/implementation/I16_ottoman_diplomatic_opening.md). **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**

## Government & Centralization

- **R-16 — Ottoman institutional modernization:** [`docs/research/R16_institutional_modernization.md`](docs/research/R16_institutional_modernization.md). 1836–1876 merkezi bürokrasi, maliye/vergi, eğitim, ordu ve altyapı/devlet kapasitesi yalnız doğrulanmış vanilla law/institution/building/technology/JE-event karşılıklarıyla eşleştirildi. **COMPLETE — RESEARCH ONLY; I-05 REQUIREMENTS IDENTIFIED.**

- **R-18 — Provincial power and centralization:** [`docs/research/R18_provincial_power_centralization.md`](docs/research/R18_provincial_power_centralization.md). Ayanlar, vali/merkez ilişkisi, doğrudan vergi denemeleri, 1858 Land Code, 1864 Vilayet Law ve eşitsiz taşra kapasitesi incelendi; map fragmentation, ayan mana ve custom provincial system reddedildi. Belgenin sonunda R-16–R-18 sentezi olarak 10 maddelik I-05 Tanzimat design requirements kaydedildi. **COMPLETE — RESEARCH ONLY; I-05 REQUIREMENTS IDENTIFIED.**

- **R-20 — Post-Tanzimat political development:** [`docs/research/R20_post_tanzimat_political_development.md`](docs/research/R20_post_tanzimat_political_development.md). Late Tanzimat opposition through Kanun-i Esasi, Hamidian autocracy and Young Turks mapped onto vanilla 1.13.11 laws, movements, agitators and existing characters. **Kanuni Nizam is rejected as a custom institution**; Kanun-i Esasi maps to monarchy plus a limited voting franchise. **COMPLETE — USED IN I-18.** Gameplay **I-18** ([`docs/implementation/I18_post_tanzimat_political_development.md`](docs/implementation/I18_post_tanzimat_political_development.md); proposal [`docs/research/I18_post_tanzimat_political_development_proposal.md`](docs/research/I18_post_tanzimat_political_development_proposal.md)): five one-shot events; 1908 SKIP. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING** in `b530930`.

## Tanzimat

- **R-07 — Tanzimat / Sick Man vanilla concordance:** [`docs/research/R07_tanzimat_vanilla_concordance.md`](docs/research/R07_tanzimat_vanilla_concordance.md). Victoria 3 1.13.11 ana Sick Man JE'si, altı başlangıç objective'i, koşullu Egypt JE'si, dört-puan/30-yıl mantığı, sonuçlar, event zincirleri, DLC gate'leri ve AI ağırlıkları vanilla script ile tarihsel mekanizma karşılaştırması üzerinden denetlendi. SME-01 exact `0.5` dead zone'u statik olarak yeniden doğrulandı; hiçbir fix veya gameplay implementasyonu yapılmadı. **COMPLETE — RESEARCH ONLY; I-05/I-06 CANDIDATES IDENTIFIED; RUNTIME AI/SME TESTS PENDING.**

- **I-06 — Sick Man outcome audit and implementation:** [`docs/research/I06_sick_man_outcome_proposal.md`](docs/research/I06_sick_man_outcome_proposal.md), [`docs/implementation/I06_sick_man_outcomes.md`](docs/implementation/I06_sick_man_outcomes.md). SME-01 inclusive failure, objective-specific success rewards, unconditional bureaucracy cleanup/ruler death, serious failure preservation, and I-04/I-05 regression boundaries were audited against installed vanilla 1.13.11. The approved package is implemented in `d3e391e`: one ten-year universal reward plus exactly one of twelve completed-objective-gated specializations, with the six generic Balkan claims reduced to one guarded Crete claim. **IMPLEMENTED — TIGER CLEAN FOR I-06; RUNTIME SMOKE TEST PENDING.**

- **I-05 Tanzimat objective gameplay design (user-requested R19 filename):** [`docs/research/R19_tanzimat_gameplay_design.md`](docs/research/R19_tanzimat_gameplay_design.md). R-07/R-16/R-17/R-18 source-of-truth senteziyle altı objective için engine-doğrulanmış exact completion sözleşmesi ve statik kalibrasyon çıkarıldı; onaylanan sözleşme [`I05_tanzimat_objective_rework.md`](docs/implementation/I05_tanzimat_objective_rework.md) ile uygulandı. Canonical roadmap'taki R-19 historical companies/institutions kaydı değiştirilmedi. **APPROVED AND IMPLEMENTED AS I-05; TIGER CLEAN FOR I-05; MANUAL RUNTIME CALIBRATION PENDING.**

## Millet System

- **R-17 — Millet, equality and Ottoman subjecthood:** [`docs/research/R17_millet_equality.md`](docs/research/R17_millet_equality.md). 1836 millet düzeni, Gülhane, 1856 Islahat, Müslim/gayrimüslim eşitliği, askerlik/vergi ve 1869 citizenship dönüşümü mevcut discrimination, law, institution, movement ve Tanzimat event sistemleriyle eşleştirildi; custom millet institution/currency reddedildi. **COMPLETE — RESEARCH ONLY; I-05 REQUIREMENTS IDENTIFIED.**

## Army

- **R-13 — Ottoman 1836 full military setup audit:** [`docs/research/R13_ottoman_military_setup.md`](docs/research/R13_ottoman_military_setup.md). Installed vanilla 1.13.11 and the current I-11 setup were audited formation-by-formation against EGY, Mansure/Hassa/Redif history, naval rebuilding, I-05, I-07, and I-03 supply constraints. The approved four-army, 160-battalion, 30%-irregular package was implemented without changing the 28-flotilla fleet or military industry. **COMPLETE AND USED IN I-09 `1049242`; TIGER CLEAN FOR I-09; RUNTIME TEST PENDING.**

## Navy

## Egypt

- **R-09 — Egypt / Eastern Question audit and I-07 proposal:** [`docs/research/R09_egypt_eastern_question.md`](docs/research/R09_egypt_eastern_question.md), [`docs/research/I07_egypt_eastern_question_gameplay_proposal.md`](docs/research/I07_egypt_eastern_question_gameplay_proposal.md). Victoria 3 1.13.11 vanilla ve mevcut mod üzerinden setup, Levant/Adana, aktif kriz internationalization, Nizip/London settlement boşluğu, GP alignment, subject/peace/front riskleri ve I-05/I-06 sınırları denetlendi. Onaylanan üç-outcome proposal değiştirilmeden I-07 olarak uygulandı. **R-09 COMPLETE AND USED; I-07 IMPLEMENTED IN `f4a8634`; TIGER CLEAN FOR I-07; RUNTIME AI/FRONT TESTS PENDING.**
- **I-16 must not duplicate I-07.** Egypt protectorate/own-market and the Eastern Question outcome layer stay I-07. I-16 added complementary 1836–41 diplomacy (Hünkâr İskelesi, Baltalimanı) without editing I-07 files. I-16B only restricts join-side during that crisis window. See [`docs/research/I16B_egypt_crisis_gp_alignment.md`](docs/research/I16B_egypt_crisis_gp_alignment.md).

## Balkans

- **R-10 — Ottoman Balkan cohesion audit:** [`docs/research/R10_ottoman_balkan_cohesion.md`](docs/research/R10_ottoman_balkan_cohesion.md). Victoria 3 1.13.11 Cultural Fervor → cultural-minority movement → radicalism/obstinance/turmoil → secession chain; 1836 Bulgarian, Serbian, Greek, Albanian, Bosniak, Romanian and Croat setup; `Support Separatism`; laws/institutions; subjects; I-04–I-07 interactions and three vanilla-first player routes were audited. The dossier rejects a custom cohesion bar/mana, permanent stability buff and per-state checklist. **COMPLETE AND USED IN I-08 `64ca4e9`; DATE-GATED GEC CULTURE-FILTER ROWS DEFERRED TO FINAL RELEASE VALIDATION.**
- **I-08 — Ottoman Balkan cohesion:** [`docs/research/I08_balkan_cohesion_gameplay_proposal.md`](docs/research/I08_balkan_cohesion_gameplay_proposal.md), [`docs/implementation/I08_balkan_cohesion.md`](docs/implementation/I08_balkan_cohesion.md). One non-progress guidance JE, one effect-free introductory event, Police/Home Affairs clarity, the verified seven-culture GEC-01 activation predicate and GEC-04 movement-gate filter were implemented in `64ca4e9`. Global war, growing-secession convenience triggers and crushed-secession attribution remain deliberately deferred. **IMPLEMENTED — STATIC/TIGER REVIEW COMPLETE; 1836 `sp_balkan_cohesion.1` PASS (informational/effect-free).**

## Kurdish Regions & Tribes

- **R-21 — Kurdish provincial autonomy and centralization:** [`docs/research/R21_kurdish_provincial_autonomy_centralization.md`](docs/research/R21_kurdish_provincial_autonomy_centralization.md). User-supplied 1836–47 contract audited against vanilla 1.13.11 and current mod overlap (I-01, I-05, I-06, I-08, I-09, I-11, I-18). Frame is **centralization vs emirates/local notables**, not Kurdish nationalism. **COMPLETE — USED IN I-21 PROPOSAL.**
- **I-21 — Kurdish provincial centralization:** proposal [`docs/research/I21_kurdish_provincial_centralization_proposal.md`](docs/research/I21_kurdish_provincial_centralization_proposal.md); dossier [`docs/implementation/I21_kurdish_provincial_centralization.md`](docs/implementation/I21_kurdish_provincial_centralization.md). Four additive TUR events (`sp_i21.1`–`.4`), 1836–1850 window, I-18 yearly-pulse pattern, event-only Bedirhan, read-only I-05 centralization triggers, double-punishment gate (SKIP + negligible enforce radicals). **No JE, no `c:KUR`, no forced revolt, no permanent buffs.** `.1`/`.2`/`.4` zero-effect; accommodate = Landowners +2 + tiny loyalists; enforce = tiny Kurdish radicals in Diyarbakır only. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**

## Armenian Question & Eastern Anatolian Nationalism

- **R-22 — Armenian Question and eastern Anatolian nationalism:** [`docs/research/R22_armenian_question_eastern_anatolian_nationalism.md`](docs/research/R22_armenian_question_eastern_anatolian_nationalism.md). User-supplied three-phase contract (Tanzimat communal reform → 1878 Berlin turning point → 1880s+ organized nationalism) audited against vanilla 1.13.11 and current mod overlap (I-01, I-05, I-06, I-08, I-12, I-14, I-16, I-18, I-21). Vanilla already covers discrimination, `movement_cultural_minority` secession, Islahat (`tanzimat_events.4`), communal violence (`.5`–`.8`), and GEC Balkan filtering. **1863 YES** (NO-EFFECT communal-constitution acknowledgement). **1878 YES** (reactive diplomatic flavor; date + political/state gate, not exact war outcome). **Hunchak/Dashnak NO.** R-22 mechanical scope unchanged (no forced revolt, no new nationalism system). **COMPLETE — RESEARCH ONLY; USED IN I-22.** **Journal Presentation Pass Phase 2** informational umbrella JE implemented via I-22 — see [`docs/implementation/I22_armenian_question.md`](docs/implementation/I22_armenian_question.md).
- **I-22 — Armenian Question:** proposal [`docs/research/I22_armenian_question_proposal.md`](docs/research/I22_armenian_question_proposal.md); dossier [`docs/implementation/I22_armenian_question.md`](docs/implementation/I22_armenian_question.md). Two additive TUR events (`sp_i22.1`, `sp_i22.2`) + one informational umbrella JE (`sp_je_armenian_question`). Both events **NO EFFECT** (one-shot flags only); repression path **loc variant only**; no `change_relations`; no Diyarbakır effects; no `c:ARM`; no forced revolt. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**

## Arab Provinces

- **R-23 — Imperial Periphery:** [`docs/research/R23_imperial_periphery.md`](docs/research/R23_imperial_periphery.md). User-supplied three-theatre contract (Trablusgarp / Tunis / Arabia–Red Sea) audited against vanilla 1.13.11. Vanilla already splits sovereignty: `c:TRI` TUR **puppet** with Ottoman governor Mahmud Raif (1835 restoration abstraction) + Fezzan starting war + unincorporated Cyrenaica; `c:TUN` TUR **protectorate** (Husaynid Mustafa/Ahmad; cannot annex until LD &lt; 25 then decrease autonomy); Hedjaz `c:HDJ` is **EGY tributary** (I-07); Nejd/Jabal Shammar independent (JAB in Ottoman power bloc + pro-TUR lobby); Yemen split among Azal/Lahej/Mahra/Kathiri/Hedjaz with **Aden as Lahej city hub**, not British; al-Hasa is a Nejd farm hub; **no Senussi** tag/religion/JE (closest native: decentralized `c:ZWY` Zuwayya). **Tripoli YES** (1 informational event; no map rewrite). **Tunisia YES** (2 events; keep protectorate). **Arabia NO.** **Yemen YES** (Aden alarm only). **Al-Hasa NO.** **Senussi NO.** **Umbrella JE NO.** **Subject rewrite NO.** Approx **4** events. **COMPLETE — RESEARCH ONLY; PROPOSAL-READY.** I-23 proposal not written and not authorized.

## Migration & Muhacirs

- **R-14 — Ottoman Muhacir chronology and settlement audit:** [`docs/research/R14_muhacir_chronology.md`](docs/research/R14_muhacir_chronology.md). 1854–58 is a Tatar precursor, not the mass wave; 1859–62 Tatar/Nogai *Büyük Göç*, 1860 Muhacirin Komisyonu, 1857 immigration regulations, 1863–66 Circassian peak (1864 centerpiece), and 1877–78 Rumelian refugee crisis were verified against scholarship and installed vanilla 1.13.11. Vanilla SoI already `move_pop`s Circassians into Eastern Thrace/Kastamonu/Trabzon. Hybrid conservation-first architecture is recommended. **COMPLETE — RESEARCH ONLY.**

- **I-12 — Muhacir migration slice:** [`docs/research/I12_muhacir_gameplay_proposal.md`](docs/research/I12_muhacir_gameplay_proposal.md); dossier [`docs/implementation/I12_muhacir_migration.md`](docs/implementation/I12_muhacir_migration.md). **IMPLEMENTED** in `c99a081` (Waves A/B/C, commission JEs, B9 provenance stamps, EN/TR). Tiger clean for I-12; runtime pending. No Circassian `create_pop`; no `create_mass_migration`; no I-01–I-11 gameplay edits.

- **I-13 — Muhacir settlement flavor:** [`docs/research/I13_muhacir_settlement_flavor_proposal.md`](docs/research/I13_muhacir_settlement_flavor_proposal.md); dossier [`docs/implementation/I13_muhacir_settlement_flavor.md`](docs/implementation/I13_muhacir_settlement_flavor.md). Four one-shot vanilla-style events bound to wired I-12 identifiers. No pop movement, no new JE/system, no I-12 retune. **IMPLEMENTED — TIGER CLEAN FOR I-13; RUNTIME PENDING.**

## Settlement Policies

## Great Power Diplomacy

- **R-08 — Great Eastern Crisis reproduction matrix:** [`docs/research/R08_gec_reproduction_matrix.md`](docs/research/R08_gec_reproduction_matrix.md). Victoria 3 1.13.11 vanilla and current-mod script/scope audit completed for GEC-01–08. The approved four-fix minimum slice was implemented as I-04 in `53e870d`; controlled runtime validation, player/AI comparison, and SME exact-0.5 reproduction remain pending/unproduced. **COMPLETE — USED IN I-04; TIGER CLEAN FOR I-04; RUNTIME SMOKE TEST PENDING.**

- **I-16 — Ottoman Diplomatic Opening (1836–1841):** proposal [`docs/research/I16_ottoman_diplomatic_opening_proposal.md`](docs/research/I16_ottoman_diplomatic_opening_proposal.md); dossier [`docs/implementation/I16_ottoman_diplomatic_opening.md`](docs/implementation/I16_ottoman_diplomatic_opening.md). Installed vanilla 1.13.11 diplomacy audit of TUR vs RUS, GBR, AUS, PRU, FRA, EGY, GRE, PER, SER, WAL, MOL, TUN. Gameplay `0cf714d20468e1d03491ac77b4666e89deda2022`. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**

  Vanilla sources inspected: `common/history/treaties/00_historical_treaties.txt`; `common/history/diplomacy/00_{relations,rivalries,subject_relationships,truces,embargos}.txt`; `common/history/ai/00_{behavior_variables,strategy,secret_goals}.txt`; `common/history/lobbies/00_lobbies.txt`; `common/treaty_articles/{00_alliance,01_defensive_pact,02_guarantee_independence,12_military_assistance,25_trade_privilege,07_foreign_investment_rights,21_no_tariffs,33_strait_access,34_no_strait_closure,treaty_articles.md}`; `common/ai_strategies/00_default_strategy.txt`; `common/on_actions/00_code_on_actions.txt` (Egypt yearly flip; `on_country_broke_treaty`); `common/defines/00_{defines,ai}.txt`; `common/diplomatic_catalysts/00_diplomatic_catalysts.txt`; `localization/english/{diplomatic_treaties,concepts}_l_english.yml`; unused loc `treaty_name_hunkar_iskelesi`.

  **NO CHANGE countries (vanilla already matches the historical target closely enough):** GBR 1836 setup, AUS, PRU (keep existing Military Assistance; do not duplicate), EGY subject/market/truce (I-07 owns the crisis), GRE, PER, SER, WAL, MOL, TUN.

  **Implemented v1:** Hünkâr İskelesi as historical `guarantee_independence` (keep rivalry); 1841 lapse `withdraw` event because binding period does not auto-delete treaties; 1838 Baltalimanı sign/refuse → one-way `trade_privilege`. I-16 FRA `veiled_protectorate_support_egypt` was **removed by I-16B** (military join risk). GBR/AUS/RUS/PRU Egypt-crisis weights already exist in vanilla.

  **Runtime risks / not static blockers:** rivalry+guarantee coexistence (RT-1); Call Ally only when TUR is defender (RT-2); 1841 withdraw without break penalties (RT-3); Baltalimanı market impact (RT-5); I-16B join-side restriction (RT-16B-01–10).

- **I-16B — Egypt Crisis Great-Power alignment:** [`docs/research/I16B_egypt_crisis_gp_alignment.md`](docs/research/I16B_egypt_crisis_gp_alignment.md); dossier [`docs/implementation/I16B_egypt_crisis_gp_alignment.md`](docs/implementation/I16B_egypt_crisis_gp_alignment.md). Vanilla `veiled_protectorate_support_ottomans` is only +100 TUR-side weight, not an EGY-side ban. I-07 does not steer the play. Native hook is `can_join_side_in_diplomatic_play`. Gameplay `01a18aec4789320d6899cbc4b5bf10cbad594fe9`. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**

## Crimean War

## Ottomanism

- **R-20 mapping:** inclusive citizenship/subjecthood, legitimacy and I-05/I-08 equality/reform routes. Not a custom movement. See [`docs/research/R20_post_tanzimat_political_development.md`](docs/research/R20_post_tanzimat_political_development.md). **RESEARCH ONLY.**

## Islamism

- **R-20 mapping:** `law_millet_system`, Devout IG, `movement_religious_majority`, traditionalist/theocrat characters (including I-10A Ahmed Cevdet). Not a theocracy mandate or custom Islamist ideology. **RESEARCH ONLY.**

## Turkism

- **R-20 mapping:** late `movement_cultural_majority` / `ideology_ethno_nationalist` / vanilla Enver. Do not back-project into 1836. Turan and new Turkic cultures remain deferred. **RESEARCH ONLY.**

## Young Ottomans

- **R-20 + I-10A:** named window from 1865. Nâmık Kemal already implemented as ungated Intelligentsia liberal agitator (`1865.6.1–1888.12.2`). Vanilla liberal movement is blocked while Traditionalism or Peasant Levies remain. Ziyâ/Ali Suâvi remain deferred. **RESEARCH ONLY for R-20 flavor; I-10A character already shipped.**

## First Constitutional Era

- **R-20:** Kanun-i Esasi (23 Dec 1876; parliament 1877–Feb 1878) maps to keeping `law_monarchy` and enacting a limited voting franchise (`law_wealth_voting` / `law_census_voting` preferred over oligarchy or universal suffrage). Vanilla Midhat already covers the constitutional grand vizier. No custom constitution law. **USED IN I-18** (`sp_i18.4` names an existing franchise; does not enact one).

## Abdulhamid II

- Vanilla NA succession (`ottoman_monarchs.2`, `tur_abdulhamid_ii_osmanoglu_template`, authoritarian Landowners). Hamidian restoration maps to re-enacting `law_autocracy` after a franchise. Do not replace the succession chain. **I-18 `sp_i18.5` is flavor only** after `sp_i18_constitution_seen`.

## Young Turks

- **R-20:** named organization not before 1889; restoration not before 1908. Vanilla Enver (1906 agitator / 1908 IG leader) and Prince Sabahaddin (1899 agitator) already cover CUP-military and liberal-decentralist poles. Do not reimplement Enver. **I-18 SKIPPED 1908.**

## Second Constitutional Era

- **R-20:** 1908 restoration of the 1876 constitution; 1909 amendments are a later law-state, not a new mechanic. Optional late event only; vanilla characters/radicals may suffice. **RESEARCH ONLY.**

## CUP

- Covered by vanilla Enver + late Armed Forces ethno-nationalism. No CUP institution, party object or 1836 spawn. **RESEARCH ONLY.**

## Historical Characters

- **Ottoman Characters & Naming Audit — Victoria 3 1.13.11:** [`docs/audits/ottoman-characters-naming-audit.md`](docs/audits/ottoman-characters-naming-audit.md). Vanilla Turkish name pools, rulers/heirs, starting and generated commanders, and existing mod overlap audited against 19th-century register studies and commander biographies; final proposal retains five day-one commanders by replacing Abdülkerim Nâdir with Dârendeli İzzet Mehmed Paşa. **R-12 COMPLETE; OPENING-COMMANDER SLICE USED BY COMPLETED R-11; IMPLEMENTED AS CANONICAL I-11 IN COMMIT `e456401`; RUNTIME SMOKE TEST PENDING.**
- **R-11 — Character/Commander Dossier:** [`docs/research/R11_character_commander_dossier.md`](docs/research/R11_character_commander_dossier.md). I-10A is implemented in `c91e515`. The approved three-officer [`I-10B gameplay proposal`](docs/research/I10B_iconic_officers_gameplay_proposal.md) is implemented in `a85a34c` and documented in [`docs/implementation/I10B_iconic_officers.md`](docs/implementation/I10B_iconic_officers.md): MUST Fevzi 1850, Mustafa Kemal 1852 and Kâzım Karabekir 1857 use additive one-shot events and generated appearance; I-10B Tiger findings are 0/0/0 and runtime testing is pending. Cemal is **DEFERRED**. Enver is **VANILLA / VotP CONTENT — DO NOT REIMPLEMENT, RETIME OR DUPLICATE**. All custom/external DNA work is moved out of I-10B and its immediate follow-up into [`Phase 5 — Final Visual & Polish / Balance / Compatibility / Release`](docs/MASTER_PRODUCT_PLAN.md#phase-5--final-visual--polish--balance--compatibility--release), after gameplay and flavor scope is complete; external assets require a separate source/permission/license/provenance and Victoria 3 technical-compatibility audit before copying. **R-11 COMPLETE; I-10A AND I-10B IMPLEMENTED; I-10B RUNTIME TEST PENDING; R-14 COMPLETE.**

## Historical Companies

- **R-19 — Ottoman companies/institutions inventory:** canonical dossier [`docs/research/R19_ottoman_companies_institutions_inventory.md`](docs/research/R19_ottoman_companies_institutions_inventory.md). Do not confuse with [`docs/research/R19_tanzimat_gameplay_design.md`](docs/research/R19_tanzimat_gameplay_design.md), which is the I-05 Tanzimat design file under a colliding filename. **COMPLETE AND USED IN I-14.**
- **I-14 — Ottoman company/institution flavor:** proposal [`docs/research/I14_ottoman_company_institution_proposal.md`](docs/research/I14_ottoman_company_institution_proposal.md); implementation [`docs/implementation/I14_ottoman_company_institution_flavor.md`](docs/implementation/I14_ottoman_company_institution_flavor.md). Hayriye company + Ottoman Bank one-shot event. Gameplay `77397d57901284b68dcce37769fa470a7d851a08`; docs `109d43e514a0a1b4e3caf98204588a37c3b0539e`. **IMPLEMENTED; TIGER CLEAN FOR I-14; 1836 VISUAL PASS; 1863 BANK EVENT DEFERRED TO FINAL RELEASE VALIDATION.** Do not expand (no Düyun / Memleket companies).

## Journal Presentation

- **Journal Presentation Pass — research / design only:** [`docs/research/JOURNAL_PRESENTATION_PASS.md`](docs/research/JOURNAL_PRESENTATION_PASS.md). Audited I-01–I-21 implemented content plus R-22 against vanilla 1.13.11 informational JE patterns (`sp_ottoman_balkan_cohesion_guidance`, `sp_egyptian_question`). Current additive custom JE count **4**; REPLACE mod JE count **8**. Recommended **4** new informational umbrella JEs: *Treaty of Hünkâr İskelesi* (I-16), *The Eastern Provinces* (I-21), *The Post-Tanzimat Era* (I-18), *The Armenian Question* (future I-22; 1878+ only). Preserve existing I-05/I-07/I-08/I-12 JEs; no progress bars; no gameplay effect changes. Projected additive total **8**; max simultaneous **~9–11**. **COMPLETE — RESEARCH ONLY; PRESENTATION ARCHITECTURE PROPOSAL-READY; NOT IMPLEMENTED.**
- **Journal Presentation Pass — Phase 1 implementation:** [`docs/implementation/JOURNAL_PRESENTATION_PASS_PHASE1.md`](docs/implementation/JOURNAL_PRESENTATION_PASS_PHASE1.md). Three informational umbrella JEs implemented: `sp_je_hunkar_iskelesi`, `sp_je_eastern_provinces`, `sp_je_post_tanzimat_era`. Additive JE + loc + read-only triggers only; I-16/I-18/I-21 event semantics unchanged. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**
- **Journal Presentation Pass — Phase 2 implementation (I-22):** [`docs/implementation/I22_armenian_question.md`](docs/implementation/I22_armenian_question.md). Fourth informational umbrella JE `sp_je_armenian_question` plus I-22 events/triggers/on_actions. **IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING.**

## Validation & Release

- **I-15 — v1.0 release validation:** [`docs/research/I15_release_validation_matrix.md`](docs/research/I15_release_validation_matrix.md). **PLAYER VISUAL / FIRST-RUNTIME CLOSED 2026-08-25.** Static `6767622`: 16 PASS / 0 FAIL. Tester 1836 visual pass: no visible bug. `sp_balkan_cohesion.1` informational PASS. I-15 fix pass **not required**. Date-gated campaigns remain NOT RUN and are not v1.0 blockers.
- **Phase 5 release-facing polish:** [`docs/implementation/P5_v1_release_polish.md`](docs/implementation/P5_v1_release_polish.md). **COMPLETE 2026-08-25** in loc `b5315e9` and docs/metadata `08c800a`. Player-facing EN/TR text, `1.0.0` / `1.13.*` metadata, README, and changelog. Tiger `fatal 0 / error 1 / warning 10`. Gameplay unchanged. DNA/artwork/Workshop images remain optional. **I-18 IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING** ([`docs/implementation/I18_post_tanzimat_political_development.md`](docs/implementation/I18_post_tanzimat_political_development.md)). **I-21 IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING** ([`docs/implementation/I21_kurdish_provincial_centralization.md`](docs/implementation/I21_kurdish_provincial_centralization.md)). **Journal Presentation Pass Phase 1 IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING** ([`docs/implementation/JOURNAL_PRESENTATION_PASS_PHASE1.md`](docs/implementation/JOURNAL_PRESENTATION_PASS_PHASE1.md)). **I-22 IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING** ([`docs/implementation/I22_armenian_question.md`](docs/implementation/I22_armenian_question.md)). **Journal Presentation Pass Phase 2 (Armenian Question JE) IMPLEMENTED — STATIC VALIDATED / RUNTIME PENDING** via I-22. Canonical next work: I-22 / Phase 1 / I-21 / I-18 / I-16 runtime checklists remain pending; **R-23 research is COMPLETE — PROPOSAL-READY** ([`docs/research/R23_imperial_periphery.md`](docs/research/R23_imperial_periphery.md)); I-23 proposal is not authorized; R-24 remains Future v1.x / not started. Community localization contributor support is **I-17**.

## Alternative History
