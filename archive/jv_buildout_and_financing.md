# JV Build-Out & Financing Plan — 140MW France AI Factory

**Program:** 40MW GB300 (now) + 100MW Vera Rubin (2027+), built in **7 × 20MW tranches**, France (Dunkerque ZGI or Le Bosquel).
**Sponsor:** JV consortium — **General Intuition, Gradium, AmiLabs, Aire** — holding equity, NVIDIA allocation, site/power control, and build+operate capability in-house.
**Demand:** Captive (the four members) + anchor tenants (**Nebius, Meta**) + merchant resale as backstop.
**Equity:** €100–300M from the consortium for tranche 1, treated as **revolving downpayment capital**.
**Debt:** Senior secured GPU-backed + infrastructure debt, lead-arranged by **Morgan Stanley** (+ a French/EU bank), with vendor finance and an ABS take-out.

> All euro figures are **planning ranges** synthesized from the six research files in this folder, not vendor quotes or loan terms. They are for structuring, not for an IC vote.

---

## 1. The deal in one page

You are not financing one €7–8B project. You are financing **seven ~€1B tranches in sequence**, where each tranche:

1. is **legally ring-fenced** (its own PropCo + ChipCo SPVs, non-recourse to the others and to the four members);
2. is split into a **slow asset** (powered shell, 10–15yr life → cheap long infra debt) and a **fast asset** (GPUs, 3–5yr useful life → shorter GPU-backed debt + vendor finance);
3. is **sized for debt by the credit quality of its offtake**, not by who physically uses the chips;
4. is **refinanced once stabilized** to recycle equity into the next tranche.

The **GB300 phase (tranches 1–2) is the proof phase**: GB300 ships now, generates revenue in 2026–27, and seasons the offtake contracts and the debt structure. That track record is what makes the **Vera Rubin phase (tranches 3–7)** debt larger and cheaper, and what brings the institutional co-equity partner in at a higher valuation.

**Your €100–300M is the skin-in-the-game / promote-generating slice — not the whole equity bill.** The rest of the ~€2–2.5B cumulative equity comes from (a) refinancing proceeds recycled tranche-to-tranche, and (b) an infrastructure co-equity partner brought in once the GB300 tranches de-risk the thesis.

---

## 2. Program scope and tranche sequencing

| Tranche | Platform | Power | Indicative all-in capex | Window | Purpose |
|---|---|---:|---:|---|---|
| **T1** | GB300 NVL72 | 20MW | ~€0.8–1.15B | 2026–27 | Proof tranche. Real revenue, season offtake + debt. |
| **T2** | GB300 NVL72 | 20MW | ~€0.8–1.15B | 2027 | Complete the 40MW GB300; first refinancing demonstrated. |
| **T3** | Vera Rubin NVL72 | 20MW | ~€0.95–1.25B | 2027–28 | First Rubin; bring co-equity partner + larger MS facility. |
| **T4** | Vera Rubin NVL72 | 20MW | ~€0.95–1.25B | 2028 | |
| **T5** | Vera Rubin NVL72 | 20MW | ~€0.95–1.25B | 2028 | |
| **T6** | Vera Rubin NVL72 | 20MW | ~€0.95–1.25B | 2028–29 | |
| **T7** | Vera Rubin NVL72 | 20MW | ~€0.95–1.25B | 2029 | Completes 100MW Vera Rubin. |
| **Total** | — | **140MW** | **~€6.8–9.5B** | 2026–29 | |

**Rack / GPU planning counts per 20MW tranche** (from `estimate_chips.md` and the research):
- GB300 NVL72 @ ~132–142kW/rack → **~140–150 racks**, **~10,000–10,800 GPUs**.
- Vera Rubin NVL72 @ ~150–210kW/rack → **~95–130 racks**, **~7,000–9,000 GPUs**.

**Why GB300 first, then Vera Rubin:**
- GB300 is in production *now* → time-to-revenue is the whole point of the proof phase.
- Vera Rubin (Oberon) ramps 2027; its denser, 800VDC-era racks need a campus that's **800VDC-ready from civil day one**. Build the shell once, drop Rubin tranches into reserved electrical/cooling corridors.
- GB300 depreciates → put **shorter-tenor debt** on the GB300 ChipCos and plan the refresh/redeploy; don't over-lever a fast-aging asset.

**Campus standard:** freeze a repeatable **5MW pod → 20MW block** design (per `france_AI_factory.md`) so every tranche is a copy, not a redesign. This is what makes tranche financing repeatable and what lenders reward.

---

## 3. JV structure and governance

```
            ┌─────────────────────────────────────────────┐
            │   JV TopCo / HoldCo (the four members + later │
            │   infra co-equity partner)                    │
            │   Holds: NVIDIA allocation, brand, master     │
            │   agreements, dev team, site rights           │
            └───────────────┬───────────────────────────────┘
                            │ owns
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   ┌──────────┐       ┌──────────┐        ┌──────────┐
   │ TrancheCo│  ...  │ TrancheCo│   ...  │ TrancheCo│   (one per 20MW)
   │   T1     │       │   T3     │        │   T7     │
   │ ┌──────┐ │       │          │        │          │
   │ │PropCo│ │  powered shell → infra debt (long, cheap)
   │ ├──────┤ │
   │ │ChipCo│ │  GPUs/network/storage → GPU-backed debt + vendor finance
   │ └──────┘ │
   └────┬─────┘
        │ rents shell + leases chips to
        ▼
   ┌──────────────────────────────────────────────┐
   │ OpCo (operator)                                │
   │ Signs offtake: Meta/Nebius take-or-pay,        │
   │ intercompany with members, merchant spot.      │
   │ Collects revenue; pays SPVs.                   │
   └──────────────────────────────────────────────┘
```

**Why this shape:**
- **TopCo** keeps the crown jewels — the NVIDIA allocation and site rights — at the consortium level, so they're never trapped in a single financed SPV and you keep negotiating leverage with every counterparty.
- **PropCo / ChipCo split per tranche** is what lets you put 10–15yr infra debt on the building and 3–5yr GPU debt on the silicon — different lenders, different tenors, different cost. Mixing them is the most common way sponsors leave money on the table.
- **Ring-fencing** makes each tranche non-recourse: a problem in T4 can't default T1 or reach the members' balance sheets. Lenders require this; it's also what lets you sell/refinance one tranche without touching the rest.
- **OpCo** is the single revenue face. Critically, it signs **arm's-length take-or-pay contracts even with your own members** — that's what makes captive demand *bankable* rather than just an internal cost transfer.

**Governance among the four members (do this early, it's the thing that kills consortiums):**
- **Capacity allocation:** each member reserves a committed MW block via an internal take-or-pay, priced at arm's length. Reserved-but-unused capacity flows to merchant/anchor — so utilization stays high and contracts stay bankable.
- **Cash calls & dilution:** pre-agree the equity contribution mechanism and a default/dilution regime per tranche, so one member's funding gap doesn't stall a tranche.
- **Decision rights:** allocation, vendor selection, and offtake pricing need a clear board + supermajority map. Reserved matters (taking on debt, admitting the co-equity partner) protect minority members.
- **VC backers' role:** the members are VC-backed labs. Get the backers' position early — they may provide **equity into TopCo** and/or **credit support** behind their portfolio company's intercompany offtake, which directly increases debt capacity (see §8).

---

## 4. Partners to bring in

You have the four capabilities internally, so the partner roster is **financial + commercial + supply + advisory**, not capability-filling.

| Layer | Partner type | Specific candidates | What they do | When |
|---|---|---|---|---|
| **Lead debt arranger** | Investment bank / structuring agent | **Morgan Stanley** (lead), + JPMorgan / Goldman as syndicate; **a French/EU bank** — SocGen, BNP Paribas, Crédit Agricole CIB, or MUFG — for the local infra tranche | Structure + underwrite the senior secured facility; warehouse/bridge GPU deposits; arrange the ABS take-out | Mandate before T1 FID |
| **GPU / asset private credit** | Direct-lending funds | Blackstone, Blue Owl, Carlyle, Magnetar, PIMCO, Ares | Buy/hold the GPU-backed debt the bank originates; provide delayed-draw term loans per tranche | T1–T2 |
| **Vendor finance** | OEM/ODM + NVIDIA | NVIDIA (backstop), HPE Financial Services, Dell Financial, Supermicro; ODM Wiwynn/QCT/Foxconn | Deferred payment / lease lines on 10–20% of hardware; NVIDIA backstop strengthens the whole stack | Each tranche |
| **Co-equity (the big one)** | Infrastructure / sovereign | Infra funds: Brookfield, DigitalBridge, Antin, KKR, EQT. **France/EU public**: Bpifrance, Caisse des Dépôts, an IPCEI / France-2030 vehicle; sovereign: MGX/Mubadala | Fund the bulk of cumulative equity for the €5B+ Vera Rubin phase; you keep GP/operator + promote | Brought in *after* GB300 proof (T3) |
| **Anchor offtake** | Tenants | **Meta** (investment-grade → cheapest debt), **Nebius** (NeoCloud — anchor *and* possible merchant-resale/operating partner) | Take-or-pay contracts that the senior debt is sized against | LOIs *before* T1 debt close |
| **Site / power** | Landowner + grid | Grand Port Maritime de Dunkerque or CC2SO (Le Bosquel); **RTE** (400kV fast-track) | Land exclusivity, grid connection, tranche-phased energization | Now |
| **Build** | EPC + cooling + electrical | CAP INGELEC / Eiffage / Bouygues / Equans; Schneider / Vertiv / CoolIT; Omexom for HV | Deliver the standardized 20MW block 800VDC-ready | RFP now (see `vendor_strategy_100MW.md`) |
| **Advisory** | Legal / technical / tax | Project-finance counsel (Clifford Chance, Linklaters, A&O Shearman — Paris infra teams); owner's engineer; Big 4 for model, French tax, EU state-aid/IPCEI | Bankable docs, SPV/tax structuring, lender's technical advisor | Pre-FID |

**The two partners that gate everything:**
1. **The anchor tenant LOI (Meta and/or Nebius).** No anchor → debt collapses to merchant terms (more equity, higher rate). This is the highest-leverage thing to lock first.
2. **The lead arranger (Morgan Stanley).** Mandate them early so the capital stack, covenants, and the warehouse line are designed *before* you commit capex, not after.

---

## 5. The capital stack — "downpayment + debt"

Take a representative **€1.0B 20MW tranche** and split it the way the lenders will:

### PropCo — the powered shell (~€220M, slow asset)
| Layer | % | € | Notes |
|---|---:|---:|---|
| Infra / project debt | 65% | ~€143M | 10–15yr, ~5–7%, secured on shell + long lease/PPA. Cheapest money in the stack. |
| Equity | 35% | ~€77M | Recyclable via infra refinance once leased. |

### ChipCo — the GPUs/network/storage (~€780M, fast asset)
| Layer | % | € | Notes |
|---|---:|---:|---|
| Senior secured GPU-backed debt (Morgan Stanley-led) | ~55% | ~€430M | 3–5yr, SOFR/EURIBOR + ~4–7%, sized on **contracted** offtake (DSCR), collateralized by chips + receivables. |
| Vendor finance / lease (NVIDIA / OEM) | ~20% | ~€155M | Deferred payment or lease; NVIDIA backstop lowers cost across the whole stack. |
| Equity | ~25% | ~€195M | First-loss; recycled at refi/ABS. |

### Blended tranche
| | € | % |
|---|---:|---:|
| **Total equity (your "downpayment")** | **~€272M** | **~27%** |
| Total debt + vendor finance | ~€728M | ~73% |
| **Tranche** | **~€1.0B** | 100% |

### Why your €100–300M still funds a €7–8B program — the revolving-equity engine
You do **not** stack €272M × 7 = €1.9B of fresh equity. Each tranche, once **built + contracted + stabilized** (12–18 months of offtake history), is **refinanced**:
- the GPU-backed debt is **upsized** against now-seasoned cash flows, and/or
- the tranche is taken out into a **data-center / GPU ABS** (Morgan Stanley arranges these),

returning a chunk of the equity (realistically ~€100–150M of the ~€272M) to **redeploy into the next tranche**. Combined with the infra co-equity partner who funds the *bulk* of equity for the Vera Rubin phase, your **€100–300M behaves like a revolving fund** — it's the control/promote slice that cycles, not the total bill.

```
T1 equity ─build─stabilize─► REFINANCE ─returns equity─► T2 equity ─► … 
   €272M                          ↑                          
                          + co-equity partner from T3 onward
                          + ABS take-out recycles further
```

---

## 6. The "downpayment" — defined precisely

"Downpayment" splits into **three cash needs**, in order of when you pay them:

| # | Component | Size (tranche 1) | Source | Notes |
|---|---|---:|---|---|
| 1 | **Pre-FID development capital** | ~€15–30M | Consortium, now | Site exclusivity + RTE deposit, FEED/owner's engineer, legal, financial model, EPC RFP. Small but must come first and is at-risk. |
| 2 | **GPU deposit / prepayment to NVIDIA/OEM** | ~10–25% of GPU cost ≈ **€70–175M** | Equity, then refinanced on delivery | Secures the allocation slot. With confirmed allocation + a financing commitment, push for a *smaller* deposit or have the bank's **warehouse line fund it** against delivery. |
| 3 | **Equity draw into the SPV at FID** | balance of the ~€272M tranche equity | Consortium (+ co-investor) | Funds construction alongside debt drawdowns. |

**So the real upfront cash gate for tranche 1 is roughly €85–200M** (items 1 + 2, before senior debt fully funds), inside a total tranche-1 equity of ~€272M that you then work to recycle. **That fits your €100–300M** — but it consumes most of it on T1, which is exactly why T2 onward must lean on refinancing proceeds and the co-equity partner.

**Two levers to shrink the downpayment:**
- **NVIDIA/OEM vendor finance + backstop** reduces the deposit and the equity you must sink into silicon.
- **A bank warehouse / bridge facility** (ask Morgan Stanley for it in the mandate) funds the GPU deposit and construction, converting to the term loan at energization — so your equity isn't tied up in undelivered chips.

---

## 7. The debt plan and Morgan Stanley's role

**Morgan Stanley = lead structuring agent + arranger**, doing four jobs across the program:

1. **Senior secured facility (per tranche).** A **delayed-draw term loan** that funds each 20MW tranche as it's built, secured on the GPUs + the offtake receivables. Sized by **DSCR against contracted cash flows** (not gross capacity). Indicative: advance rate **60–75%** of contracted EBITDA, **3–5yr** tenor on GPU debt matched to contract + refresh, cash sweep, reserve accounts, GPU-refresh reserve.
2. **Warehouse / bridge.** Funds GPU deposits and construction before the term debt converts — keeps your equity out of undelivered hardware.
3. **ABS / securitization take-out.** Once tranches season, refinance the GPU debt into a **data-center/GPU ABS**. This is the equity-recycling exit and lets you scale into the Vera Rubin phase without proportional fresh equity.
4. **Syndication.** Distribute to the private-credit funds (Blackstone, Blue Owl, Carlyle, Magnetar, PIMCO) and co-arrange the infra tranche with a French/EU bank.

**Full debt menu** (from `france_100MW.md` / `vera_rubin_france_100MW.md`):

| Instrument | Rate (modeled) | Secured on | Role |
|---|---|---|---|
| Senior secured GPU-backed (MS-led) | ~SOFR/EURIBOR + 4–7% | GPUs + offtake receivables | The big lever |
| Infra / project debt (PropCo) | ~5.0–7.5% | Powered shell + long lease/PPA | Cheap, long, on the building |
| Vendor finance / lease | ~6–9% | The hardware itself | Fills 10–20%; NVIDIA backstop |
| Green / sustainability-linked | ~4.5–6.5% | As above + heat-reuse/low-carbon | France's low-carbon grid + heat reuse makes this real, not greenwash |
| Mezzanine (gap filler) | ~9–13% | Structurally subordinated | Only if needed to top up |

**Offtake → debt mapping (the core underwriting logic):** senior debt is sized against the *weighted credit of the contracted offtake*, so route contracts deliberately:

| Offtake source | Credit | Debt it supports |
|---|---|---|
| **Meta** take-or-pay | Investment-grade | **Largest, cheapest** senior debt — anchor the biggest tranches on Meta |
| **Nebius** contract | Strong NeoCloud | Supports senior debt at a spread |
| **JV members** (General Intuition, Gradium, AmiLabs, Aire) | VC-backed, sub-IG | Lenders haircut heavily — back with member equity and/or **VC-backer credit support** to make it count |
| **Merchant** resale | None contracted | **Sized at zero** for debt; pure equity upside |

**Practical sequencing:** anchor the senior debt of each tranche on **Meta/Nebius take-or-pay**; use **captive member demand** to fill utilization (funded with more equity/vendor finance); keep **merchant** as upside the equity captures.

---

## 8. Offtake & credit strategy

Your mixed demand is a strength *if* you contract it in the right order:

1. **Lock anchor LOIs before debt close.** A Meta or Nebius take-or-pay LOI is the gating document for the senior facility. Prioritize Meta for the IG credit; Nebius can double as **operating/merchant-resale partner** for surplus capacity.
2. **Make captive demand bankable.** Each member signs an **arm's-length intercompany take-or-pay** with OpCo. Then ask their **VC backers** to stand behind it (parent guarantee, prepay, or equity into TopCo). VC-backed offtake that's *credit-supported* converts from "lenders ignore it" to "lenders count it."
3. **Layer the merchant book on top.** Nebius (or your own OpCo) resells uncontracted hours. Don't promise it to lenders; let it accrue to equity returns and improve refinancing metrics.
4. **Diversify anchor concentration.** Over the program, don't let one tenant dominate — spread across Meta, Nebius, members, and merchant so a single counterparty's downgrade doesn't impair the debt.

---

## 9. How we get started — first ~180 days

**Phase 0 (weeks 0–6) — form and mandate**
- [ ] Stand up **TopCo** + the **T1 PropCo/ChipCo SPVs**; sign the four-member JV agreement (capacity allocation, cash calls, governance, dilution).
- [ ] Get the **VC backers' position** on equity into TopCo and credit support for member offtake.
- [ ] **Mandate Morgan Stanley** as lead arranger + a French/EU bank for the infra tranche; scope the warehouse/bridge line in the mandate.
- [ ] Engage project-finance counsel + owner's engineer + Big-4 model/tax.

**Phase 1 (weeks 4–12) — lock the gating items**
- [ ] Convert **Meta / Nebius** interest into **take-or-pay LOIs / term sheets** (the debt gate).
- [ ] Sign **site exclusivity** at Dunkerque ZGI or Le Bosquel; open the **RTE** tranche-phasing dialogue and pay the connection deposit (`france_100MW_locations.md` has the contacts).
- [ ] Confirm **GB300 allocation** for T1 with NVIDIA; negotiate the **deposit** down against allocation + financing commitment.
- [ ] Issue the **EPC RFP** for the standardized 20MW, 800VDC-ready block (shortlist in `vendor_strategy_100MW.md`).

**Phase 2 (weeks 10–20) — structure the money**
- [ ] Build the **bankable financial model** + information memorandum (per-tranche, with the refinancing/recycle engine modeled).
- [ ] Morgan Stanley structures the **senior facility + warehouse**; circulate to private-credit syndicate.
- [ ] Negotiate **NVIDIA/OEM vendor finance** and backstop.
- [ ] Close the **consortium equity** (€100–300M) for T1; begin diligence with the **infra co-equity partner** for the Vera Rubin phase (don't need them for T1, but start now so they're ready for T3).

**Phase 3 (weeks 16–26) — FID tranche 1**
- [ ] **Final investment decision on T1.** Fund development capital + GPU deposit; sign EPC; first debt drawdown via warehouse.
- [ ] Freeze the campus standard so T2–T7 are copies.

**Milestone:** T1 (GB300) energized → first revenue → first refinancing → recycle equity into T2. That cycle, demonstrated twice on GB300, is what unlocks the co-equity partner and the larger Vera Rubin debt.

---

## 10. Risks and mitigants

| Risk | Mitigant |
|---|---|
| **No anchor LOI** → debt collapses to merchant terms | Lock Meta/Nebius take-or-pay *before* FID; treat as gating |
| **GPU obsolescence / depreciation** (esp. GB300) | Short-tenor GPU debt matched to contract; refresh reserve; campus 800VDC-ready for Rubin |
| **Equity runs out before the program scales** | Revolving-equity engine (refinance + ABS) + infra co-equity partner from T3 |
| **Anchor concentration** | Diversify across Meta / Nebius / members / merchant over the program |
| **Captive offtake not bankable** (members are sub-IG) | Arm's-length intercompany contracts + VC-backer credit support / parent guarantees |
| **RTE / grid timing slips** | Dunkerque/Bosquel fast-track phasing; provisional 30–40MW starter feed at Dunkerque; tranche to the energization schedule |
| **Tech transition GB300→Rubin** | 800VDC-ready shell day one; reserved Rubin corridors; phase, don't cliff-edge |
| **French/EU regulatory** (state aid, heat-reuse, ICPE) | IPCEI / France-2030 alignment; heat-reuse designed in (also unlocks green debt); early DREAL/prefecture dialogue |
| **Member default on a cash call** | Pre-agreed dilution/default regime in the JV agreement |

---

## 11. Key numbers (planning ranges)

| Metric | GB300 (per 20MW) | Vera Rubin (per 20MW) | 140MW program |
|---|---|---|---|
| All-in capex | €0.8–1.15B | €0.95–1.25B | ~€6.8–9.5B |
| Racks | ~140–150 | ~95–130 | — |
| GPUs | ~10,000–10,800 | ~7,000–9,000 | ~60,000–75,000 |
| Powered shell | ~€220M (€10–12/W) | ~€220M | ~€1.5B |
| Equity per tranche (~27%) | ~€220–310M | ~€260–340M | ~€2.0–2.5B cumulative (recycled) |
| Upfront cash gate (dev + GPU deposit) | ~€85–200M | ~€90–220M | — |
| Annual power @ €70/MWh, PUE 1.15 | ~€11–14M | ~€11–14M | ~€55–70M @ 100MW+ |

> Sources: `estimate_chips.md`, `france_100MW.md`, `france_AI_factory.md`, `vera_rubin_france_100MW.md`, `vendor_strategy_100MW.md`, `france_100MW_locations.md`. Replace every range with LOIs, RTE offers, NVIDIA allocation terms, EPC bids, and lender term sheets before any IC decision.
