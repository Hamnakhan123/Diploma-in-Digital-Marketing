# A tiny social listening tool: classify brand mentions (English + Roman Urdu) by sentiment
# with a keyword lexicon, find themes, compute net sentiment and share of voice, and chart it.
# Prepared by Hamna Zahid Khan, Junior Lecturer. The mentions below are invented for practice.
import re
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
POS = {"love", "great", "best", "zabardast", "behtareen", "acha", "achi", "fast", "fresh", "mazay", "recommend", "thanks", "shukriya", "kamaal"}
NEG = {"late", "cold", "worst", "bekar", "ganda", "refund", "rude", "missing", "kharab", "slow", "never", "disappointed", "mehnga", "expensive"}
NEGATORS = {"not", "nahi", "nahin", "na"}
THEMES = {"delivery": {"delivery", "late", "rider", "time", "fast", "slow"},
          "taste": {"taste", "mazay", "fresh", "cold", "biryani", "zinger"},
          "price": {"price", "mehnga", "expensive", "deal", "discount", "sasta"},
          "service": {"rude", "staff", "support", "refund", "reply", "helpline"}}

mentions = [
    ("BiryaniBox", "BiryaniBox ki biryani zabardast thi, delivery bhi fast!"),
    ("BiryaniBox", "Order 45 min late aur biryani cold. Bekar experience"),
    ("BiryaniBox", "Best deal in Karachi for family platter, recommend"),
    ("BiryaniBox", "Support ne reply hi nahi kiya, refund chahiye"),
    ("BiryaniBox", "Taste acha hai lekin price thora mehnga hai"),
    ("BiryaniBox", "Rider was rude, never ordering again"),
    ("BiryaniBox", "Shukriya BiryaniBox, fresh aur garam mila"),
    ("BiryaniBox", "Zinger not fresh today, disappointed"),
    ("BiryaniBox", "Eid deal kamaal hai, mazay aa gaye"),
    ("BiryaniBox", "Delivery time theek tha"),
    ("Rival", "Rival ka zinger behtareen, fast delivery"),
    ("Rival", "Rival app slow and expensive"),
    ("Rival", "Rival deal acha hai"),
    ("Rival", "Rival order missing items, worst"),
    ("Rival", "Rival biryani mazay ki"),
    ("Rival", "Rival staff helpful, thanks"),
]

def sentiment(text):
    words = re.findall(r"[a-z]+", text.lower())
    score = 0
    for i, w in enumerate(words):
        s = 1 if w in POS else -1 if w in NEG else 0
        if s and i > 0 and words[i - 1] in NEGATORS:
            s = -s                                     # "not fresh" -> negative
        if s and i + 1 < len(words) and words[i + 1] in NEGATORS and w in POS:
            s = -s
        score += s
    return "positive" if score > 0 else "negative" if score < 0 else "neutral"

counts = {"BiryaniBox": Counter(), "Rival": Counter()}
themes = Counter()
print(f"{'Brand':<11}{'Sentiment':<10}Mention")
for brand, text in mentions:
    s = sentiment(text)
    counts[brand][s] += 1
    words = set(re.findall(r"[a-z]+", text.lower()))
    if brand == "BiryaniBox":
        for t, kw in THEMES.items():
            if words & kw:
                themes[(t, s)] += 1
    print(f"{brand:<11}{s:<10}{text}")

total = len(mentions)
for b, c in counts.items():
    n = sum(c.values())
    nss = (c["positive"] - c["negative"]) / n * 100
    print(f"\n{b}: {n} mentions, SOV {n / total:.0%} | +{c['positive']} / ={c['neutral']} / -{c['negative']} | net sentiment {nss:+.0f}")
print("\nBiryaniBox themes (theme, sentiment): count")
for (t, s), v in sorted(themes.items()):
    print(f"  {t:<9}{s:<9}{v}")

fig, ax = plt.subplots(figsize=(8, 3.6), facecolor=BG); ax.set_facecolor(BG)
labels = list(counts)
left = [0, 0]
for s, col in (("positive", GOLD), ("neutral", VIOLET), ("negative", EMBER)):
    vals = [counts[b][s] for b in labels]
    ax.barh(labels, vals, left=left, color=col, label=s)
    left = [l + v for l, v in zip(left, vals)]
ax.set_title("Mentions by sentiment (invented sample)", color=GOLD); ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-04_social_listening.png", dpi=110, facecolor=BG)
print("\nSaved session-04_social_listening.png")
