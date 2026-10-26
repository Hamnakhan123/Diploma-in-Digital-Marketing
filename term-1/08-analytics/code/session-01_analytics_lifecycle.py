# The data analytics lifecycle on a small marketing dataset: discover -> collect -> clean ->
# analyse -> visualise -> act. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Data: 600 synthetic online orders for a Lahore shoe store (fixed seed so results repeat).
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
# 1. DISCOVER - business question
print("Question: which marketing channel brings the most valuable customers, and where should next month's budget go?\n")

# 2. COLLECT - simulate an export from the shop + GA4 (with realistic mess)
rng = np.random.default_rng(7)
channels = np.array(["Instagram", "Google Search", "TikTok", "Email", "WhatsApp"])
probs = [0.30, 0.25, 0.20, 0.10, 0.15]
n = 600
df = pd.DataFrame({
    "order_id": np.arange(1001, 1001 + n),
    "channel": rng.choice(channels, n, p=probs),
    "order_value": rng.normal(4200, 1300, n).round(-1),
    "city": rng.choice(["Lahore", "Karachi", "Islamabad", "Faisalabad"], n, p=[.45, .25, .2, .1]),
})
df.loc[df.channel == "Email", "order_value"] += 600            # email buyers spend more
df.loc[df.channel == "TikTok", "order_value"] -= 500
df = pd.concat([df, df.sample(12, random_state=1)])              # duplicate rows from a double export
df.loc[df.sample(9, random_state=2).index, "channel"] = None     # missing source
df.loc[df.sample(3, random_state=3).index, "order_value"] = -1   # refund rows logged as -1
df.to_csv("session-01_orders_raw.csv", index=False)
print(f"Collected {len(df)} rows -> session-01_orders_raw.csv")

# 3. CLEAN
before = len(df)
df = df.drop_duplicates("order_id")
df["channel"] = df["channel"].fillna("Unknown")
df = df[df.order_value > 0]
print(f"Cleaning: removed {before - len(df)} rows (duplicates + invalid values); {(df.channel == 'Unknown').sum()} orders with unknown source kept as 'Unknown'")

# 4. ANALYSE
spend = {"Instagram": 260_000, "Google Search": 210_000, "TikTok": 150_000, "Email": 15_000, "WhatsApp": 40_000, "Unknown": 0}
summary = df.groupby("channel").agg(orders=("order_id", "count"), revenue=("order_value", "sum"), aov=("order_value", "mean"))
summary["spend"] = summary.index.map(spend)
summary["roas"] = (summary.revenue / summary.spend).replace(np.inf, np.nan)
summary["cpa"] = (summary.spend / summary.orders).replace(0, np.nan)
summary = summary.sort_values("revenue", ascending=False)
pd.set_option("display.width", 120)
print("\n" + summary.round({"aov": 0, "roas": 2, "cpa": 0}).to_string())

# 5. VISUALISE
s = summary.drop("Unknown", errors="ignore")
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4), facecolor=BG)
for ax in (a1, a2):
    ax.set_facecolor(BG); ax.tick_params(colors=TEXT, labelsize=8)
    for sp in ax.spines.values(): sp.set_color("#3b3355")
a1.bar(s.index, s.revenue / 1000, color=FIRE); a1.set_title("Revenue by channel (PKR thousands)", color=GOLD)
a2.bar(s.index, s.roas, color=[GOLD if r > 4 else VIOLET for r in s.roas]); a2.set_title("ROAS by channel", color=GOLD)
for ax in (a1, a2): ax.set_xticks(range(len(s))); ax.set_xticklabels(s.index, rotation=15)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-01_channel_analysis.png", dpi=110, facecolor=BG)

# 6. ACT
best = s.roas.idxmax(); worst = s.roas.idxmin()
print(f"\nInsight: {best} has the highest ROAS ({s.roas.max():.1f}); {worst} the lowest ({s.roas.min():.1f}).")
print(f"Action: grow the email list (cheap, high value), test new {worst} creatives and audiences before adding spend,")
print("        and fix source tracking for the 'Unknown' orders.")
print("Saved session-01_channel_analysis.png")
