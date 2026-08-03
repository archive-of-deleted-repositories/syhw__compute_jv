# Draft Term Sheet — Anchor Compute Capacity Agreement (Take-or-Pay)
## [JV OpCo] ("Provider") — [Meta / Nebius] ("Customer")

**Non-binding heads of terms for discussion.** Final terms subject to definitive documentation. This outline is engineered so the contract is **bankable** — i.e., our lenders (Morgan Stanley + syndicate) can size senior debt against the committed revenue. Clauses marked **[BANKABILITY]** are the ones lenders will test hardest; do not soften them without re-checking debt impact.

---

## 1. Parties & structure

| Term | Provision |
|---|---|
| **Provider** | [JV OpCo], operator of the 140MW France AI factory, contracting on behalf of the relevant **TrancheCo SPV(s)** |
| **Customer** | [Meta Platforms entity] / [Nebius entity] |
| **Guarantor (Provider side)** | Limited — obligations sit in the bankruptcy-remote SPV; TopCo provides only specified performance undertakings |
| **Guarantor (Customer side)** | **[BANKABILITY]** Parent guarantee from the **investment-grade parent** (Meta Platforms, Inc.) — the guarantee is what gives the debt its credit rating |

---

## 2. Capacity & service

| Term | Provision |
|---|---|
| **Committed capacity** | [X] MW of GPU compute = [N] × NVIDIA [GB300 NVL72 / Vera Rubin NVL72] racks, in dedicated halls within the campus |
| **Allocation to tranches** | Customer capacity allocated to specific TrancheCos so each financed SPV carries identifiable contracted revenue **[BANKABILITY]** |
| **Service model** | Bare-metal / dedicated GPU capacity (reserved instances), Customer-operated or Provider-managed [select]; power, cooling, space, network, remote-hands included |
| **Performance SLA** | Power availability ≥ [99.9%]; GPU goodput / availability ≥ [X%]; defined remedies as **service credits**, NOT termination, except on sustained material failure (protects revenue floor) **[BANKABILITY]** |
| **Ramp** | Capacity drawn down on a delivery schedule tied to tranche energization; billing begins at **service-ready date** per block |

---

## 3. Term & commercial

| Term | Provision |
|---|---|
| **Term** | **[BANKABILITY]** Initial **[7–15] years**, matched to/longer than the senior debt tenor on the relevant tranche. (Meta-Hyperion-class structures run to 2049; Oracle-Crusoe is a 15-yr lease.) |
| **Renewal** | [1–2] × [3–5] yr extension options; pricing reset to then-market with collar |
| **Pricing** | **$/MW/month** (or **$/GPU-hour** with a committed-hours floor). Indicative reserved-capacity pricing benchmarked to market (e.g., GB300/VR reserved rates) |
| **Step-downs** | Pricing may step down as GPUs age (reflecting ~2x/generation rental decay) — but the **take-or-pay floor (below) holds**, protecting debt service **[BANKABILITY]** |
| **Escalation** | Power-cost pass-through or CPI-linked escalator on the service fee |

---

## 4. Take-or-pay — the core bankability clause **[BANKABILITY]**

| Term | Provision |
|---|---|
| **Minimum revenue commitment** | Customer pays for the committed capacity **irrespective of actual usage or consumption** — the verbatim standard from the Nebius–Microsoft agreement (*"obligated to pay the Fees … irrespective of the actual usage or consumption"*, filed as Exhibit 4.4 to Nebius's SEC Form 20-F). This **minimum monthly payment is the figure the debt is sized on.** |
| **Floor level** | ≥ [90–100]% of contracted capacity × contract price, for the full initial term |
| **Unconditional / hell-or-high-water** | Payment obligation not subject to set-off, counterclaim, or Customer's own demand conditions, except for defined Provider material default with cure |
| **Payment** | Monthly in advance; direct to **SPV collection account** controlled under the financing (cash waterfall) **[BANKABILITY]** |

---

## 5. Termination & make-whole **[BANKABILITY]**

| Term | Provision |
|---|---|
| **Customer convenience termination** | If permitted at all, only against a **make-whole / termination payment** = NPV of remaining minimum payments (or sufficient to repay attributable debt + return). Lenders require this. |
| **Provider default** | Termination only on sustained, uncured material failure (beyond SLA credits); cure periods + lender step-in rights |
| **Lender step-in** | **[BANKABILITY]** Customer consents to assignment of the contract to lenders as security; lenders / a replacement operator may step in and the contract survives Provider insolvency (direct agreement) |
| **Change of control** | Provider CoC permitted to lenders/replacement operator; Customer CoC does not release the parent guarantee |

---

## 6. Risk allocation

| Term | Provision |
|---|---|
| **Power price** | Pass-through to Customer or hedged via PPA; Provider not left with merchant power risk on contracted capacity |
| **GPU obsolescence / refresh** | Defined refresh rights/obligations; who funds the refresh and how pricing resets; aligns with the funded refresh reserve |
| **Force majeure** | Narrowly drafted; FM relieves performance but **does not extinguish the minimum payment** beyond a short defined period (lender-protective) **[BANKABILITY]** |
| **MAC** | No broad Customer MAC walk-away; tightly defined |
| **Exclusivity / expansion** | Customer right of first offer on additional tranches; Provider may sell uncommitted capacity merchant or to other anchors (diversification) |

---

## 7. Accounting & structuring

| Term | Provision |
|---|---|
| **Lease classification** | Structure as **service contract / operating lease** (vs finance lease) per the parties' ASC 842 / IFRS 16 objectives — confirm with both sides' auditors |
| **Confidentiality** | Mutual; permitted disclosure to lenders, rating agencies, co-equity partner under NDA |
| **Governing law** | [English / French] law; [LCIA / ICC] arbitration |

---

## 8. How each anchor maps to our debt (internal note — not for the counterparty)

- **Meta** → pursue the **parent guarantee / residual-value-guarantee** structure (Hyperion template). This is what lifts a single-campus GPU SPV to **investment grade** and unlocks the cheapest, largest senior tranche. Put Meta on the tranches we most want to securitize.
- **Nebius** → the **Microsoft–Nebius "pay regardless of utilization"** language is the model; strong-but-sub-IG, so debt at a spread. Nebius can also be our **merchant-resale / operating partner** for uncommitted capacity — discuss a dual role.
- **JV members** → mirror these terms in **intercompany** take-or-pay, then have the members' **VC backers credit-support** them (parent guarantee / prepay / equity into TopCo) so lenders count the revenue.
- **Sequencing** → land **at least one anchor LOI before tranche-1 debt close**. It is the single gating document for the senior facility.

---

*Non-binding. For negotiation use. Bankability clauses align to `morgan_stanley_mandate_brief.md` and the comparables in `deal_comparables.md`.*
