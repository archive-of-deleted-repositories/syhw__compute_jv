# JV3 model critique — `JV3_financial_model.md` and `jv_economics_v3.csv`

**Review date:** 13 July 2026  
**Scope:** consolidated review following the evolution of JV3 into a three-member, self-guaranteed compute cooperative, with GB300 deployed first in existing AI-ready colocation and the owned PropCo campus constructed in parallel for Vera Rubin and later platforms.

## Bottom line

The strategic sequence is sound:

1. deploy GB300 quickly in existing colocation;
2. start the owned Rubin campus from day one;
3. compare generations using dense FP8 compute delivered by an equal 20MW-IT block;
4. keep Rubin provisional and Rubin Ultra optional;
5. finance ChipCo and PropCo separately.

The two reviewed files do not yet implement that structure consistently.

The most important corrections are:

- **GB300 ChipCo should be underwritten at approximately $270M per member for 48 integrated racks and their associated fabric, storage, spares and integration.** The CSV currently uses $210M, which reflects the earlier $3.8M/rack plus 15% formulation and is likely too low.
- **PropCo must be a separate asset and financing schedule.** It should not be hidden inside sleeve “all-in” cost, paid entirely with member equity, or allocated to GB300 deployed in third-party colo.
- **A 35% member-equity target is reasonable if the remaining 65% is split among senior GPU debt, OEM/vendor finance and, for owned buildings, separate PropCo debt.** It is not reasonable to represent all non-equity funding as one chip loan.
- **`jv_economics_v3.csv` is a member cost, financing and liquidity schedule—not a complete project financial model.** It does not need revenue, CFADS, DSCR or project IRR. It does need accurate deposits, construction draws, separate financing instruments, operating costs, reserves and monthly member cash requirements.
- **The FP8 comparison should be expressed per equal 20MW block.** Use GB300 = 1.00× and Vera Rubin = approximately 2.43×. Rubin Ultra must remain TBD until NVIDIA publishes a usable dense FP8 specification and freezes the deployable topology.
- **The Rubin construction schedule is too aggressive for a new French campus unless the site already has binding land, permits and energized capacity.** Fifteen months should be an accelerated case, not the base case.

The current documents remain useful planning drafts, but the headline program cost, member funding requirement and future-platform unit costs should not be circulated as reconciled outputs until these changes are made.

---

## 1. Define the two files' different jobs

### `JV3_financial_model.md`

This should be the program's conceptual build and financing specification. It should define:

- what the JV owns;
- which tranches are in colo versus owned PropCo;
- platform status and re-underwriting gates;
- the target capital stacks;
- the FP8-per-20MW comparison method;
- construction cases and decision gates;
- optional financing levers, including public capital and refinancing.

It may describe the member take-or-pay and lender requirements, but it should not imply that those revenues are modeled in the CSV if they are not.

### `jv_economics_v3.csv`

This should be renamed conceptually as:

> **JV3 Member Cost, Financing and Liquidity Schedule**

Its purpose is to show what one member funds, when it funds it, and the resulting cost of owned compute. It should contain no inbound operating revenue unless a later version explicitly adds a separate project-finance module.

Appropriate outputs are:

- member equity contributions;
- senior debt and vendor-finance draws;
- PropCo debt and equity draws;
- deposits and progress payments;
- interest, principal and financing fees;
- colo rent and operating costs;
- maximum monthly and quarterly member cash calls;
- cumulative member cash paid;
- closing balances of each financing instrument;
- refresh-reserve contributions and ending restricted cash;
- cost per FP8 PFLOPS-hour and cost per GB300-equivalent 20MW-block-hour.

Revenue, CFADS, DSCR and project IRR belong in a separate lender/project model and are not required in this cost schedule.

---

## 2. GB300 ChipCo is understated in both files

### Current treatment

`JV3_financial_model.md` calculates a full GB300 tranche as:

```text
144 racks × $3.8M × 1.15 = approximately $629M ChipCo
+ approximately $182M PropCo
= approximately $811M total
```

This produces approximately $210M of ChipCo and $60.7M of PropCo per member.

`jv_economics_v3.csv` then removes the GB300 PropCo because T1/T2 are in colo, but leaves the member ChipCo at only **$210M**.

### Recommended treatment

The working base should be:

```text
GB300 ChipCo per member = approximately $270M
GB300 ChipCo per 20MW tranche = approximately $810M
T1 + T2 GB300 ChipCo = approximately $1.62B
```

Public pricing is not sufficiently transparent to establish a single exact figure. Current reporting ranges from roughly $4M per GB300 NVL72 system for large-CSP economics to approximately $6–6.5M for more fully configured inference-oriented systems. NVIDIA's reference architecture also confirms that a deployable cluster requires material scale-out and storage networking beyond the compute cabinets. Relevant references include the [NVIDIA NVL72 AI Factory reference architecture](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/network-logical-architecture.html) and current reporting on [GB300 and Rubin system pricing](https://www.tomshardware.com/tech-industry/artificial-intelligence/price-of-nvidias-vera-rubin-nvl72-racks-skyrockets-to-as-much-as-usd8-8-million-apiece-but-server-makers-margins-will-be-tight-nvidia-is-moving-closer-to-shipping-entire-full-scale-systems).

At $270M, the member is underwriting an effective all-in ChipCo cost of:

```text
$270M / 48 racks = $5.625M per integrated rack
```

That is a reasonable planning midpoint once compute racks, scale-out fabric, optics, storage, spares, support and integration are included.

### Suggested GB300 ChipCo budget

| Component | Base | Planning range |
|---|---:|---:|
| 48 integrated GB300 NVL72 systems | $220M | $195–260M |
| Scale-out switching, optics and cabling | $18M | $12–28M |
| Storage and storage network | $12M | $8–20M |
| Spares, support and management software | $8M | $5–15M |
| OEM integration, FAT, freight and installation | $6M | $4–10M |
| Contingency | $6M | $5–12M |
| **Total ChipCo** | **$270M** | **$229–345M** |

The model should replace this range with actual OEM/ODM quotes. Every quote must state whether it includes external scale-out fabric, optics, storage, software, warranty, FAT, freight, installation, duties and spares.

The markdown should not call GB300 pricing “firm” until those quotes exist.

---

## 3. GB300 in colo has no owned PropCo

T1 and T2 are now planned for existing AI-ready colocation. Their economics should be divided into:

### GB300 ChipCo capital

- approximately $270M per member per tranche;
- financed against the equipment and member credit package;
- five-year useful life from the in-service date;
- residual and refresh modeled separately.

### Colo-specific upfront cash

- reservation/security deposit;
- advance capacity payment;
- member share of liquid-cooling and electrical fit-out;
- network cross-connect and fiber installation;
- mobilization, installation and commissioning;
- restoration or decommissioning obligation.

### Recurring colo cost

- contracted critical-IT kW fee;
- metered power and PUE pass-through;
- cooling or facility-energy charge if not included;
- remote hands and security;
- connectivity and cross-connect charges;
- indexation and minimum-take provisions.

The CSV currently assumes $130/kW-IT/month and charges it on the installed 6.48MW member load. If the member reserves one third of a 20MW tranche, the contractual capacity may instead be 6.667MW. The schedule should distinguish:

```text
reserved IT capacity used for colo rent = 6.667MW
installed rack IT load used for engineering = 6.48MW
actual electrical load used for metered power = workload-dependent, with an idle floor
```

At $130/kW-month, using 6.48MW instead of 6.667MW understates the fixed colo charge by approximately 2.9%.

The $130 rate itself must be sourced from a term sheet and decomposed into included services, escalation, minimum term and exit costs.

---

## 4. Finance GB300 ChipCo with 35% equity, not one 63% chip loan

For a $270M member ChipCo sleeve, the recommended target structure is:

| Source | Share | Amount |
|---|---:|---:|
| Member/backer equity | **35%** | **$94.5M** |
| Senior GPU-backed debt | **42%** | **$113.4M** |
| OEM/vendor finance | **23%** | **$62.1M** |
| **Total** | **100%** | **$270.0M** |

This is consistent with the member's approximate $100M equity anchor while keeping senior debt around the intended 40–45% borrowing-base range.

The CSV currently uses 37% equity and a single 63% loan. That obscures materially different economics and terms. Senior debt and vendor finance must have separate columns for:

- initial commitment;
- draw dates;
- rate and benchmark;
- upfront and unused fees;
- amortization;
- security and ownership restrictions;
- balloon or purchase option;
- closing balance.

Vendor finance should not be assumed cheap. CoreWeave reported an approximately 10% effective rate on OEM and software-license financing at year-end 2025. Its filings also confirm that GPU facilities are sized using depreciable equipment cost, projected debt coverage and project conditions, rather than a blanket percentage of program CAPEX. See the [CoreWeave 2025 annual filing](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) and [Q1 2026 filing](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm).

A useful financing sensitivity is:

| Case | Equity | Senior GPU debt | Vendor finance |
|---|---:|---:|---:|
| Conservative fallback | 45% | 35% | 20% |
| **Target** | **35%** | **42%** | **23%** |
| Enhanced/seasoned | 25–30% | 45–50% | 20–25% |

The enhanced case should require actual backer support, prepayment, an NVIDIA/OEM backstop or seasoned operating history. It should not be assumed merely because the equipment exists.

---

## 5. PropCo must be separate and separately financed

The CSV currently draws the entire $60.7M member share of each owned block as construction equity. It then finances most of the remaining combined sleeve cost with the chip loan. This is the wrong asset/liability matching.

PropCo should have its own schedule with:

- land and site-development cost;
- shared campus backbone;
- grid and substation cost;
- building shell;
- electrical distribution;
- cooling plant;
- network meet-me rooms and external fiber;
- construction contingency;
- PropCo construction debt;
- PropCo equity;
- interest during construction;
- operating cost after commissioning.

Using the current $182M per 20MW-IT block:

| Per owned block | Whole JV | Per member |
|---|---:|---:|
| PropCo cost | $182.0M | $60.7M |
| Construction debt at 60% | $109.2M | $36.4M |
| Construction equity at 40% | $72.8M | $24.3M |
| Stabilized debt target at 65% | $118.3M | $39.4M |
| Stabilized equity at 35% | $63.7M | $21.2M |

The base construction case should be **40% equity / 60% debt**, with **35% / 65%** treated as a completion or stabilized target. The exact leverage depends on site control, permits, fixed-price EPC coverage, grid certainty and the credit support behind the member capacity obligations.

PropCo refinancing may be shown as an optional liquidity event, but not as an assumed reduction in economic cost. Refinancing returns cash while creating replacement debt service.

The Vantage €640M ABS is evidence that a European data-center takeout market exists, but it refinanced four operating, fully leased hyperscale data centers. It is not evidence that an unseasoned self-guaranteed construction project can issue ABS after a predetermined number of months. See [Vantage's transaction announcement](https://vantage-dc.com/fr/news/vantage-data-centers-completes-industrys-first-euro-based-data-center-asset-backed-securitization-abs-with-e640m-transaction/).

---

## 6. Do not allocate Rubin PropCo to GB300—but show parallel cash calls

The fact that PropCo construction begins while T1 is being deployed does not make that construction part of T1 ChipCo.

The member schedule should show concurrent modules:

```text
A. T1/T2 GB300 ChipCo in colo
B. T1/T2 colo deposits, rent and operating costs
C. shared Rubin campus development and backbone
D. T3 PropCo block
E. T3 Rubin ChipCo
F. later PropCo and ChipCo blocks
```

This will make the real liquidity requirement visible. At month zero, for example, the member may fund a GB300 deposit and early campus development simultaneously. That is a valid member cost-schedule output even though there is no inbound revenue.

Recommended liquidity outputs are:

- maximum one-month cash call;
- maximum three-month cash call;
- maximum twelve-month member funding;
- cumulative member equity;
- cumulative financing cost;
- each debt balance;
- committed-but-undrawn purchase obligations.

Because there are no inbound cash flows, “peak equity outstanding” and project payback are not meaningful CSV outputs. The focus should be the timing and magnitude of member cash paid.

---

## 7. FP8 normalization: use equal 20MW blocks

The revised FP8 framework is directionally correct. The primary comparison should now be:

```text
GB300 20MW-IT block      = 1.00×
Vera Rubin 20MW-IT block = approximately 2.43×
Rubin Ultra 20MW block   = TBD
```

Using one consistent set of NVIDIA dense FP8/FP6 training figures:

```text
GB300:
144 racks × 72 GPUs × 4.5 PFLOPS = 46.656 EFLOPS

Vera Rubin:
90 racks × 72 GPUs × 17.5 PFLOPS = 113.400 EFLOPS

20MW-block ratio:
113.400 / 46.656 = 2.43×
```

NVIDIA publishes the relevant product specifications on its [HGX platform page](https://www.nvidia.com/en-in/data-center/hgx/) and [Vera Rubin page](https://www.nvidia.com/en-gb/data-center/vera-rubin-nvl72/). The workbook should state explicitly whether figures are dense or sparse and should not mix chip-spec and rack-slide conventions within one ratio.

The most useful cost output is:

```text
member five-year cost
divided by
operating hours × member share of 20MW-block-equivalent FP8 output
```

Retain absolute $/PFLOPS-hour as a secondary audit metric.

The current extra measures—per-package equivalents, normalized GB300 watts, $/TFLOPS installed and $/GB300-W/month—create more opportunities for denominator mistakes than decision value. Keep only metrics with a clear business use and document each formula in the assumptions section.

---

## 8. Rubin Ultra specifications in v3 are not supportable

The CSV assigns Rubin Ultra:

- 34.7 dense FP8 PFLOPS per physical package;
- a 7.72× per-package multiplier;
- 144 packages/576 NVIDIA GPUs per physical rack;
- 600kW per rack;
- 33 physical racks per 20MW tranche;
- 5 EFLOPS per NVL576 domain.

These figures should not be used as a base case.

NVIDIA currently describes Vera Rubin Ultra NVL576 as a **576-GPU NVLink domain combining eight separate 72-GPU MGX racks**, not one physical 576-GPU cabinet. NVIDIA has not published a decision-grade dense FP8 specification for the Rubin Ultra GPU. See NVIDIA's current [Rubin Ultra NVL576 topology description](https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/).

Current July 2026 reporting also indicates continuing Kyber manufacturability and schedule uncertainty. Whether or not every reported redesign survives, that reinforces the option treatment already stated in the markdown.

Accordingly, T6/T7 should contain only:

- reserved site and electrical envelope;
- an optional earliest-possible window;
- a broad, clearly labeled placeholder budget;
- no fixed rack count, package count, FP8 multiplier or cost per normalized unit.

Required gates are:

1. NVIDIA/OEM topology freeze;
2. dense FP8 specification;
3. rack and domain power specification;
4. liquid-cooling and electrical reference design;
5. OEM price and delivery quote;
6. refreshed member financing and take-or-pay support.

Until then, the Ultra rows should be excluded from the base program total and presented only as an option scenario.

---

## 9. Construction and hardware timing need three cases

### GB300 in existing colo

The CSV uses a six-month interval from buyout to online. That is a reasonable base planning duration, but “buyout” should not mean paying and drawing 100% of the equipment loan on day one.

A realistic payment schedule is likely to include:

- order deposit;
- manufacturing/progress payment;
- payment at factory acceptance;
- payment at delivery;
- retention until site acceptance.

Debt should draw against eligible paid equipment and normally begin close to shipment or acceptance, not automatically six months before service. The schedule should include commitment fees and interest only on actually drawn debt.

Recommended operating-date cases from notice to proceed are:

| Case | Conditions | Time to service |
|---|---|---:|
| Accelerated | integrated racks allocated; AI-ready colo; long-lead network reserved | 16 weeks |
| **Base** | moderate colo fit-out and phased OEM delivery | **20–24 weeks** |
| Downside | component procurement, cooling/network delays or substantial fit-out | 28–40 weeks |

If the consortium acquires components before ODM assembly, use at least 25 weeks for procurement, 8–12 weeks for integration/FAT and 4–6 weeks for delivery/commissioning, with overlap modeled explicitly.

### New Rubin PropCo campus

The CSV places T3 online after 15 months of construction. For a genuinely new French campus, that should be the accelerated case. The base case should be 22–24 months from binding site/grid readiness, with a 30–36 month downside where permits or transmission work are required.

| Case | T3 service date from PropCo notice to proceed |
|---|---:|
| Accelerated powered/brownfield site | 18–21 months |
| **Base new PropCo build** | **22–24 months** |
| Grid/permitting downside | 30–36 months |

Follow-on blocks can then target four-to-six-month intervals if the common substation, cooling backbone, utility corridors and repeatable block design were sized in advance.

RTE's “fast-track” label does not mean generic energization in a few months. Its first disclosed Campus IA agreement provides an initial power block by the end of 2027 under a specifically allocated program. See the [RTE Campus IA announcement](https://www.rte-france.com/actualites/campus-ia-rte-signent-contrat-raccordement-accelere-campus-infrastructures-numeriques).

The schedule must be driven by actual gates:

- binding site control;
- RTE/utility connection agreement and energization date;
- environmental and planning status;
- EPC notice to proceed;
- long-lead electrical and cooling orders;
- mechanical completion;
- staged commissioning;
- hardware delivery and FAT/SAT.

---

## 10. Refresh reserve: show cash and asset separately

`JV3_financial_model.md` calls for an 8–12% annual refresh reserve from year two, but `jv_economics_v3.csv` excludes it. It should be added because this is specifically a member cash schedule.

However, reserve contributions are not automatically economic expense. Until spent, the ending reserve is restricted cash owned by the member/sleeve.

Show two totals:

1. **five-year cash cost excluding unspent reserve**;
2. **total member funding including reserve contributions**, with ending reserve shown as an asset.

The preferred formula is:

```text
required refresh cash
= target equity for replacement hardware
− expected net sale proceeds from old hardware
− committed refresh financing

monthly reserve
= required refresh cash / months remaining to refresh
```

Retain 8%, 10% and 12% of ChipCo CAPEX as comparison cases only. A flat 10% contribution over four years accumulates only 40% of original ChipCo cost; whether that is sufficient depends on replacement cost, residual value and expected refresh leverage.

---

## 11. Electricity, utilization and FX

The schedule still multiplies power directly by 90%, while the markdown says energy should contain an idle-draw floor. Separate:

- reserved IT capacity;
- installed rack IT load;
- availability;
- workload/GPU utilization;
- electrical load factor;
- idle electrical draw;
- PUE.

A simple formula is:

```text
IT load factor
= idle draw percentage
+ utilization × (1 − idle draw percentage)

facility energy
= installed IT MW × IT load factor × PUE × hours
```

The €90/MWh input must also be labeled either wholesale energy or delivered power. A delivered-power build should include energy, network tariff, electricity taxes, balancing/supplier margin, guarantees and hedging costs.

EDF's CAPN product requires an upfront contribution and shares nuclear-production cost and volume risk; it is not simply a fixed €70/MWh PPA. Treat it as a procurement scenario. See [EDF's CAPN terms](https://www.edf.fr/groupe-edf/edf-en-bref/optimisation-et-trading/souscription-capn).

The CSV uses $1.08/€. The ECB reference rate on 10 July 2026 was $1.143/€. FX should be an explicit dated input with base and hedge/stress cases, not a hard-coded conversion. See the [ECB reference-rate page](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.pl.html).

---

## 12. Public capital should remain outside the base cost schedule

The user has explicitly chosen not to make member economics dependent on EU or French public funding. That is the correct base-case treatment.

The markdown should reduce the public-capital discussion to an optional note or scenario:

```text
EU/France support option
Potential member-cash reduction: TBD
Included in base case: no
Subject to public ownership/access-time and governance conditions
```

The EuroHPC 17% contribution is not a free unrestricted grant. The regulation links it to ownership or guaranteed access time and requires participating-state matching and public governance rights. See [Council Regulation (EU) 2026/150](https://www.eurohpc-ju.europa.eu/document/download/2eebc3f6-bd4d-4908-8e55-db5e8d588051_en?filename=EuroHPC+Regulation+2026-150.pdf).

It should not reduce base ChipCo or PropCo equity in either reviewed file.

---

## 13. Specific inconsistencies to remove from `JV3_financial_model.md`

The next revision should correct the following:

1. **GB300 price:** replace $3.8M/rack plus 15% with a $270M/member ChipCo base and quoted sensitivity.
2. **GB300 PropCo:** remove $182M owned PropCo from T1/T2; they are deployed in colo.
3. **Program totals:** rebuild every cumulative total after separating GB300 colo, Rubin PropCo and each ChipCo.
4. **Financing:** replace 50/32/18 as the sole base with separate target stacks:
   - GB300 ChipCo: 35% equity / 42% senior / 23% vendor;
   - PropCo construction: 40% equity / 60% debt;
   - stabilized PropCo target: 35% equity / 65% debt.
5. **T1 example:** remove the $270M example that currently combines only $210M ChipCo with PropCo and omits vendor debt service from the stated DSCR.
6. **FP8 credits:** replace the legacy $/credit table based on 3.33×/6.94× with the equal-20MW method: GB300 1.00×, Rubin 2.43×, Ultra TBD.
7. **Rubin Ultra:** delete fixed 34.7 PF/package, 33-rack, 600kW and $/credit conclusions until platform freeze.
8. **Commitment language:** T1/T2 are actionable planning; T3/T5 remain provisional; T6/T7 are options and must not be included in a “firm” total.
9. **Refresh:** describe the reserve as a liquidity requirement and balance-sheet asset until spent.
10. **Public funding:** keep it outside the base case and describe its access/ownership consequences.
11. **Timeline:** distinguish accelerated, base and downside construction cases.
12. **Document identity:** rename the markdown to v3 when it actually incorporates the v3 cost-schedule architecture.

---

## 14. Specific corrections to `jv_economics_v3.csv`

The CSV should be rebuilt around these rows and instruments:

### Assumptions

- GB300 ChipCo base: $270M/member/tranche;
- GB300 ChipCo range: $229–345M;
- contracted colo IT capacity and installed IT MW separately;
- senior GPU loan terms;
- vendor-finance terms;
- PropCo construction debt terms;
- PropCo equity contribution;
- equipment deposit/progress/acceptance schedule;
- refresh target and reserve formula;
- idle-power floor;
- dated FX rate;
- FP8-per-20MW ratios: 1.00× / 2.43× / TBD.

### Monthly cash flow

Add separate columns for:

- ChipCo deposit;
- ChipCo progress payment;
- ChipCo final acceptance payment;
- member ChipCo equity;
- senior GPU debt draw/payment/balance;
- vendor-finance draw/payment/balance;
- PropCo construction spend;
- member PropCo equity;
- PropCo debt draw/payment/balance;
- interest during construction;
- financing and commitment fees;
- colo deposit and fit-out;
- recurring colo rent;
- electricity;
- owned-campus Opex;
- refresh-reserve contribution;
- ending refresh cash;
- total member cash out.

### Outputs

Report separately:

- firm path T1–T5;
- optional full path T1–T7;
- GB300 colo cost;
- Rubin PropCo cost;
- each ChipCo cost;
- maximum monthly/quarterly/twelve-month member funding;
- total interest by instrument;
- total five-year operating cost;
- ending debt by instrument;
- ending refresh reserve;
- $/20MW-block-equivalent FP8 hour;
- absolute $/PFLOPS-hour.

Do not describe cumulative member cash as project TCO without reconciling ending debt, restricted cash and residual assets.

---

## 15. Recommended planning cases

The cost schedule should carry at least these cases:

| Driver | Low/accelerated | Base | Downside |
|---|---:|---:|---:|
| GB300 ChipCo/member | $229M | **$270M** | $345M |
| GB300 time to service | 16 weeks | **20–24 weeks** | 28–40 weeks |
| GB300 equity | 30% | **35%** | 45% |
| Senior GPU advance | 45–50% | **42%** | 35% |
| Vendor finance | 20–25% | **23%** | 20% |
| PropCo construction equity | 35% | **40%** | 50% |
| T3 PropCo delivery | 18–21mo | **22–24mo** | 30–36mo |
| Power | €70/MWh procurement case | **delivered €90/MWh input** | €105–120/MWh |
| GPU life | 5yr | **5yr** | 3–4yr |
| Rubin FP8/20MW | — | **2.43× GB300** | re-set at quote/spec freeze |
| Rubin Ultra FP8/20MW | **TBD** | **TBD** | option not exercised |

No public grant should appear in these base operating cases.

---

## Conclusion

The model's next decision-useful version is not a larger project-finance workbook. It is a cleaner member cost and liquidity schedule with correct asset separation.

The core architecture should be:

```text
GB300 ChipCo in colo
  approximately $270M/member/tranche
  35% equity / 42% senior GPU debt / 23% vendor finance

GB300 colo
  separate deposits, fit-out, rent and metered power

Rubin PropCo
  separately owned and financed
  40% equity / 60% construction debt
  35% / 65% stabilized target

Rubin ChipCo
  separately quoted and financed at platform freeze

FP8 comparison
  GB300 20MW block = 1.00×
  Rubin 20MW block = approximately 2.43×
  Rubin Ultra = TBD
```

Once the files implement that structure, the schedule will answer the user's actual question: **how much cash does one member need, at what times, to own a staged share of this compute program?**
