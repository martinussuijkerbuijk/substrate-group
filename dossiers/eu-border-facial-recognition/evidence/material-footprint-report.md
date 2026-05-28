# Material Footprint Report: EU Border Biometric Infrastructure

**Agent:** Material Ecologist  
**Date:** 2026-05-27  
**Scope:** Hardware supply chains, facility locations, energy/water consumption, and end-of-life trajectories for facial recognition systems deployed at EU Schengen external borders under the Entry/Exit System (EES) and related large-scale IT systems (SIS II, VIS).  
**Confidence ceiling:** Inferred. Facility-level energy data and component-level supply chain disclosures are not publicly available.  
**Temporal coverage:** Systems operational as of 2026-05-27; mineral extraction and manufacturing references cover 2020–2025 production windows.

---

## 1. System Boundary

**Included:**
- Automated border control e-gates and biometric capture kiosks deployed at Schengen external borders (airports, seaports, land crossings) for EES enrollment and verification
- Central data center infrastructure operated by eu-LISA (Strasbourg primary, St Johann im Pongau backup)
- Network infrastructure connecting border points to central systems (fiber, routers, switches)
- Server and storage hardware within eu-LISA facilities hosting biometric matching algorithms and databases

**Excluded (noted as boundary gaps):**
- National backend systems operated by individual Member States (architecture varies by state; outside current scope)
- Traveler mobile devices (not required for EES)
- Training hardware for algorithm development (assumed to be commercial cloud or contractor facilities; no evidence of dedicated eu-LISA training clusters)
- Undersea and terrestrial fiber cables outside EU territory (relevant but too diffuse for this phase)

---

## 2. End-Use Hardware: E-Gates and Biometric Capture Devices

### 2.1 Description

EES requires third-country nationals to provide **four fingerprints** and a **facial image** at each entry and exit. At automated border control points, this is performed by **e-gates** or **self-service biometric kiosks**. These are physically imposing structures: steel enclosures, touchscreen displays, document readers (OCR/MRZ), high-resolution cameras, fingerprint scanners, and integrated PCs with network connectivity.

### 2.2 Known Suppliers

| Supplier | Role | Evidence | Confidence | Temporal |
|----------|------|----------|------------|----------|
| Vision-Box (Portugal) | Automated border control e-gates | Company disclosures; airport procurement records (AMS, LIS, others) | Corroborated | 2015–present |
| Thales (France) | Biometric systems, document readers, e-gates | Press releases; EU procurement for EES/SIS | Corroborated | 2010s–present |
| Idemia (France) | Fingerprint scanners, facial capture, biometric SDKs | Corporate disclosures; eu-LISA biometric matching platform history | Corroborated | 2010s–present |
| secunet Security Networks (Germany) | Automated border control, e-gates | German federal procurement; airport deployments | Corroborated | 2010s–present |
| Sopra Steria (France) | Systems integration for EES central infrastructure | Press releases on EES contract | Corroborated | 2019–present |

**Note on procurement architecture:** eu-LISA manages the **central** EES infrastructure (databases, matching engine). Member States procure their own **national** border infrastructure (e-gates, manual booths) to connect to the central system. [Corroborated, Regulation (EU) 2017/2226 and eu-LISA operational descriptions]. This means there is no single EU-wide e-gate supplier; national procurement fragments the material trail.

### 2.3 Component-Level Material Breakdown (Inferred)

Based on teardowns of comparable automated border control hardware and industry standards for industrial PCs and biometric devices:

| Component | Materials (typical) | Source Region | Confidence |
|-----------|---------------------|---------------|------------|
| Camera module (facial capture) | Silicon (sensor), gallium arsenide (IR emitters for liveness detection), glass, aluminum housing, rare earths (miniaturization/motors) | Sensors: Japan (Sony), Korea (Samsung), USA (ON Semi/OmniVision); assembly: China, Vietnam, Malaysia | Inferred |
| Fingerprint scanner (capacitive/optical) | Silicon (sensor array), glass/plastic (platen), gold (bonding), epoxy | Sensors: France (Idemia), Korea (Suprema), Taiwan; assembly: Asia-Pacific | Inferred |
| Document reader (OCR/MRZ/RFID) | Silicon, glass, aluminum, copper, rare earths (magnetic components) | Germany (DESKO/Access-IS), France (Thales), China | Inferred |
| Industrial PC / motherboard | Silicon (CPU/chipset), copper (traces), gold (connectors), tantalum (capacitors), tin (solder), brominated flame retardants (PCB) | CPUs: USA (Intel/AMD), manufactured Taiwan (TSMC); motherboards: Taiwan, China | Inferred |
| Display (touchscreen) | Indium tin oxide (ITO), silicon, glass, aluminum, liquid crystals | Panels: Korea, China, Taiwan | Inferred |
| Steel/aluminum enclosure | Iron, aluminum, nickel, chromium (stainless steel coatings) | EU member states (Portugal, France, Germany — near assembly) | Inferred |
| Backup battery (UPS inside gate) | Lithium, cobalt, nickel, graphite | Cells: China, Korea, Japan | Inferred |
| Cables and connectors | Copper, PVC/rubber insulation, gold-plated contacts | China, Southeast Asia | Inferred |

**Critical minerals for border infrastructure:** Tantalum, tin, tungsten, and gold (3TG) are present in all electronic assemblies. The EU Conflict Minerals Regulation (2017/821) requires EU importers to conduct due diligence on these minerals if sourced from conflict-affected or high-risk areas. [Documented, Regulation (EU) 2017/821]. However, **specific smelters and refiners in the supply chains of Thales, Idemia, or Vision-Box for border control products are not publicly identified.** [GAP — product-level conflict minerals report, 2026-05-27].

### 2.4 Assembly Locations

| Supplier | Known/Headquarters Assembly | Confidence | Notes |
|----------|----------------------------|------------|-------|
| Vision-Box | Portugal (headquarters and manufacturing in Lisbon area) | Corroborated | Portuguese company with production in-country |
| Thales | France, Netherlands, Poland (EU sites for security/biometric hardware) | Inferred | Thales is a transnational with global manufacturing; specific e-gate assembly site not confirmed |
| Idemia | France (biometric device assembly); global supply chain for components | Inferred | Component sourcing largely Asian; final assembly in EU for EU contracts |
| secunet | Germany | Corroborated | German federal security supplier |

**Displacement analysis:** The final assembly of e-gates occurs primarily in EU member states (Portugal, France, Germany), satisfying EU procurement preferences and "security of supply" requirements. However, the **component-level extraction and manufacturing** is concentrated in East Asia (China, Taiwan, Korea, Japan, Malaysia, Vietnam) and the DRC/African Great Lakes region (for 3TG minerals). [Inferred, based on global electronics supply chain mapping and conflict minerals geography].

---

## 3. Data Center Infrastructure

### 3.1 Facilities

eu-LISA operates two primary data center facilities for large-scale IT systems:

| Facility | Location | Function | Evidence | Confidence | Temporal |
|----------|----------|----------|----------|------------|----------|
| Primary data center | Strasbourg, France | Hosting SIS II, VIS, Eurodac, EES central systems | eu-LISA official descriptions; European Parliament reports | Documented | Operational since SIS II migration (2010s); EES added 2024 |
| Backup/Disaster Recovery | St Johann im Pongau, Austria | Backup for SIS II and other systems; Business continuity | eu-LISA official descriptions; Austrian government statements | Corroborated | Operational since 2010s |

**Additional notes:**
- eu-LISA headquarters is in Tallinn, Estonia, but Tallinn does not host the primary operational data centers for these systems. [Documented]
- The Strasbourg facility is physically located in the same vicinity as other EU institutions (European Parliament, Council of Europe), though exact street addresses are not always published for security reasons. [Corroborated]
- The St Johann im Pongau facility is a former military or secure government site repurposed for eu-LISA backup. [Corroborated, Austrian media]

### 3.2 Hardware Composition (Inferred)

Data center hardware for biometric databases and matching engines typically includes:

| Hardware Class | Typical Specifications | Materials | Confidence |
|----------------|------------------------|-----------|------------|
| Compute servers (biometric matching) | High-core-count CPUs (Intel Xeon / AMD EPYC) or GPU accelerators for AI matching | Silicon (chips), copper (heat sinks, traces), gold (connectors), aluminum (chassis), rare earths (HDD magnets if used) | Inferred |
| Storage (biometric templates, facial images) | All-flash arrays (SSDs) or hybrid storage; petabyte-scale | Silicon (NAND flash), cobalt/copper ( interconnects), aluminum, plastics | Inferred |
| Network | Fibre Channel switches, Ethernet routers, load balancers | Silicon (ASICs), copper, fiber optic (silica glass), gold, plastics | Inferred |
| Cooling | CRAH/CRAC units, chillers, cooling towers | Aluminum, copper (coils), steel, refrigerants (fluorinated gases — potent GHGs) | Inferred |
| Power infrastructure | UPS, diesel generators, switchgear | Lead/acid or lithium batteries, copper, steel, diesel fuel storage | Inferred |

**Specific OEMs under eu-LISA framework contracts:** [GAP — eu-LISA has framework contracts for IT infrastructure (servers, storage, network) but specific vendor names and hardware models for the Strasbourg and St Johann facilities are not published in open procurement, 2026-05-27]. Common EU framework contractors include Dell Technologies, Hewlett Packard Enterprise (HPE), Cisco, and Lenovo, but this is extrapolated from general EU IT procurement, not eu-LISA-specific disclosure.

### 3.3 Energy and Water Accounting

**Energy consumption:**
- eu-LISA operates large-scale databases storing biometric data for hundreds of millions of individuals (SIS: ~100 million alerts; VIS: ~50 million visa holders; EES: projected hundreds of millions of entries/exits annually). The computational load for 1:N biometric matching (facial recognition against watchlists or identity verification) is significant.
- **Estimated power draw for Strasbourg primary site:** 2–10 MW (inferred range based on comparable government biometric data centers and facility size). [Inferred, no published PUE or kWh figures].
- **Grid source:** Strasbourg is connected to the French national grid (RTE), which is dominated by nuclear power (~65–70%) with increasing renewables. [Documented, RTE grid data]. However, **eu-LISA does not publish power purchase agreements (PPAs) or claims of 100% renewable energy for its data centers.** [GAP — no green energy disclosure found, 2026-05-27].
- **St Johann im Pongau grid:** Austrian national grid (APG), with high hydroelectric share (~60–65%). [Documented, APG statistics]. The backup facility likely consumes minimal energy under normal operations (cold or warm standby) but requires full power capability during failover.

**Water consumption:**
- Data center cooling in continental European climates can use air-side economizers (free cooling) for significant portions of the year, reducing water use compared to evaporative cooling in hot climates.
- **Specific water withdrawal/consumption for eu-LISA Strasbourg or St Johann:** [GAP — no figures published, 2026-05-27].
- **Wastewater and thermal discharge:** [GAP — no environmental permit details accessible, 2026-05-27].

**Carbon emissions:**
- No published carbon footprint for eu-LISA operations. [GAP — eu-LISA annual reports do not include GHG inventory for data centers, 2026-05-27].
- Inferred annual emissions (Strasbourg, 5 MW average, French grid intensity ~50–80 gCO2/kWh due to nuclear dominance): ~2,200–3,500 tCO2/year for IT load alone, excluding embodied carbon of hardware. [Inferred, significant uncertainty in load factor and PUE].

---

## 4. Network Infrastructure

### 4.1 Description
Border checkpoints connect to eu-LISA central systems via national secure networks and the **sTESTA** network (or its successor), the EU's dedicated telecommunications network for justice and home affairs. [Documented, European Commission descriptions]. sTESTA uses encrypted VPNs over commercial fiber infrastructure.

### 4.2 Material Specificity
- **Fiber optic cables:** Silica glass, plastic cladding, copper power conductors, steel armor. Manufactured by companies like Corning, Prysmian, Nexans. [Inferred for this specific network].
- **Routers/switches:** Standard telecom equipment (Cisco, Juniper, Nokia). Contain silicon, copper, gold, rare earths. [Inferred].
- **Latency requirements:** Biometric verification at borders requires near-real-time response (< few seconds), meaning edge caching or distributed processing may occur at national hubs, but the authoritative biometric database resides at eu-LISA central sites. [Corroborated, EES technical specifications].

---

## 5. Supply Chain Archaeology: From Minerals to Border Gates

### 5.1 Critical Mineral Map

The following minerals are implicated in EU border biometric hardware, traced backward from the device:

| Mineral | Primary Use in Hardware | Top Extracting Countries (Global) | Conflict/High-Risk Link | Confidence |
|---------|------------------------|-----------------------------------|------------------------|------------|
| **Cobalt** | Lithium-ion batteries (gate UPS, laptop/server backup), some alloys | DRC (~70%), Indonesia, Russia, Australia | DRC artisanal mining linked to labor abuses, child labor | Documented (global pattern); Inferred (specific to border hardware) |
| **Lithium** | Batteries | Australia, Chile, China, Argentina | Water stress in Chile/Argentina; land dispossession | Documented (global pattern); Inferred (specific) |
| **Tantalum** | Capacitors (all PCBs) | DRC, Rwanda, Brazil, Nigeria | DRC conflict mineral (3TG) | Documented (global); Gap (specific smelters) |
| **Tin** | Solder (all electronics) | China, Indonesia, Myanmar, Peru | Myanmar: military junta control; Indonesia: environmental degradation | Documented (global); Gap (specific) |
| **Tungsten** | Electronic contacts, vibration motors | China, Vietnam, Russia, Bolivia | DRC conflict mineral (3TG) | Documented (global); Gap (specific) |
| **Gold** | Connectors, bonding wire | China, Australia, Russia, Canada | DRC conflict mineral; cyanide use in extraction | Documented (global); Gap (specific) |
| **Rare Earth Elements** (Nd, Dy, Pr) | Hard drive magnets, camera motors, speakers, windings | China (~60%), USA, Myanmar, Australia | Myanmar: military control; China: environmental damage from processing | Documented (global); Inferred (HDD/actuators in servers/gates) |
| **Silicon** | All semiconductors, solar (irrelevant here) | China, Russia, USA, Norway | Energy-intensive purification | Documented |
| **Indium** | ITO for touchscreens/displays | China, Korea, Japan, Canada | Byproduct of zinc mining; limited reserves | Inferred (if capacitive displays used) |
| **Gallium** | LEDs, RF components, power electronics | China (~98% of primary production), Germany, Kazakhstan | Extreme concentration; semiconductor supply chain vulnerability | Inferred |

### 5.2 Labor and Extraction Geography

**Hypothesis (Inferred):** The material substrate of EU border facial recognition is assembled through a labor regime that displaces risk and toxicity:
- **Extraction:** Artisanal cobalt in DRC; rare earth processing in China (Baotou region, Inner Mongolia — documented environmental destruction); tin dredging in Indonesia (documented marine destruction).
- **Component manufacturing:** Semiconductor fabrication in Taiwan (TSMC), Korea (Samsung), China (SMIC) — highly controlled cleanrooms, but dependent on water-stressed regions (Taiwan droughts have threatened chip production). [Documented, industry reports].
- **Final assembly:** EU-based (Portugal, France, Germany) — labor standards higher, but assembly of security infrastructure for border control participates in the political economy of "Fortress Europe."

**Temporal note:** Mineral extraction for EES hardware deployed in 2024–2025 likely occurred during 2020–2023, given semiconductor and component lead times. [Inferred, based on post-COVID electronics supply chain delays].

---

## 6. Facility Mapping

### 6.1 Mapped Facilities

| Facility | Coordinates (approx.) | Owner/Operator | Function | Confidence |
|----------|----------------------|----------------|----------|------------|
| eu-LISA Primary DC | Strasbourg, France (~48.58°N, 7.75°E) | eu-LISA | Central biometric databases, EES | Corroborated (city-level); Gap (exact address unpublished) |
| eu-LISA Backup DC | St Johann im Pongau, Austria (~47.35°N, 13.20°E) | eu-LISA | Disaster recovery | Corroborated (town-level); Gap (exact address unpublished) |
| Vision-Box HQ/Mfg | Lisbon area, Portugal (~38.7°N, -9.1°W) | Vision-Box (investment by Nordic Capital) | E-gate design, assembly | Corroborated |
| Thales DIS (Digital Identity & Security) | Moirans / Paris area, France | Thales Group | Biometric systems, document readers, e-gates | Corroborated (division HQ); Inferred (specific e-gate factory) |
| Idemia | Paris area, France | Idemia (Advent International majority stake) | Fingerprint/face scanners, biometric SDKs | Corroborated |
| secunet | Essen, Germany | secunet Security Networks AG | German e-gates, ABC systems | Corroborated |

### 6.2 Ownership and Financialization
- **Vision-Box:** Acquired by Nordic Capital (private equity) in 2021. [Documented, press releases]. Private equity ownership incentivizes cost reduction and rent extraction; supply chain transparency is not a priority.
- **Idemia:** Majority owned by Advent International (private equity). [Documented]. Similar opacity incentives.
- **Thales:** Publicly traded French multinational (partial state ownership via French state shareholding). Publishes more comprehensive sustainability reports than private equity-owned competitors, but product-level supply chain transparency remains limited. [Documented, corporate structure].

---

## 7. Lifecycle Documentation: End-of-Life

### 7.1 Hardware Lifespan
- **E-gates and biometric capture devices:** Typical lifespan for automated border control hardware is **7–10 years** before obsolescence or replacement due to wear, security updates, or biometric standard changes. [Inferred, industry standard for industrial electronics; corroborated by airport infrastructure replacement cycles].
- **Data center servers:** 3–5 year refresh cycles typical for high-performance compute. [Inferred].
- **EES launch date:** October 2024. First wave of hardware obsolescence expected 2031–2034. [Inferred].

### 7.2 End-of-Life Trajectories
**Current status:** [GAP — no published e-waste management plan for EES hardware, 2026-05-27].

**Inferred scenarios:**
1. **EU WEEE Directive compliance:** Electronic waste from EU institutions and their contractors must be processed under the WEEE Directive (2012/19/EU). Likely handled by certified recyclers in France, Germany, or Portugal. [Inferred, legal requirement].
2. **Data security concerns:** Biometric capture devices contain storage media (flash, SSDs) that must be destroyed rather than reused to prevent data leakage. This requires specialized shredding or incineration, not standard refurbishment. [Inferred, security protocol].
3. **Export risk:** There is no evidence that decommissioned EU border hardware is exported to Global South e-waste processing hubs (Agbogbloshie, Ghana; Guiyu, China), but this has occurred with other government IT. [Gap — no tracking documented].

---

## 8. Confidence Register

| Claim | Confidence | Basis | Temporal |
|-------|-----------|-------|----------|
| EES requires facial images and fingerprints of non-EU travelers | Documented | Regulation (EU) 2017/2226 | 2017 (regulation); 2024 (operation) |
| eu-LISA operates EES, SIS II, VIS, Eurodac | Documented | EU regulations establishing eu-LISA mandate | Ongoing since respective system launches |
| eu-LISA primary DC in Strasbourg; backup in St Johann im Pongau | Corroborated | eu-LISA official docs; Austrian government sources | 2010s–present |
| Vision-Box, Thales, Idemia, Sopra Steria, secunet are major contractors | Corroborated | Multiple procurement records, press releases | 2010s–present |
| e-gates contain cameras, fingerprint scanners, PCs, document readers, steel enclosures | Documented | Technical descriptions of ABC gates | 2020s |
| Specific minerals (tantalum, tin, tungsten, gold, cobalt, lithium, rare earths) present in electronics | Documented | Electronics industry material science; EU Conflict Minerals Regulation | 2020s manufacturing |
| Specific smelters/refiners in Thales/Idemia/Vision-Box supply chains for border products | Gap | Not disclosed at product level | 2026-05-27 |
| Assembly of e-gates in EU (Portugal, France, Germany) | Corroborated (Vision-Box Portugal, secunet Germany); Inferred (Thales, Idemia final assembly) | Company HQ locations; EU procurement rules favoring EU suppliers | 2020s |
| Component sourcing from East Asia (sensors, processors, memory) | Inferred | Global electronics supply chain patterns; no product-specific BOM available | 2020s |
| Strasbourg DC energy: 2–10 MW | Inferred | Comparable facility estimates; no published load data | 2024–present |
| French grid ~65–70% nuclear | Documented | RTE (French TSO) statistics | 2024–2025 |
| eu-LISA does not publish PUE, water use, or carbon footprint | Gap | Review of eu-LISA annual reports and EMAS statements | 2026-05-27 |
| E-gate lifespan 7–10 years | Inferred | Industrial electronics standard; airport infrastructure cycles | 2024–2034 |
| No published e-waste plan for EES | Gap | Absence in public procurement and environmental disclosures | 2026-05-27 |

---

## 9. Key Gaps Requiring Escalation or Further Investigation

1. **Component-level Bill of Materials (BOM)** for Thales, Idemia, and Vision-Box e-gates. Without this, mineral tracing remains at the level of generic electronics.
2. **Facility-level energy and water data** from eu-LISA Strasbourg and St Johann. This may require freedom of information requests to eu-LISA or the French/Austrian environmental regulators.
3. **Specific hardware OEMs** under eu-LISA server/storage framework contracts (Dell? HPE? Others?).
4. **End-of-life contracts** — who is contracted to decommission EES hardware, and where does it go?
5. **Member State procurement records** for national e-gate purchases. This is fragmented across 29 Schengen states (including associated states) and requires national-level procurement database searches.
6. **Labor conditions** at component manufacturing sites (camera sensor fabs, PCB factories) in the supply chain.

---

## 10. Synthesis: The Material Politics of Border Recognition

The facial recognition infrastructure at EU borders is not immaterial. It requires:
- **Cobalt** (likely from the DRC) for batteries and alloys
- **Rare earths** (likely from China) for drives and actuators
- **High-purity silicon** (likely from East Asian fabs) for the chips that process biometric templates
- **Water and electricity** (from the Rhine and Rhône river basins, and the French nuclear grid) to keep databases running in Strasbourg
- **Steel and aluminum** (European smelters) for the gates that travelers walk through

This is a **displacement architecture**: the violence of extraction is geographically and temporally separated from the moment of recognition at the border. The traveler sees a sleek gate; they do not see the cobalt pit, the rare earth tailings lake, or the data center humming in Strasbourg. The system is designed to make the border visible (to the state) while making its material substrate invisible (to everyone).

The opacity is not incidental. It is produced by:
- Commercial confidentiality clauses in EU framework contracts
- The fragmentation of procurement between eu-LISA (central) and Member States (national)
- The absence of environmental disclosure requirements for EU agencies operating security infrastructure
- The structural invisibility of Global South extraction within European technology discourse

The Material Ecologist tags this as a **threshold-of-detectability** problem: the supply chain is not technically impossible to trace, but it is institutionally designed to fall below the threshold of what EU citizens — and affected travelers — are permitted to see.

---

*Material Footprint Report v0.1 — Material Ecologist — Substrate Collective — 2026-05-27*
