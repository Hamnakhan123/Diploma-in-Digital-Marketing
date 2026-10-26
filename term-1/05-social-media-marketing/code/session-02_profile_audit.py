# Score a business profile against a 10-point social media presence audit.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Example: a Multan bakery's Instagram profile.
CHECKS = [  # (item, weight)
    ("Handle matches brand on all platforms", 10),
    ("Profile photo is the logo, readable at small size", 8),
    ("Bio says what, where and for whom in <150 characters", 12),
    ("Clear call to action in bio (order/WhatsApp/visit)", 10),
    ("Link in bio with UTM-tagged links", 10),
    ("Contact button: phone, WhatsApp or email", 8),
    ("Business category and location set", 6),
    ("Story highlights: menu, prices, reviews, how to order", 10),
    ("Posted at least 3 times in the last 14 days", 14),
    ("Replies to comments and DMs within 24 hours", 12),
]
profile = {  # True = passes
    "Handle matches brand on all platforms": False,
    "Profile photo is the logo, readable at small size": True,
    "Bio says what, where and for whom in <150 characters": False,
    "Clear call to action in bio (order/WhatsApp/visit)": True,
    "Link in bio with UTM-tagged links": False,
    "Contact button: phone, WhatsApp or email": True,
    "Business category and location set": True,
    "Story highlights: menu, prices, reviews, how to order": False,
    "Posted at least 3 times in the last 14 days": True,
    "Replies to comments and DMs within 24 hours": False,
}
score = sum(w for item, w in CHECKS if profile[item])
total = sum(w for _, w in CHECKS)
print(f"{'Check':<56}{'Weight':>7}  Result")
for item, w in CHECKS:
    print(f"{item:<56}{w:>7}  {'PASS' if profile[item] else 'FIX'}")
print(f"\nScore: {score}/{total} = {score / total:.0%}")
grade = "Strong" if score >= 80 else "Needs work" if score >= 55 else "Weak"
print("Grade:", grade)
fixes = sorted(((w, i) for i, w in CHECKS if not profile[i]), reverse=True)
print("Fix first (highest weight):")
for w, i in fixes[:3]:
    print(f"  +{w:>2} pts  {i}")
