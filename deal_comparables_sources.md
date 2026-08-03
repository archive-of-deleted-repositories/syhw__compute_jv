# Bibliography & Source Verification — `deal_comparables.md`

Full sourcing behind the comparables. Each claim is mapped to a **primary source** (SEC filing, company press release, rating-agency report, regulator publication) where one exists, or clearly-labelled credible secondary reporting where the primary is paywalled/private. Confidence is graded **High / Med / Low**. A **Corrections** block at the top lists every figure that was wrong or imprecise in the original `deal_comparables.md` — these have been applied to that file.

**Method:** five focused agents ran a citation-only pass (SEC EDGAR via authenticated `curl`; rating-agency presales from KBRA / DBRS Morningstar / S&P; company IR; BIS/IMF/FSB; trade press IFR/Bloomberg/Reuters). ~120 tool calls total. Where a primary document sits behind a paywall (IFR, Moody's, SemiAnalysis), the figure is corroborated across multiple secondary outlets and flagged.

---

## ⚑ Corrections applied to `deal_comparables.md`

| # | Original claim | Correction | Source |
|---|---|---|---|
| C1 | GPU-backed private-credit debt "low-teens %" | **Mid-teens (~14–15%) at inception** (CoreWeave DDTL 1.0, 2023); compressed to ~10.5% blended (DDTL 2.0) and to **IG pricing SOFR+2.25% / ~5.9% by 2026** (DDTL 4.0) | CoreWeave S-1; Blackstone PR |
| C2 | "ABS premium over CMBS ~100–150 bps" | **Inverted.** The ~100–150 bps premium is structured DC debt (ABS/CMBS) **over hyperscale corporate/IG bonds**. Between the two, **CMBS prices *wider* than ABS** (ABS is tighter). | Penn Mutual AM; KBRA |
| C3 | Meta Hyperion "~$27–30B" | **~$27B development cost** (Meta PR); bond tranche **$27.294B**. "$30B" is press rounding incl. equity/contingency. | Meta PR; IFR |
| C4 | Meta equity "~$2.5B" | Primary figures: **Blue Owl ~$7B cash contribution / Meta ~$3B one-time distribution**; "$2.5B" was pre-close Bloomberg reporting. Residual-value guarantee is **capped to first 16 years**, not open-ended. | Meta PR |
| C5 | Microsoft "~62% of revenue" | **62% in FY2024 → ~67% (or ~71% in Q2'25) FY2025.** | CoreWeave S-1 & 10-K |
| C6 | OpenAI "$11.9B + $4B" | Grew to **~$22.4B** with the **+$6.5B Sept 2025** expansion (on top of $11.9B Mar 2025 + $4B May 2025). | CoreWeave 10-K; PR |
| C7 | CoreWeave "DDTL 2.0 $7.5B" | Facility documented at **$7.6B** in the S-1 ("$7.5B" is the press headline). Blackstone **lead**, Magnetar **co-lead**. | CoreWeave S-1 |
| C8 | Vantage / Switch "KBRA" | Vantage NA ($1.35B) and EMEA (€640M) were rated by **S&P** (EMEA also **Scope**), not KBRA. Switch 2024-1 by **DBRS**. | Issuer PRs; DBRS |
| C9 | "BX 2023-VLT2/VLT3 … DC ABS" | These are **CMBS (SASB) trusts rated by DBRS**, not ABS — recategorized. | DBRS |
| C10 | Moody's "$662B off balance sheet via JVs/SPVs" | Specifically **$662B of data-center lease commitments *not yet commenced*** (off-B/S under GAAP); $969B total undiscounted; ~113% of the five hyperscalers' combined adjusted debt. | Moody's (via reporting) |
| C11 | DSCR "~1.25x", debt yield "7–10%" | **Not a universal standard** — varies materially by deal (Low confidence). Retained as indicative only. | Aligned presale |
| C12 | Take-or-pay wording "regardless of actual utilization" | Exact Nebius–Microsoft contract language is **"irrespective of the actual usage or consumption"** (SEC 20-F Ex. 4.4). | Nebius 20-F |

**Unverified / flagged (left in `deal_comparables.md` with a caveat, not asserted as fact):** Burry fund *deregistration*; SemiAnalysis exact "$8/hr→38% IRR / $4.92/hr breakeven" trio (paywalled); **A2 Capital** role in the Mistral JV; **"OpCore"** and **"Data4"** in the SoftBank–Le Bosquel deal (SoftBank's primary release names Sesterce, EDF/Bouchain, Schneider/Dunkirk).

---

## §1 — CoreWeave

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| DDTL 1.0 | **$2.3B**; loan agmt **30 Jul 2023** (announced 3 Aug); **Magnetar + Blackstone** lead, +Coatue/DigitalBridge/BlackRock/PIMCO/Carlyle; **~14–15%** floating (post-2024 amend: SOFR+9.62%) | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) · [Blackstone PR](https://www.blackstone.com/news/press/coreweave-secures-2-3-billion-debt-financing-facility-led-by-magnetar-capital-and-blackstone-to-meet-surging-demand-and-ongoing-expansion-of-specialized-cloud-infrastructure-to-power-ai/) | SEC + PR | High |
| DDTL 2.0 | **$7.6B** facility (agmt 16 May 2024) / "$7.5B" headline; **Blackstone lead, Magnetar co-lead**, Coatue; +Carlyle, CDPQ, DigitalBridge, BlackRock, Eldridge, Great Elm; **~10.5% blended** YE2024, tiered **SOFR+6% (IG) / +13% (non-IG)** | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) · [Blackstone PR](https://www.blackstone.com/news/press/coreweave-secures-7-5-billion-debt-financing-facility-led-by-blackstone-and-magnetar/) | SEC + PR | High |
| Later facilities | **DDTL 2.1 $3.0B** (Sep 2025); **DDTL 3.0 $2.6B** (31 Jul 2025, SOFR+4%, OpenAI); **DDTL 4.0 $8.5B** (30 Mar 2026, **first IG GPU-backed, A3/A(low)**); **DDTL 5.0 $3.1B** (May 2026, first publicly syndicated HPC-backed); revolver **$2.5B**; OEM/software **~$5.2B**; notes $2.0B/$1.75B/$2.6B conv.; **total debt $21.6B** YE2025 | [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) · [DDTL 4.0 PR](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-Landmark-8-5-Billion-Financing-Facility-Achieving-First-Investment-Grade-Rated-GPU-backed-Financing/default.aspx) | SEC + PR | High |
| GPU borrowing-base | Verbatim: *"total loans available are constrained by the purchase price of assets … based upon the depreciable cost of GPU servers"* | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) | SEC | High |
| Security / SPV | First-priority pledge of **SPV equity + substantially all SPV assets**; SPVs = **CoreWeave Compute Acquisition Co.** (CCAC II/IV/V/VII/VIII) | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) | SEC | High |
| Microsoft concentration | **62% FY2024 → ~67% FY2025** (~71% Q2'25) | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) · [10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) | SEC | High |
| OpenAI contracts | **$11.9B** (7 Mar 2025) + **$4B** (May 2025) + **$6.5B** (25 Sep 2025) → **~$22.4B** | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) · [$6.5B PR](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx) | SEC + PR | High |
| NVIDIA | **>5% owner** (~$250M invested); **$6.3B capacity backstop** through 13 Apr 2032; first **"Elite" CSP** | [$6.3B backstop](https://nvidianews.nvidia.com/news/nvidia-and-coreweave-strengthen-collaboration-to-accelerate-buildout-of-ai-factories) · ["Elite" PR](https://www.coreweave.com/blog/coreweave-becomes-nvidias-first-elite-cloud-services-provider-for-compute) | PR/SEC | High |
| Contract duration | Weighted-avg **~4 years** (31 Dec 2024) | [S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm) | SEC | High |

## §2 — Hyperscaler JV / SPV templates

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Meta Hyperion size | **~$27B dev cost**; bond **$27.294B** | [Meta PR](https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/) · [IFR](https://www.ifre.com/ifr-awards/2327933/financing-package-blue-owl-capitalbeignet-investors-us27.3bn-23.6-year-bond) | PR + trade | High |
| Bond terms | **6.581%**, **T+225bp**, **A+ (S&P, single agency)**, due **30 May 2049**, 23.6yr fully amortizing | [IFR](https://www.ifre.com/ifr-awards/2327933/financing-package-blue-owl-capitalbeignet-investors-us27.3bn-23.6-year-bond) | trade | High |
| Ownership / equity | **Blue Owl 80% / Meta 20%**; **Blue Owl ~$7B cash / Meta ~$3B distribution** | [Meta PR](https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/) | PR | High |
| SPV / arranger | SPV **Beignet Investor LLC**; **PIMCO** anchor (~$18B); **Morgan Stanley** sole underwriter + JV structuring adviser | [IFR](https://www.ifre.com/ifr-awards/2327933/financing-package-blue-owl-capitalbeignet-investors-us27.3bn-23.6-year-bond) | trade | High |
| Backstop / off-B/S | **Residual-value guarantee capped to first 16 years**; 4-yr initial operating lease + extensions; JV unconsolidated (off-B/S) | [Meta PR](https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/) | PR | High |
| xAI Colossus | **$5B debt + $5B equity**, Morgan Stanley, 1 Jul 2025 | [MS (X)](https://x.com/MorganStanley/status/1939768047780172184) · [TechCrunch](https://techcrunch.com/2025/07/01/xai-raises-10b-in-debt-and-equity/) | Co. + press | High |
| xAI GPU SPVs | **Valor Compute Infrastructure (VCI)** raised **$5.4B** (Apollo $3.5B; NVIDIA backer), triple-net-leases GPUs to xAI; separate **~$20B lease-to-own SPV** (~$7.5B equity / $12.5B debt; NVIDIA up to $2B) for Colossus 2 | [DCD](https://www.datacenterdynamics.com/en/news/valor-equity-partners-raises-54bn-to-buy-nvidia-gpus-for-xai/) · [Bloomberg](https://www.bloomberg.com/news/articles/2025-10-07/musk-s-xai-nears-20-billion-capital-raise-tied-to-nvidia-chips) | trade + Bloomberg | High/Med |
| Crusoe/Stargate | JV **Crusoe + Blue Owl + Primary Digital**; **$3.4B** initial (Oct 2024; JPMorgan $2.3B loan); **$11.6B** (May 2025); **~$15B** total 1.2GW Abilene | [Crusoe PR](https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture) · [Bloomberg](https://www.bloomberg.com/news/articles/2025-01-22/jpmorgan-lends-2-3-billion-for-blue-owl-tied-oracle-data-center) | PR + Bloomberg | High |
| Oracle lease | ~**15-yr Oracle lease**; OpenAI end-user | [Crusoe PR](https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture) | PR | High/Med |

## §3 — Neoclouds (incl. Nebius)

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Nebius–Microsoft | **$17.4B through 2031**, expandable **$19.4B**, **5-yr**, 8 Sep 2025, Vineland NJ | [Nebius PR](https://nebius.com/newsroom/nebius-announces-multi-billion-dollar-agreement-with-microsoft-for-ai-infrastructure) · [6-K](https://www.sec.gov/Archives/edgar/data/0001513845/000110465925088312/tm2525580d1_6k.htm) | PR + SEC | High |
| Take-or-pay wording | *"…obligated to pay the Fees … irrespective of the actual usage or consumption…"* | [20-F Ex. 4.4](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926052948/nbis-20251231xex4d4.htm) | SEC (contract) | High |
| NVIDIA in Nebius | **$700M** placement Dec 2024 (Accel/NVIDIA/Orbis; ~0.5% stake); **~$2B via pre-funded warrants, ~8.3% stake** (11 Mar 2026), targeting 5GW by 2030 | [Nebius PR](https://nebius.com/newsroom/nebius-announces-oversubscribed-strategic-equity-financing-of-usd-700-million-to-accelerate-roll-out-of-full-stack-ai-infrastructure) · [CNBC](https://www.cnbc.com/2026/03/11/nebius-nvidia-ai-cloud.html) | PR + press | High/Med-High |
| Post-Yandex cash | ~**$5.4B** asset sale; **>$2B cash**; Nasdaq relisted 21 Oct 2024 | [6-K](https://www.sec.gov/Archives/edgar/data/0001513845/000110465924105281/tm2425437d1_ex99-1.htm) | SEC | Med-High |
| Nebius convertibles | **$1.0B** (Jun 2025: $500M 2.00%'29 + $500M 3.00%'31); **$2.75B** senior conv. (Sep 2025), part of ~$4.2B raise | [FWP](https://www.sec.gov/Archives/edgar/data/0001513845/000110465925088873/tm2525503d5_fwp.htm) | SEC | High |
| Lambda | **$500M** Macquarie GPU facility (2 Apr 2024); **Series D ~$480M** (Feb 2025, ~$2.5B val); **Series E ~$1.5B** (Nov 2025); Microsoft deal 3 Nov 2025 (undisclosed) | [Lambda PR](https://www.businesswire.com/news/home/20240402148086/en/Lambda-Announces-$500M-GPU-Backed-Facility-to-Expand-Cloud-for-AI) · [TechCrunch](https://techcrunch.com/2025/11/18/ai-data-center-provider-lambda-raises-whopping-1-5b-after-multibillion-dollar-microsoft-deal/) | PR + press | High/Med-High |
| Applied Digital | **250MW Ellendale ND ~$7B** (2 Jun 2025) + **150MW** (Aug 2025) → **~400MW, ~$11B** aggregate; two **~15-yr** CoreWeave leases | [APLD PR](https://ir.applieddigital.com/news-events/press-releases/detail/123/applied-digital-announces-250mw-ai-data-center-lease-with) | IR PR | High |

## §4 — Debt benchmarks

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Construction spread | ~**SOFR + 250–400 bps** (senior, leased); market range, not a fixed benchmark | [CREFC E-Primer](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf) | industry | Med |
| Senior LTV | **65–70%** (Aligned Class A capped at **70% LTV**) | [ASR/S&P](https://asreport.americanbanker.com/news/aligned-data-centers-presents-350-million-to-the-abs-market) | trade→agency | High |
| DSCR / debt yield | **No universal ~1.25x / 7–10% standard** — deal-specific | [ASR](https://asreport.americanbanker.com/news/aligned-data-centers-presents-350-million-to-the-abs-market) | trade | Low |
| GPU-debt cost | **~15% (mid-teens) at inception (2023)** → ~10.5% (2024) → **IG SOFR+2.25%/~5.9% (2026)** | [Qz](https://qz.com/gpu-collateralized-debt-ai-neocloud-coreweave-financing-risks-050526) · [DDTL 4.0 PR](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-Landmark-8-5-Billion-Financing-Facility-Achieving-First-Investment-Grade-Rated-GPU-backed-Financing/default.aspx) | trade + PR | Med-High |
| ABS vs CMBS | Premium is **structured DC debt over hyperscale corporate bonds (~100–150bps)**; **CMBS wider than ABS** | [Penn Mutual AM](https://www.pennmutualam.com/market-insights-news/blogs/chart-of-the-week/2025-10-09-pricing-the-infrastructure-boom-data-center-trends-in-structured-markets) · [KBRA](https://www.kbra.com/publications/wtXJZSZt) | research | Med |
| Issuance volume | **≥$200B in 2025**; **Morgan Stanley projects $250–300B for 2026** (hyperscalers + JVs) | [Bloomberg via EnergyNow](https://energynow.com/2026/02/the-3-trillion-ai-data-center-build-out-becomes-all-consuming-for-debt-markets/) | trade/news | High |

## §5 — Data-center ABS deals

| Deal | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Aligned DC Issuer LLC | Master trust; **2022-1 $350M Class A-2 S&P A-, 70% LTV**, 6 campuses $3.8B appraised; A1FCF **AAA (KBRA/Fitch)**; inaugural 2021-1 part of **$1.725B** financing | [S&P presale](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/12812725) · [Aligned PR](https://aligneddc.com/blog/aligned-sets-record-for-largest-ever-inaugural-data-center-securitization-as-part-of-1-725-billion-in-structured-sustainable-debt-financing/) | agency + PR | High |
| Vantage NA Issuer LLC | **2023-1/2 $1.35B**, **S&P: A- / BBB-**, Oct 2023 (not KBRA) | [Vantage PR](https://vantage-dc.com/news/vantage-data-centers-raises-usd1.35-billion-in-securitized-notes-for-north-american-platform) | PR (cites S&P) | High |
| Vantage EMEA | **€640M** (+€80M VFN), **first euro DC ABS**, **Class A-2 A- / B BBB- (S&P + Scope)**, Jun 2025, 4 German DCs, green bond | [Vantage PR](https://vantage-dc.com/news/vantage-data-centers-completes-industrys-first-euro-based-data-center-asset-backed-securitization-abs-with-e640m-transaction/) | PR | High |
| Switch 2024-1 | DBRS: **A-1-L A(sf), A-2 A(low)(sf), B BBB(low)(sf)**, 15 Mar 2024 | [DBRS](https://dbrs.morningstar.com/research/429395/morningstar-dbrs-finalizes-provisional-credit-ratings-on-switch-abs-issuer-llc-series-2024-1) | agency | High |
| Compass II 2024-1 | **DBRS** (not KBRA); senior **(P)AAA(sf)**; Guggenheim-structured | [DBRS](https://dbrs.morningstar.com/research/429104/compass-datacenters-issuer-ii-llc-series-2024-1-rating-report) | agency | Med-High |
| Centersquare (CyrusOne-adjacent colo) | **Centersquare Issuer LLC**, **KBRA**, Series **2025-1 … 2025-7**; 2025-1/2 = 26 DCs, ~$438.8M AMRR | [KBRA](https://www.kbra.com/publications/rnrKqqXt/kbra-assigns-preliminary-ratings-to-centersquare-series-2025-1-and-series-2025-2) | agency | Med-High |
| Flexential 2026 | **$2.1B** (Series 2026-1/2/3/4), **largest-ever DC + green-bond ABS**; 28 DCs, ~$663M ann. rev, ~199MW; **Class A2 A- (KBRA)**; ARD Mar 2031 | [KBRA](https://www.kbra.com/publications/HxrLsNRT/) · [BusinessWire](https://www.businesswire.com/news/home/20260312837230/en/) | agency + PR | High |
| BX 2023-VLT2/3 (QTS/Blackstone) | **CMBS (SASB), DBRS-rated** — *not ABS*; sponsor QualityTech LP/Blackstone | [DBRS](https://dbrs.morningstar.com/research/423356/dbrs-morningstar-finalizes-provisional-ratings-on-bx-commercial-mortgage-trust-2023-vlt3) | agency | High |

## §6 — GPU depreciation / residual value

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Microsoft server life | **4→6 yrs** FY23 (eff. 1 Jul 2022); +$3.7B op income FY23 | [MSFT FY23 10-K](https://microsoft.gcs-web.com/static-files/e2931fdb-9823-4130-b2a8-f6b8db0b15a9) | SEC | High |
| Google server life | **4→6 yrs** (Jan 2023); ~$3.4B less 2023 depreciation | [DCD](https://www.datacenterdynamics.com/en/news/google-increases-server-life-to-six-years-will-save-billions-of-dollars/) | reporting | High |
| Amazon server life | →6 yrs (2022), then **6→5 yrs** eff. 1 Jan 2025 (−$0.7B op income; cited AI pace) | [DeepQuarry](https://deepquarry.substack.com/p/amazon-revises-server-lifespan-amid) | reporting | High |
| Burry critique | *"artificially boosts earnings… one of the more common frauds of the modern era"*; **~$176B** cumulative understated depreciation 2026–28; Q3'25 13F puts **~$187M** NVIDIA / **~$912M** Palantir notional | [Burry (X)](https://x.com/michaeljburry/status/1987918650104283372) · [CNBC](https://www.cnbc.com/2025/11/11/big-short-investor-michael-burry-accuses-ai-hyperscalers-of-artificially-boosting-earnings.html) | primary + reporting | High |
| Moody's off-B/S | **$662B of not-yet-commenced DC lease commitments** off-B/S; $969B total undiscounted; ~113% of 5 firms' adj. debt | [Yahoo/Moody's](https://finance.yahoo.com/news/moody-flags-662-billion-risk-081000616.html) | reporting | High |
| SemiAnalysis economics | GPU IRR/breakeven models; H100 ~$8/hr peak → ~$2–3/hr. **Exact "$8→38% IRR / $4.92 breakeven" is paywalled — unconfirmed verbatim** | [SemiAnalysis](https://newsletter.semianalysis.com/p/ai-neocloud-playbook-and-anatomy) | primary (paywall) | Low-Med |

## §7 — Circular financing

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| NVIDIA–OpenAI | LOI 22 Sep 2025: **≥10GW**, up to **$100B** ($10B first tranche), first GW H2 2026 | [NVIDIA PR](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems) | PR | High |
| NVIDIA–CoreWeave | **$6.3B** backstop through 13 Apr 2032 | [Fool/SEC](https://www.fool.com/investing/2025/10/05/coreweave-nvidia-6-3-billion-backstop-explained/) | reporting | High |
| NVIDIA–xAI | ~**$2B** equity into $20B Series E SPV (Jan 2026) | [xAI](https://x.ai/news/series-e) | PR | High |
| BIS warning | 2026 Annual Report (28 Jun 2026): >$1T AI capex 2025–26 outpacing FCF; circular financing; direct-lending funds **quadrupled** AI/IT lending to ~15%; "same asset pledged multiple times" | [BIS AR 2026](https://www.bis.org/publ/arpdf/ar2026e1.htm) · [Bulletin](https://www.bis.org/publ/bisbull120.pdf) | regulator | High |
| IMF / FSB | IMF GFSR Oct 2025; FSB 10 Oct 2025 AI-vulnerabilities report | [IMF](https://www.imf.org/en/publications/gfsr/issues/2025/10/14/global-financial-stability-report-october-2025) · [FSB](https://www.fsb.org/2025/10/monitoring-adoption-of-artificial-intelligence-and-related-vulnerabilities-in-the-financial-sector/) | regulator | High |
| OpenAI economics | ~**$13B revenue vs ~$34B cost → ~$20.9B operating loss** 2025 (reported/leaked, not filed) | [Fortune](https://fortune.com/2026/06/16/openai-financials-leaked-losses-revenue-profit/) | reporting | Med-High |

## §8 — European / French precedents

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Mistral campus | **MGX + Bpifrance + Mistral + NVIDIA** JV, up to **1.4GW**; construction H2 2026, ops 2028; first node **44MW Bruyères-le-Châtel (Eclairion), ~18,000 GB200**; scaled to 3GW ("Campus AI"); Mistral **~$830M** debt (7 banks). **A2 Capital role unverified.** | [NVIDIA blog](https://blogs.nvidia.com/blog/france-advances-europes-ai-future/) · [DCD](https://www.datacenterdynamics.com/en/news/mgx-bpifrance-nvidia-and-mistral-ai-plan-14gw-paris-data-center-campus/) | blog + reporting | High |
| SoftBank/Sesterce Le Bosquel | **SoftBank + Sesterce** (SoftBank majority) selected for **1GW** at Le Bosquel; 31 May 2026; part of SoftBank **5GW / up to €75B** France commitment. **"OpCore"/"Data4" not in primary release** (names Sesterce, EDF/Bouchain, Schneider/Dunkirk) | [SoftBank PR](https://group.softbank/en/news/press/20260531) | PR | High |
| French/EU public capital | **France 2030 €54B** (via Bpifrance / CDC / ADEME / ANR); **InvestAI ~€200B** (€20B for 4–5 AI gigafactories); Macron **€109B** AI package (Feb 2025; incl. MGX €30–50B, Brookfield €20B) | [CSIS](https://www.csis.org/analysis/frances-ai-action-summit) · [Bloomberg](https://www.bloomberg.com/news/articles/2025-02-09/france-to-announce-109-billion-in-ai-investments-macron-says) | think-tank + reporting | Med-High |

## §9 — Take-or-pay anatomy

| Claim | Verified | Source | Type | Conf |
|---|---|---|---|---|
| Exact floor language | Nebius–Microsoft: *"irrespective of the actual usage or consumption"* | [20-F Ex. 4.4](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926052948/nbis-20251231xex4d4.htm) | SEC | High |
| CoreWeave contracts | Pay through lease end even if unused (except nonperformance); MSFT ~71% Q2'25 rev; $8.5B facility collateralized by Meta contracts | [Yahoo/filings](https://finance.yahoo.com/news/data-center-operator-coreweave-stock-130000056.html) | reporting | Med-High |
| Oracle–Crusoe wrapper | Newmark arranged **$2.3B** loan; **Oracle IG "credit wrapper"** makes it bankable; Oracle leases + subleases to OpenAI; Oracle lease commitments **+150%** (Dec 2025) | [CNBC](https://www.cnbc.com/2025/12/11/oracle-lease-commitments-increase-almost-150percent-to-accommodate-ai-demand.html) | reporting | Med-High |
| Lease accounting | **ASC 842** (operating vs finance, 5 criteria) vs **IFRS 16** (single on-B/S model); embedded-lease test for colocation | [PwC Viewpoint](https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/leases/leases__4_US/chapter_2_scope__1_US/24_separating_lease__US.html) | accounting | High |
| Litigation / off-B/S risk | Emerging AI-DC financing litigation risks | [Quinn Emanuel](https://www.quinnemanuel.com/the-firm/publications/client-alert-emerging-litigation-risks-in-financing-ai-data-centers-boom/) | law firm | High |

---

*Compiled via a citation-only verification pass. Paywalled primaries (IFR, Moody's, SemiAnalysis) are corroborated by multiple secondary outlets and flagged. Re-pull the SEC/agency primaries into the data room before any IC vote.*
