# Project Ampère — Compute Cooperative
## Member cost schedule, assumptions, options & next steps

**Confidential · For discussion · Assumptions as of 14 July 2026**
Companions: `project_ampere.html` (one-pager) · `project_ampere_cost_model.csv` (monthly engine, scenarios, sensitivities). All three are generated from one canonical assumption set; every headline reconciles to the CSV. **To recompute after changing any assumption:** edit the parameters at the top of `scripts/generate_cost_model.py` and run `python3 scripts/generate_cost_model.py` — it rewrites the CSV and re-injects the monthly table into the HTML in one pass.

**Scope.** This is a **member cost schedule**: the outbound funding and running costs borne by one member for its ⅓ of the program. It contains no revenue, utilization income, or project IRR — internal transfer pricing is cost-recovery by construction, so any coverage ratio computed from it would be circular. Financeability is addressed separately (§7) on the basis of actual member payment contracts plus credit support.

---

## 1. The concept

Three AI labs ("members") form a joint venture to build the compute they train on, at cost. Each member takes an **equal ⅓ sleeve of every tranche** and commits to it through a **two-leg take-or-pay**: a reserved-capacity fee payable irrespective of usage (the leg debt is underwritten on) plus a usage-linked leg (metered power and variable costs). Members are venture-backed, so their commitments are hardened with **backer credit support** (letters of credit, guarantees, or prepaid reserves).

**Entities.** A shared **TopCo** holds the NVIDIA relationship, site rights and master agreements. Each tranche is ring-fenced: a shared **PropCo** owns land and buildings (cost-split ⅓, financed separately), and each member's GPUs sit in its own **ChipCo sleeve** with its own financing — one member's difficulty never touches another's sleeve. An **OpCo** operates the estate and bills members at cost-plus.

**Governance hard points** (lenders read these before pricing): cash-call cure periods and dilution mechanics; no cross-default between sleeves; transfer restrictions with ROFR and a buy-sell (shotgun) to break 2-of-3 deadlocks; insolvency step-in with automatic capacity re-marketing; overuse/underuse rules between sleeves; per-sleeve refresh authority within campus-level power and cooling coordination.

---

## 2. The program

**Firm program: T1–T5, ~102MW IT nameplate, ~$5.0B.** T6–T7 are **unpriced options** — Rubin Ultra or the then-best platform, priced only after NVIDIA specification freeze and vendor quotes. **No T1–T7 total exists.**

| Tranche | Platform | Siting | Status | Constr. | Buyout | **Online** | All-in / tranche |
|---|---|---|---|---|---|---|---:|
| T1 | GB300 NVL72 | existing colo | Commit-grade | — | m0 | **m6** | ~$0.80B |
| T2 | GB300 NVL72 | existing colo | Commit-grade | — | m6 | m12 | ~$0.80B |
| T3 | Rubin NVL72 | own campus* | Provisional | m0–m21 | m15 | m21 | ~$1.15B |
| T4 | Rubin NVL72 | own campus | Provisional | m6–m27 | m21 | m27 | ~$1.15B |
| T5 | Rubin NVL72 | own campus | Provisional | m12–m33 | m27 | **m33** | ~$1.15B |
| T6–T7 | TBD at spec freeze | own campus | **Options** | TBD | TBD | TBD | unpriced |

*T3 siting is an open decision — see §6.

**Timing scenarios.** GB300 order-to-live: **6 months base** (16 weeks only if liquid-cooled colo and allocated, integrated systems are all ready; 8–10 months downside with self-procured components or facility retrofit). Rubin construction: **21 months modelled** (the accelerated end, defensible only on a pre-de-risked fast-track site with early long-lead orders and prefabricated MEP); **22–24 months standard; 30–36 downside** (grid, permitting, transformer/switchgear delay). A 22–24-month base shifts T3 to ~m24 and T5 to ~m36. "Buyout" is a simplification for deposit → progress payments → delivery → acceptance; debt draws should ultimately match eligible invoices.

---

## 3. Physical configuration & compute accounting

| | GB300 NVL72 | Vera Rubin NVL72 |
|---|---|---|
| Racks (member / tranche) | 48 / 144 | 30 / 90 |
| GPU packages (member) | 3,456 | 2,160 |
| kW/rack · tranche nameplate | 142 · 20.45 MW | 227 MaxP · 20.43 MW (MaxQ 187 scenario) |
| **Dense FP8** per rack / member | 360 PF / **17.28 EF** | 1,260 PF / **37.80 EF** |

**Conventions (disclosed, consistently applied):** GPUs are counted as **physical packages**. Performance is **dense FP8** — GB300's published 720 PF/rack is a with-sparsity figure, halved to 360 PF dense; Rubin's 1,260 PF is dense. FP4/marketing flops are not used. Cross-generation ratios: **3.50× per GPU; ~2.19× per MW** ((1260/227)/(360/142)). "**Normalized GB300-Watt**" = watts of GB300 delivering equal dense FP8 (baseline 2.535 EF/MW-IT); Rubin = ×2.19 per actual watt. All unit costs state their denominator; headlines use **90% billed availability** (the CSV's cumulative columns are labelled 100%-hours).

---

## 4. Cost assumptions — with status labels and brackets

Nothing below is an executed quote. Status: **[EST]** street/benchmark estimate · **[ASM]** management assumption · **[QP]** quote-pending.

### 4.1 GB300 ChipCo — $266.0M/member [QP], band $244–294M
Bottom-up build: 48 × **$4.0M rack** [EST — top of the Loop Capital street band $3.7–4.0M, derived from a reported ~$1B/250-rack order; set at band top as memory-inflation buffer; a weakly-sourced $6–6.5M "inference-optimized" configuration tail exists] = $192M, **+ fabric/storage/spares $38.4M** [ASM — training-grade fat-tree + storage tier], **+ deployment $35.6M** (year-1 software/support ~$8.4M; freight ~$1.7M; installation & acceptance ~$5.3M; VAT working-capital carry ~$2.6M; ~7% contingency ~$17.6M) [ASM] = **$5.54M/rack fully loaded**. Replace with an OEM bill of materials and quote (§10).

### 4.2 Rubin ChipCo — $293.3M/member conservative [QP], low case $234M
Conservative complete case: 30 × $8.5M × 1.15. A public report of ~$7.8M per *configured system* (memory/storage included) gives the $234M low case — the 15% must not be stacked on top of it. The Rubin quote is the **single biggest open number** in the program (~$180M/member swing across three sleeves).

### 4.3 PropCo — $267.5M/block [EST], range $260–275M
From the Turner & Townsend Paris benchmark ($10.8/W air-cooled) + 7–10% liquid-cooling premium + grid allowance + owner costs the index excludes (land, fees, utility works). Member share $89.2M/block, drawn as equity over construction (linear simplification; milestone/S-curve draws are a modelling backlog item). Built for T3–T5 only — GB300 rents. Grid spend to be split campus-common vs per-block by engineering study; **no RTE connection is assumed until an executed offer exists**.

### 4.4 Colocation (GB300) — $130/kW-mo [ASM], sensitivity 130/155/180
Billed on **⅓ of a contractual 20MW reservation** (6,667 kW → $0.867M/mo/member), a documented choice vs the 6,816 kW installed nameplate. $130 is an unquoted low case in a constrained European market; moving to $180 adds ~$20M per GB300 sleeve over five years. The colo term sheet must pin what the fee includes (remote hands, security) and **who furnishes sidecar CDUs** (~$2–5M/sleeve if the tenant).

### 4.5 Energy
Formula: IT nameplate × PUE 1.20 × **90% electrical load factor** (a distinct concept from billed availability) × **€90/MWh all-in delivered** [ASM — €70 commodity is *not* an all-in price; TURPE, levies, capacity and hedge cost to be bridged at PPA term sheet; scenarios €70/€90/€110] × **$1.143/€** (ECB reference). At the member's ~13.6MW GB300+Rubin steady state this is ~$1.1M/month per live sleeve.

### 4.6 Operating costs [ASM — test against vendor-support and colo-service inclusions]
Chip maintenance/support 2.5%/yr of ChipCo; owned-campus staff $0.13M/mo + security $0.028M/mo per sleeve; colo cluster-ops $0.05M/mo; PropCo owning cost 3%/yr of share (property tax, insurance, facility maintenance). Flagged as not yet modelled: insurance, network transit, decommissioning, refresh-migration overlap.

### 4.7 Refresh reserve & residuals
**Refresh reserve:** 8.75%/yr of ChipCo capex, funded monthly from each sleeve's online+12 through online+60 into **restricted cash** — a funding movement, not an expense; excluded from cost totals (memo columns in the CSV). Accumulates ≈ **$494M/member** over four years ≈ 35% replacement equity for the year-5/6 refresh. **Residuals (memo, not netted):** chips 10% (sensitivities 0/5/10/15%); buildings retain ~12 of 15 years' life at schedule end — terminal treatment (re-lease to refreshed fleet / sale / refinance) is an explicit follow-on modelling item, not an omission.

---

## 5. Outputs (from the cost model)

| Per member | GB300 sleeve | Rubin sleeve | **Firm T1–T5** |
|---|---:|---:|---:|
| Capex (all-in) | $266.0M | $382.5M | **$1,679M** |
| — equity (37%) | $98M | $142M | **$622M** |
| — debt (63%) | $168M | $240.5M | $1,057M |
| Interest (9.5% / 8.5%, 5yr) | $43.7M | $55.6M | $254M |
| Operating (5yr) | $121.4M | $92.7M | $521M |
| **5-yr all-in cost** | **$431M** | **$531M** | **$2,454M** |
| $/GPU-hr @90% | $3.16 | $6.23 | — |
| $/GB300-equiv-hr @90% | $3.16 | **$1.78** | **$2.10** |
| $/PFLOPS-hr dense FP8 @90% | $0.633 | $0.356 | **$0.421** |
| $/normalized-GB300-W/month | $1.05 | $0.59 | **$0.70** |

**JV totals (×3):** firm capex **~$5.0B**; 5-yr total **~$7.4B**; **444 EF** dense FP8; 40,176 GPU packages. **Year-one member cash ≈ $0.34B.** Peak single month: T3 buyout (m15, ~$77M). Merchant reference for GB300-class reserved capacity is ~$5–8/GPU-hr — the cooperative runs at roughly **⅓ of merchant** even on conservative assumptions.

---

## 6. Open decision: T3 in colo vs owned campus

Bringing T3 online at ~m18 instead of m21 is achievable by siting it in **Rubin-ready colo** (as T1–T2) rather than waiting for the first campus block:

| Per member, T3 sleeve | Owned (base) | Colo @$130 | @$155 | @$180 |
|---|---:|---:|---:|---:|
| Capex / equity | $382.5M / $142M | $293.3M / $109M | — | — |
| 5-yr all-in cash | $530.7M | **$460.7M** | $470.7M | $480.7M |
| Economic view (owned netted of ~⅔ building residual) | ~$471M | $461M | $471M | $481M |
| Compute available | m21 | **~m18** | ~m18 | ~m18 |

**Read:** colo wins the 5-year cash view ($50–70M/member) and delivers compute a quarter earlier (~10.9M GB300-equiv hours/member — worth $55–85M at merchant rates if the training roadmap consumes it); economically it is a wash at ~$155/kW-mo; **owning wins from the second hardware generation** (refresh-in-place facility cost ~$13M per 5-yr term vs $52–72M of colo fees). Recommended posture: **colo-bridge T3 if a Rubin-grade term sheet materializes; campus carries T4/T5 and the T3 refresh lands there at gen-2.** Decision gate: a real term sheet for ~20MW of 187–227kW/rack liquid-cooled capacity — **scarcity, not price, is the binding constraint** in Europe today; $130 is optimistic for 227kW racks. Alternatives if colo fails: brownfield/powered-shell retrofit (~12–15 months fit-out on sites with legacy grid), or greenfield compression to 18–19 months (requires simultaneously: pre-permitted site, provisional power, long-leads ordered at FID, prefab MEP, overlapped commissioning — ~+5–10% block cost, fragile).

---

## 7. Financing

**Working case (simplified):** **37% member equity deposit / 63% single five-year amortizing facility** per sleeve — **9.5%** first close (GB300), **8.5%** once seasoned (Rubin). **Detailed alternative for term-sheet stage:** **35% equity / 42% senior GPU debt / 23% vendor finance**, with separate margins, tenors, draw timing, security and intercreditor terms — the senior and vendor instruments are not economically identical and must be split before documentation. PropCo is financed **separately** (construction ~40/60 and stabilized ~35/65 planning cases; currently modelled as member equity during construction — a conservative simplification). Stated plainly for transparency: with sleeve debt attributed to chips, **Rubin chip-level leverage is ~82%** — the split stack plus separate PropCo debt is the clean fix.

**Not yet modelled (placeholders):** upfront/OID and commitment fees, interest during construction, DSRA funding, rate hedging, refinancing costs. **Market benchmarks** (public record; contract-specific, not a curve): CoreWeave's March-2026 $8.5B facility priced at SOFR+2.25% with contract-specific A3/A(low) ratings *after* years of seasoning on investment-grade offtake — its May-2026 $3.1B facility priced at SOFR+4.50% a month later; CoreWeave's 2023 first-close debt cost ~14–15%. Stabilized European data-centre ABS (Vantage's €640M EMEA transaction) demonstrates the PropCo take-out route, but on fully-occupied, long-lease assets — an 18–24-month-plus path here, PropCo only.

**Financeability** rests on the two-leg take-or-pay plus **backer credit support**, evidenced by actual contracted payment schedules — not on cost-plus coverage arithmetic. That analysis belongs in a financing appendix once contracts are papered.

**Funding options & levers** (base = member equity + sleeve debt; everything else improves it): sovereign/EU public capital (up to ~17% of eligible capex under EU AI-infrastructure programs — **zero in the base**, underwrite on award only); NVIDIA/OEM vendor finance and capacity backstop (powerful but priced strategic capital — cf. the $6.3B CoreWeave backstop); sale-leaseback or infra co-equity at PropCo (Meta–Blue Owl 80/20 template); euro ABS take-out on stabilized PropCo; member-level convertibles; forward capacity pre-sale to an external anchor with 15–25% prepay (pure upside, not required).

---

## 8. Subsidies & public capital — upside only, zero in the base case

**Posture:** the base schedule carries **no subsidy**. Public money is underwritten only on an executed award or term sheet, after review of conditions (clawback, open-access/ecosystem obligations, localization, reporting). Award timing (~2027 for the flagship program) means subsidies de-pressure later funding rounds, not the first close.

| Source | Type | Realistic size for the JV | Status / timing |
|---|---|---|---|
| **EuroHPC "AI Gigafactories" (InvestAI, €20B)** | Capex grant — **17% of eligible computing-infrastructure capex** | **$600–850M** on the firm ~$5.0B program (eligibility scope to confirm) | Formal call **summer 2026** (info session held 16 Jun 2026); 77 EOIs across 16 member states / 60 sites already filed |
| **EIB / InvestEU** | Co-lending, guarantees, venture-debt instruments | Cheapens the ~$3.2B JV debt stack by ~100–200bps; can substitute part of backer credit support | Ongoing; explicit crowding-in role in InvestAI |
| **Bpifrance** (€10B AI envelope to 2029) | Equity co-investment, loans, guarantees | $100–300M+ (TopCo minority and/or PropCo co-invest) | Open; direct precedent — Bpifrance is an equity partner in the Campus AI JV |
| **Caisse des Dépôts (CDC)** | Long-duration infrastructure equity | PropCo co-investor scale | Open; pairs with Bpifrance track |
| **ADEME + CEE + reduced electricity excise** | Efficiency/heat-reuse grants, energy-savings certificates, tax relief | €20–60M over the program | Site-dependent; apply at permitting; requires heat-reuse/efficiency commitments (campus is designed for them) |
| **Regional investment aid (GBER)** | Regional grant | Site-dependent | Check once site exclusivity lands |
| **IPCEI** (cloud/AI infrastructure) | State-aid clearance enabling larger national funding | Enabler, not a check | 12–24 months; politically driven — monitor via DGE |

### EuroHPC AI Gigafactory — how to participate

**What it takes:** an EU-based consortium with **member-state backing**, ~65–70% private funding, and gigafactory-class ambition (~100k-GPU scale). Our firm program (40k packages) is sub-scale alone; the options and campus expansion headroom close the gap, or we enter someone else's bid. A French consortium has already bid ~$10B, and the Campus AI (Bpifrance/MGX) project is incumbent — competition and partnership dynamics in one.

**Next steps (this quarter):**
1. **Obtain the call documents on publication day** (EuroHPC JU) and map eligibility scope against our capex lines — what fraction of the $5.0B counts as "computing infrastructure."
2. **Standalone-vs-join decision memo within ~4 weeks of the call:** take meetings with the existing French bidders (anchor-offtaker/co-investor entry) and score both paths on probability, timeline, and conditions. *This decision gates the rest of the list.*
3. **Secure the member-state letter** — France 2030 / DGE backing is a hard requirement; open via the Bpifrance/CDC track below.
4. **Assemble the bid pack** — consortium description, site + grid plan, financing plan, open-access approach; ~80% already exists in this data room.
5. **Legal review of award conditions** (open-access/ecosystem obligations vs our captive-cooperative model; clawback triggers) *before* committing.

### Bpifrance / CDC — how to participate

1. **Entry point:** DGE / France 2030 secretariat + Bpifrance (Large Venture and infrastructure teams), presented with this pack — the ask is a **PropCo co-investment and/or TopCo minority**, mirroring Bpifrance's Campus AI position. CDC in the same meeting cycle for long-duration PropCo equity.
2. **Channel:** the Choose France track gives the political wrapper; the sovereign-AI, three-French-lab framing is precisely the profile these vehicles exist to fund.
3. **Deliverable to target:** a term sheet (equity amount, governance rights, co-investment conditions) — which then doubles as the member-state backing evidence for the EuroHPC bid (step 3 above).
4. **In parallel:** EIB conversation alongside the bank mandate (guarantee/co-lending sizing on the sleeve debt), and ADEME/CEE/excise applications keyed to the permitting calendar once the site is set.

## 9. Sensitivities (brackets the model carries)

| Driver | Low / Base / High | ~Impact per member |
|---|---|---|
| GB300 ChipCo | $244 / **266** / 294M | ∓$44M / +$56M capex |
| Rubin ChipCo | $234 / **293**M | −$178M capex (largest single swing) |
| PropCo block | $260 / **267.5** / 275M | ∓$2.5M per block share |
| Colo rate | $130 / 155 / 180 per kW-mo | +$10M / +$20M per GB300 sleeve (5yr) |
| Energy (all-in) | €70 / **90** / 110 per MWh | ∓22% of energy line |
| FX | 1.05 / **1.143** / 1.25 $/€ | −8% / +9% on €-denominated opex |
| Rates | working 9.5→8.5% | ±150bps ≈ ±$8M/sleeve interest |
| Construction | 21 / 24 / 33 months | +3–12mo compute delay + idle debt service |
| Chip residual | 0 / 5 / **10** / 15% | memo ±$29M/sleeve at exit |
| Refresh reserve | 0 / **8.75** / 12%/yr | restricted-cash pacing |

---

## 10. Risks & downside cases

**Platform risk** — Rubin re-priced at spec freeze; T6–T7 unpriced by design; a Rubin slip extends GB300 sleeves and forces merchant buy-in for unserved growth. **Construction** — standard-case (22–24mo) shifts the fleet right by ~3 months; GPUs are not bought until online−6, so slips cost time, not stranded silicon. **Colo scarcity/repricing** — the GB300 phase's main opex exposure; mitigate with a 5-year term and a campus-migration option. **Member distress** — sleeve isolation, several (not joint) guarantees, buy-sell, lender step-in, capacity re-marketing. **Energy** — French nuclear-era supply is a good starting point, not a cheap-power guarantee; hedge/procurement strategy required. **FX** — €/$ on all European opex; hedge assumption to be set. **Concentration** — three correlated AI labs; backer credit support and any external anchor reduce it.

---

## 11. Research base (public sources)

Hardware & specs: NVIDIA GB300 NVL72 and Vera Rubin NVL72 product disclosures (dense-FP8 basis; NVL72 package-counting convention); ASUS Vera Rubin power disclosure (227kW MaxP / 187kW MaxQ); NVIDIA enterprise reference architecture (142kW GB300 rack). Pricing: Loop Capital GB300 street band (via reported ~$1B/250-rack order); Tom's Hardware reporting on configured Rubin system costs (~$7.8M, memory-driven) and rack-price inflation. Build costs: Turner & Townsend Data Centre Cost Index (Paris $10.8/W; liquid premium; methodology exclusions); CBRE data-centre market reports (colo rates, vacancy). Financing precedents: CoreWeave SEC filings (facility terms, GPU borrowing-base mechanics, SPV security, take-or-pay underwriting); Meta–Blue Owl "Hyperion" JV ($27.3B bond, 6.581%, A+, residual-value guarantee); Vantage EMEA €640M ABS (Scope/S&P-rated); NVIDIA–CoreWeave $6.3B capacity backstop; Nebius–Microsoft take-or-pay ("irrespective of actual usage or consumption" — SEC-filed contract language). Macro/energy: ECB reference FX; French post-ARENH nuclear pricing framework (CAPN). Public capital: EU AI-infrastructure funding regulation (17% capex contribution), European Commission AI Gigafactories pages, EuroHPC JU gigafactory FAQs and call materials (info session 16 Jun 2026; 77 EOIs / 16 member states / 60 sites), InvestAI facility (€20B), Bpifrance AI envelope announcements, Campus AI (Bpifrance/MGX) JV precedent.

---

## 12. Next steps (ordered)

1. **Member agreements** — sign the two-leg take-or-pay per member; secure **backer credit support** (LC/guarantee/prepay). *Gating item for everything else.*
2. **OEM engagement** — GB300 BOM + quote against the $266M build-up; Rubin budgetary quote to collapse the $234–293M range; allocation and delivery schedule; vendor-finance term sheet.
3. **Colo RFP** — T1/T2 capacity (~20MW liquid-cooled, GB300-grade) *and* the T3 Rubin-grade option (§6 decision gate): rate, reserved-power basis, energy pass-through, CDU responsibility, term and expansion rights.
4. **Bank mandate** — structuring + warehouse (fund GPU deposits against delivery); split senior/vendor stack (35/42/23) at term-sheet stage; PropCo construction and stabilization financing; ABS take-out path.
5. **Site process** — shortlist → exclusivity → grid-connection application → permitting diligence (water, fibre, geotech, environment); long-lead equipment reservations (transformers, switchgear, chillers, CDUs) at FID.
6. **Public capital track (upside only, but time-critical)** — the EuroHPC Gigafactory call lands **this summer**: execute §8's steps now (call docs on day one; standalone-vs-join memo in ~4 weeks; Bpifrance/CDC meetings to secure the member-state letter). Underwrite on award, never in base.
7. **T1 FID** — each member funds its **$98M** equity check; colo fit-out begins; campus construction breaks ground the same month.
8. **Modelling backlog (bank-grade)** — milestone/S-curve construction draws, invoice-matched debt draws, financing fees & IDC, DSRA, dual-currency ledgers, VAT working capital, PropCo terminal state, refresh-event modelling.

---

*Prepared as a planning and diligence basis. Every figure carries its status label; replace estimates and assumptions with executed quotes and term sheets at each gate. Not an offer of securities; not a financing commitment.*
