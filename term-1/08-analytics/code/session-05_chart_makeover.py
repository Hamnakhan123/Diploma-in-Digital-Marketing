# Data visualisation: a bad chart vs a good chart for the same data, plus a 4-panel marketing
# dashboard. Prepared by Hamna Zahid Khan, Junior Lecturer. Illustrative monthly data (PKR).
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
channels = ["Google Search", "Instagram", "TikTok", "Facebook", "Email", "WhatsApp", "YouTube", "Referral", "Direct"]
revenue = [620, 540, 390, 300, 280, 260, 110, 90, 70]   # PKR thousands

# BAD: 3-D-style pie with 9 slices, legend lookup, no sorting, no numbers
fig, ax = plt.subplots(figsize=(6, 4.5))
ax.pie(revenue, labels=None, startangle=90, shadow=True, explode=[0.05] * 9)
ax.legend(channels, loc="center left", bbox_to_anchor=(1, .5), fontsize=7)
ax.set_title("Revenue")
plt.tight_layout(); plt.savefig("session-05_bad_chart.png", dpi=90)

# GOOD: sorted horizontal bars, direct labels, highlight, clear title with the insight
fig, ax = plt.subplots(figsize=(7.5, 4.5), facecolor=BG); ax.set_facecolor(BG)
order = sorted(zip(revenue, channels))
vals, names = zip(*order)
cols = [FIRE if n in ("Google Search", "Instagram") else "#5b5470" for n in names]
bars = ax.barh(names, vals, color=cols)
for b, v in zip(bars, vals): ax.text(v + 8, b.get_y() + b.get_height() / 2, f"{v}k", va="center", color=TEXT, fontsize=8)
ax.set_title("Google Search and Instagram bring 44% of revenue", color=GOLD, loc="left")
ax.set_xlabel("Revenue, PKR thousands (October)", color=TEXT)
ax.tick_params(colors=TEXT, labelsize=8)
for side in ("top", "right"): ax.spines[side].set_visible(False)
for side in ("left", "bottom"): ax.spines[side].set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-05_good_chart.png", dpi=110, facecolor=BG)
share = (620 + 540) / sum(revenue) * 100
print(f"Top-2 share check: (620 + 540) / {sum(revenue)} = {share:.1f}%")

# DASHBOARD: KPI tiles + trend + channel mix + funnel
months = ["May", "Jun", "Jul", "Aug", "Sep", "Oct"]
rev = [2.1, 2.0, 2.2, 2.35, 2.5, 2.66]; spend = [0.62, 0.6, 0.64, 0.66, 0.7, 0.72]
fig = plt.figure(figsize=(12, 6.5), facecolor=BG)
gs = fig.add_gridspec(2, 3)
tiles = [("Revenue (Oct)", "PKR 2.66 M", "+6.4% MoM"), ("ROAS (Oct)", f"{rev[-1] / spend[-1]:.2f}", "target 3.5"), ("Orders (Oct)", "640", "+5.1% MoM")]
for i, (t, v, d) in enumerate(tiles):
    ax = fig.add_subplot(gs[0, i]); ax.set_facecolor("#1b1430"); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color("#3b3355")
    ax.text(.5, .68, t, ha="center", color=VIOLET, fontsize=11, transform=ax.transAxes)
    ax.text(.5, .4, v, ha="center", color=GOLD, fontsize=24, weight="bold", transform=ax.transAxes)
    ax.text(.5, .16, d, ha="center", color=TEXT, fontsize=9, transform=ax.transAxes)
ax = fig.add_subplot(gs[1, 0]); ax.set_facecolor(BG)
ax.plot(months, rev, color=FIRE, marker="o", label="Revenue"); ax.plot(months, spend, color=VIOLET, marker="s", label="Ad spend")
ax.set_title("Revenue vs spend (PKR M)", color=GOLD, fontsize=10); ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=7)
ax2 = fig.add_subplot(gs[1, 1]); ax2.set_facecolor(BG)
ax2.barh(list(names[-5:]), list(vals[-5:]), color=FIRE); ax2.set_title("Top 5 channels (PKR k)", color=GOLD, fontsize=10)
ax3 = fig.add_subplot(gs[1, 2]); ax3.set_facecolor(BG)
stages, cnt = ["Sessions", "Product views", "Add to cart", "Checkout", "Orders"], [52000, 21000, 4300, 1500, 640]
ax3.bar(stages, cnt, color=[VIOLET, "#38BDF8", GOLD, FIRE, EMBER]); ax3.set_yscale("log"); ax3.set_title("Funnel (log scale)", color=GOLD, fontsize=10)
for a in (ax, ax2, ax3):
    a.tick_params(colors=TEXT, labelsize=7)
    for s in a.spines.values(): s.set_color("#3b3355")
ax3.set_xticks(range(5)); ax3.set_xticklabels(stages, rotation=20)
fig.suptitle("Monthly marketing dashboard - October", color=TEXT, fontsize=13)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-05_dashboard.png", dpi=100, facecolor=BG)
print("Saved session-05_bad_chart.png, session-05_good_chart.png, session-05_dashboard.png")
