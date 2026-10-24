# Sort search queries into voice-style questions vs typed keywords, then build FAQ JSON-LD.
import json, re

queries = [
    "dentist clifton",
    "where is the nearest dentist open now",
    "how much does teeth whitening cost in karachi",
    "teeth whitening price",
    "can i eat after a filling",
    "best dentist near me",
]
QUESTION_WORDS = ("who", "what", "where", "when", "why", "how", "can", "is", "does", "should")

def is_voice_style(q):
    w = q.split()
    return w[0] in QUESTION_WORDS or len(w) >= 6 or "near me" in q or "open now" in q

for q in queries:
    print(f"{'VOICE' if is_voice_style(q) else 'TYPED'}  {q}")

faqs = [
    ("How much does teeth whitening cost in Karachi?",
     "At our Clifton clinic, in-chair whitening costs PKR 25,000 and takes about one hour."),
    ("Can I eat after a filling?",
     "Wait until the numbness wears off, usually two to three hours, before eating."),
]
schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
    ],
}
print('\n<script type="application/ld+json">')
print(json.dumps(schema, indent=2))
print("</script>")
for q, a in faqs:
    print(f"Answer length: {len(a.split())} words -> {'good for voice' if len(a.split()) <= 30 else 'too long'}")
