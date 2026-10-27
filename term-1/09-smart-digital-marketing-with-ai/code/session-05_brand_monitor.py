# Brand-reputation monitoring in the style of Brand24: daily mention volume and sentiment,
# with an automatic alert when volume spikes AND sentiment drops. Prepared by Hamna Zahid Khan, Junior Lecturer.
# 30 days of simulated mentions for an illustrative Pakistani cosmetics brand.
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(9)
days = np.arange(1, 31)
volume = rng.poisson(120, 30)
pos_share = np.clip(rng.normal(0.62, 0.04, 30), 0, 1)
neg_share = np.clip(rng.normal(0.12, 0.03, 30), 0, 1)
# Day 18: an influencer posts about a skin reaction; day 24: a positive charity campaign
volume[17:20] = [610, 480, 260]; neg_share[17:20] = [0.58, 0.47, 0.30]; pos_share[17:20] = [0.20, 0.27, 0.40]
volume[23] = 340; pos_share[23] = 0.80; neg_share[23] = 0.05

net = (pos_share - neg_share) * 100
alerts = []
for d in range(7, 30):
    base_v, base_net = volume[d - 7:d].mean(), net[d - 7:d].mean()
    if volume[d] > 2 * base_v and net[d] < base_net - 20:
        alerts.append(d + 1)
        print(f"ALERT day {d + 1}: volume {volume[d]} (7-day avg {base_v:.0f}), net sentiment {net[d]:+.0f} (avg {base_net:+.0f})")
    elif volume[d] > 2 * base_v:
        print(f"Spike day {d + 1}: volume {volume[d]} with net sentiment {net[d]:+.0f} -> positive buzz, amplify it")
print(f"\nMonth: {volume.sum():,} mentions, average net sentiment {net.mean():+.1f}")
# reach-weighted share of voice vs two competitors (illustrative monthly totals)
sov = {"Our brand": volume.sum(), "Competitor X": 3900, "Competitor Y": 2600}
tot = sum(sov.values())
print("Share of voice: " + ", ".join(f"{k} {v / tot:.0%}" for k, v in sov.items()))

fig, ax1 = plt.subplots(figsize=(9, 4), facecolor=BG); ax1.set_facecolor(BG)
ax1.bar(days, volume, color=VIOLET, alpha=0.7, label="Mentions")
ax2 = ax1.twinx()
ax2.plot(days, net, color=GOLD, lw=2, marker="o", ms=3, label="Net sentiment")
for a in alerts:
    ax1.annotate("crisis alert", (a, volume[a - 1]), xytext=(a + 1.2, volume[a - 1] - 40), color=EMBER,
                 arrowprops=dict(arrowstyle="->", color=EMBER), fontsize=8)
ax1.set_xlabel("Day of month", color=TEXT); ax1.set_ylabel("Mentions", color=TEXT); ax2.set_ylabel("Net sentiment", color=TEXT)
ax1.set_title("Brand mentions and sentiment: a crisis on day 18, positive buzz on day 24", color=GOLD, fontsize=10)
for a in (ax1, ax2):
    a.tick_params(colors=TEXT)
    for sp in a.spines.values(): sp.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · simulated", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-05_brand_monitor.png", dpi=110, facecolor=BG)
print("Saved session-05_brand_monitor.png")
