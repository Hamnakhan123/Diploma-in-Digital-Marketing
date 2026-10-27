# A simple predictive model of customer behaviour: will a website visitor buy?
# The same steps a visual tool such as RapidMiner shows as boxes (retrieve -> split -> train -> apply -> evaluate),
# written in Python. Prepared by Hamna Zahid Khan, Junior Lecturer. Data is synthetic (an illustrative Lahore fashion store).
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(7)
N = 2000
# 1. Retrieve: one row per visit
pages = rng.poisson(4, N) + 1
minutes = np.round(rng.gamma(2, 2.2, N), 1)
returning = rng.binomial(1, 0.35, N)
from_ad = rng.binomial(1, 0.4, N)
cart_add = rng.binomial(1, np.clip(0.08 + 0.04 * pages, 0, 0.9))
logit = -5.2 + 0.18 * pages + 0.12 * minutes + 0.9 * returning + 0.3 * from_ad + 2.1 * cart_add
bought = rng.binomial(1, 1 / (1 + np.exp(-logit)))
X = np.column_stack([pages, minutes, returning, from_ad, cart_add])
names = ["pages_viewed", "minutes_on_site", "returning_visitor", "came_from_ad", "added_to_cart"]
print(f"Visits: {N}  purchases: {bought.sum()}  base conversion rate: {bought.mean():.1%}")

# 2. Split: learn on 75%, test on 25% the model has never seen
Xtr, Xte, ytr, yte = train_test_split(X, bought, test_size=0.25, random_state=1, stratify=bought)
# 3. Train
model = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
# 4. Apply
prob = model.predict_proba(Xte)[:, 1]
pred = (prob >= 0.5).astype(int)
# 5. Evaluate
tn, fp, fn, tp = confusion_matrix(yte, pred).ravel()
print(f"\nTest set: {len(yte)} visits")
print(f"Accuracy  {accuracy_score(yte, pred):.1%}   (always guessing 'no' would score {1 - yte.mean():.1%})")
print(f"Precision {precision_score(yte, pred):.1%}   Recall {recall_score(yte, pred):.1%}")
print(f"Confusion matrix: TP={tp} FP={fp} FN={fn} TN={tn}")
# A lower threshold catches more buyers at the cost of more false alarms
pred20 = (prob >= 0.2).astype(int)
print(f"At threshold 0.20 -> precision {precision_score(yte, pred20):.1%}, recall {recall_score(yte, pred20):.1%}")
print("\nWhat the model learned (odds multiplier per +1 unit):")
for n, c in sorted(zip(names, model.coef_[0]), key=lambda t: -t[1]):
    print(f"  {n:<18} x{np.exp(c):.2f}")

# Marketing use: rank visitors by probability and target the top 20% with a retargeting offer
order = np.argsort(-prob)
top = order[: len(order) // 5]
lift = yte[top].mean() / yte.mean()
print(f"\nTop 20% scored visitors convert at {yte[top].mean():.1%} vs {yte.mean():.1%} overall -> lift {lift:.1f}x")
new_visitor = np.array([[6, 9.5, 1, 1, 1]])
print(f"New visitor (6 pages, 9.5 min, returning, from ad, added to cart): P(buy) = {model.predict_proba(new_visitor)[0, 1]:.0%}")

# Chart: cumulative gains (how many buyers we reach by contacting the top-scored visitors first)
cum = np.cumsum(yte[order]) / yte.sum()
x = np.arange(1, len(order) + 1) / len(order)
fig, ax = plt.subplots(figsize=(8, 4.4), facecolor=BG); ax.set_facecolor(BG)
ax.plot(x * 100, cum * 100, color=FIRE, lw=2.5, label="AI model ranking")
ax.plot([0, 100], [0, 100], color=VIOLET, ls="--", label="Random targeting")
ax.axvline(20, color=GOLD, lw=1, ls=":")
ax.text(21, 10, f"Top 20% of visitors\n= {cum[len(order)//5 - 1]:.0%} of buyers", color=GOLD, fontsize=9)
ax.set_xlabel("% of visitors contacted (highest score first)", color=TEXT)
ax.set_ylabel("% of buyers reached", color=TEXT)
ax.set_title("Cumulative gains: the model finds buyers faster than random", color=GOLD)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-01_gains_chart.png", dpi=110, facecolor=BG)
print("Saved session-01_gains_chart.png")
