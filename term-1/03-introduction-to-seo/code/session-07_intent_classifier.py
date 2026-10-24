# A tiny machine-learning model: Naive Bayes that learns search intent from labelled examples.
import math, re
from collections import Counter, defaultdict

train = [
    ("how to tie a hijab", "informational"), ("what is net metering", "informational"),
    ("why is my phone slow", "informational"), ("how does seo work", "informational"),
    ("buy iphone 15 online", "transactional"), ("order pizza near me", "transactional"),
    ("lawn suit price sale", "transactional"), ("cheap flights karachi to dubai book", "transactional"),
    ("best laptop under 150000", "commercial"), ("daraz vs amazon review", "commercial"),
    ("top 10 seo tools compared", "commercial"), ("best solar company reviews", "commercial"),
    ("facebook login", "navigational"), ("daraz", "navigational"),
    ("youtube", "navigational"), ("hbl internet banking login", "navigational"),
]

def words(t): return re.findall(r"[a-z0-9]+", t.lower())

word_counts, class_counts, vocab = defaultdict(Counter), Counter(), set()
for text, label in train:                      # "training" = counting
    class_counts[label] += 1
    for w in words(text):
        word_counts[label][w] += 1; vocab.add(w)

def predict(text):
    best, best_lp = None, -1e9
    for label in class_counts:
        lp = math.log(class_counts[label] / len(train))
        total = sum(word_counts[label].values())
        for w in words(text):                  # Laplace smoothing for unseen words
            lp += math.log((word_counts[label][w] + 1) / (total + len(vocab)))
        if lp > best_lp: best, best_lp = label, lp
    return best

for q in ["how to clean solar panels", "buy solar panels online", "best solar panels review", "k-electric login"]:
    print(f"{q:30} -> {predict(q)}")
