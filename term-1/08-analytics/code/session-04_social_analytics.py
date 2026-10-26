# Social media metrics and content engagement analysis on 120 posts: engagement rates,
# format comparison, best posting day/hour heat-map, and the save/share signal.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Synthetic posts (fixed seed) for a Karachi cafe.
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(5)
n = 120
fmt = rng.choice(["Reel", "Carousel", "Static", "Story"], n, p=[.4, .25, .2, .15])
day = rng.choice(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], n)
hour = rng.choice([9, 13, 17, 20, 22], n)
base = {"Reel": 9000, "Carousel": 5000, "Static": 3000, "Story": 2500}
reach = np.array([base[f] for f in fmt]) * rng.lognormal(0, .35, n)
reach *= np.where(np.isin(hour, [20, 22]), 1.35, 1.0) * np.where(np.isin(day, ["Fri", "Sat", "Sun"]), 1.2, 1.0)
er = {"Reel": .055, "Carousel": .07, "Static": .035, "Story": .015}
eng_rate = np.array([er[f] for f in fmt]) * rng.lognormal(0, .25, n)
eng = reach * eng_rate
df = pd.DataFrame({"format": fmt, "day": day, "hour": hour, "reach": reach.round(), "likes": (eng * .7).round(),
                   "comments": (eng * .06).round(), "shares": (eng * .1).round(), "saves": (eng * .14).round(),
                   "followers": 15_000})
df["engagements"] = df[["likes", "comments", "shares", "saves"]].sum(axis=1)
df["er_reach"] = df.engagements / df.reach * 100
df["er_followers"] = df.engagements / df.followers * 100
df["save_share_rate"] = (df.saves + df.shares) / df.reach * 100
df.to_csv("session-04_posts.csv", index=False)

print(f"Posts analysed: {len(df)} | total reach {df.reach.sum():,.0f} | total engagements {df.engagements.sum():,.0f}")
print(f"Average ER by reach {df.er_reach.mean():.2f}% | by followers {df.er_followers.mean():.2f}%\n")
by = df.groupby("format").agg(posts=("reach", "size"), avg_reach=("reach", "mean"), er_reach=("er_reach", "mean"),
                              save_share=("save_share_rate", "mean"), comments=("comments", "mean"))
print(by.round(2).sort_values("er_reach", ascending=False).to_string())
pivot = df.pivot_table(index="day", columns="hour", values="engagements", aggfunc="mean").reindex(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
best = pivot.stack().idxmax()
print(f"\nBest slot by average engagements: {best[0]} at {best[1]}:00 PKT")
top = df.sort_values("engagements", ascending=False).head(5)[["format", "day", "hour", "reach", "engagements", "er_reach"]]
print("\nTop 5 posts:\n" + top.round(1).to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 4.2), facecolor=BG)
im = ax.imshow(pivot.values, cmap="inferno", aspect="auto")
ax.set_xticks(range(len(pivot.columns))); ax.set_xticklabels([f"{h}:00" for h in pivot.columns], color=TEXT)
ax.set_yticks(range(7)); ax.set_yticklabels(pivot.index, color=TEXT)
for y in range(7):
    for x in range(len(pivot.columns)):
        v = pivot.values[y, x]
        if not np.isnan(v): ax.text(x, y, f"{v:.0f}", ha="center", va="center", fontsize=7, color=BG if v > np.nanmean(pivot.values) else TEXT)
ax.set_title("Average engagements per post by day and hour (PKT)", color=GOLD)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic posts", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-04_engagement_heatmap.png", dpi=110, facecolor=BG)
print("Saved session-04_posts.csv and session-04_engagement_heatmap.png")
