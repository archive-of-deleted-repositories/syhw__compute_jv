# Project Ampère — JV3
### Three AI labs · one 140MW French AI factory · demand self-guaranteed

**Confidential — data room summary · v2 (July 2026)**

---

## What this is

Three frontier AI labs ("neolabs") form a joint venture to build the compute they each need, at cost, on a French fast-track site (Dunkerque or Le Bosquel). Each member takes an equal ~7MW slice of every 20MW tranche and signs a **two-leg take-or-pay** guaranteeing it — a **reserved-capacity fee payable irrespective of usage** (debt is sized on this leg only) plus a usage-linked leg. Demand is 100% committed from day one; no external anchor tenant is required.

**Structure:** shared **PropCo** (land, RTE 400kV grid, powered shell, 800VDC-ready backbone, operations — cost-split 1/3) + three ring-fenced **ChipCo sleeves** per tranche (each member funds its own GPUs, guarantees its own demand, bears its own obsolescence risk). One member's problems never touch the others' sleeves.

## The build — 7 × 20MW-IT tranches (~24MW gross each)

| Tranches | Platform | Status | Racks (per member) | GPU pkgs | All-in each |
|---|---|---|---:|---:|---:|
| T1–T2 · 2026–27 | GB300 NVL72 | **Committed** | 144 (48) | 10,368 | ~$0.81B |
| T3–T5 · 2027–28 | Vera Rubin NVL72 | Committed path¹ | 90 (30) | 6,480 | ~$1.06B |
| T6–T7 · 2028–29 | Rubin Ultra NVL576 (Kyber) | **Options²** | 33 (11) | 4,752 | ~$2.15B |
| **Firm path (T1–T5)** | | | | **40,176** | **~$4.8B** |
| **Full program** | 140MW · ~49,700 pkgs (~78,200 NVIDIA GPUs) | | | | **~$9.1B** |

¹ Re-priced at NVIDIA spec freeze. ² Exercised only at Rubin-Ultra spec freeze, fully re-underwritten. Per member: **~$1.6B firm / ~$3.0B with options**, funded on a revolving basis. Cost per *normalized* compute credit is flat-to-falling across generations even as $/rack rises.

## Financing — underwritten on member credit alone; everything else is upside

**Base stack (per member GB300 sleeve, ~$270M):** **50% member + backer equity · 32% GPU-backed debt · 18% OEM vendor finance**, plus 6–12 months of prepaid fees funding the debt-service reserve. First-close debt: ~SOFR+450–650, DSCR ≥1.4× on the reserved leg, advance ≤40–45% of depreciable GPU cost — refinancing toward the investment-grade benchmark (CoreWeave DDTL 4.0, ~SOFR+2.25%) after seasoning.

**Upside levers (improve the base; never assumed):** EU InvestAI / Bpifrance award (−10–17pp equity, on term sheet only) · VC-backer LCs/guarantees behind each take-or-pay (the gating item) · NVIDIA capacity backstop + strategic equity (CoreWeave $6.3B template) · infra co-equity partner at scale · **PropCo ABS take-out at month 18–24** (euro DC ABS — Vantage €640M template) recycling equity into the next tranche. ChipCo refinancing treated as upside only.

**First-tranche cash per member: ~$60–140M** (development share + GPU deposit + first equity draws).

## Why now, and why France

GB300 ships today; Rubin follows 2H-2026. France offers fast-track 400kV connection (3–4yr), low-carbon nuclear power (€70–105/MWh scenarios), and the EU/France AI-gigafactory capital wave (InvestAI €20B; Bpifrance €10B; Choose France) — the JV is the exact target profile. The shell is built 800VDC-ready so later Rubin tranches drop into reserved corridors.

## Key risks & mitigants

**Sub-IG member credit** → sleeve isolation, several guarantees, backer support, prepaid DSRA, conservative first-close leverage. **NVIDIA roadmap movement** → T6–T7 held as options; per-tranche re-underwriting gates. **Power price** → PPA negotiation + hedging strategy (energy ≈ €85M/yr at 100MW IT, €90/MWh). **Member distress** → buy-sell, lender step-in, capacity re-marketing, no cross-default. **Grid/permits** → state fast-track site, phased energization matched to tranches.

---

*Further materials in this data room: full financial model (`JV3_financial_model.md`), structure & governance (`JV3_plan.md`), external review (`critique.md`), market precedents with sources (`deal_comparables.md` / `deal_comparables_sources.md`), site diligence (France reports). All figures are planning assumptions — GB300 firm; Rubin/Rubin-Ultra preliminary — to be replaced by NVIDIA allocation terms, EPC bids, and lender term sheets at each tranche FID. Not an offer of securities.*
