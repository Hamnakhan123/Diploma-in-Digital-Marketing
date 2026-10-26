# A/B split test for two social ad creatives: sample size planning, a two-proportion z-test,
# confidence intervals and a chart. Standard library + matplotlib only.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Illustrative data (PKR) for a Karachi gym's lead ads.
import math
from statistics import NormalDist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
Z = NormalDist()

def sample_size(p1, mde_rel, alpha=0.05, power=0.80):
    """people needed PER variant to detect a relative lift of mde_rel over baseline p1"""
    p2 = p1 * (1 + mde_rel)
    za, zb = Z.inv_cdf(1 - alpha / 2), Z.inv_cdf(power)
    pbar = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)

base_ctr = 0.012
for lift in (0.10, 0.20, 0.30):
    print(f"Baseline CTR 1.2%, detect +{lift:.0%} lift -> {sample_size(base_ctr, lift):,} impressions per variant")

# Results after 10 days (equal budget split)
A = dict(name="A: gym interior photo", imp=48_000, clicks=528, leads=42, spend=24_000)
B = dict(name="B: member transformation video", imp=47_500, clicks=693, leads=66, spend=24_000)

def ztest(x1, n1, x2, n2):
    p1, p2 = x1 / n1, x2 / n2
    p = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se
    return p1, p2, z, 2 * (1 - Z.cdf(abs(z)))

def ci(x, n):
    p = x / n; h = 1.96 * math.sqrt(p * (1 - p) / n)
    return p - h, p + h

p1, p2, z, pv = ztest(A["clicks"], A["imp"], B["clicks"], B["imp"])
print(f"\nCTR  A {p1:.2%}  vs  B {p2:.2%}  | relative lift {(p2 - p1) / p1:+.1%} | z = {z:.2f}, p = {pv:.1e}")
print("Result:", "significant at 95% - B wins on CTR" if pv < 0.05 else "not significant - keep testing")
l1, l2, zl, pl = ztest(A["leads"], A["clicks"], B["leads"], B["clicks"])
print(f"Lead rate per click  A {l1:.2%}  vs  B {l2:.2%} | z = {zl:.2f}, p = {pl:.3f}")
for v in (A, B):
    print(f"  {v['name']:<32} CPL = PKR {v['spend']:,} / {v['leads']} = PKR {v['spend'] / v['leads']:,.0f}")

fig, ax = plt.subplots(figsize=(8, 4), facecolor=BG); ax.set_facecolor(BG)
for i, (v, c) in enumerate(((A, VIOLET), (B, FIRE))):
    p = v["clicks"] / v["imp"]; lo, hi = ci(v["clicks"], v["imp"])
    ax.bar(i, p * 100, color=c, width=.5)
    ax.errorbar(i, p * 100, yerr=[[p * 100 - lo * 100], [hi * 100 - p * 100]], color=TEXT, capsize=8)
    ax.text(i, hi * 100 + .03, f"{p:.2%}", ha="center", color=TEXT)
ax.set_xticks([0, 1]); ax.set_xticklabels([A["name"], B["name"]], color=TEXT)
ax.set_ylabel("CTR % (95% confidence interval)", color=TEXT); ax.tick_params(colors=TEXT)
ax.set_title(f"A/B test: CTR with 95% intervals (p = {pv:.1e})", color=GOLD)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-07_ab_test.png", dpi=110, facecolor=BG)
print("Saved session-07_ab_test.png")
