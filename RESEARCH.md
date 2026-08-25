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

## Ottoman Debt

## Capitulations

## Government & Centralization

- **R-16 — Ottoman institutional modernization:** [`docs/research/R16_institutional_modernization.md`](docs/research/R16_institutional_modernization.md). 1836–1876 merkezi bürokrasi, maliye/vergi, eğitim, ordu ve altyapı/devlet kapasitesi yalnız doğrulanmış vanilla law/institution/building/technology/JE-event karşılıklarıyla eşleştirildi. **COMPLETE — RESEARCH ONLY; I-05 REQUIREMENTS IDENTIFIED.**

- **R-18 — Provincial power and centralization:** [`docs/research/R18_provincial_power_centralization.md`](docs/research/R18_provincial_power_centralization.md). Ayanlar, vali/merkez ilişkisi, doğrudan vergi denemeleri, 1858 Land Code, 1864 Vilayet Law ve eşitsiz taşra kapasitesi incelendi; map fragmentation, ayan mana ve custom provincial system reddedildi. Belgenin sonunda R-16–R-18 sentezi olarak 10 maddelik I-05 Tanzimat design requirements kaydedildi. **COMPLETE — RESEARCH ONLY; I-05 REQUIREMENTS IDENTIFIED.**

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

## Balkans

- **R-10 — Ottoman Balkan cohesion audit:** [`docs/research/R10_ottoman_balkan_cohesion.md`](docs/research/R10_ottoman_balkan_cohesion.md). Victoria 3 1.13.11 Cultural Fervor → cultural-minority movement → radicalism/obstinance/turmoil → secession chain; 1836 Bulgarian, Serbian, Greek, Albanian, Bosniak, Romanian and Croat setup; `Support Separatism`; laws/institutions; subjects; I-04–I-07 interactions and three vanilla-first player routes were audited. The dossier rejects a custom cohesion bar/mana, permanent stability buff and per-state checklist; it identifies only narrow I-08 guidance/scope candidates. **COMPLETE — RESEARCH ONLY; I-08 CANDIDATES IDENTIFIED; RUNTIME CALIBRATION PENDING.**
- **I-08 — Ottoman Balkan cohesion:** [`docs/research/I08_balkan_cohesion_gameplay_proposal.md`](docs/research/I08_balkan_cohesion_gameplay_proposal.md), [`docs/implementation/I08_balkan_cohesion.md`](docs/implementation/I08_balkan_cohesion.md). One non-progress guidance JE, one effect-free introductory event, Police/Home Affairs clarity, the verified seven-culture GEC-01 activation predicate and GEC-04 movement-gate filter were implemented in `64ca4e9`. Global war, growing-secession convenience triggers and crushed-secession attribution remain deliberately deferred. **IMPLEMENTED — STATIC/TIGER REVIEW COMPLETE; MANUAL RUNTIME TEST PENDING.**

## Kurdish Regions & Tribes

## Arab Provinces

## Migration & Muhacirs

## Settlement Policies

## Great Power Diplomacy

- **R-08 — Great Eastern Crisis reproduction matrix:** [`docs/research/R08_gec_reproduction_matrix.md`](docs/research/R08_gec_reproduction_matrix.md). Victoria 3 1.13.11 vanilla and current-mod script/scope audit completed for GEC-01–08. The approved four-fix minimum slice was implemented as I-04 in `53e870d`; controlled runtime validation, player/AI comparison, and SME exact-0.5 reproduction remain pending/unproduced. **COMPLETE — USED IN I-04; TIGER CLEAN FOR I-04; RUNTIME SMOKE TEST PENDING.**

## Crimean War

## Ottomanism

## Islamism

## Turkism

## Young Ottomans

## First Constitutional Era

## Abdulhamid II

## Young Turks

## Second Constitutional Era

## CUP

## Historical Characters

- **Ottoman Characters & Naming Audit — Victoria 3 1.13.11:** [`docs/audits/ottoman-characters-naming-audit.md`](docs/audits/ottoman-characters-naming-audit.md). Vanilla Turkish name pools, rulers/heirs, starting and generated commanders, and existing mod overlap audited against 19th-century register studies and commander biographies; final proposal retains five day-one commanders by replacing Abdülkerim Nâdir with Dârendeli İzzet Mehmed Paşa. **R-12 COMPLETE; OPENING-COMMANDER SLICE USED BY COMPLETED R-11; IMPLEMENTED AS CANONICAL I-11 IN COMMIT `e456401`; RUNTIME SMOKE TEST PENDING.**
- **R-11 — Character/Commander Dossier:** [`docs/research/R11_character_commander_dossier.md`](docs/research/R11_character_commander_dossier.md). Vanilla 1.13.11 inventory, I-10A roster, exact vanilla trait audit, I-10B event feasibility and duplicate risks are complete. I-10A v1 is fixed at Âlî Paşa, Fuad Paşa, Ahmed Cevdet Paşa and Nâmık Kemal; Ziyâ and Mahmud Nedim are deferred. The approved four-character slice is implemented in `c91e515` and documented in [`docs/implementation/I10A_historical_character_pack.md`](docs/implementation/I10A_historical_character_pack.md); runtime testing remains pending. I-10B is canonically **INTENTIONAL ALTERNATE-HISTORY / GAMEPLAY VISIBILITY / PLAYER APPEAL**, with mandatory emergence targets Fevzi 1850, Mustafa Kemal 1852, Enver 1855 and Karabekir 1857; Cemal is SHOULD for 1853. Shifted fictional adult birth dates and differentiated strong vanilla traits replace the rejected late/conservative design. Enver uniquely has vanilla `dna_pasha_enver`, but its existing VotP agitator/IG behavior makes early reuse **NEEDS SEPARATE TECHNICAL PROPOSAL**. External DNA discovery remains separate implementation prep. **R-11 COMPLETE; I-10A IMPLEMENTED; I-10B TECHNICAL PREP NOT STARTED.**

## Historical Companies

## Alternative History
