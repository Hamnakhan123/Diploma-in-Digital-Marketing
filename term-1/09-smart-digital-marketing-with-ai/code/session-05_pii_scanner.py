# Data discovery and masking, the first job of privacy tools such as BigID and OneTrust:
# find personal data hiding in marketing files, classify it, and mask it before sharing.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Every record below is fake.
import re

PATTERNS = {
    "CNIC":   (r"\b\d{5}-\d{7}-\d\b", "high"),
    "Phone":  (r"(?:\+92|0)3\d{2}[- ]?\d{7}\b", "medium"),
    "Email":  (r"\b[\w.+-]+@[\w-]+\.[\w.]+\b", "medium"),
    "Card":   (r"\b(?:\d{4}[- ]?){3}\d{4}\b", "high"),
    "IBAN":   (r"\bPK\d{2}[A-Z]{4}\d{16}\b", "high"),
}
records = [
    "lead_id=101, name=Ayesha K, phone=03001234567, interest=bridal wear",
    "lead_id=102, email=hamza.test@example.com, note='wants EMI, CNIC 42101-1234567-1 sent on WhatsApp'",
    "survey: 'Great service!' rating=5",
    "refund request, card 4111 1111 1111 1111, IBAN PK36SCBL0000001123456702, phone +923211234567",
    "campaign=winter-sale, clicks=420, ctr=2.1%",
]

def mask(kind, value):
    if kind == "Email":
        user, dom = value.split("@"); return user[0] + "***@" + dom
    digits = re.sub(r"\D", "", value)
    return "*" * (len(value) - 4) + value[-4:] if kind != "CNIC" else value[:5] + "-*******-" + value[-1]

found = {k: 0 for k in PATTERNS}
risky_rows = 0
for i, rec in enumerate(records, 1):
    hits, clean = [], rec
    for kind, (pat, risk) in PATTERNS.items():
        for m in re.findall(pat, rec):
            hits.append(f"{kind}({risk})"); found[kind] += 1
            clean = clean.replace(m, mask(kind, m))
    risky_rows += bool(hits)
    print(f"Row {i}: {hits or 'no personal data'}")
    if hits: print(f"   masked -> {clean}")
print("\nInventory:", {k: v for k, v in found.items() if v})
print(f"{risky_rows}/{len(records)} rows contain personal data -> restrict access, set retention, record a lawful basis")
