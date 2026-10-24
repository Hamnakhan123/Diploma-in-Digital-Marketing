# Compare two sites' backlink profiles: quantity is not quality.
links = {
    "SiteA": [  # (referring domain, authority 0-100, relevant?, rel)
        ("dawn.com", 90, True, "follow"), ("techjuice.pk", 60, True, "follow"),
        ("university.edu.pk", 75, True, "follow"), ("forum-post", 20, True, "ugc"),
    ],
    "SiteB": [("spam-dir-%d.xyz" % i, 5, False, "follow") for i in range(40)],
}

def quality(profile):
    score = 0
    for domain, auth, relevant, rel in profile:
        weight = 1.0 if rel == "follow" else 0.3   # nofollow/ugc/sponsored pass little value
        score += auth * (1.0 if relevant else 0.1) * weight
    return round(score)

for site, profile in links.items():
    domains = len({d for d, *_ in profile})
    print(f"{site}: {len(profile):3} links from {domains:3} domains -> quality score {quality(profile)}")
