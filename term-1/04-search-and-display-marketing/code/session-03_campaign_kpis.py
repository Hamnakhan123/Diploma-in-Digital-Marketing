# Compare Google Ads campaign types for one online clothing store using the core KPIs.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Figures are an illustrative month, in PKR.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
GROSS_MARGIN = 0.40          # 40% of revenue is profit before advertising

campaigns = {  # type: impressions, clicks, cost, conversions, revenue
    "Search":           (180_000, 9_000, 405_000, 270, 1_350_000),
    "Shopping":         (420_000, 8_400, 294_000, 210, 1_050_000),
    "Display":        (2_400_000, 6_000, 120_000,  30,   150_000),
    "Video (YouTube)":(1_500_000, 4_500, 150_000,  15,    75_000),
    "Performance Max":  (900_000, 12_600, 378_000, 252, 1_260_000),
}

def kpis(imp, clk, cost, conv, rev):
    ctr = clk / imp * 100
    cpc = cost / clk
    cpm = cost / imp * 1000
    cr = conv / clk * 100
    cpa = cost / conv
    roas = rev / cost
    roi = (rev * GROSS_MARGIN - cost) / cost * 100
    return ctr, cpc, cpm, cr, cpa, roas, roi

print(f"{'Campaign':<17}{'CTR%':>6}{'CPC':>7}{'CPM':>7}{'CR%':>6}{'CPA':>8}{'ROAS':>6}{'ROI%':>7}")
res = {}
for name, v in campaigns.items():
    res[name] = k = kpis(*v)
    print(f"{name:<17}{k[0]:>6.2f}{k[1]:>7.1f}{k[2]:>7.0f}{k[3]:>6.2f}{k[4]:>8,.0f}{k[5]:>6.1f}{k[6]:>7.0f}")

tot = [sum(v[i] for v in campaigns.values()) for i in range(5)]
t = kpis(*tot)
print(f"{'TOTAL':<17}{t[0]:>6.2f}{t[1]:>7.1f}{t[2]:>7.0f}{t[3]:>6.2f}{t[4]:>8,.0f}{t[5]:>6.1f}{t[6]:>7.0f}")
breakeven = 1 / GROSS_MARGIN
print(f"\nBreak-even ROAS at a {GROSS_MARGIN:.0%} margin = 1 / {GROSS_MARGIN} = {breakeven:.1f}")
for name, k in res.items():
    verdict = "profitable" if k[5] > breakeven else "loses money on last-click sales"
    print(f"  {name:<17} ROAS {k[5]:.1f} -> {verdict}")
print("Note: Display and Video are usually judged on reach, views and assisted conversions, not last-click ROAS.")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.4), facecolor=BG)
names = list(res)
cols = [FIRE, GOLD, VIOLET, EMBER, "#38BDF8"]
for ax in (a1, a2):
    ax.set_facecolor(BG); ax.tick_params(colors=TEXT, labelsize=8)
    for s in ax.spines.values(): s.set_color("#3b3355")
a1.bar(names, [res[n][4] for n in names], color=cols)
a1.set_title("Cost per acquisition (PKR) - lower is better", color=GOLD)
a2.bar(names, [res[n][5] for n in names], color=cols)
a2.axhline(breakeven, color=TEXT, ls="--", lw=1)
a2.text(4.4, breakeven + 0.15, "break-even ROAS 2.5", color=TEXT, ha="right", fontsize=8)
a2.set_title("ROAS (revenue / ad cost) - higher is better", color=GOLD)
for ax in (a1, a2):
    ax.set_xticks(range(len(names))); ax.set_xticklabels(names, rotation=15)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-03_campaign_kpis.png", dpi=110, facecolor=BG)
print("Saved session-03_campaign_kpis.png")
