# Check a responsive search ad (RSA) against Google Ads character limits and basic quality rules.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
LIMITS = {"headline": 30, "description": 90, "path": 15}

ad = {
    "keyword": "ac repair",
    "headlines": [
        "AC Repair in Karachi",
        "Same-Day Technician Visit",
        "Gas Refill From PKR 4,500",
        "Inverter AC Specialists",
        "Book on WhatsApp in 1 Minute",
        "4.8 Stars From 900+ Customers",
        "Free Checkup With Every Service Visit",   # too long on purpose
        "AC Repair in Karachi",                    # duplicate on purpose
    ],
    "descriptions": [
        "Certified technicians for split and inverter ACs. Clear prices, 30-day service warranty.",
        "Open 7 days, 9am-9pm. Serving DHA, Clifton, Gulshan and North Nazimabad. Book now.",
    ],
    "paths": ["ac-repair", "karachi"],
}

problems = 0
for kind, items in (("headline", ad["headlines"]), ("description", ad["descriptions"]), ("path", ad["paths"])):
    for text in items:
        n = len(text)
        ok = n <= LIMITS[kind]
        problems += not ok
        print(f"{'OK ' if ok else 'TOO LONG'} {kind:<11} {n:>3}/{LIMITS[kind]:<3} {text}")

dupes = {h for h in ad["headlines"] if ad["headlines"].count(h) > 1}
unique = len(set(ad["headlines"]))
kw = sum(ad["keyword"] in h.lower() for h in set(ad["headlines"]))
print(f"\nUnique headlines: {unique} (Google allows 3-15; aim for 8-15 distinct ones)")
print(f"Descriptions: {len(ad['descriptions'])} (Google allows 2-4)")
print(f"Duplicates: {sorted(dupes) or 'none'}")
print(f"Headlines containing the keyword '{ad['keyword']}': {kw}")
print(f"Has a number/price: {any(ch.isdigit() for h in ad['headlines'] for ch in h)}")
print(f"\nProblems to fix: {problems + len(dupes)}")
