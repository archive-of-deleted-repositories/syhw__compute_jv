# Financial Model Skeleton — 140MW France AI Factory JV

A build-ready spec for the tranche-by-tranche model: the PropCo/ChipCo split, DSCR-based debt sizing, the **equity-recycle engine**, and equity IRR. Build as an Excel/Sheets workbook with the tabs below. All numbers here are **placeholder planning ranges** from `deal_comparables.md` and the program research — replace with LOIs, NVIDIA terms, EPC bids, and lender term sheets.

---

## Workbook structure (tabs)

1. **Assumptions** — global drivers (one place, colour-coded inputs)
2. **Tranche engine** — one parametric 20MW block, copied/flagged GB300 vs Vera Rubin
3. **Debt sizing** — DSCR/advance-rate solver per tranche
4. **Recycle & refinance** — seasoning → refi/ABS → equity returned
5. **Program roll-up** — 7 tranches on a timeline, consolidated cash flow
6. **Equity returns** — sponsor vs co-equity waterfall, IRR/MOIC
7. **Scenarios** — power price, utilization, GPU residual, rate, delay
8. **Outputs** — IC dashboard

---

## 1. Assumptions tab (global inputs)

| Driver | GB300 | Vera Rubin | Notes |
|---|---|---|---|
| Tranche IT power | 20 MW | 20 MW | |
| All-in capex / tranche | €0.8–1.15B | €0.95–1.25B | |
| — Powered shell (PropCo) | ~€220M (€10–12/W) | ~€220M | Slow asset, 10–15yr life |
| — GPU+net+storage (ChipCo) | ~€580–930M | ~€730–1,030M | Fast asset |
| Racks / tranche | ~140–150 | ~95–130 | |
| GPUs / tranche | ~10,000–10,800 | ~7,000–9,000 | |
| GPU useful life (depreciation) | **4–5 yr** | 4–5 yr | Conservative; bear-case 3yr scenario |
| GPU residual value @ end-life | 10–20% | 10–20% | Scenario-tested |
| PUE | 1.15 | 1.15 | |
| Power price | €70/MWh base (55 / 85 cases) | same | |
| Utilization | 90% base (75 / 97 cases) | same | |
| Contract price (reserved) | $/MW/mo or $/GPU-hr | same | From offtake LOIs |
| Take-or-pay floor | 90–100% of contracted | same | Debt sized on this |

**Capital-stack inputs (per tranche):**
| Layer | Target | Rate | Tenor |
|---|---|---|---|
| PropCo infra debt | 65% of shell | EURIBOR + 250–400bps (≈5–7%) | 10–15yr |
| ChipCo senior GPU debt | 55–60% of ChipCo | SOFR/EURIBOR + 400–700bps | 3–5yr |
| Vendor finance/lease | 15–20% of ChipCo | 6–9% | 3–5yr |
| Equity | balance (~25–30% blended) | — | — |

**Refinance assumptions:** seasoning to refi = 12–18 mo; effective leverage at take-out = 75–80%; ABS spread inside construction debt by ~100–150bps over CMBS-equivalent.

---

## 2. Tranche engine tab (the parametric 20MW block)

Monthly columns over the asset life. Core rows:

```
REVENUE
  Contracted capacity (MW)                 = committed MW per offtake
  Take-or-pay floor revenue                = floor% × contracted MW × price        ← debt sizes on this
  Merchant/spot revenue                    = (available − contracted) MW × util × spot price
  Total revenue                            = floor + overage + merchant

OPEX
  Power                                    = IT_MW × PUE × 8760/12 × util × €/MWh
  Staff, maintenance, service, spares      = €/MW/yr ÷ 12 × MW
  Land lease / property                    = from PropCo
  EBITDA                                   = Total revenue − OPEX

CAPEX & DEPRECIATION
  Shell capex (PropCo)                     = €/W × MW   (drawn during construction)
  GPU capex (ChipCo)                       = rack count × rack price
  GPU depreciation                         = (GPU capex − residual) / useful-life months
  Shell depreciation                       = shell / (10–15 yr)

DEBT (links to Debt-sizing tab)
  PropCo infra debt: draw, interest, amort, balance
  ChipCo senior debt: draw, interest, amort, balance, DSRA
  Vendor finance: draw, interest, amort, balance
  Total debt service                       = Σ interest + scheduled amort

CASH FLOW
  CFADS (cash flow available for debt svc) = EBITDA − taxes − maintenance reserve
  DSCR                                     = CFADS / Total debt service             ← covenant ≥1.25x
  Cash to equity                           = CFADS − debt service − reserve sweeps
```

Flag cell `Platform = {GB300, VeraRubin}` switches the platform-specific assumptions.

---

## 3. Debt-sizing tab (solver per tranche)

Two independent sizings, take the binding constraint:

```
A) Advance-rate constraint
   ChipCo debt ≤ advance% × depreciable GPU cost        (CoreWeave borrowing-base mechanic)
   PropCo debt ≤ LTV% × stabilized shell value

B) DSCR constraint
   Sustainable debt service = min-period CFADS / DSCR_min (1.25x)
   → solve max debt balance given rate & tenor (PMT goal-seek)

C) Offtake-credit haircut (applied to CFADS used for sizing)
   Eligible CFADS = Meta_revenue × 100%
                  + Nebius_revenue × [70–85%]
                  + member_revenue × [0–50% unless credit-supported → up to 80%]
                  + merchant_revenue × 0%

Tranche senior debt = MIN(A, B) on haircut-eligible (C) cash flows
```

Output per tranche: senior debt €, vendor finance €, **required equity = capex − all debt**, day-1 DSCR, LTV, debt yield.

---

## 4. Recycle & refinance tab (the engine that makes €100–300M work)

```
For each tranche, at month = stabilization (12–18mo post-energization):
  Stabilized value          = stabilized EBITDA / cap rate   (or contracted-CF NPV)
  Refi/ABS proceeds         = takeout_leverage% (75–80%) × value
  Debt repaid at refi       = existing senior balance
  EQUITY RETURNED           = Refi proceeds − existing debt repaid      ← cash back to sponsors
  Redeploy                  = equity returned → funds next tranche's equity draw

Track: Cumulative equity deployed, Equity outstanding (peak), Equity recycled.
KEY OUTPUT: Peak equity outstanding  ← this is the real cash the consortium+partner must fund,
            NOT the sum of all tranche equity.
```

This tab is where you prove the consortium's **€100–300M + co-equity partner** can fund a €7–8B program: model how much each refi returns and how much the co-equity partner must bridge in the Vera Rubin phase.

---

## 5. Program roll-up tab

Place the 7 tranches on a monthly timeline (T1 GB300 → T7 Vera Rubin, per the schedule in `france_AI_factory.md`). Sum all SPV cash flows. Outputs:

- Consolidated capex draw curve, debt balance, EBITDA ramp.
- **Peak funding requirement** (the max of cumulative equity-out before recycling kicks in) — the headline number for the equity raise.
- Program-level net debt/EBITDA and weighted DSCR.
- When the co-equity partner is needed and for how much.

---

## 6. Equity-returns tab (waterfall)

```
Sources of equity: Consortium (€100–300M revolving) + Co-equity partner (from T3)
Distribution waterfall:
  1. Return of capital (pro rata)
  2. Preferred return (hurdle, e.g. 8–10%) to co-equity partner
  3. GP catch-up
  4. Carried interest / promote split to consortium (e.g. 80/20 above hurdle)

Compute: Consortium IRR & MOIC (boosted by promote + operator fees),
         Co-equity partner IRR & MOIC,
         Blended project IRR.
```

Consortium also earns **operator/management + development fees** from OpCo — model these as a separate cash line (they improve consortium returns independent of equity %).

---

## 7. Scenarios tab (the sensitivities that move the deal)

| Scenario | Lever | Range | Watch |
|---|---|---|---|
| Power | €/MWh | 55 / 70 / 85 | ~€3.8M/yr per €10/MWh at 40MW; ~€9.6M at 100MW |
| Utilization | % | 75 / 90 / 97 | bigger than PUE; drives merchant + refi value |
| GPU residual / life | yr & % | 3yr/10% (bear) … 5yr/20% (base) | hits depreciation, advance rate, refi |
| Rate | bps | ±150 | DSCR headroom |
| Offtake mix | Meta vs member vs merchant | shift weights | drives debt capacity directly |
| Delay | months | +3 / +6 | grid + allocation slip; carry cost |
| **Stress combo** | low util + high power + 3yr GPU life | — | the bear/IC downside case |

---

## 8. Outputs dashboard (IC one-look)

- Program capex, peak equity, total debt, blended cost of capital.
- Per-tranche: capex / debt / equity / day-1 DSCR / LTV.
- Consortium IRR & MOIC; co-equity IRR; blended project IRR.
- Equity-recycle chart (deployed vs outstanding vs recycled over time).
- Downside: min DSCR and equity IRR under the stress combo.

---

### Build notes
- Keep **PropCo and ChipCo as separate sub-models** inside each tranche — different lenders, tenors, rates; never blend.
- Debt is sized on the **take-or-pay floor after credit haircuts**, not on total or merchant revenue.
- The decision-useful horizon is **5 years** (the GPU refresh decision dominates year-10 economics — see `france_100MW.md`).
- Match **GPU-debt tenor to contract tenor**; fund the **refresh reserve**; bias long/cheap debt to the **shell**.
