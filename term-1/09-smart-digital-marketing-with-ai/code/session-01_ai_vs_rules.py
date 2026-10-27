# Rules versus learning: a hand-written rule compared with a decision tree that learns its own rules.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Synthetic email-subscriber data for an illustrative Karachi bakery.
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

rng = np.random.default_rng(3)
N = 1200
opens_30d = rng.poisson(3, N)
days_since_order = rng.integers(1, 120, N)
orders_total = rng.poisson(2, N)
# hidden truth: people re-order when they open emails AND ordered recently, or are loyal
p = 0.04 + 0.12 * (opens_30d >= 4) + 0.55 * (days_since_order < 25) * (orders_total >= 2) + 0.25 * (orders_total >= 5)
reorder = rng.binomial(1, np.clip(p, 0, 0.95))

# A marketer's rule of thumb
rule = (opens_30d >= 5).astype(int)
print(f"Hand-written rule 'opens >= 5' accuracy: {(rule == reorder).mean():.1%}")

X = np.column_stack([opens_30d, days_since_order, orders_total])
tr, te = slice(0, 900), slice(900, N)
tree = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X[tr], reorder[tr])
print(f"Learned decision tree accuracy on unseen data: {(tree.predict(X[te]) == reorder[te]).mean():.1%}")
print("\nRules the tree learned by itself:")
print(export_text(tree, feature_names=["opens_30d", "days_since_order", "orders_total"], decimals=0))
