# Social listening with sentiment analysis, the core idea behind tools like Hootsuite Insights:
# score each mention, group by topic, and flag issues. Works on English and Roman Urdu with a small lexicon.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Mentions are invented for an illustrative food-delivery brand.
import re
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
POS = {"love", "great", "fast", "tasty", "best", "amazing", "zabardast", "mazay", "maza", "acha", "achi", "fresh", "shukriya", "kamaal"}
NEG = {"late", "cold", "worst", "rude", "bad", "bekar", "ganda", "slow", "missing", "refund", "never", "ghatiya", "wrong"}
NEGATORS = {"not", "nahi", "na", "never"}
TOPICS = {"delivery": {"late", "delivery", "rider", "fast", "slow", "time"},
          "food": {"food", "cold", "tasty", "fresh", "biryani", "pizza", "maza", "mazay", "burger"},
          "service": {"rude", "support", "refund", "missing", "wrong", "helpline", "app"}}

mentions = [
    "Biryani was zabardast and delivery was fast, love it",
    "Rider came 50 minutes late and the pizza was cold",
    "Worst support ever, still waiting for my refund",
    "Burger maza aa gaya, fresh and tasty",
    "App is not bad but delivery time is slow in Gulshan",
    "Order missing items again, helpline is rude",
    "Shukriya for the quick delivery, kamaal service",
    "Food acha tha lekin rider late tha",
    "Pizza not fresh, bekar experience",
    "Best deal on Friday, amazing biryani",
    "Wrong order delivered, refund nahi mila",
    "Fast delivery in DHA, tasty food",
]

def score(text):
    words = re.findall(r"[a-z]+", text.lower())
    s = 0
    for i, w in enumerate(words):
        v = (w in POS) - (w in NEG)
        if v and i and words[i - 1] in NEGATORS:
            v = -v                      # "not bad" -> positive, "not fresh" -> negative
        s += v
    return s, words

by_topic = defaultdict(lambda: [0, 0, 0])   # pos, neu, neg
total = [0, 0, 0]
for m in mentions:
    s, words = score(m)
    label = "POS" if s > 0 else "NEG" if s < 0 else "NEU"
    idx = {"POS": 0, "NEU": 1, "NEG": 2}[label]
    total[idx] += 1
    topics = [t for t, kw in TOPICS.items() if kw & set(words)] or ["other"]
    for t in topics: by_topic[t][idx] += 1
    print(f"[{label} {s:+d}] {m}  -> topics {topics}")

net = (total[0] - total[2]) / len(mentions) * 100
print(f"\nTotals: positive {total[0]}, neutral {total[1]}, negative {total[2]}  | net sentiment {net:+.0f}")
print("By topic (pos/neu/neg):")
for t, (p, n, g) in sorted(by_topic.items()):
    flag = "  <-- ALERT: more negative than positive" if g > p else ""
    print(f"  {t:<9} {p}/{n}/{g}{flag}")

fig, ax = plt.subplots(figsize=(8, 3.8), facecolor=BG); ax.set_facecolor(BG)
names = sorted(by_topic)
p = [by_topic[t][0] for t in names]; n = [by_topic[t][1] for t in names]; g = [by_topic[t][2] for t in names]
ax.barh(names, p, color=GOLD, label="Positive")
ax.barh(names, n, left=p, color=VIOLET, label="Neutral")
ax.barh(names, g, left=[a + b for a, b in zip(p, n)], color=EMBER, label="Negative")
ax.set_xlabel("Mentions", color=TEXT)
ax.set_title("Sentiment by topic: service is the problem, food is the strength", color=GOLD)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8, loc="lower right")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · invented mentions", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-04_sentiment_topics.png", dpi=110, facecolor=BG)
print("Saved session-04_sentiment_topics.png")
