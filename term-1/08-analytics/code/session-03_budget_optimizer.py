# Measure campaign performance and re-allocate budget using marginal CPA from diminishing-returns
# curves. Prepared by Hamna Zahid Khan, Junior Lecturer. Illustrative channels for a Karachi retailer.
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
# conversions(spend) = a * ln(1 + spend / b): fast early gains, then diminishing returns
curves = {"Google Search": (420, 120_000), "Meta Ads": (520, 220_000), "TikTok Ads": (300, 150_000), "YouTube": (160, 200_000)}
current = {"Google Search": 150_000, "Meta Ads": 250_000, "TikTok Ads": 200_000, "YouTube": 200_000}
BUDGET = sum(current.values())

def conv(ch, spend):
    a, b = curves[ch]
    return a * math.log(1 + spend / b)

def report(alloc, title):
    print(title)
    tot = 0
    for ch, s in alloc.items():
        c = conv(ch, s); tot += c
        marginal = (conv(ch, s + 10_000) - c) / 10_000
        cpa = f"{s / c:>6,.0f}" if c else "     -"
        print(f"  {ch:<14} spend {s:>8,.0f}  conv {c:>6.0f}  CPA {cpa}  marginal CPA {1 / marginal:>6,.0f}")
    print(f"  TOTAL conversions {tot:,.0f}  blended CPA {BUDGET / tot:,.0f}\n")
    return tot

before = report(current, "Current allocation:")
# Greedy optimisation: give each PKR 10,000 to the channel with the lowest marginal CPA
alloc = {ch: 0 for ch in curves}
for _ in range(BUDGET // 10_000):
    best = max(curves, key=lambda ch: conv(ch, alloc[ch] + 10_000) - conv(ch, alloc[ch]))
    alloc[best] += 10_000
after = report(alloc, "Optimised allocation (equal marginal CPA):")
print(f"Same budget, {after - before:+.0f} conversions ({(after - before) / before:+.1%})")

fig, ax = plt.subplots(figsize=(9, 4.4), facecolor=BG); ax.set_facecolor(BG)
xs = range(0, 600_001, 10_000)
for (ch, c) in zip(curves, [FIRE, VIOLET, EMBER, GOLD]):
    ax.plot([x / 1000 for x in xs], [conv(ch, x) for x in xs], color=c, lw=2, label=ch)
    ax.scatter(alloc[ch] / 1000, conv(ch, alloc[ch]), color=c, s=60, edgecolor=TEXT)
ax.set_xlabel("Monthly spend (PKR thousands)", color=TEXT); ax.set_ylabel("Conversions", color=TEXT)
ax.set_title("Diminishing returns by channel (dots = optimised spend)", color=GOLD)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative curves", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-03_budget_curves.png", dpi=110, facecolor=BG)
print("Saved session-03_budget_curves.png")
