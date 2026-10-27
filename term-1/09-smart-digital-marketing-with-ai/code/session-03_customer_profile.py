# Building unified digital customer profiles, the way a customer data platform (CDP) such as Segment does:
# collect events from many sources, stitch identities (device -> phone -> email), then compute traits
# and audiences. Prepared by Hamna Zahid Khan, Junior Lecturer. All people and numbers are fictional.
from collections import defaultdict

events = [  # source, identifiers seen, event, properties
    ("website",  {"device": "d-101"},                              "page_view", {"page": "/kurtas"}),
    ("website",  {"device": "d-101", "email": "sana@example.pk"},  "signup",    {}),
    ("app",      {"device": "a-555", "phone": "+923001112233"},    "add_to_cart", {"item": "lawn-3pc", "price": 6500}),
    ("whatsapp", {"phone": "+923001112233"},                       "message",   {"text": "Is COD available in Multan?"}),
    ("store_pos",{"phone": "+923001112233", "email": "sana@example.pk"}, "purchase", {"amount": 6500, "city": "Multan"}),
    ("email",    {"email": "sana@example.pk"},                     "email_open", {"campaign": "eid-preview"}),
    ("website",  {"device": "d-202"},                              "page_view", {"page": "/men/shalwar-kameez"}),
    ("website",  {"device": "d-202", "email": "bilal@example.pk"}, "purchase",  {"amount": 4200, "city": "Lahore"}),
    ("app",      {"device": "a-777"},                              "page_view", {"page": "/kids"}),
]

# Union-find over identifiers: any event that shows two identifiers links them to one person
parent = {}
def find(x):
    parent.setdefault(x, x)
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    parent[find(a)] = find(b)

for _, ids, _, _ in events:
    keys = [f"{k}:{v}" for k, v in ids.items()]
    for k in keys: find(k)
    for k in keys[1:]: union(keys[0], k)

profiles = defaultdict(lambda: {"ids": set(), "sources": set(), "events": [], "revenue": 0, "city": None})
for src, ids, ev, props in events:
    root = find(f"{next(iter(ids))}:{next(iter(ids.values()))}")
    p = profiles[root]
    p["ids"].update(f"{k}:{v}" for k, v in ids.items()); p["sources"].add(src); p["events"].append(ev)
    p["revenue"] += props.get("amount", 0)
    p["city"] = props.get("city", p["city"])

print(f"{len(events)} raw events from 5 sources -> {len(profiles)} unified profiles\n")
for i, p in enumerate(profiles.values(), 1):
    traits = {
        "known": any(x.startswith(("email", "phone")) for x in p["ids"]),
        "buyer": p["revenue"] > 0,
        "omnichannel": len(p["sources"]) >= 3,
    }
    audiences = []
    if traits["buyer"] and traits["omnichannel"]: audiences.append("VIP omnichannel")
    if "add_to_cart" in p["events"] and not traits["buyer"]: audiences.append("Cart abandoners")
    if not traits["known"]: audiences.append("Anonymous - retarget only")
    if traits["buyer"] and not traits["omnichannel"]: audiences.append("Single-channel buyers")
    print(f"Profile {i}: ids={sorted(p['ids'])}")
    print(f"  sources={sorted(p['sources'])} events={len(p['events'])} revenue=PKR {p['revenue']:,} city={p['city']}")
    print(f"  audiences={audiences}\n")
