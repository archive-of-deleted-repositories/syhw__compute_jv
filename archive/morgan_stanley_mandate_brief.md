# Confidential — Financing Mandate Brief
## Project [Codename] — 140MW France AI Factory JV

**To:** Morgan Stanley — Global Capital Markets / Structured Finance / Project & Infrastructure Finance
**From:** [JV TopCo] (consortium: General Intuition, Gradium, AmiLabs, Aire)
**Re:** Mandate to arrange the senior debt program for a 140MW phased NVIDIA GPU compute build in France
**Status:** Draft for discussion — not a financing commitment by any party

---

## 1. Transaction in brief

We are building **140MW of NVIDIA GPU compute in France** — **40MW GB300 (2026–27) + 100MW Vera Rubin (2027–29)** — in **7 ring-fenced 20MW tranches**, on a state fast-track site (Dunkerque ZGI or Le Bosquel; see site dossiers). Total program capex **~€6.8–9.5B**.

- **Sponsor:** consortium of four AI labs that hold NVIDIA allocation, site/power control, and build+operate capability in-house.
- **Demand:** **captive** (the four members) + **anchor take-or-pay** (Meta, Nebius) + **merchant** backstop.
- **Equity:** **€100–300M** consortium equity for tranche 1, treated as **revolving** downpayment capital; an **infrastructure co-equity partner** to be admitted from tranche 3.
- **What we want from Morgan Stanley:** lead-arrange and structure the **senior debt program** across all tranches, provide a **warehouse/bridge**, and deliver the **ABS take-out** that recycles equity.

**Why this is bankable (and different from a speculative neocloud):** debt is sized **only against contracted, credit-supported offtake** (anchored on Meta's IG credit), in **bankruptcy-remote SPVs** secured on the GPUs and receivables, with the **slow asset (shell) and fast asset (GPUs) financed separately**. This is the CoreWeave / Meta-Hyperion / xAI template, applied tranche-by-tranche.

---

## 2. Mandate scope — the four jobs

We propose to mandate Morgan Stanley as **Sole/Lead Structuring Agent, Lead Arranger and Bookrunner** for:

1. **Senior secured term debt (per tranche).** A **delayed-draw term loan (DDTL)** program that funds each 20MW tranche as built, secured on the ChipCo (GPUs + receivables), sized on contracted EBITDA. Structured to march from private-credit pricing on the GB300 proof tranches toward **investment-grade** on the Meta-anchored Vera Rubin tranches — the CoreWeave DDTL→IG path.
2. **Warehouse / bridge facility.** Funds **GPU deposits and construction** before term debt converts at energization — so our equity is not trapped in undelivered hardware. (xAI/CoreWeave precedent.)
3. **ABS / securitization take-out.** Refinance seasoned, contracted tranches into a **data-center/GPU ABS** (KBRA/DBRS/S&P-rated, senior/mezz classes, ARD with cash sweep) to recycle equity into later tranches. EU DC ABS is proven (Vantage €640M EMEA, 2025).
4. **Syndication & co-arrange.** Distribute to private-credit funds (Blackstone, Blue Owl, Carlyle, Magnetar, PIMCO, Ares) and **co-arrange the long-dated infra tranche on the PropCo (shell)** with a French/EU bank (SocGen, BNP Paribas, Crédit Agricole CIB, or MUFG).

We will run an **infra co-equity partner process in parallel** (Brookfield / Blue Owl / DigitalBridge / MGX / Bpifrance-CDC type) and would welcome Morgan Stanley's introductions; we expect to admit that partner from tranche 3.

---

## 3. Proposed capital structure (per representative ~€1.0B 20MW tranche)

| Layer | Entity | ~% of tranche | ~€ | Target terms |
|---|---|---:|---:|---|
| **Infra / project debt** | PropCo (powered shell, €220M) | ~14% | ~€143M | 10–15yr, **SOFR/EURIBOR + 250–400bps**, 65% LTV, DSCR ≥1.25x |
| **Senior secured GPU-backed debt** | ChipCo (GPUs €780M) | ~43% | ~€430M | 3–5yr (matched to contract), advance ≤ depreciable GPU cost, 55–60% of ChipCo, DSRA + refresh reserve |
| **Vendor finance / lease** | ChipCo | ~15% | ~€155M | NVIDIA / OEM (HPE FS, Dell, Supermicro) deferred/lease; NVIDIA backstop sought |
| **Equity (the "downpayment")** | PropCo + ChipCo | ~27% | ~€272M | Consortium + co-investor; recycled at refi/ABS |
| **Tranche total** | | 100% | ~€1.0B | |

**Equity-recycling engine:** each tranche, once **built + contracted + ~12–18mo stabilized**, is refinanced (DDTL upsizing and/or ABS take-out at ~75–80% effective leverage) returning **~€100–150M** of the ~€272M equity to redeploy. Combined with the co-equity partner funding the bulk of the Vera Rubin phase, the consortium's €100–300M behaves like a **revolving fund**, not a cumulative bill.

---

## 4. The specific structuring asks

We would like Morgan Stanley's view and term-sheet indications on:

1. **Advance rate / borrowing base.** Confirm the basis — % of **depreciable GPU cost** vs % of **contracted EBITDA** (DSCR-driven) — and the advance rate achievable at each offtake-credit mix. Target ≥55–60% of ChipCo on the Meta-anchored tranches.
2. **The Meta credit lift.** How far does a Meta take-or-pay (or residual-value guarantee, à la Hyperion's "Beignet Investor LLC" / A+ structure) move the senior tranche toward **investment grade** and inside **T+225bps**? What contract form maximizes the lift?
3. **Warehouse sizing & advance for GPU deposits.** Can the warehouse fund the **10–25% NVIDIA/OEM deposit** (~€70–175M/tranche) against delivery, so equity isn't pre-committed to undelivered chips?
4. **GPU depreciation / residual value.** What useful-life and residual assumptions will the desk and rating agencies accept? We propose a **conservative 4–5yr** schedule + funded **refresh reserve**, with **GPU-debt tenor matched to contract tenor**.
5. **Counterparty-credit haircuts.** How will you haircut **captive member offtake** (VC-backed) vs **Nebius** (strong-but-sub-IG) vs **Meta** (IG)? What **credit support** (parent guarantee / prepay from members' VC backers) converts member offtake into countable debt capacity?
6. **ABS take-out timing & structure.** Earliest seasoning to securitize; note classes (A/B), ARD/cash-sweep, expected ratings and spread vs the construction/GPU debt; can EU and US assets sit in one platform?
7. **Cross-tranche vs siloed.** Keep each tranche fully non-recourse (our preference) vs a master-trust/platform facility that lowers cost but adds cross-collateralization — trade-offs.
8. **Reserves & covenants.** DSRA size, refresh reserve, maintenance reserve, leverage/DSCR covenants, cash-sweep triggers, and what permits **distributions to equity**.
9. **Hedging.** Rate hedging on the floating debt; €/$ exposure on NVIDIA/ODM payments.

---

## 5. Offtake → debt sizing (the credit basis)

| Offtake source | Credit | Role in the debt |
|---|---|---|
| **Meta** take-or-pay | Investment-grade | Anchor the **largest, cheapest** senior tranches; pursue IG execution |
| **Nebius** capacity contract | Strong NeoCloud (the Microsoft "pay regardless of utilization" template) | Supports senior debt at a spread; possible operating/merchant-resale partner |
| **JV members** (General Intuition, Gradium, AmiLabs, Aire) | VC-backed, sub-IG | Fills utilization; **credit-supported** by members' VC backers (guarantee/prepay/equity into TopCo) to count |
| **Merchant** | Uncontracted | **Sized at zero** for debt; equity upside only |

We will deliver a contracted-revenue waterfall and a backlog (RPO) schedule per tranche, with counterparty credit, term, and floors — the same basis CoreWeave used to size its DDTLs against Microsoft/OpenAI backlog.

---

## 6. Indicative process & timeline

| Phase | Weeks | Milestone |
|---|---|---|
| Mandate & kickoff | 0–2 | Engagement letter; data-room build; appoint counsel (CC/Linklaters/A&O Shearman) + owner's engineer + model auditor |
| Structuring | 2–8 | Term sheet for senior DDTL + warehouse; rating-agency soundings; co-equity partner soundings |
| Anchor & allocation | 4–12 | Meta/Nebius take-or-pay LOIs; NVIDIA GB300 allocation + deposit terms |
| Underwrite & syndicate | 8–18 | Credit-approved commitments; private-credit syndicate; infra-bank co-arrange on PropCo |
| **FID Tranche 1** | 16–26 | First drawdown via warehouse; EPC signed |
| Season → refinance | +12–18mo per tranche | DDTL upsize / first ABS take-out → recycle equity into next tranche |

---

## 7. Information we will provide (data room)

- JV structure chart, members' agreement, governance, and consolidated/SPV financials.
- **Contracted-offtake pack:** Meta/Nebius LOIs/term sheets, member intercompany take-or-pay, RPO/backlog schedule, counterparty credit files.
- **NVIDIA allocation** confirmation + deposit terms; OEM/ODM quotes; vendor-finance indications.
- **Site & grid:** RTE connection offer / fast-track phasing, land control, permits.
- **EPC:** standardized 20MW, 800VDC-ready block bid pack and critical-path schedule.
- **Financial model:** per-tranche capex, the PropCo/ChipCo split, DSCR sizing, the recycle engine, and equity IRR (see `financial_model_skeleton.md`).
- Independent technical, insurance, and market (utilization/price) reports.

---

*Prepared for discussion. All terms indicative and subject to definitive documentation, credit approval, due diligence, and market conditions. Figures synthesized from public comparables (see `deal_comparables.md`) and the program research in this folder; to be replaced by actual quotes and term sheets.*
