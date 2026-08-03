# JV3 Member Cost Schedule — specification v4 (as of 14 Jul 2026)

**Scope:** this document specifies a **member cost schedule** — outbound member funding and member-borne costs for one neolab's ⅓ of the JV3 program. It is **not** a revenue forecast or a complete project-finance model; financeability is treated separately (§6). Working numbers: **`jv_economics_v4.csv`** (monthly engine, auto-injects the one-pager table); partner summary: `jv_economics_v4_redux.csv`; one-pager: `jv3_onepager_full_v3.html`.

**v4 integrates the external review (`feedback.md`), with these dispositions:** adopted — cost-schedule scope, bottom-up GB300 capex, dense-FP8 baseline (360 PF/rack), 2.19×/MW ratio, FX 1.143, 142/227 kW, reservation-based colo billing, PropCo $267.5M range, entity-level financing transparency, visible refresh reserve, Ultra de-numbering, timeline scenarios, "verified"→status labels. **Rejected/amended** — the "35/42/23 user decision" (it is the *detailed alternative*, not the working case — user confirmed), the "$270M user decision" (replaced by a **bottom-up $266M**; the reviewer's figure matched the old chips+building sleeve, i.e. anchoring), deletion of the normalized GB300-Watt metric (user's metric; kept with convention disclosed), and the NVL144 platform claim from the earlier `critique.md` (naming was scrapped by NVIDIA).

**Underwriting posture:** **T1–T2 (GB300, colo): commit-grade planning.** **T3–T5 (Rubin NVL72, own campus): provisional** — re-priced at NVIDIA spec freeze; delivery subject to vendor allocation and facility completion. **T6–T7: unpriced options** — Rubin Ultra or then-current best platform; configuration, price, power and schedule set only after specification freeze and vendor quotes. **There is no full T1–T7 program total.** (Prior single-rack 600kW/144-package Ultra modelling is withdrawn: newer NVIDIA documentation describes NVL576 as an 8-rack domain.)

---

## 1. Canonical assumptions (per member = ⅓ of a ~20MW-nominal tranche)

| | GB300 NVL72 | Vera Rubin NVL72 | Status |
|---|---|---|---|
| Siting | **Existing colo** | **Own campus** (PropCo block) | — |
| Racks (member / tranche) | 48 / 144 | 30 / 90 | — |
| kW/rack · tranche nameplate | 142 · **20.45 MW** | 227 MaxP · **20.43 MW** (MaxQ 187 scenario) | NVIDIA RA / ASUS |
| GPU packages (member) | 3,456 | 2,160 | — |
| Dense FP8 (member) | **17.28 EF** (360 PF/rack) | **37.80 EF** (1,260 PF/rack) | NVIDIA (dense, not sparsity-inflated) |
| **ChipCo capex (member)** | **$266.0M** | **$293.3M** (low case $234M) | Assumption / quote-pending |
| PropCo share (member) | — (rents) | **$89.2M** ($267.5M/block; range $260–275M) | Benchmark-derived |
| All-in sleeve | **$266.0M** | **$382.5M** | — |

**GB300 ChipCo $266M — bottom-up, not anchored:** 48 × **$4.0M rack** (street-band top — Loop Capital $3.7–4.0M; *street-band estimate, not a quote*) = $192M, + fabric/storage/spares **$38.4M** (~20%, training fat-tree), + deployment **$35.6M** (yr-1 software/support ~$8.4M, freight ~$1.7M, install & acceptance ~$5.3M, VAT working-capital carry ~$2.6M, ~7% contingency ~$17.6M) = **$5.54M/rack fully loaded**; band **$244–294M**. Replace with OEM BOM + quote (diligence register, §9).

**Rubin ChipCo $293.3M** = 30 × $8.5M × 1.15, the **conservative complete case**; the $7.8M configured-system report (incl. memory/storage) gives the **$234M low case** — do not stack 15% on top of it. Range pending quotes.

**PropCo $267.5M/block** central (T&T Paris $10.8/W + 7–10% liquid premium + grid + owner costs; T&T excludes land/fees/utility works). Built for **T3–T5 only**; grid spend to be split campus-common vs per-block by engineering study — no RTE connection is assumed until an executed offer exists.

**Other globals:** FX **$1.143/€** (ECB Jul 2026); power **€90/MWh all-in-delivered planning case** (€70 commodity ≠ delivered; TURPE/levies/capacity bridged at PPA term sheet; scenarios €70/€90/€110); PUE 1.20; **electrical load factor 90%** (distinct from **90% billed availability** used in unit-cost denominators); colo **$130/kW-mo** (unquoted low case; 130/155/180 sensitivity) billed on **⅓ of a 20MW reservation** (6,667 kW — documented choice vs 6,816 kW nameplate); chip maintenance 2.5%/yr and staffing lines are assumptions to be tested against vendor-support and colo-service inclusions; chip life 5yr, residual 10% memo (0/5/10/15% sensitivities); building 15yr.

---

## 2. Schedule (months from program start)

| Tranche | Platform | Status | Constr. | Buyout | **Online** | All-in $/tranche | Cum. (firm) |
|---|---|---|---|---|---|---:|---:|
| T1 | GB300 (colo) | Commit | — | m0 | **m6** | $0.80B | $0.80B |
| T2 | GB300 (colo) | Commit | — | m6 | **m12** | $0.80B | $1.60B |
| T3 | Rubin NVL72 | Provisional | m0–m21 | m15 | **m21** | $1.15B | $2.74B |
| T4 | Rubin NVL72 | Provisional | m6–m27 | m21 | m27 | $1.15B | $3.89B |
| T5 | Rubin NVL72 | Provisional | m12–m33 | m27 | **m33** | $1.15B | **~$5.0B** |
| T6–T7 | Ultra / best-then | **Unpriced options** | TBD | TBD | TBD | — | — |

**Timing scenarios (per `feedback.md`, adopted):** GB300 buyout→online **6mo base** (accelerated 16wk only with ready liquid-cooled colo + allocated integrated systems; downside 32–40wk). Rubin construction **21mo** modelled (accelerated-to-base for a pre-de-risked fast-track site); scenarios **18–21 / 22–24 / 30–36 months** — the 22–24 base would shift T3 online to ~m24 and T5 to ~m36. "Buyout" is a simplification: real payments stage as deposit → progress payments → delivery → acceptance; debt draws should match eligible invoices (phase-3 modelling item).

---

## 3. Compute accounting (dense FP8; conventions disclosed)

- **Baseline:** GB300 NVL72 publishes 720 PF FP8 *with sparsity* → **360 PF dense/rack = 5.0 PF/GPU**. Rubin NVL72: **1,260 PF dense/rack = 17.5 PF/GPU**.
- **Ratios:** per GPU **3.50×**; per MW **(1260/227)/(360/142) = 2.19×**. (The earlier 2.43× rested on a 4.5 PF/GPU chip-spec baseline inconsistent with NVIDIA's rack figure; withdrawn.)
- **Normalized GB300-Watt** (retained by user decision, convention disclosed): watts of GB300 delivering equal dense FP8; baseline **2.535 EF/MW-IT**. Rubin = ×2.19/actual-W.
- Every unit cost states its denominator and availability basis; headline unit costs use **90% billed availability**; the CSV's cumulative columns are labelled **100% hours**.

---

## 4. Member costs (workbook outputs, 5-yr per sleeve)

| | GB300 sleeve | Rubin sleeve | Firm T1–T5 (member) |
|---|---:|---:|---:|
| Capex (all-in) | $266.0M | $382.5M | **$1,679M** |
| — equity (37%) | $98M | $142M | **$622M** |
| — debt (63%) | $168M | $240.5M | $1,057M |
| Interest (9.5% / 8.5%, 5yr) | $43.7M | $55.6M | $254M |
| Opex (colo/energy/maint/staff/PropCo) | $121.4M ($2.02M/mo) | $92.7M ($1.54M/mo) | $521M |
| **5-yr all-in cost** | **$431M** | **$531M** | **$2,454M** |
| $/GPU-hr @90% | **$3.16** | $6.23 | — |
| $/GB300-equiv-hr @90% | $3.16 | **$1.78** | **$2.10** |
| $/PFLOPS-hr (FP8) @90% | $0.633 | **$0.356** | **$0.421** |
| $/normalized-GB300-W/mo | $1.05 | **$0.59** | **$0.70** |

JV ×3: firm capex **~$5.0B**, 5-yr total **~$7.4B**, **444 EF** dense FP8, 40,176 GPU packages. Year-one member cash ≈ **$0.34B**. Merchant reference remains $5–8/GB300-class-hr — the co-op holds ~55–60% discount at the blended $2.10.

**Refresh reserve (now visible, per review):** 8.75%/yr of ChipCo, funded monthly from each sleeve's online+12 through online+60 into **restricted cash** — a funding movement, not an expense; shown as memo columns (≈ **$494M/member** accumulated over 4 years — the war-chest for the year-5/6 refresh, ≈ 35% replacement equity). **PropCo terminal state:** buildings have ~12 years of life at m93; model re-lease to refreshed fleet / vacancy / sale explicitly in phase 3 — they do not vanish.

---

## 5. Financing (working case + documented alternative)

**Working case (simplified, user-confirmed):** **37% member equity deposit / 63% single 5-yr amortizing loan** per sleeve — GB300 **9.5%** first close, Rubin **8.5%** seasoned. Vendor finance sits inside the 63% for simplicity.

**Detailed alternative (for term-sheet stage, user-approved as alternative):** **35% equity / 42% senior GPU debt / 23% vendor finance**, with separate margins, tenors, draw timing, security and intercreditor terms — the senior and vendor tranches are *not* economically identical and must be split before executing documents. PropCo is financed **separately** (construction ~40/60, stabilized ~35/65 planning cases); in the current workbook PropCo is member-equity-funded during construction — a conservative simplification that overstates near-term equity and understates ChipCo-only leverage transparency, so: **entity-level view: GB300 ChipCo 37/63; Rubin ChipCo ~18/82 net of PropCo equity... stated plainly, Rubin chip-level leverage is ~82% of ChipCo if all sleeve debt is attributed to chips** — lenders will read it this way; the 35/42/23 split plus separate PropCo debt is the clean fix at term-sheet stage.

**Not yet modelled (placeholders):** upfront/OID fees, commitment fees (cf. CoreWeave DDTL-5's 0.5%), interest during construction, DSRA funding, rate hedging, refinancing costs. CoreWeave benchmarks corrected: DDTL-4 $8.5B at SOFR+2.25% (contract-specific A3/A(low)); **DDTL-5 $3.1B at SOFR+4.50%** one month later — pricing is contract- and credit-specific, not a market constant.

**Financeability (kept out of the base schedule):** cost-plus internal pricing makes any DSCR tautological. Debt should be underwritten on **actual member take-or-pay payment schedules with hard credit support** (backer LCs/guarantees, prepaid reserves) — a separate financing appendix once contracts are papered.

---

## 6. Downside cases

| Case | Shock | Treatment |
|---|---|---|
| Rubin slip | +6–12mo | GB300 sleeves run longer; merchant buy-in for unserved growth |
| Construction base-case (22–24mo) | T3 online ~m24 | Carry cost + idle-debt-service quantified in scenario run |
| No public award | L-levers = 0 | Base already assumes zero subsidy ✓ |
| Merchant power / no PPA | €110 all-in | +22% program energy |
| Colo squeeze | $130→$180/kW-mo | +$20M per GB300 sleeve over 5yr |
| One-member distress | missed calls / insolvency | Sleeve isolation, several guarantees, buy-sell, lender step-in |
| GB300 capex high case | $294M | +$56M/member capex; $3.4–3.5/GPU-hr |
| FX | 1.05–1.25 $/€ | ∓8/+9% on €-denominated opex |

---

## 7. Site & public capital (conditionalized per review)

Site: **to be selected**, subject to executed land exclusivity, confirmed grid-connection offer, permitting diligence, water/cooling design, fibre diversity, geotechnical/environmental review. Candidates include the French fast-track cohort (noting **Le Bosquel is committed to SoftBank/Sesterce** — entry only via carve-out) and EDF CEI sites. No RTE 400kV entitlement is claimed. **Public capital (EU InvestAI up to ~17% of eligible capex, Bpifrance):** upside lever only — base schedule carries **zero subsidy**; underwrite only on award, with clawback/conditions reviewed.

## 8. Governance hard points

Unchanged from v3 (cure periods & dilution; no cross-default across sleeves; ROFR + buy-sell; insolvency step-in with capacity re-marketing; overuse/underuse rules; refresh authority per sleeve; 2-of-3 supermajority + deadlock). Lenders read these before pricing.

## 9. Diligence register (assumption → document)

OEM quote & BOM per generation · allocation & delivery schedule · vendor-finance term sheet · senior-lender term sheet · **colo term sheet** (reserved-power basis, pass-through energy, sidecar-CDU responsibility) · site exclusivity & land price · RTE/DSO connection offer · permitting path · EPC budget & liquid-cooling scope · long-lead reservations · member commitment + backer credit support · insurance & tax · energy/CAPN all-in bridge · PropCo construction & stabilization term sheets · VAT/customs structuring.

---

*Member cost schedule specification, v4 · as of 14 Jul 2026 · GB300 figures are street-band-anchored assumptions; Rubin provisional; Ultra unpriced. Phase-3 modelling backlog (bank-grade): S-curve/milestone construction draws, invoice-matched debt draws, financing fees & IDC, dual-currency ledgers, VAT working capital, PropCo terminal state. Sources: `deal_comparables_sources.md`; reviews: `critique.md`, `feedback.md` (dispositions in header).*
