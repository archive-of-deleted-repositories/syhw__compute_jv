# Revision brief for the JV3 compute build-up plan

**To:** The AI revising `JV3_financial_model.md`, `jv3_onepager_full_v3.html`, and `jv_economics_v3.csv`  
**Date:** 13 July 2026  
**Purpose:** Convert the current materials into a coherent, auditable **member cost schedule** for a compute joint venture. This is not a revenue forecast or a complete project-finance model.

## 1. Revision mandate

Revise all three files from one canonical set of assumptions and formulas. Do not merely patch visible totals. The current documents are arithmetically connected, but several foundational inputs and structural choices are wrong or unsupported, so their apparent internal consistency is misleading.

The revised plan must:

1. Treat the CSV as a **member cash-cost schedule with outbound cash flows only**. Do not introduce customer revenue, utilization revenue, EBITDA, project IRR, or inbound cash receipts.
2. Separate **ChipCo** and **PropCo** in ownership, capitalization, financing, draw schedules, operating costs, and residual value.
3. Treat GB300 as a deployment into existing liquid-cooled colocation capacity.
4. Treat Rubin as equipment installed in new data-centre buildings developed by PropCo from day one.
5. Use dense FP8 performance per MW as the cross-generation comparison. Do not use the old 2.43× factor or the undefined phrase “GB300-Watt equivalent.”
6. Remove Rubin Ultra from the firm model until NVIDIA publishes sufficiently stable specifications and vendors provide budgetary quotes. It may appear only as an unpriced, unmodelled option.
7. Keep EU or French public support as a side-note/upside option. Do not make the member cost schedule depend on receiving it.
8. Label all sourced facts, management assumptions, vendor quotes, estimates, and sensitivities distinctly. “Verified” must not be used for an unquoted market estimate.
9. Make every headline in the markdown and HTML reproducible from the CSV or the same canonical assumptions table.

## 2. Non-negotiable user decisions already made

Carry these decisions through the revised materials:

- The schedule has no inbound cash flows; it shows member funding and member-borne costs.
- GB300 ChipCo should be underwritten at **$270M per member**, or **$810M per three-member tranche**, unless a later quote supports a different number.
- PropCo must be financed separately from ChipCo.
- The target ChipCo capital stack is **35% member equity, 42% senior GPU debt, and 23% vendor finance**. Do not collapse the latter two into one generic debt line in the detailed schedule.
- Cross-generation comparisons should use dense FP8 throughput per equal MW, not card counts or marketing model names.
- GB300 is built in existing ready colocation space. Rubin is installed in a purpose-built PropCo facility.
- EU/public money is optional upside and not part of the base case.
- T6 and T7 are options, not part of the committed-program total or base monthly path.

## 3. Correct the physical configurations first

### 3.1 GB300 NVL72

Use the following public NVIDIA facts:

- 72 Blackwell Ultra GPUs per NVL72 rack.
- NVIDIA publishes 720 PFLOPS of FP8/FP6 performance **with sparsity** per rack.
- The comparable dense FP8 figure is approximately half of that, or **360 PFLOPS per rack**.
- NVIDIA's current enterprise reference architecture gives a full-rack maximum of up to **142 kW**, not 135 kW.

For the current 144-rack tranche:

- GPUs: `144 × 72 = 10,368`.
- Nameplate IT load: `144 × 142 kW = 20.448 MW`.
- Dense FP8: `144 × 360 PFLOPS = 51.84 EFLOPS`.
- Per member at 48 racks: 3,456 GPUs, 6.816 MW, and 17.28 dense-FP8 EFLOPS.

Primary references:

- [NVIDIA GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)
- [NVIDIA NVL72 enterprise reference architecture](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/components.html)
- [NVIDIA HGX performance convention](https://www.nvidia.com/en-in/data-center/hgx/)

### 3.2 Vera Rubin NVL72

Use the following public NVIDIA/OEM facts:

- 72 Rubin GPUs per rack.
- **1,260 PFLOPS dense FP8 per rack**, or 17.5 PFLOPS per GPU.
- ASUS publishes **227 kW MaxP** and 187 kW MaxQ for its Vera Rubin NVL72 implementation.
- NVIDIA describes production/shipping in the second half of 2026. Do not imply that delivery is presently firm unless an executed vendor allocation supports it.

For the current 90-rack tranche at MaxP:

- GPUs: `90 × 72 = 6,480`.
- Nameplate IT load: `90 × 227 kW = 20.430 MW`.
- Dense FP8: `90 × 1,260 PFLOPS = 113.40 EFLOPS`.
- Per member at 30 racks: 2,160 GPUs, 6.810 MW, and 37.80 dense-FP8 EFLOPS.

Primary references:

- [NVIDIA DGX Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/dgx-vera-rubin-nvl72/)
- [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-gb/data-center/vera-rubin-nvl72/)
- [ASUS Vera Rubin NVL72 power disclosure](https://press.asus.com/news/press-releases/asus-ai-pod-nvidia-vera-rubin-nvl72)
- [NVIDIA Vera Rubin platform overview](https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/)

### 3.3 The correct performance ratio

The current 144 GB300 racks and 90 Rubin racks are remarkably close in nameplate power: 20.448 MW versus 20.430 MW. Call them **nominal 20 MW blocks**, but always disclose the actual nameplate load. Do not state that either configuration is strictly 20.000 MW.

The correct dense-FP8 ratios are:

- Equal current tranche ratio: `113.40 / 51.84 = 2.1875×`.
- Per-MW ratio: `(1,260 / 227) / (360 / 142) = 2.1894×`.
- Per-GPU ratio: `17.5 / 5.0 = 3.50×`.

Therefore use:

> **Dense FP8 per MW: GB300 1.00×; Vera Rubin approximately 2.19× at MaxP.**

The earlier 2.43× claim mixed incompatible chip/rack and power conventions and must be removed everywhere.

If the revision instead enforces a hard ceiling of 20 MW while keeping equal thirds, use 138 GB300 racks (46/member, 19.596 MW, 49.68 EFLOPS) and 87 Rubin racks (29/member, 19.749 MW, 109.62 EFLOPS). However, doing so changes the purchased scope and breaks the agreed $270M-per-member GB300 case. The preferred presentation is therefore to retain 144/90 racks, call each a nominal 20 MW block, disclose ~20.44 MW actual nameplate, and normalize the comparison per MW.

### 3.4 Rubin Ultra is materially misdescribed

Delete all numerical Rubin Ultra economics and performance from the base and option schedules.

The current files assert that one 600 kW “rack” contains 144 packages or 576 GPUs because the NVL576 name counts dies. That is false. NVIDIA describes Vera Rubin Ultra NVL576 as **eight separate MGX racks**, each with 72 physical Rubin Ultra GPUs, for 576 GPUs total. NVIDIA separately describes Kyber as a future 144-GPU rack design and NVL1152 as eight Kyber racks.

Consequences:

- The existing Ultra rack count is invalid.
- The package/GPU count is invalid.
- The 600 kW rack definition is invalid or at least badly conflated with a multi-rack system.
- The 34.7 PFLOPS/package assumption is not underwritable.
- The $52M/rack cost has no adequate public basis.
- All Ultra capex, debt, interest, operating cost, unit-cost, and full-program totals derived from those inputs are invalid.
- The **$8.8B full-program headline is not a valid result**.

Retain only an option marker such as: “T6–T7: Rubin Ultra or then-current best available platform; configuration, price, power and schedule to be set after specification freeze and vendor quote.”

Reference: [NVIDIA Vera Rubin platform overview](https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/).

## 4. Rebuild capex rather than preserving the current headline

### 4.1 GB300 ChipCo

The current formula is:

`48 racks/member × $4.0M/rack × 1.15 = $220.8M/member`.

Replace this with the agreed underwriting case:

- **$270.0M/member**.
- **$810.0M/tranche**.
- Implied fully loaded cost: **$5.625M/rack**.

The public market contains conflicting estimates: older bare/system estimates were around $3.7M–$4.0M per rack, while more complete configurations have been reported around $6.0M–$6.5M. This is precisely why `$4.0M × 1.15` must not be presented as a July 2026 verified cost. Show $270M as an underwriting assumption pending a vendor bill of materials and quote, then run sensitivities around it.

Secondary market reference: [Tom's Hardware on complete GB300/Rubin rack pricing](https://www.tomshardware.com/tech-industry/artificial-intelligence/price-of-nvidias-vera-rubin-nvl72-racks-skyrockets-to-as-much-as-usd8-8-million-apiece-but-server-makers-margins-will-be-tight-nvidia-is-moving-closer-to-shipping-entire-full-scale-systems-one-ai-supercomputer).

The revised bill of materials should state whether the price includes:

- compute racks;
- NVLink/network fabric outside the rack;
- storage;
- spares;
- software/support;
- freight, duties and VAT working capital;
- installation and acceptance testing;
- owner contingency; and
- initial maintenance/support contracts.

Do not add a blanket 15% uplift to a rack quote without showing which of these items the quote already includes.

### 4.2 Rubin ChipCo

The current case is:

`90 racks × $8.5M × 1.15 = $879.75M/tranche`, or `$293.25M/member`.

A current public estimate reported approximately **$7.8M per configured system**, including substantial memory/storage content. Applying a further generic 15% may therefore double-count some storage, network or integration items.

Until actual quotes exist, use a clearly labelled range for 90 racks:

- Lower/current configured-system case: `90 × $7.8M = $702M/tranche`, or `$234M/member`.
- Conservative current complete case: **$879.75M/tranche**, or **$293.25M/member**.

Do not call either amount verified. The sensitivity table must state what is included in each price point.

Reference: [reported Vera Rubin configured-system cost](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-memory-costs-soar-485-percent-latest-ai-systems-now-cost-usd7-8-million-to-build-memory-now-comprises-25-percent-of-the-total-cost-rubin-gpus-a-mere-usd50-000-apiece).

### 4.3 PropCo capex

The current PropCo allowance is only `$170M + $12M grid = $182M` for a nominal 20 MW block. This is not adequately supported and omits several owner costs.

Turner & Townsend's 2025 Paris benchmark is **$10.8/W for an air-cooled data centre**, with a further **7%–10% premium for AI liquid cooling**. Applying that to 20 MW gives:

- Base hard build: `$216M`.
- With liquid-cooling premium: approximately **$231M–$238M**.
- Adding the current $12M grid placeholder: approximately **$243M–$250M**, before omitted owner costs.

The benchmark explicitly excludes or may exclude land, utility works, site works, professional fees and client-direct costs. Use **$260M–$275M per nominal 20 MW block as an early planning range**, before exceptional land/grid work and financing costs. A reasonable central placeholder is **$267.5M/block**.

References:

- [Turner & Townsend 2025 data-centre cost trends](https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/data-centre-cost-trends)
- [Turner & Townsend methodology and exclusions](https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/methodology)

Do not repeat an identical $12M grid charge for every building without an engineering basis. Split grid spending into:

1. common campus-enabling connection/substation/transmission costs; and
2. marginal building/block connection costs.

The one-pager's specific “RTE 400 kV” assertion must be removed unless supported by an executed connection offer or formal grid study.

### 4.4 Recomputed firm-program capex

The present T1–T5 arithmetic is:

| Component | Current total |
|---|---:|
| Two GB300 ChipCos | $1.3248B |
| Three Rubin ChipCos | $2.63925B |
| Three Rubin PropCos | $0.546B |
| **Current firm total** | **$4.51005B** |
| **Current per-member total** | **$1.50335B** |

Rebuild it as:

| Component | Revised range |
|---|---:|
| Two GB300 ChipCos at $810M | $1.620B |
| Three Rubin ChipCos | $2.106B–$2.639B |
| Three Rubin PropCos | $0.780B–$0.825B |
| **Revised T1–T5 total** | **$4.506B–$5.084B** |
| **Revised per-member total** | **$1.502B–$1.695B** |

A central planning example using $790.0M per Rubin ChipCo and $267.5M per PropCo is:

- Total T1–T5 capex: **$4.7925B**.
- Per-member total: **$1.5975B**.

The fact that the bottom of the corrected range resembles the old $4.5B headline is coincidental: lower Rubin pricing offsets the old model's understated GB300 and PropCo cost. Do not use that coincidence to imply the old assumptions were sound.

There must be no “full T1–T7” total until Ultra is sufficiently specified and quoted.

## 5. Rebuild financing by legal entity

### 5.1 The current 37% aggregate equity case is manufactured

The CSV forces an aggregate equity percentage of approximately 37%, but does so with inconsistent sleeve-level financing:

- GB300 ChipCo is about 37% equity / 63% debt.
- Rubin PropCo is effectively 100% member equity.
- Rubin ChipCo is roughly 24% equity / 76% debt.
- Ultra PropCo is effectively 100% equity.
- Ultra ChipCo is roughly 31% equity / 69% debt.

Across the current full CSV, about $1.8505B of member-level debt sits against approximately $2.6345B of member ChipCo capex—roughly 70% ChipCo leverage—despite the “conservative” narrative. This is not the agreed stack and obscures risk.

Delete the mixed “37/63 working case” versus “50/32/18 base/fallback” descriptions. They are mutually inconsistent and neither is the user's chosen case.

### 5.2 ChipCo financing

Use the user's target stack for each ChipCo tranche:

- 35% member equity.
- 42% senior GPU debt.
- 23% vendor finance.

For one $270M GB300 member allocation:

| Source | Percentage | Amount |
|---|---:|---:|
| Member equity | 35% | $94.5M |
| Senior GPU debt | 42% | $113.4M |
| Vendor finance | 23% | $62.1M |
| **Total** | **100%** | **$270.0M** |

Senior debt and vendor finance must have separate:

- interest rates/margins and reference rates;
- tenors and amortization profiles;
- draw timing;
- fees and commitment fees;
- security and intercreditor ranking;
- covenants; and
- residual balloon/refinancing assumptions.

Do not use one blended 9.5% facility as if these instruments were economically identical. It may be retained only as a labelled illustration. At 65% debt, 9.5% and five-year level amortization, a $270M member allocation would have:

- Debt principal: **$175.5M**.
- Monthly payment: approximately **$3.686M**.
- Total five-year interest: approximately **$45.65M**.
- First six months' interest: approximately **$8.06M**.

### 5.3 PropCo financing

PropCo needs its own construction and stabilized capital stacks. Do not fund it as a hidden 100%-equity appendage and do not include its leverage in the ChipCo ratio.

For a $267.5M block, show at least:

| Phase | Equity | Debt | Block amounts | Per-member amounts |
|---|---:|---:|---:|---:|
| Construction example | 40% | 60% | $107.0M / $160.5M | $35.7M / $53.5M |
| Stabilized example | 35% | 65% | $93.6M / $173.9M | $31.2M / $58.0M |

These are planning cases, not claims of executable leverage. Any refinance assumption must depend on completed construction, tenant/member contracts, credit support, operating history and valuation.

The cited Vantage transaction had roughly 69% notes-to-market but involved fully occupied assets, investment-grade tenants and around 22 years of weighted-average lease term. It is not direct evidence that JV3 can refinance after 18 months. Reference: [Scope rating report on Vantage stabilized data-centre financing](https://www.scopegroup.com/ScopeGroupApi/api/analysis?id=7f39134d-fea6-48ed-a361-84bdbc82310f).

### 5.4 Debt benchmark corrections and missing financing costs

Correct the CoreWeave references:

- DDTL 4: $8.5B, SOFR + 2.25%, contract-specific ratings of A3/A(low).
- DDTL 5: $3.1B, SOFR + 4.50%, completed roughly one month later.
- The current text's “A3/A−” is inaccurate.

Primary references:

- [CoreWeave DDTL 4 SEC filing](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/crwv-20260330.htm)
- [CoreWeave DDTL 5 SEC filing](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000236/crwv-20260515.htm)

These facilities illustrate that pricing is highly contract- and credit-dependent. The schedule must also model, or explicitly leave placeholders for:

- upfront and OID fees;
- legal/arrangement fees;
- undrawn commitment fees (DDTL 5 included 0.5%);
- interest during construction;
- debt-service reserve accounts;
- interest-rate hedging; and
- refinancing costs.

## 6. Correct operating-cost logic

### 6.1 Colocation

The CSV currently charges GB300 colocation using `6.48 MW/member × $130/kW-month = $0.8424M/month`, based on the obsolete 135 kW/rack input.

Show clearly which commercial basis applies:

- One third of a contractual 20 MW reservation: `6,666.7 kW × $130 = $0.8667M/month`.
- Actual 48-rack nameplate at 142 kW/rack: `6,816 kW × $130 = $0.8861M/month`.

Do not switch between reserved power and installed nameplate without explanation. The $130/kW-month input is an unquoted low-case assumption in a constrained European market. Include at least a rate sensitivity, for example $130/$155/$180. Moving from $130 to $180 adds roughly **$20M over five years per member** when charged on one third of a 20 MW reservation.

Market context: [CBRE Global Data Center Trends 2025](https://www.cbre.com/insights/reports/data-center-trends-2025).

Clarify whether the colo charge already includes remote hands, basic maintenance, security or on-site personnel before adding a separate staffing line.

### 6.2 Electricity

The current formula incorrectly uses 90% “billed availability” as an electrical-load multiplier. Separate these concepts:

- contractual availability/SLA;
- compute utilization;
- electrical load factor;
- PUE; and
- billed/reserved capacity.

A clear electricity formula is:

`IT MW × electrical load factor × PUE × hours × all-in €/MWh × USD/EUR`.

At 100 MW IT, PUE 1.20, 90% electrical load factor, €90/MWh and $1.143/€:

- Annual facility energy: **946.08 GWh**.
- Annual energy cost: **€85.147M**.
- Annual dollar cost: **$97.323M**.

At 140 MW under the same assumptions:

- Annual facility energy: **1.324512 TWh**.
- Annual energy cost: **€119.206M**.
- Annual dollar cost: **$136.253M**.

The July 10, 2026 ECB reference rate is **€1 = $1.1430**, not $1.08. Reference: [ECB euro reference exchange rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html).

Do not treat €70/MWh generation supply as an all-in delivered price. Separate:

- commodity energy;
- TURPE/network charges;
- taxes and levies;
- capacity, imbalance and balancing;
- hedge cost; and
- any CAPN upfront contribution and annual management payment.

References:

- [EDF CAPN subscription information](https://www.edf.fr/groupe-edf/edf-en-bref/optimisation-et-trading/souscription-capn)
- [French AI summit energy/infrastructure material](https://www.elysee.fr/admin/upload/default/0001/17/d9c1462e7337d353f918aac7d654b896b77c5349.pdf)

Maintain separate EUR and USD ledgers, or at minimum provide FX sensitivities and state the hedge assumption.

### 6.3 Maintenance, staff and other omissions

The current 2.5% annual maintenance and $0.05M/month staffing assumptions are unverified. Retain them only as labelled assumptions and test whether vendor support or colo operating services already include those costs.

Add or explicitly identify the treatment of:

- software and enterprise support;
- replacement parts and spares consumption;
- insurance;
- property tax and local taxes;
- water and cooling consumables;
- network transit/backhaul;
- security and facilities management;
- VAT/import-duty working capital;
- decommissioning and disposal; and
- migration/overlap costs at refresh.

## 7. Recompute member unit costs with explicit denominators

The CSV currently has unlabeled 100% and 90% columns, while prose sometimes quotes one and describes the other. Every unit-cost result must specify:

- whether hours are at 100% theoretical or 90% billable/utilized availability;
- whether the unit is GPU, package, rack, dense-FP8 PFLOPS, sparse/marketing PFLOPS, or MW;
- whether financing principal is treated as a cost or a funding-flow repayment; and
- the period and residual-value assumption.

Specific corrections:

- Current Rubin package cost is about **$5.18/hour at 100%** and **$5.76/hour at 90%**. The markdown's “~$5.2” while describing 90% is wrong.
- Rubin's official per-GPU dense-FP8 ratio is **3.50×**, not 3.89×.
- On the current cost base, Rubin at 90% divided by the correct 3.50 ratio is roughly **$1.65 per GB300-equivalent hour**, not $1.48.
- The CSV program PF cost around $0.3679 uses 100% hours, while the one-pager's $0.41 headline uses 90%. Label both or choose one standard.
- Remove every use of “normalized GB300-Watt.” Use dense-FP8 PFLOPS-hour and dense-FP8-per-MW instead.

### 7.1 Illustrative corrected GB300 five-year member cost

Using the agreed $270M capex, 65% illustrative debt at 9.5% over five years, colo charged on one third of a 20 MW reservation at $130/kW-month, actual 6.816 MW rack nameplate, PUE 1.20, 90% electrical load factor, €90/MWh, $1.143/€, 2.5% annual maintenance and $0.05M/month staffing gives:

| Item | Five-year member amount |
|---|---:|
| Principal/capex funded | $270.00M |
| Interest | $45.65M |
| Colocation | $52.00M |
| Electricity | $33.17M |
| Maintenance | $33.75M |
| Staffing | $3.00M |
| **Total member cash cost** | **$437.57M** |

This compares with approximately $367.8M in the current CSV. The resulting illustrative unit costs are approximately:

- **$3.21 per GPU-hour at 90%**; and
- **$0.642 per dense-FP8 PFLOPS-hour at 90%**, using 5 dense-FP8 PFLOPS/GPU.

This example is not a final base case: it retains unverified maintenance and staffing inputs, may double-count staff included in colo, and uses one blended debt instrument solely for comparability. The revision should improve these inputs rather than blindly copy the example.

## 8. Model the refresh reserve and terminal state correctly

The markdown says an 8%–12% annual refresh reserve is funded from year two, but the CSV contains no such cash flow. Add it visibly or remove the claim.

On the current firm-program ChipCo capex of $1.32135B per member, four annual contributions would be:

- 8%: **$422.8M cumulative**.
- 10%: **$528.5M cumulative**.
- 12%: **$634.2M cumulative**.

A more principled base is **8.75% of original ChipCo capex annually for four years**, which accumulates cash equal to 35% replacement equity before return/interest. Treat contributions as movement into a restricted cash asset, not as an accounting expense when funded. Expense/capitalize them only when the replacement assets are purchased.

Do not allow PropCo buildings to disappear from the schedule when the first GPU fleet reaches month 60. The current `m99` endpoint effectively removes long-lived buildings. Model one of the following explicitly:

- a compute refresh and continued occupancy;
- a vacancy/carrying-cost period;
- re-leasing to a new ChipCo/fleet; or
- sale/refinancing and distribution.

Replace the single 10% equipment residual assumption with at least 0%/5%/10%/15% sensitivities and include decommissioning, data erasure, removal, sale commission and migration overlap.

## 9. Replace the deployment timelines

### 9.1 GB300 into existing colocation

“16 weeks” is possible only as an accelerated case when liquid-cooled space, power, network, integrated racks and vendor allocation are all ready. It is not a generic order-to-production assumption.

Use three scenarios:

- **Accelerated: 16 weeks** — ready liquid-cooled colo, integrated NVL72 systems already allocated, no major grid or cooling retrofit, rapid acceptance.
- **Base: 20–28 weeks** — procurement/allocation, delivery, integration, network and storage deployment, burn-in and acceptance.
- **Downside: 32–40 weeks** — self-procured components, 25+ week supply, assembly/integration, or facility retrofit constraints.

The public example of a GB300-compatible retrofit in 45 working days is an execution record for a particular retrofit, not evidence for a standard procurement-to-production schedule. Reference: [Zettabyte/Chief Telecom retrofit announcement](https://www.prnewswire.co.uk/news-releases/zettabyte-and-chief-telecom-retrofit-legacy-data-center-into-gb300-compatibility-ai-hub-in-just-45-working-days-302596598.html).

Define “buyout” precisely. The schedule must distinguish:

1. reservation/PO deposit;
2. manufacturing or vendor progress payments;
3. title transfer/delivery;
4. installation and integration;
5. burn-in/acceptance; and
6. production start.

Do not draw all debt at an arbitrary “buyout” date six months before service without matching it to collateral eligibility and actual invoices.

### 9.2 Rubin in a new PropCo building

The current 15-month greenfield assumption is not a reliable base case unless the land, permits, grid connection and long-lead equipment are already de-risked.

Use:

- **Accelerated: 18–21 months** — shovel-ready land, secured power, expedited permits, early long-lead procurement and parallel workstreams.
- **Base: 22–24 months** — credible purpose-built delivery from day one.
- **Downside: 30–36 months** — grid, permitting, transformer/switchgear or construction delay.

Show milestones for site control, design, permits, RTE/DSO connection, transformers/switchgear/generators/chillers/CDUs, groundworks, shell, MEP, commissioning levels, compute delivery, integration and acceptance. European authorization processes can themselves run upward of 20 months. Reference: [EU Council working paper on data-centre permitting](https://data.consilium.europa.eu/doc/document/WK-2581-2025-INIT/en/pdf).

Do not provide a numerical Ultra delivery schedule until its design and vendor configuration are frozen.

## 10. Correct site and power claims

The one-pager presently makes unsupported claims about fast-track/exclusive access at Dunkerque and Le Bosquel.

- Le Bosquel is associated with SoftBank/Sesterce's announced 1 GW project. Reference: [SoftBank announcement](https://group.softbank/en/news/press/20260531).
- Dunkirk is also part of announced/current development activity and should not be described as exclusive without executed documentation.

Replace site certainty with:

> “Site to be selected subject to executed land exclusivity, confirmed grid-connection offer, permitting diligence, water/cooling design, fibre diversity and geotechnical/environmental review.”

Creys-Mépieu/EDF's CEI can appear as a possible option, not an assumed site or entitlement. Reference: [EDF CEI data-centre offering](https://www.edf.fr/en/the-edf-group/supporting-our-clients/cei-data-centers).

## 11. Keep public support optional

EU rules can allow support of up to 17% of eligible computing-infrastructure capital expenditure, but only after selection and subject to program conditions and Member State participation. It is not committed funding.

The base CSV should contain **zero public subsidy**. Include a separate sensitivity or note showing possible impact only after clearly defining eligible cost, selection probability, timing, matching requirements and clawback/operating conditions.

The one-pager currently gives this too much prominence by making “anchor public capital” an execution step. Move it to optional financing upside.

References:

- [EU Regulation 2026/150](https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX%3A32026R0150)
- [EuroHPC AI Gigafactory FAQs](https://www.eurohpc-ju.europa.eu/ai-gigafactories/faqs-ai-gigafactories_en)

## 12. Fix the scope: cost schedule, not synthetic revenue model

The member transfer price currently makes DSCR tautological: price is set to recover cost, so a calculated coverage ratio does not demonstrate financeability. “100% demand self-guaranteed” likewise does not mean the cash flows are bankable. Venture-backed members may require prepayment, letters of credit, parent guarantees, funded reserves or other hard credit support.

For the base materials:

- Rename `JV3_financial_model.md` internally as a **member cost schedule specification**, even if the filename is retained for compatibility.
- Remove revenue architecture, utilization revenue, project IRR and circular transfer-pricing calculations.
- Remove DSCR from the base schedule unless supported by a separate, actual contracted payment schedule.
- Keep debt service as a member cash outflow and show member funding calls.
- If financeability is discussed, put it in a separate financing appendix with explicit credit-support scenarios.

The schedule should distinguish economic cost from cash funding. For example, debt principal is a funding inflow to the SPV and later a repayment outflow, while equipment capex is the asset purchase; adding capex and principal repayment without showing financing sources can double-count economic cost. Because the user wants no inbound cash flows in the member schedule, use one of these consistent presentations:

1. **Member contribution schedule:** show equity calls plus debt service plus operating costs, with debt proceeds and supplier payments held in a separate SPV sources-and-uses table; or
2. **Asset cash-cost schedule:** show member-attributable capex and operating/financing cost, but do not also add repaid debt principal to the same “total economic cost.”

State which view is used. Prefer the first for monthly member cash calls and include a reconciliation to full project sources and uses outside the no-inbound member schedule.

## 13. CSV modelling requirements

Rebuild `jv_economics_v3.csv` from explicit assumptions rather than editing totals manually.

Required sections:

1. Version/date and scope statement.
2. Global assumptions with units and source status.
3. Physical configuration by tranche.
4. ChipCo sources and uses by tranche.
5. PropCo sources and uses by building.
6. Separate senior, vendor and PropCo debt schedules.
7. Member equity/funding-call schedule.
8. Colocation operating schedule for GB300.
9. Owned-facility operating schedule for Rubin.
10. Electricity schedule with IT load, load factor, PUE, energy tariff and FX separated.
11. Refresh-reserve funding and restricted-cash balance.
12. Residual/decommission/refinancing scenarios.
13. Unit-cost outputs with denominator and utilization in every header.
14. Sensitivities.
15. Reconciliation checks.

Mandatory modelling changes:

- Exclude T6–T7 from committed totals and monthly base path.
- Do not turn entire tranches on instantaneously; provide procurement/construction draws and commissioning ramp.
- Replace linear construction draws with a reasonable S-curve or milestone draws.
- Match debt draws to eligible invoices and actual funding dates.
- Do not assume all equipment debt begins six months before service without basis.
- Continue PropCo operating costs and asset value after the first GPU fleet expires.
- Add financing fees, IDC, commitment fees, reserves and hedging.
- Add multi-currency treatment and FX sensitivities.
- Add VAT/import working capital treatment.
- Add explicit flags for quote/assumption/source date.

Recommended validation checks:

- Sources equal uses for every legal entity and tranche.
- Equity + senior debt + vendor finance = 100% of ChipCo uses.
- PropCo sources equal PropCo uses independently.
- Opening cash + funding − uses = closing cash for every month.
- Opening debt + draws − principal repayment = closing debt.
- Interest recalculates from average or exact-period debt balance.
- Restricted reserve opening + contribution + return − use = closing reserve.
- Rack × GPU/rack = GPU count.
- Rack × kW/rack = IT nameplate.
- IT load × load factor × PUE × hours = facility energy.
- Aggregate member totals equal one third of three-member totals, except explicitly member-specific items.
- Markdown and HTML headline values match the CSV outputs exactly.

## 14. Markdown-specific corrections

In `JV3_financial_model.md`:

- Change the title/description from a full financial model to a member cost-schedule specification.
- Replace 135 kW GB300 with 142 kW and recompute all downstream figures.
- Replace the Rubin performance/power inputs with 1,260 dense-FP8 PFLOPS/rack and 227 kW MaxP, with MaxQ as a scenario.
- Replace 2.43×/3.89× and “GB300-Watt” with the 2.19× per-MW dense-FP8 comparison.
- Insert the $270M/member GB300 ChipCo case.
- Replace the Rubin cost point with a range pending quote.
- Replace $182M PropCo with the $260M–$275M planning range and separate campus grid costs.
- Remove all Ultra numerical claims and the $8.8B full-program total.
- Replace the financing narrative with separate ChipCo 35/42/23 and PropCo stacks.
- Remove circular revenue, DSCR and project-IRR claims from the base.
- Add explicit GB300 and Rubin timing scenarios.
- Add reserve cash flows or remove the reserve claim.
- Correct CoreWeave ratings and pricing references.
- Label every unit-cost denominator and utilization basis.
- Stop using “commit-grade,” “verified” or “committed path” where no executed quote/allocation/financing exists.

## 15. One-pager-specific corrections

In `jv3_onepager_full_v3.html`:

- Ensure every visible number comes from the revised cost schedule.
- Do not retain stale hard-coded values after the CSV changes.
- Replace the headline 2.43× ratio with approximately 2.19× dense FP8 per MW.
- Replace the GB300, Rubin and PropCo capex cards with the revised assumptions/ranges.
- Remove the $8.8B full-program headline and all numeric Ultra cards.
- Show T1–T5 as the firm planning scope; show T6–T7 as unpriced options.
- Replace “Vera Rubin committed path” with “planned/provisional path subject to vendor allocation and facility delivery.”
- Remove unsupported site exclusivity and RTE 400 kV certainty.
- Move EU/public capital out of the main execution sequence and into optional upside.
- Fix the heading that says “Seven options” while listing Options 1–8.
- Do not call the plan “critique-verified.” Use a dated assumptions/as-of label.
- Correct the $0.41 versus $0.3679 utilization-basis mismatch.
- Avoid “100% demand self-guaranteed”; describe the actual member commitment and required credit support.
- Make clear that 16 weeks is the accelerated ready-colo case, not the general GB300 schedule.
- Present Rubin greenfield delivery as 18–21/22–24/30–36 month scenarios.

## 16. Sensitivities the revised plan should show

At minimum, calculate member cash calls and unit costs under:

- GB300 fully loaded rack cost or member capex: low/base/high around $270M/member.
- Rubin configured rack cost: at least $7.8M, an intermediate case, and $8.5M plus clearly identified extras.
- PropCo block cost: $260M/$267.5M/$275M, plus a grid-overrun case.
- Colo: $130/$155/$180 per kW-month.
- Energy: commodity and all-in delivered cases; at least €70/€90/€110 per MWh all-in where appropriate.
- USD/EUR: downside/base/upside around the current 1.143 reference.
- PUE and electrical load factor separately.
- ChipCo senior/vendor interest and tenor independently.
- PropCo construction leverage and stabilized refinance leverage independently.
- Schedule delay of 0/6/12 months.
- Residual value of 0%/5%/10%/15%.
- Refresh reserve of 0%/8.75%/12% annually.
- Rubin MaxP versus MaxQ, including performance and power consequences only where supported.

## 17. Claims requiring documentary diligence before investment use

Create a diligence register for the following. Until documents are obtained, label them as assumptions—not facts:

- OEM quote and bill of materials for each compute generation.
- GPU/rack allocation and delivery schedule.
- Vendor-finance term sheet.
- Senior GPU-lender term sheet.
- Colo term sheet, including reserved-power measurement and pass-through energy.
- Site exclusivity and land price.
- RTE/DSO grid connection offer, capacity, voltage, schedule and cost.
- Planning/permitting path.
- EPC or design-build budget and liquid-cooling scope.
- Long-lead equipment reservations.
- Member compute commitment and credit support.
- Insurance and tax advice.
- Energy/CAPN term sheet and all-in delivered-cost bridge.
- PropCo construction and stabilization financing term sheets.
- VAT/customs and cross-border structuring advice.

## 18. Acceptance criteria for the revision

The revision is complete only when all of the following are true:

- There is one canonical assumptions set and no contradictory values across the three files.
- GB300 and Rubin physical counts, power and dense-FP8 totals recompute exactly.
- The performance ratio is approximately 2.19× per MW and the convention is disclosed.
- GB300 uses $270M/member in the base underwriting case.
- PropCo is a separately capitalized and financed legal/economic sleeve.
- The current planning range for T1–T5 is shown, not an unsupported single precise number.
- T6–T7/Ultra are excluded from committed totals and base cash flows.
- Member cash calls do not contain inbound revenue.
- Financing sources and asset costs are not double-counted.
- Senior debt, vendor finance and PropCo debt have separate schedules.
- Electricity does not use availability as a proxy for electrical load.
- FX, PUE, load factor and all-in power cost are explicit.
- Refresh reserve cash flows and terminal PropCo treatment are present.
- GB300 and Rubin schedules use the realistic scenario ranges above.
- Site, grid, public-support and vendor-delivery claims are appropriately conditional.
- All unit-cost headers state denominator and utilization.
- The markdown and HTML can be reconciled to the CSV with no unexplained difference.

## 19. Recommended order of work

1. Remove Ultra numerical content and optional tranches from the base.
2. Create the canonical physical and commercial assumptions table.
3. Correct rack counts, power, dense-FP8 and per-MW ratios.
4. Rebuild GB300 and Rubin ChipCo sources, uses and financing.
5. Rebuild PropCo capex, timing, sources, uses and residual state separately.
6. Rebuild energy, colo and facility opex formulas.
7. Rebuild monthly member calls, debt schedules and refresh reserve.
8. Add sensitivities and validation checks.
9. Regenerate all markdown headline tables from the revised outputs.
10. Update the HTML last, using only values reconciled to the final schedule.

The revised plan should be candid about uncertainty. Precision is useful only where supported by a physical configuration, a formula and a dated source or quote. The immediate goal is not to make the proposal look financeable; it is to make its member funding needs, execution risks and economic sensitivities transparent enough that financing and procurement counterparties can engage with it seriously.
