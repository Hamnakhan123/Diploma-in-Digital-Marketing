# Estimate a competitor's monthly Google Ads clicks and spend, the way SpyFu-style tools do.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Estimates only - tools model these from samples.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F5EEFF"
AD_CTR = {1: 0.07, 2: 0.035, 3: 0.02, 4: 0.012}   # illustrative CTR by ad position
SHARE_SHOWN = 0.6                                 # share of searches where the ad actually appeared

# keyword: (monthly searches, observed ad position, average CPC in PKR)
seen_ads = {
    "grocery delivery near me": (9900, 1, 62),
    "online grocery karachi": (6600, 1, 55),
    "cooking oil price in pakistan": (8100, 2, 28),
    "baby diapers price": (5400, 2, 35),
    "monthly ration list": (3600, 3, 18),
    "atta 10kg price": (4400, 3, 22),
}

rows = []
for kw, (vol, pos, cpc) in seen_ads.items():
    clicks = vol * SHARE_SHOWN * AD_CTR[pos]
    rows.append((kw, vol, pos, cpc, clicks, clicks * cpc))
rows.sort(key=lambda r: -r[5])

print(f"{'Keyword':<32}{'Vol':>7}{'Pos':>4}{'CPC':>5}{'Clicks':>8}{'Spend PKR':>11}")
for kw, vol, pos, cpc, clk, spend in rows:
    print(f"{kw:<32}{vol:>7,}{pos:>4}{cpc:>5}{clk:>8.0f}{spend:>11,.0f}")
tc, ts = sum(r[4] for r in rows), sum(r[5] for r in rows)
print(f"{'TOTAL':<32}{'':>16}{tc:>8.0f}{ts:>11,.0f}")
print(f"\nEstimated competitor budget: about PKR {ts:,.0f}/month, PKR {ts/30:,.0f}/day")
print(f"Top 2 keywords take {sum(r[5] for r in rows[:2]) / ts:.0%} of the estimated spend")

fig, ax = plt.subplots(figsize=(10, 4.2), facecolor=BG)
ax.set_facecolor(BG); ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
names = [r[0] for r in rows][::-1]
ax.barh(names, [r[5] for r in rows][::-1], color=[FIRE, FIRE, GOLD, GOLD, VIOLET, VIOLET][::-1])
for i, v in enumerate([r[5] for r in rows][::-1]):
    ax.text(v + 300, i, f"PKR {v:,.0f}", va="center", color=TEXT, fontsize=9)
ax.set_xlim(0, max(r[5] for r in rows) * 1.25)
ax.set_title("Estimated monthly ad spend by keyword - Competitor A", color=GOLD)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · estimates", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-05_competitor_spend.png", dpi=110, facecolor=BG)
print("Saved session-05_competitor_spend.png")
