# Subject-line lab: pre-check subject lines for length, spam triggers and personalisation,
# then evaluate an A/B test on click rate. Prepared by Hamna Zahid Khan, Junior Lecturer.
import math, re
from statistics import NormalDist

SPAM = ["free!!!", "100% free", "act now", "winner", "risk-free", "$$$", "click here", "guaranteed", "cash bonus"]

def check(subject, preheader=""):
    notes = []
    if len(subject) > 50: notes.append(f"{len(subject)} chars - may be cut on mobile (aim 30-50)")
    if sum(1 for c in subject if c.isupper()) > len(subject) * 0.5: notes.append("mostly CAPITALS - looks like spam")
    if subject.count("!") > 1: notes.append("multiple exclamation marks")
    for w in SPAM:
        if w in subject.lower(): notes.append(f"spam-trigger phrase '{w}'")
    if "{{first_name}}" in subject: notes.append("personalised (good - check the fallback value)")
    if not preheader: notes.append("no preheader text - inbox will show random body text")
    return notes or ["looks good"]

tests = [
    ("FREE!!! CLICK HERE TO WIN A CASH BONUS", ""),
    ("{{first_name}}, your 10% welcome code is inside", "Plus 5 Urdu novels readers love"),
    ("New arrivals: 12 books we can't stop talking about this week at Kitab Ghar Karachi", "Staff picks inside"),
    ("Last day: 11.11 prices end at midnight", "Up to 40% off bestsellers - COD available"),
]
for s, p in tests:
    print(f"'{s}'")
    for n in check(s, p): print("   - " + n)

# A/B test on unique clicks (clicks are not distorted by privacy-protected opens)
A = ("Our 11.11 sale is live", 7_400, 296)                       # name, delivered, clickers
B = ("Ayesha, your 11.11 wishlist is now 40% off", 7_400, 370)
pa, pb = A[2] / A[1], B[2] / B[1]
p = (A[2] + B[2]) / (A[1] + B[1])
se = math.sqrt(p * (1 - p) * (1 / A[1] + 1 / B[1]))
z = (pb - pa) / se
pv = 2 * (1 - NormalDist().cdf(abs(z)))
print(f"\nA/B on click rate: A {pa:.2%} vs B {pb:.2%} | lift {(pb - pa) / pa:+.0%} | z = {z:.2f}, p = {pv:.4f}")
print("Winner: B (personalised + specific)" if pv < 0.05 else "No significant winner - keep A or test again")
