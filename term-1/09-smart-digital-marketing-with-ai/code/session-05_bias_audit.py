# Auditing an AI targeting model for unfair outcomes: compare who gets shown a loan-offer ad by group,
# using selection rate, the "four-fifths" disparate-impact ratio and error rates.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Synthetic applicants; groups are illustrative.
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(21)
N = 4000
group = rng.choice(["Men", "Women"], N, p=[0.6, 0.4])
creditworthy = rng.binomial(1, 0.5, N)          # truly eligible: same 50% in both groups
# A model trained on historical data where women were under-served scores them lower for the same eligibility
score = 0.35 + 0.35 * creditworthy + rng.normal(0, 0.12, N) - 0.10 * (group == "Women")
shown = score > 0.55

def audit(shown_mask, label):
    print(label)
    rates = {}
    for g in ["Men", "Women"]:
        m = group == g
        sel = shown_mask[m].mean()
        tpr = shown_mask[m & (creditworthy == 1)].mean()   # eligible people who were shown the offer
        rates[g] = sel
        print(f"  {g:<6} selection rate {sel:.1%}   eligible people reached (TPR) {tpr:.1%}")
    di = rates["Women"] / rates["Men"]
    print(f"  Disparate-impact ratio = {di:.2f}  ->  {'FAILS' if di < 0.8 else 'passes'} the four-fifths (0.80) rule\n")
    return rates

before = audit(shown, "BEFORE mitigation (one threshold for everyone):")
# Mitigation used here for teaching: remove the biased adjustment by re-scoring without group effect.
# In real projects you would fix the training data/features and re-validate, not just move thresholds.
score_fixed = score + 0.10 * (group == "Women")
after = audit(score_fixed > 0.55, "AFTER mitigation (biased feature removed and model re-scored):")

fig, ax = plt.subplots(figsize=(7, 3.8), facecolor=BG); ax.set_facecolor(BG)
x = np.arange(2)
ax.bar(x - 0.18, [before["Men"] * 100, before["Women"] * 100], 0.36, color=EMBER, label="Before")
ax.bar(x + 0.18, [after["Men"] * 100, after["Women"] * 100], 0.36, color=GOLD, label="After")
ax.set_xticks(x); ax.set_xticklabels(["Men", "Women"], color=TEXT)
ax.set_ylabel("% shown the offer", color=TEXT)
ax.set_title("Selection rate by group before and after a bias fix", color=GOLD)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-05_bias_audit.png", dpi=110, facecolor=BG)
print("Saved session-05_bias_audit.png")
