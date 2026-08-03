# Deal Comparables & Precedents — GPU / AI-Infra Financing

Evidence base for the JV financing plan. Figures are drawn from public SEC filings (CoreWeave, Nebius, Oracle), company press releases, rating-agency presales (KBRA / DBRS Morningstar / S&P / Moody's / Fitch), regulator publications (BIS/IMF/FSB), and credible reporting (Bloomberg, FT, Reuters, WSJ, IFR), plus analyst work (SemiAnalysis).

> **Sourcing:** every claim below is mapped to a primary-source URL with a confidence grade in the companion bibliography **`deal_comparables_sources.md`**. That file also lists the corrections from a citation-verification pass — all of which have been applied to this document. A handful of items remain flagged as unverified (Burry fund deregistration; SemiAnalysis's exact IRR/breakeven figures; A2 Capital's role in the Mistral JV; "OpCore"/"Data4" in the SoftBank–Le Bosquel deal). Re-pull the SEC/agency primaries into the data room before any IC vote.

---

## 1. CoreWeave — the canonical GPU-backed debt playbook

CoreWeave is the closest public template for what we're building: a non-hyperscaler that financed an NVIDIA GPU fleet with **asset-level debt secured on the chips and on take-or-pay contracts**, in ring-fenced SPVs, then recycled into cheaper capital as it scaled.

| Facility | ~Size | Date | Lead capital | Key terms |
|---|---:|---|---|---|
| DDTL 1.0 (delayed-draw term loan) | **$2.3B** | Jul 2023 | Magnetar + Blackstone lead; +Coatue, DigitalBridge, BlackRock, PIMCO, Carlyle | GPU-collateralized; **~14–15%** floating (mid-teens at inception) |
| DDTL 2.0 | **$7.6B** (agmt) / $7.5B headline | May 2024 | **Blackstone lead, Magnetar co-lead**, Coatue; +Carlyle, CDPQ, DigitalBridge, BlackRock, Eldridge, Great Elm | Largest of its kind at the time; **~10.5% blended**, tiered **SOFR+6% (IG) / +13% (non-IG)** |
| DDTL 2.1 / 3.0 / 4.0 / 5.0 | $3.0B / $2.6B / **$8.5B** / $3.1B | 2025–26 | Private credit → **banks / public** | **DDTL 4.0 (Mar 2026) = first *investment-grade* GPU-backed financing, A3/A(low)**; 5.0 first publicly syndicated. Total debt **$21.6B** YE2025 |

**The mechanics that matter for us:**
- **Borrowing base = depreciable cost of the GPU servers.** Advances were explicitly "constrained by the purchase price of assets… based upon the depreciable cost of GPU servers." Lenders lend against the chips' depreciating book value, not nameplate.
- **Security = first-priority pledge of the financing-SPV equity + substantially all SPV assets.** Each facility sat in a bankruptcy-remote SPV. This is exactly our **PropCo/ChipCo per-tranche ring-fence**.
- **Debt was sized against contracted revenue.** Weighted-average contract duration was ~4 years (end-2024). Microsoft was **62% of revenue in FY2024 (rising to ~67% FY2025)**; the OpenAI relationship grew from **$11.9B (Mar 2025) + $4B (May 2025)** to **~$22.4B** with the **+$6.5B Sept 2025** expansion. The take-or-pay backlog is what made the debt financeable.
- **NVIDIA was equity holder + backstop + allocator** — a >5% stake (~$250M invested), a **$6.3B capacity backstop (through Apr 2032)**, and preferred first-"Elite"-CSP chip allocation. NVIDIA support materially de-risked the lenders.
- **Restricted-cash / DSRA reserves and maintenance covenants** throughout.

**Lessons for our JV:** the structure works; lenders will lend ~50–60%+ against GPUs *if* contracted offtake and (ideally) an NVIDIA backstop are present. Concentration (one tenant = 62–67%) is the headline risk — we diversify across Meta / Nebius / members / merchant.

---

## 2. Off-balance-sheet JV / SPV templates (the "how to structure the JV" comps)

| Deal | Total | Equity | Debt | Equity partner / arranger | Structure & backstop |
|---|---:|---:|---:|---|---|
| **Meta "Hyperion"** (Richland Parish, LA) | **~$27B** dev cost (~$30B all-in, press) | Blue Owl **~$7B** contribution / Meta **~$3B** distribution (Meta 20%) | **$27.294B bonds** | **Blue Owl 80% + PIMCO** anchor (~$18B); **Morgan Stanley** sole underwriter | SPV = **"Beignet Investor LLC."** Bond: **6.581% coupon, T+225bp, A+ (S&P), due 30 May 2049, 23.6yr fully amortizing.** Meta's **residual-value guarantee is capped to the first 16 years** → still lifts it to **A+**. Off Meta's balance sheet (unconsolidated). |
| **xAI Colossus** (Memphis) | **~$10B** (+ separate ~$20B SPV) | ~$5B | ~$5B | **Morgan Stanley** arranged (1 Jul 2025) | Two vehicles: Valor's **VCI raised $5.4B** (Apollo $3.5B; NVIDIA backer) triple-net-leasing GPUs to xAI; plus a separate **~$20B lease-to-own SPV** (~$7.5B equity / $12.5B debt; NVIDIA up to $2B) for Colossus 2. Don't conflate. |
| **Crusoe / Stargate Abilene** | **~$15B** (campus) | Blue Owl + Primary Digital Infrastructure equity | ~$3.4B → **$11.6B+** debt (JPMorgan-led) | Blue Owl JV | **15-year Oracle lease**; OpenAI is end-user. Landlord/colo structure — long IG-ish lease underwrites long debt. |

**The universal pattern:** first-loss **equity from an infra fund (Blue Owl / PIMCO / Brookfield-type)**, the bulk as **debt arranged by a bulge-bracket bank**, and an **investment-grade offtaker's lease/guarantee** that lifts the whole structure to IG. **Off-balance-sheet** for the sponsor. This is the template for bringing in our co-equity partner and getting a Meta-anchored tranche to cheap debt.

---

## 3. Neocloud financings (incl. Nebius — our anchor)

| Company | Capital raised / facility | Lenders / partners | Notes relevant to us |
|---|---|---|---|
| **Nebius** (NBIS) | **$17.4B Microsoft deal** (8 Sep 2025, expandable $19.4B, 5yr, through 2031); **$1.0B + $2.75B convertibles** (2025) | Microsoft (offtaker); NVIDIA ($700M 2024, ~0.5%; **~$2B / ~8.3% Mar 2026**); banks | **Explicit take-or-pay — the SEC-filed contract says Microsoft pays "irrespective of the actual usage or consumption."** Post-Yandex split left it with **>$2B cash**. **This is the contract template we want from Meta/Nebius.** |
| **Lambda** | **$500M** Macquarie GPU-backed facility (Apr 2024) — *distinct from* **Series D ~$480M** (Feb 2025) and **Series E ~$1.5B** (Nov 2025); multi-billion Microsoft deal (Nov 2025, undisclosed) | Macquarie; Microsoft; NVIDIA | GPU-backed debt at smaller scale; vendor + hyperscaler offtake. |
| **Crusoe** | See §2 — Abilene JV | Blue Owl, JPMorgan, Oracle | Shows the colo/landlord path. |
| **Applied Digital (APLD)** | Leases capacity to **CoreWeave**; project debt | Macquarie, SMBC, others | "Build-to-suit for a neocloud tenant" — a model for our anchor-tenant tranches. |
| Together, Nscale, Fluidstack, Voltage Park | Venture + GPU-backed + vendor finance | NVIDIA across several | Confirms vendor financing + GPU-backed debt is now standard. |

---

## 4. GPU-backed / data-center debt — benchmark terms

For the model and the Morgan Stanley asks:

| Parameter | Benchmark (from comps & rating-agency / lender commentary) |
|---|---|
| **Construction financing spread** | **SOFR + 250–400 bps** (senior, leased) |
| **Stabilized senior LTV / advance rate** | **65–70%** of value for hyperscale-leased assets; lower for merchant/GPU-only |
| **Stabilized DSCR / debt yield** | **~1.25x / ~7–10%** — *indicative only; not a universal standard, varies materially by deal* |
| **GPU-backed (private credit) all-in** | **mid-teens (~14–15%) at inception** (CoreWeave DDTL 1.0, 2023) → ~10.5% (2024) → **IG SOFR+2.25% / ~5.9% by 2026** |
| **Structured DC debt spread** | Data-center **ABS/CMBS prices ~100–150 bps over hyperscale corporate/IG bonds**; between the two, **CMBS prices *wider* than ABS** (ABS is the tighter execution) |
| **Reserves** | Debt-service reserve account (DSRA, ~6mo), GPU-refresh reserve, maintenance reserve |
| **Market depth** | 2025 data-center debt issuance **>$200B**; Morgan Stanley projecting **$250–300B for 2026** — the market can absorb our program |

---

## 5. Data-center ABS market (the equity-recycling take-out)

A real, rated, growing market — this is how we refinance seasoned tranches and pull equity back out.

| Program / issuer | Rating agency | Notes |
|---|---|---|
| **Aligned Data Centers Issuer LLC** (master trust; 2021-1 … 2026-1) | **S&P** (A-2 A-, 70% LTV); A1FCF **AAA (KBRA/Fitch)** | Benchmark program; inaugural 2021-1 part of **$1.725B** financing |
| **Vantage Data Centers** — NA Issuer LLC **$1.35B** (2023) + **€640M EMEA** (Jun 2025, first euro DC ABS) | **S&P** (A- / BBB-); EMEA also **Scope** | Proves **European** DC ABS is doable (4 German DCs, green bond) |
| **Switch 2024-1** | DBRS Morningstar | Class A-1-L **A(sf)**, A-2 **A(low)**, B **BBB(low)** |
| **Compass Datacenters Issuer II** (2024-1) | DBRS | Senior (P)AAA(sf); Guggenheim-structured |
| **Centersquare** (CyrusOne-adjacent colo; 2025-1…2025-7) | **KBRA** | Active colo ABS issuer |
| **Flexential** (2026-1/2/3/4) | **KBRA** | **$2.1B — largest-ever DC + green-bond ABS**; Class A2 **A-**; ARD Mar 2031 |
| **BX 2023-VLT2/VLT3** (QTS / Blackstone) | DBRS | **CMBS (SASB), not ABS** — listed for reference |

**Structure features to copy:** senior/mezz note classes (A/B), **anticipated repayment date (ARD)** with cash-sweep, tenant-quality and lease-term tests. ABS take-out typically prices inside the construction/GPU debt → that's the equity-recycling arbitrage.

---

## 6. GPU depreciation & residual value (the central underwriting debate)

- **Useful-life tension:** GPU-backed lenders historically used **2–3 year** depreciation; hyperscalers extended server life to flatter earnings — **Microsoft 4→6yr (FY23, +$3.7B op income)**, **Google 4→6yr (2023)**, **Amazon →6yr then *back to 5yr* (Jan 2025, citing AI pace)**. **Michael Burry publicly attacked this** as understated depreciation ("one of the more common frauds of the modern era"; Q3'25 puts ~$187M NVIDIA / ~$912M Palantir notional). *[His subsequent fund deregistration is reported but unconfirmed.]*
- **Moody's flagged ~$662B** of **data-center lease commitments *not yet commenced*** (off-balance-sheet under GAAP; ~113% of the five hyperscalers' combined adjusted debt) — regulators (BIS 2026 report, IMF, FSB) are now watching the leverage build-up.
- **SemiAnalysis unit economics:** confirmed direction — H100 rental fell from ~**$8/hr** peak (2023–24) toward ~**$2–3/hr**. *[The exact "$8/hr → 38% IRR, $4.92/hr breakeven" trio is behind SemiAnalysis's paywall — treat as indicative, not verified.]*
- **Implication for us:** model GPUs on a **conservative 4–5yr** schedule, fund a **refresh reserve**, match **GPU-debt tenor to contract tenor** (don't lever a fast-depreciating asset long), and bias the *cheap, long* debt to the **shell** (10–15yr life), not the silicon.

---

## 7. The "circular financing" critique (know it before the IC and the press do)

- NVIDIA invests in / commits to customers who buy NVIDIA chips: **→CoreWeave, →Nebius, →Lambda, →OpenAI (~$100B framework), →xAI.** Bears call it an **"ouroboros"** inflating demand.
- **Bear case:** vendor-financed demand isn't real end-demand; OpenAI was reported around **~$13B revenue vs much larger cost in 2025**; if model economics disappoint, the offtake (and the debt behind it) is at risk.
- **Bull case:** sovereign + enterprise AI demand is real and rationing compute; hyperscaler capex and contracted backlog are enormous; NVIDIA backstops *reduce* lender risk.
- **Our positioning:** we are **demand-side real** — the four JV members consume compute, and Meta/Nebius are independent IG/strong offtakers. We **size debt only against contracted, credit-supported offtake** and treat merchant as equity upside. Say this explicitly to lenders; it's our differentiation from a pure speculative neocloud.

---

## 8. European / French precedents & public capital

| Item | Relevance |
|---|---|
| **Mistral AI compute campus** (Essonne / Bruyères-le-Châtel) — **MGX + Bpifrance + Mistral + NVIDIA** JV, up to **1.4GW** (first node 44MW / ~18,000 GB200 at Eclairion); Mistral raised **~$830M** debt from 7 banks | The flagship French AI-infra capital stack: strategic + sovereign + infra equity. Direct template for our co-equity + public-capital layer. *[A2 Capital's role reported but unconfirmed in primary releases.]* |
| **SoftBank / Sesterce — Le Bosquel** (one of our candidate sites) | **1GW**, announced 31 May 2026; part of SoftBank's **5GW / up to €75B** France commitment. Confirms the site is live for hyperscale AI; we'd enter via JV/carve-out (see `france_100MW.md`). |
| French operating / landowner counterparts (**EDF/Bouchain, Schneider/Dunkirk**; "OpCore", "Data4", Sipartech) | SoftBank's primary release names Sesterce, EDF and Schneider; *"OpCore"/"Data4" are not confirmed in that release — verify separately.* |
| **Bpifrance, Caisse des Dépôts (CDC), EU IPCEI, France 2030, "Choose France," EU AI gigafactory program** | **Sovereign/public co-funding** — grants, equity, guarantees. A French sovereign-AI JV is exactly what these vehicles are designed to fund; lowers our equity need and de-risks debt. |
| Infra equity active in EU AI DCs: **MGX/Mubadala, Brookfield (~$100B AI-infra program / BAIIF), Blue Owl, DigitalBridge, EQT (EdgeConneX), Antin, BlackRock AIP (GIP/Microsoft/MGX/NVIDIA + $40B Aligned)** | The shortlist of co-equity partners to approach for the Vera Rubin phase. |

---

## 9. Take-or-pay / capacity offtake — what makes it bankable

From the Microsoft–CoreWeave, OpenAI–CoreWeave, Microsoft–Nebius, Meta–Hyperion, and Oracle–Crusoe contracts:

| Clause | Bankable value |
|---|---|
| **Term** | 5–15 years (matched to debt tenor) |
| **Minimum revenue commitment / take-or-pay floor** | Pay **"regardless of actual utilization"** (Nebius–Microsoft language) — the floor is what the debt is sized on |
| **Pricing** | $/MW/month or $/GPU-hour, often with step-downs as GPUs age; escalators for power |
| **Counterparty credit** | IG (Meta) → biggest/cheapest debt; strong-but-sub-IG (Nebius) → debt at a spread; VC-backed (our members) → **heavily haircut unless credit-supported** by a parent guarantee/prepay |
| **Termination / MAC** | Make-whole / termination payments protect the lender; tight MAC and force-majeure carve-outs |
| **Accounting** | Structure as **operating lease / service contract** (vs finance lease) to keep desired balance-sheet treatment (ASC 842 / IFRS 16) |

**The single most important rule:** *debt capacity is a function of the weighted credit of the contracted floor, not of nameplate capacity.* Route Meta onto the tranches you want cheapest; credit-support the member offtake; size merchant at zero for debt.
