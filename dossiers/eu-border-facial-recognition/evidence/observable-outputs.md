# Evidence Layer: Observable Outputs
**Lead:** Code Ethnographer  
**Investigation:** EU Border Facial Recognition — Supply Chain & Procurement  
**Date:** 2026-05-27  
**Confidence level:** Mixed — see per-claim tags below

---

## Documentation Archaeology

### Sources Located in Workspace
- **No primary technical documentation, API references, model cards, or changelogs** for EES/ETIAS/SIS II biometric matching systems were found in the workspace.  
  **Confidence: Documented** — exhaustive search of `raw/`, `wiki/`, `scripts/`, and dossier directories conducted 2026-05-27.
- The workspace contains a single PDF-to-markdown conversion script (`scripts/convert_2_md.py`) using PyMuPDF (`fitz`). This tool represents the substrate's own documentation-archaeology toolchain: it extracts text blocks from PDFs and reassembles them in reading order, but it does not parse structured data, tables, or redacted regions. Its limitations mirror our own: it can surface text, but not the logic embedded in procurement annexes or technical specifications locked in scanned PDFs.  
  **Confidence: Documented** — file present in workspace, dated 2026-05-26 per filesystem.
- Entity files in `evidence/entities/` document corporate actors (Accenture, eu-LISA, Frontex, IDEMIA, NEC, Sopra Steria, Thales) but contain **no technical specifications, API schemas, interface definitions, or code repositories**.  
  **Confidence: Documented** — files read 2026-05-27.

### Sources Located in Public Domain (Referenced but Not Present in Workspace)
- **eu-LISA Annual Activity Reports (2013–2024):** Describe central system architecture at a high level (CIR, BMS, NUI) but omit algorithmic specifications, data schemas, interface designs, and vendor-specific configurations.  
  **Confidence: Documented** — reports published on eu-LISA website; accessed via public domain knowledge. **Temporal referent: 2013–2024.**
- **EU Regulations:** Regulation (EU) 2017/2226 (EES) and Regulation (EU) 2018/1240 (ETIAS) mandate biometric collection but delegate technical implementation to implementing acts and eu-LISA procurement. The regulations specify *what* data is collected and *for how long*; they do not specify *how* matching occurs or *which algorithms* are used.  
  **Confidence: Documented** — EU Official Journal. **Temporal referent: 2017–2018.**
- **NIST Face Recognition Vendor Test (FRVT) Reports:** Provide independent benchmarking of NEC, IDEMIA, and Thales algorithms under controlled conditions. These do not reflect deployed EU border configurations (lighting, camera hardware, enrollment quality, demographic distribution), but they establish baseline performance differentials.  
  **Confidence: Documented** — NIST publications, ongoing series. **Temporal referent: 2019–2024.**
- **Vendor White Papers and Marketing Materials (Thales/Gemalto, IDEMIA, NEC):** Describe claimed capabilities in border management, eGates, and biometric matching. These are sales documents, not technical specifications.  
  **Confidence: Documented** — corporate publications. **Temporal referent: 2019–2024.**

### Critical Absence
- **[GAP — No API documentation for eu-LISA Biometric Matching Service (BMS) available in public domain or workspace.]**
- **[GAP — No model cards, algorithmic impact assessments, or datasheets for the facial recognition models deployed at EU borders.]**
- **[GAP — No changelogs, version histories, or software bills of materials (SBOMs) for biometric algorithm updates disclosed by eu-LISA or vendors.]**
- **[GAP — No interface screenshots, UX flows, or interaction design specifications for border guard BMS dashboards released.]**
- **[GAP — No source code, configuration files, or deployment manifests for border eGate or kiosk software available in public domain.]**

---

## Technical Reconstruction

### System Architecture (Inferred from Public Sources)

Based on eu-LISA annual reports, EU regulations, vendor disclosures, and comparable large-scale biometric systems, the EES/ETIAS/SIS II biometric architecture follows a **three-tier pattern**:

#### Tier 1: Enrollment / Capture (Border Crossing Point)
- **Hardware:** eGates, self-service kiosks, manual capture stations (cameras, fingerprint scanners, document readers).
- **Vendors:** Thales (eGate hardware and document readers, via Gemalto acquisition); IDEMIA (enrollment devices and live capture software).
- **Function:** Facial image and fingerprint capture; automated quality check (ISO/IEC 19795-1 compliant); immediate local storage at border crossing point; transmission to national system.
- **Confidence: Corroborated** — vendor marketing materials, EU procurement summaries, and Member State border authority disclosures align on vendor roles. **Temporal referent: EES enrollment infrastructure procurement ~2019–2023; operational deployment delayed to 2024–2025.**

#### Tier 2: Transmission / Middleware (National ↔ Central)
- **National Uniform Interface (NUI):** Standardized middleware connecting Member State border systems to eu-LISA central infrastructure.
- **Secure network:** sTESTA or successor (EU secure trans-European services for telematics infrastructure).
- **Function:** Encrypted transmission of biometric templates (ISO/IEC 19794-5 for face, 19794-2 for fingerprints) and transactional biographic data.
- **Confidence: Documented** — eu-LISA annual reports describe NUI and network architecture. **Temporal referent: NUI specifications updated for EES under eu-LISA 2019–2022 framework contracts.**

#### Tier 3: Central Matching / Decision (eu-LISA Data Centers)
- **Central Identity Repository (CIR):** Stores biometric templates and biographic data for EES and ETIAS.
- **Biometric Matching System (BMS):** Performs 1:N facial recognition identification and 1:N fingerprint matching against CIR; also supports 1:1 verification for eGates.
- **Automated Fingerprint Identification System (AFIS) and Facial Recognition System (FRS):** Discrete subcomponents within BMS.
- **Data centers:** Primary in Strasbourg area (France); backup in St. Johann im Pongau (Austria). Facility operators undisclosed.
- **Confidence: Documented** — eu-LISA annual reports and EU regulations describe these components. **Temporal referent: EES central infrastructure contract awarded ~2021; operational readiness declared 2024.**

### Algorithmic Stack (Inferred)

The specific algorithmic vendors for the EES central BMS are **not publicly confirmed**, but supply-chain logic and procurement patterns allow inference:

| Component | Probable Vendor(s) | Rationale | Confidence |
|-----------|-------------------|-----------|------------|
| Fingerprint matching (AFIS) | IDEMIA | Legacy supplier to VIS and SIS II; dominant in EU police AFIS markets | Inferred |
| Facial recognition (FRS) | NEC and/or IDEMIA | Top NIST FRVT performers; established EU Member State contracts | Inferred |
| Middleware / integration | Sopra Steria | Long-standing eu-LISA prime contractor for VIS/SIS integration | Inferred |
| Architecture consulting | Accenture | Documented role in large-scale EU IT architecture programs | Inferred |
| Document verification | Thales/Gemalto | Dominant in ePassport and secure document markets | Corroborated |

**Critical caveat:** The actual BMS may use a **multi-vendor fusion approach** (combining scores from multiple algorithms) or a **single-vendor lock-in**. Neither scenario is confirmed.  
**Temporal referent: Algorithm selection likely finalized 2020–2022 during central infrastructure procurement; model versions unknown.**

---

## Interface Deconstruction

### Traveler-Facing Interface (eGates / Self-Service Kiosks)

**What is shown:**
- Multilingual instructions for document insertion and facial positioning.
- Progress indicators ("Please wait," "Look at the camera," "Remove glasses").
- Error messages for capture failure (e.g., poor lighting, face not detected).
- **Confidence: Documented** — vendor marketing materials, airport operator guides, traveler footage. **Temporal referent: 2019–present.**

**What is hidden:**
- The **mandatory nature** of facial recognition for non-EU travelers; no opt-out mechanism is presented at the interface level.
- The **retention period** (3 years for standard EES records; 5 years for over-stayers and denied entries).
- The **jurisdictions where data is processed**: central matching occurs in France and Austria, but travelers are not informed of specific data center locations or facility operators.
- The **corporate vendors** operating the capture hardware, algorithms, and integration layers.
- The **existence of a central repository** (CIR) and the fact that the captured biometric will be stored at EU level, not just at the border.
- **Confidence: Documented** — EES Regulation mandates collection; privacy notices are high-level and posted at a distance from the capture moment. Comparative analysis with comparable systems (US Global Entry, UK eGates) confirms this pattern. **Temporal referent: Ongoing since 2024 operational launch.**

**Interface as political choice:** The traveler interface is designed for **compliance velocity**, not informed consent. The absence of vendor attribution is not a privacy protection; it is a **liability shield** that prevents travelers from associating a specific corporate actor with a specific biometric extraction.

### Border Guard Interface (BMS Dashboard)

**What is shown:**
- **Hit / No-Hit** result from central matching (1:N against CIR or 1:1 against ePassport chip).
- Biographic data overlay: name, date of birth, nationality, document number, visa validity.
- Alert flags: SIS II hit, overstay alert, refusal of entry record, ETIAS authorization status.
- **Confidence: Inferred** — based on eu-LISA system descriptions, comparable border control systems (US OBIM, UK Border Force), and vendor white papers. No primary source confirms exact EU dashboard design. **Temporal referent: Inferred from 2017–2024 system descriptions.**

**What is hidden:**
- **Matching confidence scores / similarity metrics**: The threshold for a "hit" is not displayed. The border guard sees a binary result without knowing the algorithm's certainty.
- **Alternative match candidates**: In a 1:N identification, the top-5 or top-10 candidate list is typically shown in police AFIS interfaces, but it is unclear whether border guards see ranked alternatives or only the top hit.
- **Demographic performance differentials**: The interface does not warn the border guard if the algorithm is known to have elevated false match rates for the traveler's apparent demographic group.
- **Vendor attribution**: The border guard does not know which algorithm (NEC, IDEMIA, Thales) generated the hit, making it impossible to trace errors to specific vendor updates.
- **Override audit trails**: While overrides are logged at the system level, it is unclear whether the guard's decision to accept or reject a hit is linked to their individual identity in real-time on the interface.
- **Confidence: Inferred** — based on standard EU procurement specifications for law enforcement decision-support systems and the absence of any public requirement for score transparency in EES implementing acts. **Temporal referent: Ongoing system design 2017–present.**

**Interface as political choice:** The border guard interface embodies **algorithmic accountability laundering**. By hiding confidence scores and vendor identity, the system transfers liability from the algorithm vendor to the border guard (who makes the "final" decision) while simultaneously denying the guard the information needed to make an informed override.

### eu-LISA Operator Interface (Central System Monitoring)

**What is shown:**
- System uptime, transaction throughput, Member State connection status.
- Technical error logs and infrastructure alerts.
- **Confidence: Inferred** — standard enterprise monitoring for large-scale government IT (Splunk, ELK, or proprietary equivalents). **Temporal referent: Ongoing.**

**What is hidden:**
- **Algorithmic accuracy metrics over time**: Drift in false accept/false reject rates as models age or as hardware degrades.
- **False accept / false reject rates by Member State, border crossing point, or demographic group**.
- **Subcontractor access logs**: Which vendor engineers (IDEMIA, NEC, Sopra Steria, Accenture) have remote or physical access to the BMS, and from which IP addresses or locations.
- **Model update histories**: When was the facial recognition model last retrained, replaced, or fine-tuned? What changed?
- **Training data provenance**: What datasets were used to train or validate the deployed model?
- **Confidence: Inferred** — based on standard enterprise monitoring limitations and the complete absence of public algorithmic audit reports for eu-LISA systems. **Temporal referent: Ongoing.**

---

## Output Pattern Analysis

### Decision Types
1. **Identity Verification (1:1):** Traveler at eGate — facial image compared to ePassport chip photo. Output: gate open / gate closed / manual referral.
2. **Identity Identification (1:N):** Central matching against CIR to detect identity fraud, multiple identities, or visa overstays. Output: hit (identity found) / no-hit / ambiguous (manual review).
3. **Risk Flagging:** SIS II alerts (missing persons, stolen documents, security threats) triggered by biographic or biometric match. Output: alert level + recommended action.
4. **Overstay Calculation:** EES entry/exit timestamp comparison. Output: compliant / overstay detected / entry without exit record.
- **Confidence: Documented** — described in EU regulations and eu-LISA system documentation. **Temporal referent: Legal framework 2017; operational outputs since 2024.**

### Error Patterns (Documented in Independent Sources)
- **Demographic differentials:** NIST FRVT 2019 and subsequent reports document elevated false match rates for African and Asian populations across most commercial facial recognition algorithms, including NEC and IDEMIA.  
  **Confidence: Documented** — NIST FRVT 2019, 2020, 2021, 2022, 2023. **Temporal referent: Findings stable since 2019; vendor improvements incremental.**
- **Age-related error:** Higher false non-match rates for very young children and elderly individuals.  
  **Confidence: Documented** — NIST FRVT and peer-reviewed literature. **Temporal referent: Ongoing.**
- **Presentation attack (spoofing):** Vulnerability to photographs, masks, replay attacks, and deepfakes. Liveness detection effectiveness varies by vendor and is not publicly audited for eu-LISA deployments.  
  **Confidence: Documented** for general liveness detection limitations; **Gap** for eu-LISA-specific testing.
- **Cross-domain degradation:** Algorithms trained on high-quality enrollment images (passport photos) may perform poorly on capture conditions at land or sea borders (lighting, angle, motion blur).  
  **Confidence: Inferred** — based on NIST FRVT cross-domain testing and border infrastructure descriptions.

### Aggregate Outputs
- eu-LISA annual reports state that VIS and SIS process millions of transactions, but **no public data exists** on:
  - Biometric matching accuracy rates for live EES/ETIAS/SIS operations.
  - Breakdown of hits by nationality, age, gender, or phenotype.
  - Rates of human override (guard accepts/rejects algorithmic recommendation).
  - Rates of technical failure (capture failure, transmission timeout, matching system unavailability).
- **Confidence: Documented** — eu-LISA annual reports publish transaction volumes but omit accuracy and demographic metrics. **Temporal referent: Annual reports 2013–2024.**

---

## Supply Chain Logic Map

The following reconstructs how **technical decisions flow through vendors** based on entity files and public procurement patterns. This is a **logic map**, not a confirmed organizational chart:

```
[eu-LISA]
   │
   ├──procures (framework contract)──► [Sopra Steria]
   │                                      │
   │                                      ├──integrates──► [IDEMIA] (fingerprint + face algorithms)
   │                                      │
   │                                      ├──integrates──► [NEC] (face algorithms)
   │                                      │
   │                                      └──subcontracts──► [Accenture] (enterprise architecture)
   │
   └──procures (hardware/framework)──► [Thales S.A. / Thales DIS]
                                          │
                                          ├──supplies──► eGates + document readers (border crossing)
                                          │
                                          └──supplies──► secure document verification toolkit
```

**What this map obscures:**
- **Tier-2 and Tier-3 subcontractors**: Whether NEC licenses neural network components from smaller AI firms; whether Thales subcontracts camera module manufacturing; whether Sopra Steria offloads development to delivery centers in India, Tunisia, or Poland.
- **Cloud/facility operators**: Even though eu-LISA claims EU-only hosting, the operators of the Strasbourg and St. Johann data centers are unnamed, as are their subcontractors (power, cooling, physical security).
- **Maintenance access topology**: Which vendor engineers have remote desktop or SSH access to the BMS; whether such access is routed through vendor HQ (Japan for NEC, USA for Accenture, France for IDEMIA/Thales/Sopra Steria).
- **IP licensing chains**: Whether IDEMIA licenses facial recognition patents from other holders; whether Thales/Gemalto cross-licenses with IDEMIA.

**Confidence: Inferred** — based on entity files and standard EU procurement consortium patterns. **Temporal referent: Contract structures stable since ~2021 EES central infrastructure award.**

---

## Version Tracking

| Date | Event | Significance | Confidence |
|------|-------|------------|------------|
| 2016 | EES legal basis proposed | Mandated facial recognition at external borders | Documented |
| 2017 | Regulation (EU) 2017/2226 adopted | Legal framework finalized; 3-year retention for EES data | Documented |
| 2019 | Thales acquires Gemalto (€4.8bn) | Consolidation of secure document and biometric markets | Documented |
| 2020 | eu-LISA EES central infrastructure tender published | Beginning of major procurement for BMS + CIR | Documented |
| 2021 | EES central infrastructure contract award | System integration phase begins; vendors selected | Documented |
| 2022–2023 | Repeated EES deployment delays | Technical integration failures; vendor coordination issues; Member State readiness gaps | Corroborated — EU Ombudsman, European Court of Auditors, press reporting |
| 2024 | EES "phased" operational launch | Partial deployment; not all Member States connected; biometric matching reportedly active at select airports | Corroborated — eu-LISA statements, Member State border authority announcements |
| 2024–present | Ongoing algorithm updates and patches | **No public disclosure of update cycles, changelogs, or model versions** | Gap |

---

## Gaps

- **[GAP — No API documentation, SDK references, or integration specifications for eu-LISA BMS available in public domain or workspace.]**
- **[GAP — No model cards, algorithmic impact assessments, or datasheets for deployed facial recognition systems published by eu-LISA or vendors.]**
- **[GAP — No changelogs, SBOMs, or version histories for biometric algorithm updates disclosed.]**
- **[GAP — No interface screenshots, UX flows, or interaction design specifications for border guard BMS dashboards publicly available.]**
- **[GAP — No source code, configuration files, or deployment manifests for border eGate or kiosk software available.]**
- **[GAP — Exact algorithm vendor mix and model versions for EES central BMS not confirmed.]**
- **[GAP — Biometric accuracy metrics (FAR/FRR) for live EES operations not published.]**
- **[GAP — Override rates and human-in-the-loop decision patterns not disclosed.]**
- **[GAP — Subcontractor access logs, remote maintenance protocols, and vendor engineer access rights not disclosed.]**
- **[GAP — Training data provenance, geographic origin, and demographic composition for deployed facial recognition models not disclosed.]**
- **[GAP — Model update history, retraining schedules, and drift monitoring results not disclosed.]**
- **[GAP — Interface usability studies, guard training materials, and error-handling protocols not publicly available.]**

---

## Interface as Governance Mechanism

The design choices in EU border biometric interfaces constitute a form of **governance by default** — political decisions sedimented into interaction patterns:

1. **Mandatory capture without vendor disclosure** removes traveler agency to contest specific algorithmic vendors or request human alternatives. The interface presents the biometric gate as a natural feature of the border, not as a contested technical system built by specific corporations.

2. **Hidden confidence scores** transfer liability from the algorithm vendor to the border guard. The guard is positioned as the decision-maker, but the interface denies them the information (matching score, demographic performance warning, alternative candidates) required to make an informed override. This is **accountability laundering**.

3. **Opaque override trails** prevent retrospective accountability. If a guard overrides a false hit or misses a true hit, the interface design makes it difficult to determine whether the error was algorithmic, human, or systemic.

4. **Centralized monitoring without public accuracy metrics** creates an **epistemic monopoly**. Only eu-LISA and vendors know how well the system performs, while travelers, guards, oversight bodies, and affected communities are denied the data needed to challenge outcomes.

5. **The absence of an "algorithmic receipt"** — a record given to the traveler showing what was captured, by which vendor's system, and where it was sent — is not an oversight. It is an architectural choice that prevents **supply chain traceability** from the point of data extraction.

**Confidence: Inferred** — based on interface analysis principles, comparable system studies (Eubanks 2018; Browne 2015; Pasquale 2015), and the documented absence of transparency requirements in EES/ETIAS implementing acts. **Temporal referent: Ongoing system design 2017–present.**
