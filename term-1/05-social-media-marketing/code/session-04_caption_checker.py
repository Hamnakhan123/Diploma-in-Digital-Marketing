# Check social captions for a hook, length, call to action, hashtags and emoji use.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
import re
CTA = ["order", "shop", "dm", "whatsapp", "comment", "tag", "save", "share", "link in bio", "book", "try", "visit", "click"]
LIMITS = {"Instagram": 2200, "TikTok": 4000, "Facebook": 63206, "X": 280, "LinkedIn": 3000}

def check(platform, caption):
    first = re.split(r"[\n.!?]", caption.strip())[0]
    tags = re.findall(r"#\w+", caption)
    emojis = re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", caption)
    has_cta = any(c in caption.lower() for c in CTA)
    issues, score = [], 100
    if len(first) > 60: issues.append(f"hook is {len(first)} chars - keep the first line under ~60 so it shows before 'more'"); score -= 20
    if not re.search(r"\?|\d|you|aap|stop|secret|new|free", first.lower()): issues.append("hook has no question, number, 'you' or curiosity word"); score -= 15
    if not has_cta: issues.append("no call to action"); score -= 25
    if len(caption) > LIMITS[platform]: issues.append(f"over the {platform} limit of {LIMITS[platform]}"); score -= 40
    if len(tags) > 5: issues.append(f"{len(tags)} hashtags - use 3-5 specific ones"); score -= 10
    if len(tags) == 0 and platform in ("Instagram", "TikTok"): issues.append("no hashtags for discovery"); score -= 5
    if len(emojis) > 6: issues.append("too many emojis hurt readability"); score -= 5
    return max(score, 0), first, tags, issues

captions = [
    ("Instagram", "We are very happy to announce that our company has launched a brand new winter collection for everyone in all cities #fashion #style #winter #love #instagood #pakistan #ootd #new"),
    ("Instagram", "3 shawls under PKR 2,500 that look like 10k? 🧣\nSwipe to see all three and comment 'SHAWL' for the link. Free delivery in Karachi this week.\n#karachifashion #winterwear #shawls"),
    ("X", "Load-shedding schedule got you down? Our UPS battery lasts 6 hours on a single charge. Order today with free installation in Lahore: link below."),
    ("TikTok", "POV: aap ne pehli dafa hamari chai try ki ☕ Comment karo apna favourite flavour! #chai #karachi #foodtok"),
]
for platform, cap in captions:
    s, first, tags, issues = check(platform, cap)
    print(f"[{platform}] score {s}/100 | hook: \"{first[:70]}\" | hashtags: {len(tags)}")
    for i in issues:
        print("   - " + i)
    if not issues:
        print("   - looks good")
