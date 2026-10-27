# Finding customer segments with AI: RFM features + k-means clustering, then naming each segment
# and choosing an action. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Synthetic orders for an illustrative online grocery store in Islamabad/Rawalpindi.
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(11)
groups = [  # (count, recency mean days, orders mean, avg basket PKR)
    (180, 8, 14, 6500),    # loyal weekly shoppers
    (260, 20, 5, 3800),    # regular
    (140, 15, 2, 11000),   # big-basket occasional
    (220, 95, 2, 2600),    # drifting away
    (200, 160, 1, 1900),   # one-time
]
rows = []
for g, (n, r, f, m) in enumerate(groups):
    for _ in range(n):
        orders = max(1, int(rng.poisson(f)))
        rows.append({"recency_days": int(np.clip(rng.normal(r, r * 0.35), 1, 365)),
                     "frequency": orders,
                     "monetary": round(orders * max(600, rng.normal(m, m * 0.25)))})
df = pd.DataFrame(rows)
print(f"Customers: {len(df)}  total revenue PKR {df.monetary.sum():,.0f}")

X = StandardScaler().fit_transform(np.column_stack([df.recency_days, np.log1p(df.frequency), np.log1p(df.monetary)]))
# Elbow check: inertia for k = 2..7
print("\nElbow check (lower inertia = tighter clusters):")
for k in range(2, 8):
    print(f"  k={k}  inertia={KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_:7.1f}")

km = KMeans(n_clusters=5, n_init=10, random_state=0).fit(X)
df["cluster"] = km.labels_
prof = df.groupby("cluster").agg(customers=("frequency", "size"), recency=("recency_days", "median"),
                                 orders=("frequency", "median"), revenue=("monetary", "sum"))
prof["avg_value"] = (prof.revenue / prof.customers).round()
prof["rev_share"] = (prof.revenue / prof.revenue.sum() * 100).round(1)

def name(r):
    if r.recency <= 14 and r.orders >= 8: return "Champions"
    if r.recency > 120: return "Lost one-timers"
    if r.recency > 60: return "At risk"
    if r.orders >= 4: return "Regulars"
    return "Big-basket occasional"
ACTION = {"Champions": "VIP early access, referral reward, no discounts needed",
          "Regulars": "Subscription / repeat-basket reminder, cross-sell",
          "Big-basket occasional": "Bulk-buy bundles before month start (salary week)",
          "At risk": "Win-back WhatsApp with free delivery, ask for feedback",
          "Lost one-timers": "Low-cost email only; suppress from paid retargeting"}
prof["segment"] = prof.apply(name, axis=1)
prof = prof.sort_values("revenue", ascending=False)
print("\nSegment profile:")
print(prof[["segment", "customers", "recency", "orders", "avg_value", "rev_share"]].to_string())
print("\nNext best action per segment:")
for s in prof.segment:
    print(f"  {s:<22} -> {ACTION[s]}")

fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor=BG); ax.set_facecolor(BG)
cols = [FIRE, GOLD, VIOLET, EMBER, "#38BDF8"]
for (c, row), col in zip(prof.iterrows(), cols):
    d = df[df.cluster == c]
    ax.scatter(d.recency_days, d.monetary / 1000, s=10 + 3 * d.frequency, color=col, alpha=0.6, label=row.segment)
ax.set_yscale("log")
ax.set_xlabel("Recency: days since last order (lower is better)", color=TEXT)
ax.set_ylabel("Total spend (PKR thousands, log scale)", color=TEXT)
ax.set_title("Five customer segments found by k-means (dot size = orders)", color=GOLD)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_segments.png", dpi=110, facecolor=BG)
print("Saved session-02_segments.png")
