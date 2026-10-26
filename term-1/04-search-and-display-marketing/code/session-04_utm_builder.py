# Build consistent UTM-tagged links so GA4 reports each campaign in the right channel.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
from urllib.parse import urlencode, urlparse, parse_qs

ALLOWED_MEDIUMS = {"cpc", "display", "email", "social", "paid_social", "sms", "affiliate", "qr", "referral"}

def utm(url, source, medium, campaign, content=None, term=None):
    clean = lambda s: s.strip().lower().replace(" ", "-")
    medium = medium.strip().lower().replace(" ", "_")
    if medium not in ALLOWED_MEDIUMS:
        raise ValueError(f"medium '{medium}' is not in the team's naming list {sorted(ALLOWED_MEDIUMS)}")
    params = {"utm_source": clean(source), "utm_medium": medium, "utm_campaign": clean(campaign)}
    if content: params["utm_content"] = clean(content)
    if term: params["utm_term"] = clean(term)
    sep = "&" if urlparse(url).query else "?"
    return url + sep + urlencode(params)

base = "https://www.zarishoes.pk/eid-collection"
plan = [
    ("facebook", "paid_social", "Eid Sale 2026", "carousel-red", None),
    ("instagram", "paid_social", "Eid Sale 2026", "reel-15s", None),
    ("newsletter", "email", "Eid Sale 2026", "hero-button", None),
    ("whatsapp", "sms", "Eid Sale 2026", "broadcast-1", None),
    ("mall-poster", "qr", "Eid Sale 2026", "dolmen-clifton", None),
]
for row in plan:
    print(utm(base, *row))

print("\nParsing one link back (what GA4 reads):")
link = utm(base + "?size=38", "Facebook", "Paid Social", "Eid Sale 2026", "Carousel Red")
print(link)
for k, v in parse_qs(urlparse(link).query).items():
    print(f"  {k:<13}= {v[0]}")

print("\nA bad medium is rejected before it pollutes reports:")
try:
    utm(base, "facebook", "FB-Ads", "eid")
except ValueError as e:
    print("  ERROR:", e)
