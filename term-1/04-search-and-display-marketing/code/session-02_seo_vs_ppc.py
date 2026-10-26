# Compare 18 months of paid search (PPC) and SEO traffic and cost for one small business.
# Prepared by Hamna Zahid Khan, Junior Lecturer. All figures are an illustrative model.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F5EEFF"
months = list(range(1, 19))
CPC = 45                     # PKR per click
ppc_budget = 90_000          # PKR per month
ppc_clicks = [ppc_budget // CPC] * 18

seo_cost = [120_000, 60_000] + [40_000] * 16         # setup, then content + links each month
seo_clicks = [50, 120, 250, 420, 650, 900, 1150, 1400, 1650, 1850, 2050, 2200,
              2350, 2500, 2600, 2700, 2750, 2800]

cum = lambda xs: [sum(xs[:i + 1]) for i in range(len(xs))]
ppc_cpc = [c / k for c, k in zip(cum([ppc_budget] * 18), cum(ppc_clicks))]
seo_cpc = [c / k for c, k in zip(cum(seo_cost), cum(seo_clicks))]

print(f"{'Month':<6}{'PPC clicks':>11}{'SEO clicks':>11}{'PPC cost/click':>16}{'SEO cost/click':>16}")
for m in months:
    print(f"{m:<6}{ppc_clicks[m-1]:>11,}{seo_clicks[m-1]:>11,}{ppc_cpc[m-1]:>16.1f}{seo_cpc[m-1]:>16.1f}")
cross = next(m for m in months if seo_cpc[m - 1] < ppc_cpc[m - 1])
monthly_cross = next(m for m in months if seo_cost[m - 1] / seo_clicks[m - 1] < CPC)
print(f"\n18-month totals: PPC {sum(ppc_clicks):,} clicks for PKR {ppc_budget*18:,}; "
      f"SEO {sum(seo_clicks):,} clicks for PKR {sum(seo_cost):,}")
print(f"SEO's cost per click within a single month drops below PPC's in month {monthly_cross}")
print(f"SEO's cumulative cost per click (all spend so far) drops below PPC's in month {cross}")
print("If the PPC budget stops, paid clicks fall to 0 the next day; organic clicks keep coming.")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.4), facecolor=BG)
for ax in (a1, a2):
    ax.set_facecolor(BG); ax.tick_params(colors=TEXT)
    for s in ax.spines.values(): s.set_color("#3b3355")
    ax.set_xlabel("Month", color=TEXT); ax.set_xticks(months)
a1.plot(months, ppc_clicks, color=FIRE, lw=2.5, marker="o", label="Paid search (PPC)")
a1.plot(months, seo_clicks, color=VIOLET, lw=2.5, marker="o", label="SEO (organic)")
a1.set_title("Monthly clicks", color=GOLD); a1.legend(facecolor=BG, labelcolor=TEXT)
a2.plot(months, ppc_cpc, color=FIRE, lw=2.5, marker="o", label="PPC")
a2.plot(months, seo_cpc, color=VIOLET, lw=2.5, marker="o", label="SEO")
a2.set_yscale("log"); a2.set_title("Cumulative cost per click (PKR, log scale)", color=GOLD)
a2.axvline(cross, color=GOLD, ls="--", lw=1); a2.legend(facecolor=BG, labelcolor=TEXT)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative model", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_seo_vs_ppc.png", dpi=110, facecolor=BG)
print("Saved session-02_seo_vs_ppc.png")
