# Plan and compare paid social campaigns: reach, frequency, CPM, CPC, CPA, ROAS, and
# the effect of the bid strategy. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Illustrative one-month data in PKR for an Islamabad online shoe store ("Qadam").
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
MARGIN = 0.45   # gross margin before advertising

# name: spend, impressions, reach, link clicks, purchases, revenue
camps = {
    "Meta - Awareness (Reels)":   (60_000, 600_000, 240_000, 1_800,  12,  54_000),
    "Meta - Traffic (Carousel)":  (80_000, 320_000, 150_000, 4_800,  48, 216_000),
    "Meta - Sales (Advantage+)":  (120_000, 400_000, 170_000, 5_200, 104, 468_000),
    "TikTok - In-Feed (Sales)":   (70_000, 700_000, 310_000, 4_200,  42, 168_000),
    "Retargeting - Cart viewers": (30_000,  90_000,  18_000, 1_350,  45, 202_500),
}
print(f"{'Campaign':<28}{'Freq':>5}{'CPM':>6}{'CTR%':>6}{'CPC':>5}{'CR%':>5}{'CPA':>7}{'ROAS':>6}")
results = {}
for n, (spend, imp, reach, clk, buy, rev) in camps.items():
    freq = imp / reach
    cpm = spend / imp * 1000
    ctr = clk / imp * 100
    cpc = spend / clk
    cr = buy / clk * 100
    cpa = spend / buy
    roas = rev / spend
    results[n] = (cpa, roas)
    print(f"{n:<28}{freq:>5.1f}{cpm:>6.0f}{ctr:>6.2f}{cpc:>5.0f}{cr:>5.1f}{cpa:>7,.0f}{roas:>6.2f}")
tot = [sum(c[i] for c in camps.values()) for i in range(6)]
print(f"\nTotal spend PKR {tot[0]:,} -> revenue PKR {tot[5]:,}; blended ROAS {tot[5] / tot[0]:.2f}; break-even ROAS {1 / MARGIN:.2f}")
profit = tot[5] * MARGIN - tot[0]
print(f"Profit after ads = {tot[5]:,} x {MARGIN} - {tot[0]:,} = PKR {profit:,.0f}")

# Bid strategy comparison for the same PKR 100,000 budget (illustrative platform behaviour)
print("\nBid strategy what-if for PKR 100,000:")
for name, cpa in (("Lowest cost (no cap)", 1_150), ("Cost cap PKR 1,000", 980), ("Bid cap PKR 900", 870)):
    delivered = 1.0 if name.startswith("Lowest") else (0.82 if "Cost" in name else 0.55)
    spent = 100_000 * delivered
    print(f"  {name:<22} spends PKR {spent:>9,.0f}  ~CPA {cpa:>5,}  ~purchases {spent / cpa:>5.0f}")

fig, ax = plt.subplots(figsize=(10, 4.6), facecolor=BG); ax.set_facecolor(BG)
cols = [VIOLET, GOLD, FIRE, EMBER, "#38BDF8"]
for (n, (cpa, roas)), c in zip(results.items(), cols):
    ax.scatter(cpa, roas, s=camps[n][0] / 150, color=c, alpha=.85, label=n)
ax.axhline(1 / MARGIN, color=TEXT, ls="--", lw=1); ax.text(4_900, 1 / MARGIN + .1, "break-even ROAS 2.22", color=TEXT, fontsize=8, ha="right")
ax.set_xlabel("CPA (PKR) - lower is better", color=TEXT); ax.set_ylabel("ROAS - higher is better", color=TEXT)
ax.set_title("Paid social campaigns: CPA vs ROAS (bubble size = spend)", color=GOLD)
ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=7, loc="upper center", markerscale=0.35)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-03_social_ad_planner.png", dpi=110, facecolor=BG)
print("Saved session-03_social_ad_planner.png")
