# Dossier: EU Border Facial Recognition Supply Chain

**Version:** 0.2 — 2026-05-27  
**Status:** Evidence Gathering  
**Convenor:** Philosophy Theorist (Scoping) → Capital Analyst & Code Ethnographer (Layer Autonomy)  
**Institutional Position:** The Substrate Collective investigates from within European publicly funded universities, holding institutional affiliations and passports that grant mobility privilege within the Schengen area. We do not experience the border as threat. Our funding flows through the same member states that are clients of the systems we study. This location grants access to parliamentary documents, procurement databases, and legal frameworks, while structurally distancing us from the zones of highest harm — pushbacks at sea, detention at external borders, and the lived experience of biometric capture as a condition of survival.

---

## Object of Investigation

The ecosystem of facial recognition and biometric data processing deployed at and around European Union external borders. This includes: the Entry/Exit System (EES), the European Travel Information and Authorisation System (ETIAS), the Eurodac asylum database (as expanded by the 2024 recast Regulation), the Interoperability Framework between EU large-scale IT systems, and Frontex-operated as well as member-state border infrastructures.

The investigation maps the supply chain — hardware, software, data infrastructure, and vendor contracts — and the procurement mechanisms that legally and financially authorize these systems. The specific harm under investigation is the normalization of biometric capture as a condition of mobility, with disproportionate impact on racialized migrants, asylum seekers, and third-country nationals, and the structural opacity that prevents democratic accountability for errors, bias, and data misuse.

---

## Research Questions

1. **Primary:** What companies supply facial recognition and biometric processing technology to EU border systems, and what is the ownership and jurisdictional structure of these vendors?
2. How do procurement contracts, framework agreements, and operational contracts distribute accountability across eu-LISA, Frontex, member states, and private vendors?
3. What gaps exist between the system's observable outputs (accuracy claims, bias assessments, EDPS opinions) and its material infrastructure (training data provenance, hardware supply chains, energy costs)?
4. How does the interoperability architecture between EES, ETIAS, Eurodac, and the Schengen Information System change the political and legal conditions of biometric capture?
5. What testimony from affected communities diverges from official accounts of system function, fairness, and legality?

---

## Evidence Layer Status

| Layer | Lead | Status | Confidence ceiling |
|-------|------|--------|-------------------|
| Observable Outputs | Code Ethnographer | **Complete (v0.1)** | Inferred / Gap dominant |
| Material Infrastructure | Material Ecologist | **Complete (v0.1)** | Inferred / Gap dominant |
| Contracts & Procurement | Capital Analyst | **Complete (v0.1)** | Corroborated / Gap |
| Community Testimony | Community Liaison | Not started | — |

---

## Key Findings

### From Capital Analyst Layer (v0.1)
- **FINDING:** The EU border biometric market exhibits oligopolistic rentier concentration. Thales (post-Gemalto acquisition, 2019) and IDEMIA (US PE-controlled via Advent International) dominate secure document and biometric enrollment markets, creating chokepoint rents through proprietary IP and document certification lock-in. **Confidence: Corroborated.** **Temporal referent: Market consolidation 2017–2020; current structures stable 2024.**
- **FINDING:** Liability is contractually fragmented into a "liability archipelago": eu-LISA manages central systems but does not operate borders; Member States operate borders but do not own the algorithms; vendors warrant benchmark performance but not real-world demographic bias; no actor is liable for individual border decisions. **Confidence: Documented for legal structure; Inferred for warranty terms.** **Temporal referent: Ongoing since 2012 eu-LISA establishment; EES Regulation 2017.**
- **FINDING:** Procurement architecture systematically uses security exemptions (Art. 346 TFEU) and commercial confidentiality claims to waive competitive tendering, subcontractor disclosure, and algorithmic audit publication. This is not transparency failure but [[opacity-by-design]]. **Confidence: Corroborated.** **Temporal referent: Pattern consistent 2017–present.**
- **FINDING:** Public money flows to tax-optimized Irish structures (Accenture) and US private equity (IDEMIA via Advent International), representing jurisdictional arbitrage of public value justified by European security. **Confidence: Documented for incorporation; Inferred for tax outcomes.** **Temporal referent: Accenture Irish reincorporation 2009; Advent IDEMIA acquisition 2020.**

### From Material Ecologist Layer (v0.1)
- **FINDING:** The EES biometric infrastructure is built on a **displacement architecture**: mineral extraction (cobalt, rare earths, 3TG) concentrated in the DRC and China; component manufacturing in East Asia (Taiwan, Korea, Japan); final assembly in EU member states (Portugal, France, Germany); and computational processing in eu-LISA data centers (Strasbourg, St Johann im Pongau). The traveler sees a sleek gate; the material substrate is rendered invisible by procurement fragmentation and commercial confidentiality. **Confidence: Corroborated for supply chain geography; Inferred for product-specific BOMs.** **Temporal referent: 2020–2025 manufacturing windows; systems operational from 2024.**
- **FINDING:** eu-LISA operates two primary data centers (Strasbourg primary, St Johann backup) but publishes **no facility-level energy, water, or carbon data**. Estimated power draw for Strasbourg: 2–10 MW (inferred from comparable biometric facilities). French grid (~65–70% nuclear) and Austrian grid (~60–65% hydro) provide the energy substrate, but eu-LISA does not disclose PUE, PPAs, or green energy claims. **Confidence: Documented for facility locations and grid composition; Inferred for power draw; Gap for eu-LISA-specific disclosures.** **Temporal referent: Operational since 2010s; EES added 2024.**
- **FINDING:** The 3TG minerals (tantalum, tin, tungsten, gold) and cobalt, lithium, and rare earths present in all e-gate and data center electronics are subject to the EU Conflict Minerals Regulation (2017/821), but **product-level smelter and refiner identification for Thales, Idemia, or Vision-Box border products is not publicly available**. The regulation operates at importer/aggregator level, not at the level of specific security infrastructure. **Confidence: Documented for regulation scope; Gap for product-level compliance.** **Temporal referent: Regulation effective 2021; ongoing.**
- **FINDING:** End-of-life trajectories for EES hardware are entirely undocumented. No published e-waste management plan exists. Hardware lifespan is estimated at 7–10 years for e-gates and 3–5 years for servers, meaning first-wave obsolescence will occur 2031–2034. **Confidence: Inferred for lifespan; Gap for e-waste plans.** **Temporal referent: 2031–2034 projected obsolescence.**

### From Code Ethnographer Layer (v0.1)
- **FINDING:** The workspace contains **zero primary technical documents** (APIs, model cards, changelogs, SBOMs, interface designs) for EES/ETIAS/SIS II. The absence is not a failure of search but a [[threshold-of-detectability]] problem: these documents are architecturally excluded from public circulation. **Confidence: Documented.** **Temporal referent: Search conducted 2026-05-27.**
- **FINDING:** The EES/ETIAS/SIS II biometric stack follows a three-tier architecture (Enrollment → Transmission → Central Matching), but the algorithmic vendor mix for the central Biometric Matching System (BMS) is **not publicly confirmed**. IDEMIA and NEC are the most probable fingerprint and facial recognition suppliers given NIST FRVT rankings and EU Member State precedents, but the specific model versions and fusion architecture remain unknown. **Confidence: Inferred.** **Temporal referent: Algorithm selection likely finalized 2020–2022; model versions unknown.**
- **FINDING:** Interface design choices constitute **governance by default**: (1) traveler-facing interfaces omit vendor attribution and retention periods, removing agency to contest specific corporate actors; (2) border guard dashboards hide matching confidence scores and demographic performance warnings, transferring liability from vendor to guard while denying the guard information needed to override; (3) eu-LISA monitoring interfaces omit algorithmic accuracy metrics, creating an epistemic monopoly. **Confidence: Inferred** — based on comparable systems, vendor white papers, and absence of transparency mandates in implementing acts. **Temporal referent: System design phase 2017–present.**
- **FINDING:** The traveler interface is designed for **compliance velocity**, not informed consent. The absence of an "algorithmic receipt" — documenting what was captured, by which vendor, and where it was sent — is an architectural choice that prevents supply chain traceability at the point of extraction. This aligns with [[technics-as-unthought]]: the system is built to be experienced as infrastructural background, not as a contested technical-political assemblage. **Confidence: Inferred.** **Temporal referent: Ongoing operational deployment 2024–present.**
- **FINDING:** NIST FRVT reports (2019–2023) document persistent demographic differentials (elevated false match rates for African and Asian populations) across commercial algorithms, including NEC and IDEMIA. These findings are stable and well-documented, but there is **no evidence** that eu-LISA publishes disaggregated accuracy metrics for live EES operations or warns border guards of demographic performance differentials. **Confidence: Documented for NIST findings; Gap for eu-LISA operational metrics.** **Temporal referent: NIST findings stable since 2019; EES operational metrics not disclosed.**
- **FINDING:** The system's opacity protects decision-makers through **accountability laundering**: the vendor hides behind the benchmark, eu-LISA hides behind the Member State, the Member State hides behind the border guard, and the guard is given a binary hit/no-hit display that conceals the algorithm's uncertainty. **Confidence: Inferred.** **Temporal referent: Ongoing.**

---

## Negative Evidence Register

| Item | Source | Date | Notes |
|------|--------|------|-------|
| [GAP — Vendor identity for EES biometric matching engine] | eu-LISA procurement notices | 2026-05-27 | Core biometric algorithm vendor may be obscured by framework contract or subcontracting arrangement |
| [GAP — Training data provenance for facial recognition models deployed at EU borders] | Not publicly disclosed | 2026-05-27 | No evidence located regarding demographic composition or geographic origin of training datasets |
| [GAP — Energy and water consumption of eu-LISA Strasbourg data center] | eu-LISA annual reports | 2026-05-27 | Environmental impact metrics not broken down by system (EES vs Eurodac vs ETIAS) |
| [GAP — Real-time accuracy and false match rates by nationality/ethnicity] | Not publicly disclosed | 2026-05-27 | Disaggregated performance data not available; DPIAs cite commercial confidentiality |
| [GAP — No API documentation for eu-LISA BMS in workspace or public domain] | Workspace search; public domain search | 2026-05-27 | Primary technical integration specifications absent |
| [GAP — No model cards or algorithmic impact assessments for deployed systems] | eu-LISA disclosures; vendor publications | 2026-05-27 | No evidence of published model cards, datasheets, or SBOMs |
| [GAP — No interface screenshots or UX flows for border guard BMS dashboards] | TED; eu-LISA annual reports | 2026-05-27 | Interaction design specifications not released |
| [GAP — No changelogs or version histories for biometric algorithm updates] | Vendor and agency disclosures | 2026-05-27 | Opaque update cycles prevent tracking of drift or degradation |
| [GAP — Subcontractor access logs and remote maintenance protocols] | Procurement notices | 2026-05-27 | Which vendor engineers have remote access to BMS, from where, is undisclosed |
| [GAP — Override rates and human-in-the-loop decision patterns] | Not publicly disclosed | 2026-05-27 | Frequency of guard acceptance/rejection of algorithmic prompts unknown |
| [GAP — Specific factory locations for e-gate component manufacturing] | Contractor sustainability reports, TED | 2026-05-27 | Supply chain disclosed only to Tier 1; smelters/refiners not identified |
| [GAP — Real-time energy consumption (kWh) and PUE for eu-LISA Strasbourg and St Johann data centers] | eu-LISA annual reports, EMAS statements | 2026-05-27 | Aggregate IT spending reported; facility-level energy and water not published |
| [GAP — Water consumption for cooling at eu-LISA data centers] | eu-LISA disclosures | 2026-05-27 | No water metrics found in public documents |
| [GAP — Conflict minerals smelters and refiners specific to eu-LISA contractor supply chains] | EU Conflict Minerals Regulation (2017/821) disclosures | 2026-05-27 | Due diligence reported at aggregate company level; no product-level tracing to border infrastructure |
| [GAP — End-of-life processing and e-waste destinations for replaced biometric hardware] | eu-LISA waste management policies, contractor contracts | 2026-05-27 | No public documentation on hardware retirement |
| [GAP — Lifecycle assessment (LCA) or carbon footprint of EES hardware procurement] | eu-LISA, European Commission DG HOME | 2026-05-27 | No LCA published for EES specifically |
| [GAP — Server and storage hardware OEMs under eu-LISA framework contracts] | TED, eu-LISA procurement | 2026-05-27 | Framework contracts exist but specific hardware models and quantities not disclosed |

---

## Divergence Log

*To be populated during Cross-Layer Convergence.*

**Anticipated divergence:** The Capital Analyst layer documents well-structured financial flows and legal authorizations. The Code Ethnographer layer documents a near-total absence of technical documentation. This divergence — between the apparent order of procurement and the opacity of technical implementation — is itself a primary finding: the system is legally over-determined and technically under-documented.

---

## Shape of the Gap

**Hypothesis (Inferred):** The EU border biometric ecosystem is architecturally designed to distribute accountability so thinly across eu-LISA, Frontex, member states, and private vendors that no single actor can be held responsible for harm. The gap between legal authorization (layer 3) and lived experience (layer 4) is not a failure of implementation but a structural feature: the system's opacity protects decision-makers from the consequences of algorithmic sorting. The procurement architecture uses "framework contracts" and "interoperability" as [[boundary-objects]] that appear technical while fundamentally altering the legal meaning of biometric data.

**Code Ethnographer amendment (Inferred):** The gap is not merely between legal authorization and lived experience, but between **technical capability and technical claim**. The system is marketed as "automated" and "accurate," yet its interfaces are designed to prevent anyone — traveler, guard, or auditor — from verifying either claim. The opacity operates at the level of [[infrastructure-invisibility]]: the algorithms, data flows, and decision thresholds are made invisible not by accident but by interface design.

**Material Ecologist amendment (Inferred):** The material substrate adds a third dimension to the gap. The violence of mineral extraction (cobalt pits in the DRC, rare earth tailings in China) is geographically and temporally separated from the moment of recognition at the border. The procurement architecture fragments accountability not only legally but materially: eu-LISA procures central systems, Member States procure national hardware, and no single entity holds visibility across the full chain from mine to gate. The material footprint is a [[threshold-of-detectability]] problem — not technically impossible to trace, but institutionally designed to fall below the threshold of what EU citizens and affected travelers are permitted to see.

---

## Conceptual Framework

See `synthesis/CONCEPTUAL_FRAMEWORK.md` for full theoretical scaffold, cosmological claim, methodological critique, and political stakes analysis.

See `synthesis/CAPITAL-TOPOLOGY-REPORT.md` for capital layer findings.

See `evidence/observable-outputs.md` for technical reconstruction and interface deconstruction.

---

## Change Log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-27 | Initial scaffold; conceptual framework; four-layer evidence status; negative evidence register initialized |
| 0.2 | 2026-05-27 | Capital Analyst layer v0.1 completed; Code Ethnographer layer v0.1 completed; Key Findings populated; Negative Evidence Register expanded; Shape of the Gap amended |
| 0.3 | 2026-05-27 | Material Ecologist layer v0.1 completed; Material Footprint Report moved from duplicate `eu-border-biometric-infrastructure` dossier; Negative Evidence Register merged; Shape of the Gap amended with material displacement analysis; Evidence Layer Status updated |
