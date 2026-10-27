# A content-optimisation score in the style of tools like Surfer SEO: compare your draft with the
# words that top-ranking pages use, then list gaps. Prepared by Hamna Zahid Khan, Junior Lecturer.
# The "competitor" texts below are short invented samples, not real pages.
import re
from collections import Counter

competitors = [
    "Best time to visit Hunza is April for cherry blossom and October for autumn colours. Karakoram Highway road trip, "
    "hotels in Karimabad, Attabad Lake boating, Eagle's Nest sunrise, travel cost and itinerary for 5 days.",
    "Hunza travel guide: how to reach by road or flight to Gilgit, Karakoram Highway, Attabad Lake, Passu Cones, "
    "Baltit Fort, hotels in Karimabad, best time to visit, 5 day itinerary and budget in PKR.",
    "Plan your Hunza trip: itinerary, Attabad Lake, Khunjerab Pass, Passu, best time to visit, weather, hotels, "
    "road conditions on Karakoram Highway, packing list and cost per person.",
]
draft = ("Hunza is beautiful. Our tour visits Attabad Lake and Baltit Fort. Book our Hunza tour today, "
         "we have the best Hunza tour packages with comfortable hotels.")

STOP = set("the and for to in of by or on a is are we our has have with how your per day".split())
def terms(text):
    words = [w for w in re.findall(r"[a-z']+", text.lower()) if w not in STOP and len(w) > 2]
    grams = words + [" ".join(p) for p in zip(words, words[1:])]
    return Counter(grams)

comp_counts = [terms(t) for t in competitors]
# a term matters if at least 2 of 3 top pages use it
important = sorted({t for c in comp_counts for t in c if sum(t in d for d in comp_counts) >= 2})
d = terms(draft)
covered = [t for t in important if t in d]
missing = [t for t in important if t not in d]
words_draft = len(draft.split()); words_avg = sum(len(t.split()) for t in competitors) / len(competitors)
stuffing = d.most_common(1)[0]

score = round(70 * len(covered) / len(important) + 30 * min(1, words_draft / words_avg))
print(f"Important terms used by 2+ top pages: {len(important)}")
print(f"Covered in draft: {len(covered)} -> {covered}")
print(f"Missing: {missing}")
print(f"Draft length {words_draft} words vs competitor average {words_avg:.0f}")
print(f"Most repeated term in draft: '{stuffing[0]}' x{stuffing[1]} (watch for keyword stuffing)")
print(f"Content score: {score}/100")
