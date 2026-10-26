# Generate and pre-score ad copy variants from building blocks - the same idea AI copy tools use
# at scale (combine hooks, benefits and CTAs, then predict which will perform).
# This version is rule-based and transparent so students can see every step.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
import itertools, re

hooks = ["Load-shedding again?", "Stop paying for fuel you don't need.", "3 hours of backup for PKR 999/month?"]
benefits = ["Our solar kit runs fans and lights all evening", "Save up to 40% on your electricity bill", "Installed in one day by certified engineers"]
ctas = ["Book a free site survey", "WhatsApp us for a quote", "Learn more"]
POWER = {"free": 3, "save": 3, "you": 2, "your": 2, "?": 2, "pkr": 2, "%": 2, "one day": 1, "whatsapp": 2, "book": 2}
WEAK = {"learn more": -3}

def score(text):
    t = text.lower()
    s = sum(v for k, v in POWER.items() if k in t) + sum(v for k, v in WEAK.items() if k in t)
    if len(text) > 125: s -= 2                       # primary text gets cut off on mobile feeds
    if re.search(r"\d", text): s += 1               # specific numbers build trust
    return s

variants = [f"{h} {b}. {c}." for h, b, c in itertools.product(hooks, benefits, ctas)]
ranked = sorted(((score(v), v) for v in variants), reverse=True)
print(f"Generated {len(variants)} variants (3 hooks x 3 benefits x 3 CTAs). Top 5 to test:")
for s, v in ranked[:5]:
    print(f"  [{s:>2}] ({len(v):>3} chars) {v}")
print("Bottom 2 (do not run):")
for s, v in ranked[-2:]:
    print(f"  [{s:>2}] ({len(v):>3} chars) {v}")
print("\nNext step: put the top 3 in a structured A/B test; the scores are a guess, the test is the truth.")
