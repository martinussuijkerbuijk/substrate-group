# Evidence: Jurisdictional Topology of EU Border Facial Recognition

**Source Type:** Legal and institutional analysis  
**Date Compiled:** 2026-05-27  
**Confidence Ceiling:** Corroborated — Based on public legal instruments and agency statutes

---

## The Four Presences

Per the Collective's lawscape method ([[lawscape]]), we map four types of presence for the EU border biometric system:

| Presence Type | Locations | Accountability Mechanism | Gap |
|--------------|-----------|--------------------------|-----|
| **Legal presence** | EU Treaties; Regulations 2017/2226 (EES), 2018/1240 (ETIAS), etc. | CJEU jurisdiction; EU Ombudsman; national DPA referrals | Strong on paper |
| **Contractual presence** | Prime contractor HQs: France (Thales, IDEMIA, Sopra Steria), Ireland (Accenture), Japan (NEC) | Belgian or French courts for EU agency contracts; arbitration clauses likely | Weakened by commercial confidentiality |
| **Material presence** | Data centers: France (Strasbourg area), Austria (St. Johann); Border hardware: manufactured globally; Algorithm development: Japan, France, USA | National data protection authorities (CNIL, DSB); physical inspection limited | Obscured by subcontracting |
| **Decisional presence** | Schengen external borders (Spain, Greece, Italy, Hungary, Poland, etc.); Frontex operations in Mediterranean and Aegean | Frontex Fundamental Rights Officer; national border guards; limited judicial review at point of decision | Weakest — individual border decisions lack effective redress |

**Confidence:** Legal presence: Documented. Contractual presence: Inferred (standard governing law clauses). Material data centers: Corroborated. Decisional presence: Documented (legal analysis of border guard accountability).

---

## Key Jurisdictional Gaps

### 1. The Estonia-Gap

eu-LISA is legally headquartered in Tallinn, Estonia. However:
- The material data centers are in France and Austria
- The prime contractors are predominantly French
- The border decisions occur in Mediterranean and Eastern European Member States
- Estonian courts and regulators have minimal practical involvement

Estonia provides a **jurisdictional shell**: legal presence without material or decisional presence. This distances accountability from impact.

**Confidence:** Documented — eu-LISA headquarters and data center locations are public. Accountability vacuum in Estonia: Inferred.

### 2. The Delaware-France Gap

IDEMIA is French-incorporated and French-designated as "strategic industry," but controlled by US private equity (Advent International, Delaware-incorporated). This means:
- French law governs the contract with eu-LISA
- US law governs the ownership and potential sale of the company
- Delaware corporate law provides maximum opacity for beneficial ownership
- CFIUS (US foreign investment review) could block or condition IDEMIA's operations, including EU contracts

The beneficial ownership is **legally present in Delaware** while the contractual liability is **legally present in France**.

**Confidence:** Documented (Advent ownership, Delaware incorporation, French strategic status). CFIUS applicability: Inferred.

### 3. The Irish Tax-Arbitrage Gap

Accenture plc is legally incorporated in Ireland. For EU procurement:
- Irish law governs the parent company
- EU contracts may be signed by Belgian, French, or German subsidiaries
- Profit likely shifts to Ireland or other low-tax jurisdictions through transfer pricing
- The entity that signs the contract may not be the entity that develops the software or hosts the data

**Confidence:** Documented (Irish incorporation). Specific transfer pricing for EU border contracts: Gap.

### 4. The Japan-EU Algorithm Gap

NEC algorithms (if deployed) are developed in Japan under Japanese law:
- Training data provenance unclear
- Japanese export controls may apply
- EU GDPR accountability chain may not extend to Japanese development centers
- No EU regulatory body can inspect the algorithm training process

**Confidence:** NEC Japanese incorporation and development centers: Documented. Specific algorithm training locations and data sources: Gap.

### 5. The Border Point Accountability Vacuum

At the actual border crossing:
- The border guard makes the decision to admit or deny entry
- The biometric system provides a match/non-match signal
- The algorithm vendor (NEC, IDEMIA, Thales) is not present
- The systems integrator (Sopra Steria, Accenture) is not present
- eu-LISA is not present
- Frontex may be present in coordinated operations but lacks legal liability for individual decisions

**Liability stops at the Member State border guard**, but the guard cannot explain or challenge the algorithmic output. The jurisdictional topology ensures that no single entity can be held accountable for algorithmic errors.

**Confidence:** Documented — Legal framework places operational liability on Member States. Algorithmic accountability gap: Corroborated (EDPB and legal scholarship).

---

## Lawscape Synthesis

The EU border biometric system is a **layered lawscape** designed to prevent accountability from co-locating with harm:

> *"The borders that divide data centers, the contracts that define cloud regions, the permits that authorize extraction."* — [[lawscape]]

In this case:
- The borders that divide **legal jurisdictions** (Estonia, France, Austria, Japan, Ireland, USA)
- The contracts that define **liability regions** (prime contractor liability terminates at subcontractor interface)
- The permits that authorize **extraction** (Regulations 2017/2226 and 2018/1240 authorize biometric capture at borders)

Each layer is legally necessary. Each layer distances the authorizer from the authorized harm.

**Confidence:** Synthesis — Inferred, grounded in documented legal structures

---

## Key Gaps

- [GAP — Full list of data processing locations for each system component]
- [GAP — Governing law and dispute resolution clauses in specific prime contracts]
- [GAP — Subcontractor liability allocation and indemnification terms]
- [GAP — Whether any EU border biometric data is processed in non-EU locations through cloud or development arrangements]
