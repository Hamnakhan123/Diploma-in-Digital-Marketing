# AI for mobile marketing: predict which app users are likely to churn (stop ordering) with a
# logistic regression, then target only high-risk users with a re-engagement push.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Data are synthetic (generated with a fixed seed).
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(42)
n = 3_000
days_since_order = rng.integers(0, 90, n)
orders_30d = rng.poisson(2.2, n)
sessions_7d = rng.poisson(4, n)
push_enabled = rng.random(n) < 0.6
# true (hidden) churn behaviour used to simulate labels
logit = -1.2 + 0.045 * days_since_order - 0.55 * orders_30d - 0.25 * sessions_7d - 0.5 * push_enabled
churn = rng.random(n) < 1 / (1 + np.exp(-logit))
X = np.column_stack([days_since_order, orders_30d, sessions_7d, push_enabled.astype(int)])
Xtr, Xte, ytr, yte = train_test_split(X, churn, test_size=0.3, random_state=0, stratify=churn)
model = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
proba = model.predict_proba(Xte)[:, 1]
print(f"Users: {n:,} | churn rate in data: {churn.mean():.1%}")
print(f"Test AUC: {roc_auc_score(yte, proba):.3f}  (0.5 = random guessing, 1.0 = perfect)")
for name, coef in zip(["days_since_order", "orders_30d", "sessions_7d", "push_enabled"], model.coef_[0]):
    print(f"  {name:<17} coefficient {coef:+.3f} -> {'raises' if coef > 0 else 'lowers'} churn risk")
print(classification_report(yte, proba > 0.5, target_names=["stays", "churns"], digits=2))

# Business decision: push a PKR 150 voucher only to the riskiest 20%
cut = np.quantile(proba, 0.80)
target = proba >= cut
caught = (target & yte).sum()
print(f"Targeting top 20% risk ({target.sum()} users) reaches {caught} of {yte.sum()} churners "
      f"({caught / yte.sum():.0%}) - vs 20% if we picked at random.")

fig, ax = plt.subplots(figsize=(8, 4), facecolor=BG); ax.set_facecolor(BG)
ax.hist(proba[~yte], bins=30, color=VIOLET, alpha=.75, label="actually stayed")
ax.hist(proba[yte], bins=30, color=FIRE, alpha=.75, label="actually churned")
ax.axvline(cut, color=GOLD, ls="--"); ax.text(cut + .01, ax.get_ylim()[1] * .9, "top-20% risk cut-off", color=GOLD, fontsize=8)
ax.set_xlabel("Predicted churn probability", color=TEXT); ax.set_ylabel("Users", color=TEXT)
ax.set_title("Churn model scores on test users", color=GOLD); ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-04_churn_model.png", dpi=110, facecolor=BG)
print("Saved session-04_churn_model.png")
