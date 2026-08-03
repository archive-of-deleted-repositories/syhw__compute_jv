# JV3 Financial Model v2 — build spec (critique-integrated)

**v2 (Jul 2026).** Incorporates the external review in `critique.md`. Headline changes from v1: (1) revenue split into a **reserved-capacity leg** (debt sizes on this) and a usage-linked leg; (2) one **IT-vs-gross MW switch** — tranches are **20MW IT ≈ 24MW gross**; (3) T3–T5 re-based on **Vera Rubin NVL72** (the interim NVL144 naming referenced in `critique.md` has since been scrapped by NVIDIA); (4) **T6–T7 are option tranches** with re-underwriting gates, priced with the 15% uplift applied consistently (**~$2.15B each**, not $1.9B); (5) transfer pricing in **normalized compute credits**, not raw GPU-hours; (6) financing re-based — **public capital and NVIDIA support are upside levers, not base case**; first-close debt priced wider than the CoreWeave IG benchmark; (7) recycling is **PropCo-first at 18–24 months**; (8) five named downside cases. Consistent with `jv3_onepager_full.html` (v4).

**Underwriting posture:** **T1–T2 (GB300): commit.** **T3–T5 (Rubin NVL72): provisional** — re-price at NVIDIA spec freeze. **T6–T7 (Rubin Ultra): options only** — the Ultra design was reportedly revised for manufacturability in mid-2026; do not fix capex or financing today.

---

## 1. Assumptions (one switch: MW = IT load)

**Tranche = 20MW IT.** At PUE 1.20 that is **~24MW gross** — grid connection, substation, and utility yard are sized at **24MW/tranche** (140MW IT ≈ 168MW gross campus). All rack counts derive from IT MW; the power bill derives from gross MW. Never apply PUE twice.

| Platform | Status | $/rack | kW/rack | GPU pkgs/rack (NVIDIA GPUs) | Racks/tranche (per member) | ChipCo $ (racks ×1.15) | PropCo $ | **All-in / tranche** |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **GB300 NVL72** | Commit | $3.8M | 135 | 72 (72) | 144 (48) | $0.63B | $0.18B | **~$0.81B** |
| **Vera Rubin NVL72** | Provisional | $8.5M† | 220 | 72 (72) | 90 (30) | $0.88B | $0.18B | **~$1.06B** |
| **Vera Rubin Ultra NVL576** | **Option** | ~$52M† | 600 | 144 (576‡) | 33 (11) | $1.97B | $0.18B | **~$2.15B** (band $1.9–2.3B) |

†Preliminary — NVIDIA specs subject to change; HBM4 pricing is the main swing. ‡GB300 and Rubin NVL72 count GPU packages (72/rack); only NVIDIA's **NVL576** naming counts dies (144 packages × 4 dies). **Finance and procurement should count packages.** The 15% networking/storage/spares uplift now applies to **all** platforms (v1 under-stated Ultra by ~$250M/tranche).

**PropCo** = $8.5/W-IT shell ($170M) + $0.5M/MW **gross** grid interface (~$12M at 24MW) ≈ **$182M/tranche**.

**Program totals:** **Firm (T1–T5): ~$4.8B** (~$1.60B/member). **With options (T6–T7): ~$9.1B** (~$3.0B/member). ~**49,700 GPU packages** (~78,200 NVIDIA-counted GPUs). Band $8.3–9.6B.

**Shared inputs:** power **€90/MWh** base (€70 long-term nuclear PPA case / €105 merchant stress — treat the PPA as a *negotiation*, not a given; EDF talks are hard and mid-2026 heatwave spikes showed the tail); **PUE 1.20**; billed availability **90%** (energy modeled with an idle-draw floor — power does not fall 1:1 with utilization); GPU depreciation **4–5yr** (bear 3yr); **funded refresh reserve** (not a placeholder: NVIDIA is on an annual cadence; reserve ≈ 8–12% of ChipCo capex/yr from year 2); USD/EUR ~1.08.

---

## 2. Tranche schedule

| Tranche | Platform | Status | Window | All-in $ | Cumulative |
|---|---|---|---|---:|---:|
| T1 | GB300 NVL72 | **Commit** | 2026–27 | $0.81B | $0.81B |
| T2 | GB300 NVL72 | **Commit** | 2027 | $0.81B | $1.62B |
| T3 | Vera Rubin NVL72 | Provisional | 2027–28 | $1.06B | $2.68B |
| T4 | Vera Rubin NVL72 | Provisional | 2028 | $1.06B | $3.74B |
| T5 | Vera Rubin NVL72 | Provisional | 2028 | $1.06B | $4.81B |
| T6 | Vera Rubin Ultra NVL576 | **Option** | 2028–29 | ~$2.15B | $6.96B |
| T7 | Vera Rubin Ultra NVL576 | **Option** | 2029 | ~$2.15B | **~$9.1B** |

**Re-underwriting gates for T3–T7** (each tranche FID requires): NVIDIA spec + price freeze for its platform; refreshed member take-or-pay sized to the new platform; debt terms re-cleared; T6–T7 additionally gated on Ultra design stability and 800VDC supply-chain maturity.

---

## 3. Revenue architecture (the bankability fix)

**Two legs per member contract — never blend them:**

```
RESERVED-CAPACITY LEG (~90% of contract value)
  Fixed monthly fee per reserved sleeve, payable IRRESPECTIVE OF USAGE
  (the Nebius–Microsoft standard), subject only to facility SLA.
  → DEBT IS SIZED ON THIS LEG ONLY.

USAGE-LINKED LEG (~10%)
  Metered power pass-through + variable O&M above a baseline.
  → Sized at zero for debt; protects the co-op from utilization swings.
```

**Pricing metric: FP8 flops, not raw GPU-hours.** Generations are not economically interchangeable, so the workbook (`jv_economics_v3.csv`) prices compute two ways — **absolute $/PFLOPS-hour (FP8 dense)**, which is convention-free and is the primary metric, and **GB300-package-equivalents** as a secondary lens. **FP4-flops ratios are deliberately foregone** — FP4 is the inference marketing metric and benefits from the NVFP4 path; FP8 is the conservative, training-grade, apples-to-apples basis. Per-package FP8 (dense, chip-spec convention): GB300 4.5 PF, Rubin 17.5 PF (**3.89×**), Rubin Ultra 34.7 PF (**7.72×**). NVIDIA's rack slides imply 5.0/16.7/34.7 (→ 3.33×/6.94×) — same ordering, different rounding; both are documented in the workbook. The **flops-per-watt normalization** at equal ~20MW tranches gives **VR/GB300 = 2.43×** (46.66 → 113.4 EF per tranche; 2.4 → 5.7 → 8.3 EF/MW-IT). Re-set at each platform's spec freeze; keep GPU-hours for reporting only.

**Illustrative 5-yr cost-recovery transfer prices** (capex/5 + opex ÷ billed hours):

| Platform | $/pkg-hr | ×multiplier → **$/credit** |
|---|---:|---:|
| GB300 (×1.0) | ~$2.5–3.0 | **~$2.5–3.0** |
| Rubin NVL72 (×3.33) | ~$5.2–6.0 | **~$1.6–1.8** |
| Rubin Ultra (×6.94) | ~$13–15 | **~$1.9–2.2** |

Cost per *credit* is flat-to-falling across generations even as $/rack triples — that is the correct internal story (v1's flat $3/GPU-hr across generations was wrong in both directions).

**Strategic value is a separate bridge, not part of project IRR.** The members' merchant-vs-co-op discount is real but lives in a "member economic benefit" schedule; putting it inside the IRR double-counts (once in the transfer price, again in avoided spend).

---

## 4. Debt (re-based for a realistic first close)

The CoreWeave $8.5B DDTL (SOFR+2.25% / ~5.9%, A3/A−) is the **destination after seasoning, not the starting point** — it sat on IG-customer backlog; CoreWeave's own earlier secured debt cost ~11–14%. Three sub-IG labs self-guaranteeing demand start wider:

| Parameter | First close (T1) | Target at refi (seasoned) |
|---|---|---|
| Sleeve senior debt | **~30–32% of sleeve capex** | up to 45–50% |
| Pricing | **~SOFR + 450–650bps (~8.5–10.5%)** | toward SOFR+225–300 |
| Sizing | DSCR ≥ **1.4–1.5×** on the **reserved leg only**; advance ≤ **40–45%** of depreciable GPU cost | DSCR 1.25–1.3× |
| Tenor | 5yr, matched to take-or-pay | 5–7yr / ABS |

**Credit-enhancement ladder (each rung tightens pricing / raises advance):** several member guarantees → **6–12mo prepayment funding the DSRA** → **VC-backer LCs / parent guarantees** (the biggest lever) → NVIDIA capacity backstop (powerful but *expensive strategic capital* — NVIDIA takes option value; model it as a scenario, §6) → seasoning + audited utilization history.

Illustrative T1 sleeve (~$270M): equity ~$135M, debt ~$86M @9.5%/5yr (DS ~$22.5M/yr), vendor ~$49M. Reserved leg ~$75M/yr − opex ~$14M → DSCR ≈ 2.7× (co-op prices cost-plus; the DSCR headroom is a policy dial, not profit).

---

## 5. Recycling (PropCo-first, slower)

**Base case: refinance the PropCo only** — long-life shell + grid with contracted capacity payments is what the takeout market (euro DC ABS; Vantage EMEA template) actually buys. **18–24 months** to first meaningful takeout, not 12–18. **ChipCo refinancing is upside only** — GPU residuals can compress in one product cycle; don't build the flywheel on them. Consequence: **equity recycles more slowly than v1 assumed** — peak member cash is higher; that's what the S-scenarios below solve.

---

## 6. Financing scenarios (public money & NVIDIA = levers, not base)

**Base (revised — "S3-leaning"), per GB300 sleeve:**

| Layer | % | Notes |
|---|---:|---|
| Member + VC-backer equity | **50%** | First-loss; backer credit support behind the take-or-pay |
| Senior GPU-backed debt | **32%** | First-close terms per §4 |
| Vendor finance (OEM) | **18%** | Dell/Supermicro deferred/lease |
| + Prepayment (off-stack) | 6–12mo fees | Funds DSRA |

**Levers (apply to the base, in order of preference):**

| Lever | Effect | Reality check |
|---|---|---|
| **L1 EU/Bpifrance award** (InvestAI ~17% capex; Bpifrance €10B AI envelope) | −10–17pp off member equity | Pursue hard; **underwrite only on a term sheet/award** |
| **L2 VC-backer hard support** (LC/guarantee) | +5–10pp debt, −100–200bps | The gating item; cheap for backers vs writing equity |
| **L3 NVIDIA backstop + strategic equity** | +5–10pp debt/vendor, −150–300bps | Real (CoreWeave $6.3B) but priced — concentration + option value to NVIDIA |
| **L4 Infra co-equity (80/20)** | Replaces most member equity from T3 | Costs governance + upside; step-in rights demanded |
| **L5 PropCo ABS takeout** | Recycles equity at month 18–24 | Base only against PropCo |

**Ranking (per the review, adopted):** most financeable early = **base above (S3-leaning)**, then base+L1/L2 (revised S1). NVIDIA-led (old S2) and sovereign+co-equity (old S4) are *potential* end-states, not first-close plans.

---

## 7. Downside cases (model each explicitly)

| Case | Shock | Primary effect to model |
|---|---|---|
| **Rubin slip** | T3–T5 +6–12mo | GB300 sleeves run longer; refresh reserve stretched; member growth unserved → merchant buy-in cost |
| **Ultra redesign** | T6–T7 spec/price reset (already reported mid-2026) | Options simply not exercised, or re-struck; no program default — this is why they're options |
| **No grant award** | L1 = 0 | Base stack stands alone; member equity stays at 50% |
| **Merchant power** | €105–120/MWh, no PPA | 100MW IT: energy €85M/yr base → +€14–28M/yr; hedge/procurement strategy required |
| **One-member distress** | A member misses cash calls / insolvency | Sleeve isolation + several guarantees; buy-sell; surviving members' ROFR on the sleeve; test debt service continuity ≤ 6mo gap |

Also stress: GPU life 3yr, utilization 75%, rate +150bps, ABS window shut at month 24.

---

## 8. Corrected sensitivities (Outputs tab)

- **Energy (the big one — v1 understated ~3×):** 100MW IT @ PUE 1.20, 90% ≈ **946 GWh/yr** → **€85M/yr @ €90**. €90→€70 saves **€18.9M/yr**; €90→€105 adds **€14.2M/yr**. Full 140MW program ≈ **1.32 TWh/yr, €119M/yr @ €90**, €46M/yr swing across €70↔€105.
- **Ultra rack price:** ±$0.2–0.4B per option tranche (band $1.9–2.3B) — largest single capex sensitivity; contained by option structure.
- **Credit-enhancement dial:** advance 40→50% and −200bps ≈ the difference between S3-leaning and revised-S1 member cash.
- **Recycle timing:** month 18 vs 30 for PropCo takeout moves peak member cash by roughly one tranche's equity.

---

## 9. Governance hard points (bankability prerequisites)

The JV agreement must specify — lenders will read these before pricing: default **cure periods and dilution mechanics** per missed call; **cross-default = none** (sleeves isolated) but shared-PropCo cost step-up if a member exits; **transfer restrictions + ROFR + buy-sell (shotgun)**; **member insolvency**: automatic capacity re-marketing with lender step-in and a pre-agreed re-pricing grid; **overuse/underuse** rules between sleeves; **refresh timing** authority per sleeve with campus-level power/cooling coordination; 2-of-3 supermajority + deadlock resolution.

---

*Planning document. GB300 figures firm; Rubin NVL72 provisional; Rubin Ultra preliminary/option. Sources: `deal_comparables_sources.md`, `critique.md`. Replace with NVIDIA quotes, EPC bids, lender term sheets, and the EU/Bpifrance award before any FID.*
