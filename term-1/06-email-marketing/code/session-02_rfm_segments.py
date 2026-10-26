# RFM segmentation of an e-commerce customer list for targeted email campaigns.
# R = days since last order, F = number of orders, M = total spend (PKR).
# Prepared by Hamna Zahid Khan, Junior Lecturer. 20 invented customers of a Lahore cosmetics store.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
customers = [  # id, recency days, frequency, monetary PKR
    ("C01", 5, 12, 64_000), ("C02", 12, 8, 41_000), ("C03", 200, 1, 2_500), ("C04", 35, 4, 15_500),
    ("C05", 3, 2, 6_800), ("C06", 95, 6, 33_000), ("C07", 400, 3, 9_000), ("C08", 20, 1, 3_200),
    ("C09", 60, 2, 7_900), ("C10", 8, 15, 92_000), ("C11", 150, 5, 21_000), ("C12", 45, 3, 11_000),
    ("C13", 310, 1, 1_900), ("C14", 15, 6, 28_500), ("C15", 120, 2, 5_600), ("C16", 2, 1, 4_100),
    ("C17", 75, 9, 47_000), ("C18", 250, 7, 38_000), ("C19", 30, 2, 8_400), ("C20", 180, 1, 2_200),
]

def score(value, cuts, reverse=False):
    """1-4 score by thresholds; reverse=True means smaller is better (recency)"""
    s = 1 + sum(value > c for c in cuts)
    return 5 - s if reverse else s

def segment(r, f, m):
    if r >= 3 and f >= 3: return "Champions"
    if r >= 3 and f <= 2: return "New / promising"
    if r == 2 and f >= 3: return "Loyal - needs attention"
    if r <= 2 and f >= 3: return "At risk (were loyal)"
    if r == 2: return "Need nurturing"
    return "Lapsed"

EMAIL = {"Champions": "VIP early access, referral programme, no discounts needed",
         "New / promising": "Welcome series, how-to-use content, second-order incentive",
         "Loyal - needs attention": "Personal recommendations based on past orders",
         "At risk (were loyal)": "'We miss you' email with a meaningful offer and survey",
         "Need nurturing": "Best-sellers, reviews, bundle offers",
         "Lapsed": "Win-back sequence; suppress if no opens after 3 emails"}

print(f"{'ID':<5}{'R days':>7}{'F':>4}{'M PKR':>9}  R F M  Segment")
segs = Counter()
for cid, r, f, m in customers:
    rs = score(r, [14, 60, 180], reverse=True)
    fs = score(f, [1, 3, 7])
    ms = score(m, [5_000, 15_000, 40_000])
    sg = segment(rs, fs, ms); segs[sg] += 1
    print(f"{cid:<5}{r:>7}{f:>4}{m:>9,}  {rs} {fs} {ms}  {sg}")
print("\nSegment sizes and the email each one should get:")
for sg, n in segs.most_common():
    print(f"  {sg:<25}{n:>3}  -> {EMAIL[sg]}")

fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=BG); ax.set_facecolor(BG)
for cid, r, f, m in customers:
    sg = segment(score(r, [14, 60, 180], True), score(f, [1, 3, 7]), 0)
    col = {"Champions": GOLD, "New / promising": "#38BDF8", "Loyal - needs attention": FIRE,
           "At risk (were loyal)": EMBER, "Need nurturing": VIOLET, "Lapsed": "#6b6280"}[sg]
    ax.scatter(r, f, s=m / 250, color=col, alpha=.85)
    ax.text(r + 6, f, cid, color=TEXT, fontsize=7)
ax.set_xlabel("Recency - days since last order (lower is better)", color=TEXT)
ax.set_ylabel("Frequency - orders", color=TEXT)
ax.set_title("RFM map: bubble size = total spend, colour = segment", color=GOLD)
ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · invented customers", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_rfm_segments.png", dpi=110, facecolor=BG)
print("Saved session-02_rfm_segments.png")
