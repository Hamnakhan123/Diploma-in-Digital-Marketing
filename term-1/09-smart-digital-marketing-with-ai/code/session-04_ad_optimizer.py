# How AI ad tools (Adzooma, Google/Meta automated bidding) shift budget to winning ads automatically:
# a Thompson-sampling "multi-armed bandit" versus a fixed equal split. Prepared by Hamna Zahid Khan, Junior Lecturer.
# True click-through rates are hidden from the algorithm; it learns them from clicks. Numbers are illustrative.
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
ADS = ["A: 'Flat 30% off'", "B: 'Free delivery Pakistan-wide'", "C: 'New Eid collection'", "D: 'Buy 2 get 1'"]
TRUE_CTR = np.array([0.010, 0.014, 0.022, 0.016])
IMPRESSIONS, BATCH = 100_000, 1_000
rng = np.random.default_rng(2)

def run(strategy):
    clicks, shown = np.zeros(4), np.zeros(4)
    share_c = []
    for _ in range(IMPRESSIONS // BATCH):
        if strategy == "equal":
            alloc = np.full(4, BATCH // 4)
        else:  # Thompson sampling: draw a plausible CTR for each ad from Beta(clicks+1, misses+1)
            draws = rng.beta(clicks + 1, shown - clicks + 1, size=(BATCH, 4))
            alloc = np.bincount(draws.argmax(axis=1), minlength=4)
        c = rng.binomial(alloc.astype(int), TRUE_CTR)
        clicks += c; shown += alloc
        share_c.append(alloc[2] / BATCH)
    return clicks, shown, share_c

for name in ["equal", "bandit"]:
    clicks, shown, share = run(name)
    print(f"{name.upper():<7} total clicks {clicks.sum():,.0f}  overall CTR {clicks.sum() / shown.sum():.2%}")
    for a, s, c in zip(ADS, shown, clicks):
        print(f"   {a:<32} impressions {s:>6,.0f}  clicks {c:>5,.0f}  CTR {c / max(s, 1):.2%}")
    if name == "equal": base = clicks.sum(); eq_share = share
    else: bandit_share = share; gain = clicks.sum() - base
cpc_budget = 25_000   # PKR
print(f"\nBandit gained {gain:+,.0f} clicks ({gain / base:+.0%}) from the same 100,000 impressions.")
print(f"With PKR {cpc_budget:,} spent on these impressions, cost per click falls from PKR {cpc_budget / base:.1f} to PKR {cpc_budget / (base + gain):.1f}")

fig, ax = plt.subplots(figsize=(8.5, 4), facecolor=BG); ax.set_facecolor(BG)
x = np.arange(1, len(eq_share) + 1) * BATCH / 1000
ax.plot(x, np.array(bandit_share) * 100, color=FIRE, lw=2, label="Bandit (learns)")
ax.plot(x, np.array(eq_share) * 100, color=VIOLET, ls="--", label="Equal split")
ax.set_xlabel("Impressions served (thousands)", color=TEXT)
ax.set_ylabel("% of traffic to best ad C", color=TEXT)
ax.set_title("The algorithm moves traffic to the winning ad within a few thousand impressions", color=GOLD, fontsize=10)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · simulated", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-04_bandit_share.png", dpi=110, facecolor=BG)
print("Saved session-04_bandit_share.png")
