#!/usr/bin/env python3
"""JV3 per-member cost schedule v4 (feedback.md-integrated, as of 14 Jul 2026).
- GB300 in existing colo, $266M/member bottom-up fully-loaded ChipCo (band $244-294M).
- Vera Rubin in purpose-built PropCo blocks ($267.5M/block central), 21mo construction.
- T6/T7 (Rubin Ultra) EXCLUDED from base: unpriced options pending spec freeze + quotes.
- Dense FP8 baseline: GB300 360 PF/rack (5.0/GPU) -> Rubin 3.50x/GPU, ~2.19x/MW.
- FX $1.143/EUR (ECB Jul 2026). Colo billed on 1/3 of 20MW reservation.
- Refresh reserve shown as restricted-cash memo (8.75%/yr of ChipCo, from online+12, 4 years).
Outputs jv_economics_v4.csv + injects monthly table into jv3_onepager_full_v3.html."""
import csv

# ---------------- Global assumptions ----------------
FX = 1.143                  # USD per EUR (ECB reference, Jul 2026; was 1.08 - stale)
POWER_EUR_MWH = 90.0        # all-in delivered planning case (commodity+TURPE+levies; scenario E70/E110)
PUE = 1.20
LOAD_FACTOR = 0.90          # ELECTRICAL load factor (distinct concept from billed availability)
AVAIL = 0.90                # BILLED availability for unit-cost denominators
HRS_MO = 730.0
LIFE_M = 60
CHIP_RESID = 0.10           # sensitivity 0/5/10/15% in docs
PROPCO_LIFE_M = 180
MAINT_CHIP_PCT = 0.025      # /yr of ChipCo (assumption - verify vs vendor support contract)
PROPCO_OPEX_PCT = 0.03      # /yr of PropCo share
STAFF_MO = 0.13; SEC_MO = 0.028
COLO_STAFF_MO = 0.05
COLO_KW_FEE = 130.0         # $/kW-mo, unquoted low case; sensitivity 130/155/180
COLO_KW_BILLED = 20000.0/3  # billed on 1/3 of contractual 20MW reservation (documented choice)
RESERVE_PCT = 0.0875        # refresh reserve /yr of ChipCo, months online+12..online+60 (restricted cash memo)

# Dense FP8 (dense, not sparsity-inflated): GB300 = 720 sparse -> 360 PF/rack = 5.0 PF/GPU.
# Rubin = 1,260 PF/rack = 17.5 PF/GPU. Ratios: 3.50x per GPU; (1260/227)/(360/142) = 2.19x per MW.
PF_GB, PF_VR = 5.0, 17.5
GB_EF_PER_MW = (48*72*PF_GB/1000.0)/6.816   # 2.535 EF/MW-IT: normalized-GB300-W baseline (convention disclosed)

# ---------------- Sleeves (per member = 1/3 tranche) ----------------
# GB300 ChipCo $266.0M bottom-up: 48 x $4.0M rack (street band top, Loop Capital) = $192M
#   + fabric/storage/spares (~20%) $38.4M + deployment $35.6M (software/support yr1 ~$8.4M,
#   freight ~$1.7M, install/acceptance ~$5.3M, VAT working-capital carry ~$2.6M, ~7% contingency ~$17.6M)
#   = $5.54M/rack fully loaded. Band $244-294M. ASSUMPTION pending OEM BOM + quote - not "verified".
# Rubin ChipCo $293.3M = 30 x $8.5M x 1.15 - the CONSERVATIVE COMPLETE case; low case $234M
#   (30 x $7.8M configured-system incl. memory/storage). Range pending quotes.
# PropCo $267.5M/block central (T&T Paris $10.8/W + liquid premium + grid + owner costs; range $260-275M).
SLEEVES = {
  "GB300": dict(chip=266.0, prop=0.0,   mw=6.816, kw_rack=142, racks=48, pkgs=3456, pf=PF_GB, rate=0.095, constr=0),
  "VR72":  dict(chip=293.3, prop=267.5/3, mw=6.810, kw_rack=227, racks=30, pkgs=2160, pf=PF_VR, rate=0.085, constr=21),
}
EQUITY_PCT = 0.37   # working case: 37% equity deposit / 63% single 5-yr amortizing debt (simplified;
                    # detailed ALTERNATIVE stack: 35% equity / 42% senior GPU debt / 23% vendor finance)

# Schedule: GB300 buyout->online 6mo (base 20-28wk scenario band). Rubin blocks: 21mo construction
# (accelerated-to-base for a pre-de-risked fast-track site; scenarios 18-21 / 22-24 / 30-36mo in docs).
SCHED = [
  ("T1","GB300", None, 0,  6),
  ("T2","GB300", None, 6,  12),
  ("T3","VR72",  0,    15, 21),
  ("T4","VR72",  6,    21, 27),
  ("T5","VR72",  12,   27, 33),
]
# T6/T7: Rubin Ultra or then-best platform - UNPRICED OPTIONS, config/price/power/schedule TBD at
# NVIDIA spec freeze + vendor quote (NVL576 = 8-rack domain per newer NVIDIA docs; prior single-rack
# 600kW/144-pkg modelling was conflated and has been withdrawn).

def ann_factor(rate, n):
    r = rate/12; return r/(1-(1+r)**-n)

info = {}
for k,s in SLEEVES.items():
    allin = s["chip"]+s["prop"]
    equity = round(EQUITY_PCT*allin); debt = allin-equity
    pmt = debt*ann_factor(s["rate"], LIFE_M)
    elec = s["mw"]*PUE*HRS_MO*LOAD_FACTOR*POWER_EUR_MWH*FX/1e6
    colo = (COLO_KW_BILLED*COLO_KW_FEE/1e6) if s["prop"]==0 else 0.0
    maint = s["chip"]*MAINT_CHIP_PCT/12
    propop = s["prop"]*PROPCO_OPEX_PCT/12
    staff = COLO_STAFF_MO if s["prop"]==0 else STAFF_MO
    sec = 0.0 if s["prop"]==0 else SEC_MO
    opex = elec+colo+maint+propop+staff+sec
    ef = s["racks"]*72*s["pf"]/1000.0
    info[k] = dict(allin=allin, equity=equity, debt=debt, pmt=pmt, interest=pmt*LIFE_M-debt,
                   elec=elec, colo=colo, maint=maint, propop=propop, staff=staff, sec=sec, opex=opex,
                   dep_c=s["chip"]*(1-CHIP_RESID)/LIFE_M, dep_p=(s["prop"]/PROPCO_LIFE_M if s["prop"]>0 else 0.0),
                   ef=ef, efmw=ef/s["mw"], eqmw=ef/GB_EF_PER_MW, equiv=s["pkgs"]*s["pf"]/PF_GB,
                   reserve_mo=s["chip"]*RESERVE_PCT/12, **s)

END = 33 + LIFE_M   # m93: T5 online m33 + 5yr
loans = []; rows = []
cum_cash = 0.0; cum_hrs = 0.0; cum_pfh = 0.0; cum_wmo = 0.0; cum_res = 0.0
for m in range(0, END+1):
    ev = []; prop_draw = chip_eq = db_draw = 0.0
    for name,k,cs,bo,on in SCHED:
        s = info[k]
        if cs is not None and cs <= m < cs+s["constr"]:
            prop_draw += s["prop"]/s["constr"]
        if m == bo:
            chip_eq += s["equity"] - s["prop"]
            db_draw += s["debt"]
            loans.append([m, s["rate"]/12, s["pmt"], s["debt"]])
            ev.append(f"{name} buyout")
        if m == on: ev.append(f"{name} ONLINE")
        if cs is not None and m == cs: ev.append(f"{name} constr start")
    interest = principal = 0.0
    for L in loans:
        bm, r, pmt, bal = L
        if m > bm and bal > 1e-6:
            i = bal*r; p = min(pmt-i, bal); interest += i; principal += p; L[3] = bal-p
    debt_bal = sum(L[3] for L in loans)
    live = [k for name,k,cs,bo,on in SCHED if on <= m < on+LIFE_M]
    def S(f): return sum(info[k][f] for k in live)
    colo,elec,staff,sec,maint,propop = S("colo"),S("elec"),S("staff"),S("sec"),S("maint"),S("propop")
    opex = colo+elec+staff+sec+maint+propop
    dep_c = S("dep_c")
    dep_p = sum(info[k]["dep_p"] for name,k,cs,bo,on in SCHED if on <= m < on+PROPCO_LIFE_M)
    fleet = S("equiv"); fleet_ef = S("ef"); fleet_eqmw = S("eqmw"); fleet_pkgs = S("pkgs")
    reserve = sum(info[k]["reserve_mo"] for name,k,cs,bo,on in SCHED if on+12 <= m < on+LIFE_M)
    cash = prop_draw + chip_eq + interest + principal + opex
    cum_cash += cash; cum_hrs += fleet*HRS_MO; cum_pfh += fleet_ef*1000.0*HRS_MO; cum_wmo += fleet_eqmw; cum_res += reserve
    cphr = cum_cash*1e6/cum_hrs if cum_hrs>0 else 0
    cpfh = cum_cash*1e6/cum_pfh if cum_pfh>0 else 0
    cpwm = cum_cash/cum_wmo if cum_wmo>0 else 0
    rows.append([m, " + ".join(ev), round(prop_draw,2), round(chip_eq,1), round(db_draw,1), round(debt_bal,1),
                 round(interest,2), round(principal,2), round(interest+principal,2),
                 round(colo,2), round(elec,2), round(staff,2), round(sec,2), round(maint,2), round(propop,2),
                 round(opex,2), round(cash,2), round(cum_cash,1), round(dep_c,2), round(dep_p,2),
                 int(fleet), round(cphr,3), round(fleet_ef,1), round(cpfh,4), round(fleet_eqmw,2), round(cpwm,3),
                 int(fleet_pkgs), round(reserve,2), round(cum_res,1)])

# ---------------- CSV ----------------
out = "/Users/gab/ff/compute/project_ampere_cost_model.csv"
n = {"GB300":2,"VR72":3}
with open(out,"w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["PROJECT AMPERE - MEMBER COST SCHEDULE (assumptions as of 14 Jul 2026) - outbound member cash only; no revenue modelled. One member's 1/3 of the T1-T5 FIRM program. T6-T7 are unpriced options (excluded). All $M. Companion docs: project_ampere.md, project_ampere.html."])
    w.writerow([])
    w.writerow(["ASSUMPTIONS (status labels: STREET-BAND EST / ASSUMPTION / QUOTE-PENDING; nothing here is an executed quote)"])
    w.writerow(["GB300 ChipCo $266.0M/member","BOTTOM-UP fully-loaded: 48 x $4.0M rack (STREET-BAND EST, Loop Capital $3.7-4.0M) = $192M + fabric/storage/spares $38.4M + deployment $35.6M (software/support yr1, freight, install/acceptance, VAT carry, ~7% contingency) = $5.54M/rack. Band $244-294M. QUOTE-PENDING (OEM BOM)."])
    w.writerow(["Rubin ChipCo $293.3M/member","CONSERVATIVE COMPLETE case (30 x $8.5M x 1.15). Low case $234M (30 x $7.8M configured system incl. memory/storage - avoid double-counting the 15% on top of it). Range pending quotes. Power 227 kW/rack MaxP (ASUS); MaxQ 187kW as scenario."])
    w.writerow(["PropCo $267.5M/block (member share $89.2M)","T&T Paris $10.8/W + 7-10% liquid premium + grid + owner costs; planning range $260-275M. Built for T3-T5 only; 21-month construction (accelerated-to-base for a pre-de-risked fast-track site; scenarios 18-21/22-24/30-36mo). Grid split (campus vs block) TBD by engineering study."])
    w.writerow(["Financing (working case)","37% equity deposit / 63% single 5-yr amortizing loan (SIMPLIFIED, agreed): GB300 9.5%, Rubin 8.5%. DETAILED ALTERNATIVE stack: 35% equity / 42% senior GPU debt / 23% vendor finance with separate tenors/margins/security - to be split at term-sheet stage. Fees/IDC/DSRA/commitment fees not yet modelled (placeholders in docs)."])
    w.writerow(["Colo (GB300)","$130/kW-mo (ASSUMPTION, unquoted low case; sensitivity 130/155/180) billed on 1/3 of contractual 20MW reservation = 6,666.7 kW -> $0.867M/mo. Electrical load computed separately on 6.816 MW nameplate (48 x 142 kW). Clarify in LOI what colo fee includes (remote hands, security) and who furnishes sidecar CDUs."])
    w.writerow(["Electricity","IT nameplate x PUE 1.20 x 90% ELECTRICAL LOAD FACTOR (distinct from billed availability) x EUR90/MWh all-in-delivered planning case x $1.143/EUR (ECB Jul 2026). EUR70 commodity is NOT all-in - TURPE/levies/capacity to be bridged at PPA term sheet. FX and EUR sensitivities in docs."])
    w.writerow(["Dense FP8 basis","GB300: 720 PF/rack WITH sparsity -> 360 PF dense = 5.0 PF/GPU. Rubin: 1,260 PF dense = 17.5 PF/GPU. Ratios: 3.50x per GPU; ~2.19x per MW ((1260/227)/(360/142)). Normalized GB300-W = watts of GB300 delivering equal dense FP8 (baseline 2.535 EF/MW-IT) - convention disclosed. FP4 marketing flops not used."])
    w.writerow(["Refresh reserve","8.75%/yr of ChipCo capex, funded monthly from online+12 through online+60 into RESTRICTED CASH (memo columns - a funding movement, NOT an expense; excluded from cost totals and unit costs)."])
    w.writerow(["T6-T7","Rubin Ultra or then-current best platform: UNPRICED OPTIONS - configuration, price, power and schedule to be set after NVIDIA specification freeze and vendor quotes. Prior 600kW/144-pkg single-rack modelling withdrawn (NVL576 = 8-rack domain per newer NVIDIA documentation)."])
    w.writerow(["Not modelled (flagged)","Insurance, network transit, decommissioning, migration overlap, PropCo terminal state after m93 (building has ~12yr life remaining - re-lease/refresh/sale to be modelled), financing fees. Chip residual 10% memo (sensitivities 0/5/10/15%)."])
    w.writerow([])
    w.writerow(["SLEEVE SUMMARY (per member; unit costs @90% BILLED availability unless '100%' stated)"])
    w.writerow(["Type","Siting","ChipCo $M","PropCo share $M","All-in $M","Equity 37%","Debt 63%","Rate","Pmt/mo","Interest $M","Opex $M/mo","5yr all-in cost $M","GPU pkgs","Dense FP8 (EF)","GB300-eq MW","$/GPU-hr @90%","$/GB300-equiv-hr @90%","$/PFLOPS-hr (FP8) @90%","$/GB300-W/mo"])
    for k in ["GB300","VR72"]:
        s = info[k]
        tot5 = s["allin"] + s["interest"] + s["opex"]*LIFE_M
        hrs90 = s["pkgs"]*8760*5*AVAIL
        eqhrs90 = s["equiv"]*8760*5*AVAIL
        pfh90 = s["ef"]*1000*8760*5*AVAIL
        w.writerow([k, "colo" if s["prop"]==0 else "owned campus", round(s["chip"],1), round(s["prop"],1), round(s["allin"],1),
                    s["equity"], round(s["debt"],1), f'{s["rate"]*100:.1f}%', round(s["pmt"],2), round(s["interest"],1),
                    round(s["opex"],2), round(tot5,1), s["pkgs"], round(s["ef"],1), round(s["eqmw"],2),
                    round(tot5*1e6/hrs90,2), round(tot5*1e6/eqhrs90,2), round(tot5*1e6/pfh90,4), round(tot5/s["eqmw"]/LIFE_M,3)])
    capex = sum(info[k]["allin"]*n[k] for k in n); eqty = sum(info[k]["equity"]*n[k] for k in n)
    debt = sum(info[k]["debt"]*n[k] for k in n); intr = sum(info[k]["interest"]*n[k] for k in n)
    opex5 = sum(info[k]["opex"]*LIFE_M*n[k] for k in n); tot = capex+intr+opex5
    eqv = sum(info[k]["equiv"]*n[k] for k in n); ef = sum(info[k]["ef"]*n[k] for k in n); eqmw = sum(info[k]["eqmw"]*n[k] for k in n)
    w.writerow([])
    w.writerow(["FIRM PROGRAM T1-T5 (member)","Capex","Equity","Debt","Interest","Opex 5yr/sleeve","TOTAL 5yr cost","GB300-equiv","Dense FP8 (EF)","GB300-eq MW","$/equiv-hr @90%","$/PF-h @90%","$/GB300-W/mo","Refresh reserve memo (4yr)","Chip residual memo (10%)"])
    res4 = sum(info[k]["chip"]*RESERVE_PCT*4*n[k] for k in n)
    w.writerow(["", round(capex), eqty, round(debt), round(intr), round(opex5), round(tot), int(eqv), round(ef,1), round(eqmw,1),
                round(tot*1e6/(eqv*8760*5*AVAIL),2), round(tot*1e6/(ef*1000*8760*5*AVAIL),4), round(tot/eqmw/60,2),
                round(res4), round(sum(info[k]["chip"]*n[k] for k in n)*CHIP_RESID)])
    w.writerow(["NO full-program (T1-T7) total exists: T6-T7 are unpriced options.",])
    w.writerow([])
    # ---- T3 siting scenario: colo vs owned PropCo ----
    v = info["VR72"]
    c_eq = round(EQUITY_PCT*v["chip"]); c_db = v["chip"]-c_eq
    c_pmt = c_db*ann_factor(v["rate"], LIFE_M); c_int = c_pmt*LIFE_M-c_db
    ownd5 = v["allin"] + v["interest"] + v["opex"]*LIFE_M
    resid_bldg = v["prop"]*(1-LIFE_M/PROPCO_LIFE_M)
    eqhrs90 = v["equiv"]*8760*5*AVAIL
    w.writerow(["SCENARIO - T3 SITING: RUBIN-READY COLO vs OWNED PROPCO (per member; same 30-rack ChipCo both ways)"])
    w.writerow(["Metric","T3 owned PropCo (base)","T3 colo @$130/kW-mo","T3 colo @$155","T3 colo @$180"])
    w.writerow(["Capex", round(v["allin"],1), round(v["chip"],1), round(v["chip"],1), round(v["chip"],1)])
    w.writerow(["Equity (37%)", v["equity"], c_eq, c_eq, c_eq])
    w.writerow(["Debt @8.5%/5yr", round(v["debt"],1), round(c_db,1), round(c_db,1), round(c_db,1)])
    w.writerow(["Interest", round(v["interest"],1), round(c_int,1), round(c_int,1), round(c_int,1)])
    colo5 = {}
    tot5c = {}
    for rate in (130,155,180):
        cf = COLO_KW_BILLED*rate/1e6
        opx = cf + v["elec"] + COLO_STAFF_MO + v["maint"]
        colo5[rate] = cf*LIFE_M
        tot5c[rate] = v["chip"] + c_int + opx*LIFE_M
    w.writerow(["Colo fees 5yr","-", round(colo5[130],1), round(colo5[155],1), round(colo5[180],1)])
    w.writerow(["5yr all-in cash", round(ownd5,1), round(tot5c[130],1), round(tot5c[155],1), round(tot5c[180],1)])
    w.writerow(["Cash delta vs owned","-", round(tot5c[130]-ownd5,1), round(tot5c[155]-ownd5,1), round(tot5c[180]-ownd5,1)])
    w.writerow(["Economic view (owned netted of ~2/3 building residual)", round(ownd5-resid_bldg,1), round(tot5c[130],1), round(tot5c[155],1), round(tot5c[180],1)])
    w.writerow(["$/GB300-equiv-hr @90%", round(ownd5*1e6/eqhrs90,2), round(tot5c[130]*1e6/eqhrs90,2), round(tot5c[155]*1e6/eqhrs90,2), round(tot5c[180]*1e6/eqhrs90,2)])
    w.writerow(["Compute available","m21 (21mo construction)","~m18 (order-to-live ~6mo)","~m18","~m18"])
    w.writerow(["Read","Wins 2nd generation: refresh-in-place facility cost ~$13M/5yr term vs $52-72M colo","Wins 5yr cash + 3 months earlier compute","~economic wash vs owned","Owned wins economically"])
    w.writerow(["Decision gate","Rubin-ready (187-227kW/rack liquid) colo term sheet: rate + reserved-power basis + CDU responsibility + ~20MW availability window. Scarcity of Rubin-grade colo in Europe is the binding constraint - $130 is optimistic for 227kW racks.",])
    w.writerow([])
    w.writerow(["SENSITIVITIES (per member unless noted)"])
    w.writerow(["GB300 ChipCo 244/266/294","5yr sleeve cost 407/431/462 approx; program capex -44/base/+56"])
    w.writerow(["Rubin ChipCo 234/293","5yr sleeve cost ~468/531; program capex -178/base"])
    w.writerow(["PropCo 260/267.5/275 per block","member share 86.7/89.2/91.7"])
    w.writerow(["Colo 130/155/180 $/kW-mo","GB300 sleeve 5yr colo 52/62/72 (+$20M low->high)"])
    w.writerow(["Energy EUR 70/90/110 all-in","program energy 5yr approx -22%/base/+22%"])
    w.writerow(["FX 1.05/1.143/1.25 $/EUR","EUR-denominated opex -8%/base/+9%"])
    w.writerow(["Residual 0/5/10/15%","memo only; not netted in costs"])
    w.writerow(["Schedule +0/6/12mo","carry cost & idle debt service; see timing scenarios in project_ampere.md"])
    w.writerow([])
    w.writerow(["MONTHLY MEMBER CASH SCHEDULE (T1-T5 firm program; outbound only). Depreciation & refresh reserve = memo, not in Cash out."])
    w.writerow(["Month","Events","PropCo constr equity","Chip equity","New debt","Debt balance","Interest","Principal","Debt service",
                "Colo fees","Electricity","Staff","Security","Chip maint","PropCo opex","Opex total","Cash out","Cum cash",
                "Dep chips (memo)","Dep bldg (memo)","Fleet GB300-equiv","Cum $/equiv-hr (100% hrs)","Fleet FP8 (EF)","Cum $/PFLOPS-hr (100% hrs)","Fleet GB300-eq MW","Cum $/GB300-W/mo","GPU pkgs online","Refresh reserve (memo)","Cum reserve (memo)"])
    for r in rows: w.writerow(r)

print(f"Written {out}")
for k in ["GB300","VR72"]:
    s = info[k]; tot5 = s["allin"]+s["interest"]+s["opex"]*60
    print(f'{k}: allin {s["allin"]:.1f} = eq {s["equity"]} + debt {s["debt"]:.1f} @ {s["rate"]*100:.1f}% | opex {s["opex"]:.2f}/mo | '
          f'5yr {tot5:.0f} | ${tot5*1e6/(s["pkgs"]*43800*AVAIL):.2f}/GPU-hr@90 | ${tot5*1e6/(s["equiv"]*43800*AVAIL):.2f}/equiv-hr@90 | '
          f'${tot5*1e6/(s["ef"]*1000*43800*AVAIL):.3f}/PF-h@90 | ${tot5/s["eqmw"]/60:.2f}/W-mo | eqMW x{s["eqmw"]/s["mw"]:.2f}')
print(f'FIRM T1-T5 member: capex {capex:.0f} (eq {eqty} / debt {debt:.0f}) + int {intr:.0f} + opex {opex5:.0f} = {tot:.0f} '
      f'| {int(eqv)} equiv | {ef:.0f} EF | ${tot*1e6/(eqv*43800*AVAIL):.2f}/equiv-hr@90 | ${tot*1e6/(ef*1000*43800*AVAIL):.4f}/PF-h@90 | ${tot/eqmw/60:.2f}/W-mo')
print(f'JV x3: capex {3*capex:.0f}, 5yr {3*tot:.0f}, EF {3*ef:.0f} | reserve memo {res4:.0f}/member over 4yr')
print(f'Ratio check: per-GPU {PF_VR/PF_GB:.2f}x, per-MW {(1260/227)/(360/142):.4f}x | y1 cash = see m11 row')

# ---------------- Inject monthly table into the v3 one-pager ----------------
HTML = "/Users/gab/ff/compute/project_ampere.html"
START, ENDM = "<!-- MONTHLY_TABLE_START -->", "<!-- MONTHLY_TABLE_END -->"
try:
    with open(HTML) as fh: page = fh.read()
    if START in page and ENDM in page:
        trs = []
        for r in rows:
            m, evs = r[0], r[1]
            cap = r[2]+r[3]; ds = r[8]; op = r[15]; totc = r[16]; cum = r[17]; pkgs = r[26]; eqv2 = r[20]
            cls = ' class="ms"' if evs else ''
            trs.append(f'<tr{cls}><td class="num">m{m}</td><td>{evs}</td>'
                       f'<td class="num">{cap:,.1f}</td><td class="num">{ds:,.2f}</td><td class="num">{op:,.2f}</td>'
                       f'<td class="num">{totc:,.1f}</td><td class="num">{cum:,.0f}</td>'
                       f'<td class="num">{pkgs:,}</td><td class="num">{eqv2:,}</td></tr>')
        block = START + "\n" + "\n".join(trs) + "\n" + ENDM
        pre, rest = page.split(START,1); _, post = rest.split(ENDM,1)
        with open(HTML,"w") as fh: fh.write(pre+block+post)
        print(f"Injected {len(trs)} monthly rows into {HTML}")
    else:
        print("NOTE: markers not found; skipped HTML injection.")
except FileNotFoundError:
    print("NOTE: v3 HTML not found; skipped injection.")
