# JV3 — Three-Member, Self-Guaranteed Compute Joint Venture

> **⚠ Numbers superseded (Jul 2026, v2).** This document's capacity parameterization (~21MW tranches; 48/35/12 racks; ~147MW; ~40% equity) was the first cut. The **current numbers** — after external review (`critique.md`) — are: 7 × 20MW-IT tranches (≈24MW gross), 48/30/11 racks per member at 135/220/600kW, platforms **GB300 → Vera Rubin NVL72 → Rubin Ultra NVL576 (T6–T7 as options)**, **~$4.8B firm (T1–T5) / ~$9.1B full program**, base stack 50% equity / 32% first-close debt / 18% vendor with public capital and NVIDIA as upside levers. See **`JV3_financial_model.md` v2** and **`jv3_onepager_full.html` v4**. The structure, governance, and credit-enhancement logic below remain current.

**Variant of** `jv_buildout_and_financing.md`. Two structural changes define JV3:

1. **Three equal members**, not four (from the founding group — General Intuition, Gradium, AmiLabs, Aire; the three-way composition is TBC).
2. **The members themselves guarantee the demand.** Each signs a take-or-pay for its own slice — **48 GB300 NVL72 racks (~7MW) per member per tranche**, then the power-equivalent in Vera Rubin. No external anchor tenant is *required* (Meta/Nebius/merchant become optional upside, not the base case).

> This is a **captive compute cooperative**: the three members build, own, and consume the capacity, funding it with a mix of equity and prepaid capacity. The demand guarantee is real because they need the compute — but the members are VC-backed (sub-investment-grade), which is the whole financing problem JV3 has to solve (§4). Rack-power figures are planning assumptions (NVL576/Kyber especially is preliminary per NVIDIA). See `deal_comparables.md` / `deal_comparables_sources.md` for the precedents these mechanics are drawn from.

---

## 1. What's different from the base plan

| | Base plan (JV1/JV2) | **JV3** |
|---|---|---|
| Members | 4 | **3, equal thirds** |
| Demand | Captive + **Meta/Nebius anchor** + merchant | **100% self-guaranteed by the 3 members** (anchor/merchant optional) |
| Debt anchor | Meta's **investment-grade** take-or-pay | The members' **sub-IG** take-or-pay + **credit enhancement** |
| Per-member unit | — | **48 GB300 racks ≈ 7MW / member / tranche** |
| Capital stack | ~27% equity | **~35–45% equity** (sub-IG offtake supports less/costlier debt) |
| Control | Shared | **Each member controls & funds its own sleeve** |

The trade is clean to state: **JV3 removes external-anchor dependency and keeps 100% of the economics with the members — at the cost of a weaker debt credit that must be shored up with guarantees, prepayment, and NVIDIA backstop.**

---

## 2. Capacity architecture — the concrete build

Each member holds a **constant ~7MW slice per tranche**; as rack density rises (GB300 → Rubin → Rubin Ultra), the **rack count per member falls** while GPUs per rack rise sharply.

| Phase | Rack platform | Planning kW/rack | **Racks / member** | MW / member | Racks / tranche (×3) | MW / tranche | GPUs / rack | GPUs / tranche |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **GB300** | GB300 NVL72 | ~145 | **48** | ~7.0 | 144 | ~20.9 | 72 | 10,368 |
| **VR-72** | Vera Rubin NVL72 | ~200 | **~35** | ~7.0 | 105 | ~21.0 | 72 | 7,560 |
| **VR-576** | Vera Rubin Ultra NVL576 (Kyber, 800VDC) | ~600 | **~12** | ~7.2 | 36 | ~21.6 | 576 | 20,736 |

*Notes:* NVL576/Kyber is the 800VDC, ~600kW–1MW-class rack; at 1MW-class the count falls further to **~7 racks/member**. GPU-per-rack for NVL576 reflects the 576-GPU Rubin Ultra domain, so tranche GPU counts jump even as rack counts collapse. "~7MW/member" is the invariant — the user's "equivalent in VR" — so each tranche stays **~21MW** regardless of platform.

**Program roll-up (7 tranches, ~21MW each ≈ ~147MW):**

| Tranche | Phase | ~MW | Cumulative |
|---|---|---:|---:|
| T1–T2 | GB300 NVL72 | ~42 | ~42 *(≈ "40MW GB300")* |
| T3–T5 | Vera Rubin NVL72 | ~63 | ~105 |
| T6–T7 | Vera Rubin Ultra NVL576 | ~43 | ~148 *(VR total ≈ "100MW")* |

**Per member over the full program:** ~225 racks (2×48 + 3×35 + 2×12), ~49MW, ~28,300 GPUs. The NVL576 phase dominates GPU count (576/rack) despite the smallest rack footprint — build the shell **800VDC-ready from day one** so the VR-576 tranches drop into reserved corridors.

---

## 3. JV structure — equal thirds, per-member sleeves, shared campus

The elegant way to express "three members who each guarantee their own demand" is a **shared PropCo + three ChipCo sleeves per tranche**:

```
                 ┌──────────────────────────────────────┐
                 │  JV3 TopCo — 3 members, equal 1/3      │
                 │  Holds NVIDIA allocation, site, brand  │
                 └───────────────┬────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                         ▼
   TrancheCo (per 21MW block)
   ┌───────────────────────────────────────────────────────┐
   │  Shared PropCo  — powered shell, split 3 ways (cost)    │
   ├───────────────┬───────────────┬───────────────────────┤
   │ ChipCo sleeve │ ChipCo sleeve │ ChipCo sleeve          │
   │  Member A     │  Member B     │  Member C              │
   │  48 racks     │  48 racks     │  48 racks              │
   │  A's take-or- │  B's take-or- │  C's take-or-pay +     │
   │  pay + gtee   │  pay + gtee   │  guarantee             │
   └───────────────┴───────────────┴───────────────────────┘
```

**Why sleeves, not a pooled facility:** each member's guarantee supports **only its own debt**. If Member C stumbles, its sleeve is isolated — A and B (and their lenders) are unaffected, and C's sleeve can be re-marketed or bought out. This is the credit-isolation logic lenders will insist on given three correlated sub-IG tenants, and it matches the "each member self-guarantees" ethos. The **shared PropCo** (grid, substation, cooling plant, campus) is a common facility, cost-shared 1/3 each, financed with long infra debt.

**Governance (3 equal members):**
- **Own-sleeve autonomy:** each member decides refresh, resale of its idle capacity, and financing of its own sleeve.
- **Shared decisions** (site, NVIDIA allocation split, PropCo capex, admitting a co-equity partner): supermajority (2 of 3) with protective reserved matters so no member is steamrolled. Note 3 members can produce a **2-1 split** — pre-agree a tie-break/escalation and a buy-sell (shotgun) mechanism.
- **Allocation:** the 48-rack-per-member split is equal by design; idle capacity in any sleeve flows to merchant/anchor to keep utilization (and refinanceability) high.

---

## 4. The self-guaranteed demand model — and how to make it bankable

This is the crux of JV3. The members *are* the demand, so utilization certainty is excellent — but their take-or-pay is only as bankable as their credit, and they are **VC-backed, sub-investment-grade**. Per the comparables, lenders sized CoreWeave's debt on **Microsoft's IG** backlog; a pure sub-IG captive offtake supports far less, and pricier, senior debt. JV3 therefore has to **manufacture credit** around the members' guarantees:

| Enhancement | What it does | Precedent / basis |
|---|---|---|
| **Several member guarantees** | Each member guarantees *its own* sleeve's take-or-pay (not joint) → clean isolation | Standard sleeve structuring |
| **Capacity prepayment** | Members prepay **6–12 months of fees** into a reserve → funds the DSRA; customer-funded working capital | Common in captive/co-op builds |
| **VC-backer credit support** | The members' backers post **LCs / parent guarantees / committed equity** behind the offtake — the single biggest lever to lift sub-IG offtake toward bankable | The offtake→debt-credit mapping in `deal_comparables.md §9` |
| **NVIDIA capacity backstop** | NVIDIA obligation to buy unsold capacity (à la the **$6.3B CoreWeave backstop**) → de-risks the lender if a member defaults | CoreWeave–NVIDIA, SEC-filed |
| **Overcollateralization** | Lower advance rate + more equity → the asset (GPUs) covers the debt even on offtake stress | GPU borrowing-base = depreciable cost |
| **Cash-collateralized DSRA + refresh reserve** | 6–12mo debt service + GPU refresh pre-funded | CoreWeave DSRA covenants |

**Concentration reality:** three tenants at ~33% each is better than CoreWeave's 62–67% single-tenant — but the three are **correlated** (all AI labs, all sub-IG, same demand cycle). Lenders will apply a correlation haircut. The sleeve structure + several guarantees + NVIDIA backstop are what keep it financeable.

**Optional upside (not base case):** the members can still (a) sell idle capacity **merchant**, or (b) layer a **Meta/Nebius anchor** onto specific tranches to *improve* debt terms and seed the ABS take-out. JV3 doesn't depend on them — but they're the cheapest way to buy back leverage if the sub-IG haircut bites.

---

## 5. Financing — the revised capital stack

Because the demand guarantee is sub-IG, JV3 shifts **~10–15 points from debt to equity** (or holds leverage only with the §4 enhancements). Representative **per-member GB300 sleeve** (~€330M for its 7MW / 48 racks, ~1/3 of a ~€1.0B tranche):

| Layer | ~% | ~€ (per member sleeve) | Terms |
|---|---:|---:|---|
| **Equity** (member + VC-backer) | ~40% | ~€130M | First-loss; the member's own capital + backer co-invest |
| **Senior GPU-backed debt** | ~40% | ~€130M | Credit-enhanced (guarantee + prepay + NVIDIA backstop); advance vs **depreciable GPU cost**, lower than the Meta-anchored ~55–60%; mid-teens→compressing as it seasons |
| **Vendor finance / lease** | ~20% | ~€65M | NVIDIA / OEM — larger role than in the anchored case |
| **+ Capacity prepayment** | (off-stack) | ~€10–20M | 6–12mo fees → funds DSRA (customer-funded) |

Shared **PropCo** (~€230M/tranche, ~€77M/member) is financed separately: ~65% long infra debt + ~35% equity, cost-shared 1/3.

**Per-member downpayment (the "get me into tranche 1" cash):**
- Pre-FID development share: ~€5–10M
- **GPU deposit** (10–25% of its 48-rack order ≈ €50–160M GPU cost) → **~€15–40M**
- Equity draw at FID: balance of the ~€130M sleeve equity
- ⇒ **Real upfront cash per member ≈ €50–120M** for its first 7MW slice.

**How the program stays fundable:** same **revolving-equity engine** as the base plan — each member seasons its sleeve (12–18mo of its own contracted usage) and **refinances to recycle equity** into the next tranche; a shared **infra co-equity partner** can still be admitted for the PropCo and the VR phase. But note: with self-guaranteed sub-IG offtake, **refinancing upside is smaller** than the Meta-anchored case (the ABS take-out prices wider), so JV3 leans more on **member equity + prepayment + vendor finance** and less on cheap senior debt.

**Comparison — same 7MW slice, anchored vs self-guaranteed:**

| | Meta-anchored (base) | **JV3 self-guaranteed** |
|---|---|---|
| Equity | ~27% | **~40%** |
| Senior debt advance | ~55–60% | **~40–50%, credit-enhanced** |
| Debt cost | Toward IG | **Higher (sub-IG + correlation haircut)** |
| Anchor dependency | High (must land Meta) | **None — but must credit-enhance** |
| Economics retained | Shared w/ anchor | **100% with members** |

---

## 6. Getting started (JV3-specific)

1. **Form TopCo + the sleeve template.** Three-member agreement: equal thirds, 48-rack allocation, per-sleeve autonomy, 2-of-3 supermajority + buy-sell, cash-call/dilution regime.
2. **Paper the self-guarantee.** Each member signs its take-or-pay; secure **VC-backer credit support** (LC / guarantee / committed equity) — this is JV3's gating item, replacing the "land an anchor LOI" gate.
3. **NVIDIA:** confirm the **144-rack GB300 allocation** for tranche 1 (48 each) and negotiate the **capacity backstop** — it matters more here than in the anchored case.
4. **Mandate Morgan Stanley** for the credit-enhanced senior facility + warehouse (fund the GPU deposits), and open the ABS-take-out and co-equity (PropCo) conversations early.
5. **Site & grid:** exclusivity at Dunkerque/Le Bosquel; RTE phasing to ~21MW tranches; **800VDC-ready** shell for the VR-576 phase.
6. **FID Tranche 1 (GB300):** each member funds its ~€50–120M and prepay; first drawdown via warehouse.

---

## 7. Risks specific to JV3

| Risk | Mitigant |
|---|---|
| **Correlated sub-IG concentration** (3 AI labs, same cycle) | Sleeve isolation + several guarantees + VC-backer support + NVIDIA backstop; option to add IG anchor to a tranche |
| **A member can't fund a cash call / defaults** | Per-sleeve isolation; pre-agreed dilution + buy-sell (shotgun); backer step-in; re-market the sleeve |
| **Weaker debt capacity than anchored case** | Accept higher equity %; lean on prepayment + vendor finance; credit-enhance |
| **Self-dealing optics (owners = customers)** | **Arm's-length pricing** on the intercompany take-or-pay (lender + tax/transfer-pricing requirement) |
| **2-1 governance deadlock** | Tie-break/escalation + buy-sell in the JV agreement |
| **GPU obsolescence across GB300→Rubin→Rubin Ultra** | Match GPU-debt tenor to contract; refresh reserve; 800VDC-ready shell; phase the density transition |
| **Refi/ABS prices wide (sub-IG)** | Season sleeves; optionally graft an IG anchor before securitizing; don't over-assume equity recycling |

---

*Planning variant. Rack-power/GPU figures are assumptions (NVL576/Kyber preliminary). Financing ranges to be replaced by member/backer credit support, NVIDIA allocation + backstop terms, EPC bids, and lender term sheets. Precedents & sources: `deal_comparables.md`, `deal_comparables_sources.md`.*
