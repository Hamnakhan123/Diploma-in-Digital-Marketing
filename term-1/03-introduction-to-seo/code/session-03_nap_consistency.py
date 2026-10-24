# Local SEO: check that Name, Address, Phone (NAP) match across listings.
import re

listings = {
    "Google Business Profile": ("Chai Corner", "Shop 4, Block 2, Clifton, Karachi", "+92 300 1234567"),
    "Website footer":          ("Chai Corner", "Shop 4, Block-2, Clifton, Karachi", "0300-1234567"),
    "Facebook page":           ("Chai Corner Cafe", "Shop 4, Block 2, Clifton, Karachi", "0300 1234567"),
    "Food directory":          ("Chai Corner", "Shop 14, Block 5, Clifton, Karachi", "021-35870000"),
}

def norm_phone(p):
    d = re.sub(r"\D", "", p)
    return "92" + d[1:] if d.startswith("0") else d

def norm_text(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())

ref = listings["Google Business Profile"]
for source, (name, addr, phone) in listings.items():
    issues = []
    if norm_text(name) != norm_text(ref[0]): issues.append("name")
    if norm_text(addr) != norm_text(ref[1]): issues.append("address")
    if norm_phone(phone) != norm_phone(ref[2]): issues.append("phone")
    print(f"{source:24} {'OK' if not issues else 'FIX: ' + ', '.join(issues)}")
