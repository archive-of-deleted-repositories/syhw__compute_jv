# Project Ampère — Sequoia One-Pager

**Confidential · for discussion · assumptions as of 14 July 2026**

## The one line
Three frontier AI labs are building **~100MW of NVIDIA compute in France as a member-owned cooperative** — a firm **~$5.0B** program (T1–T5) with two further tranches held as unpriced options. We are one of the three. The ask to Sequoia is small in cash and large in leverage: **your credit support behind our take-or-pay is the gating item that makes our sleeve debt financeable**, and it secures the portfolio's scarcest input — training compute — at roughly a third of merchant cost.

## Why this matters for Sequoia
- **Compute at ~⅓ of merchant.** Our firm sleeve delivers **148 exaflops of dense-FP8** (13,392 GPU packages: 2× GB300 + 3× Vera Rubin sleeves) at a blended **$2.10 per GB300-equivalent GPU-hour** (5-yr all-in, 90% billed availability) vs **$5–8 merchant** for GB300-class reserved capacity. That spread compounds directly into iteration speed and gross margin.
- **Fast first compute, honest schedule.** GB300 racks in existing colo are **live at month 6**; the owned campus carries Vera Rubin from month 21 (site subject to executed exclusivity and grid offer; a Rubin-ready colo option could pull T3 to ~month 18). Full firm fleet by ~month 33.
- **Security of supply, owned not rented.** We hold the racks and the reserved capacity — not spot-market scraps or a neocloud's allocation queue.

## The structure (why it's financeable)
- **Three equal members**; each funds and controls its own ChipCo sleeve per tranche; a shared PropCo owns the campus (cost-split ⅓, financed separately). Sleeves are ring-fenced — one member's problems never touch another's.
- **Demand is contracted, not assumed:** each member signs a **two-leg take-or-pay** (reserved-capacity fee payable irrespective of usage + metered usage leg). Because the members are venture-backed, lenders underwrite the contracts **plus backer credit support** — that's you.
- **Discipline is built in:** T6–T7 are unpriced options (no commitment to unfrozen NVIDIA specs); public capital is zero in the base case; every input carries a status label (street estimate / assumption / quote-pending); a funded **refresh reserve** (~$0.49B/member of restricted cash by year 5) pre-finances the next hardware generation.

## The numbers (per member, firm program)
| | |
|---|---|
| Capex | **$1.68B** (equity **$0.62B** + 5-yr debt $1.06B at 9.5%→8.5%) |
| 5-yr all-in cost | **$2.45B** (capex + interest + operations) |
| First check | **$98M** at T1 FID (GB300 racks live 6 months later) |
| Year-one cash | **~$0.34B** |
| What it buys | 148 EF dense FP8 · ~29,600 GB300-equivalents · $2.10/equiv-hr |
| Cost basis | GB300 **$266M/sleeve bottom-up** ($4.0M/rack street band + fabric/storage + deployment, band $244–294M); Rubin conservative $293M (low case $234M, quote-pending) |

## The asks
1. **Credit support behind our take-or-pay** — an LC, guarantee, or committed backstop on our sleeve. This is the single lever that converts a venture-backed lab's commitment into underwritable debt (first close ~9.5%, stepping down as the JV seasons; the market path from mid-teens first-close pricing to investment-grade GPU debt is established — CoreWeave's public record). Low cash outlay, disproportionate impact.
2. **Anchor our sleeve equity** — the $0.62B firm-program equity, drawn tranche-by-tranche ($98M → ~$44M chip equity + construction draws per Rubin sleeve). Working stack 37/63 simplified; detailed alternative 35% equity / 42% senior / 23% vendor at term-sheet stage.
3. **Optional:** infra-style co-investment at the PropCo (separately financed, ABS-able once stabilized — the euro data-centre securitization market is proven).

## Downside posture
No revenue is assumed anywhere in the base — this is a cost schedule, stress-tested: GPUs are never bought more than 6 months before service; construction slips cost time, not stranded silicon; sleeve isolation + several guarantees + buy-sell handle member distress; the largest open number (the Rubin quote, ~$180M/member swing) is bracketed, not hidden. Full assumptions, brackets and diligence register: `project_ampere.md`; monthly member wallet: `project_ampere_cost_model.csv`.

## Next step
Term sheet on (1) credit support and (2) sleeve equity, in parallel with our OEM quotes and colo RFP. The data-room pack (one-pager, cost model, assumptions memo) is ready to share.
