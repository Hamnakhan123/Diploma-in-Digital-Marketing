# Check a YouTube video's metadata (title, description, tags, chapters) before publishing.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
import re

video = {
    "keyword": "chicken karahi recipe",
    "title": "Chicken Karahi Recipe in 20 Minutes | Restaurant Style at Home",
    "description": """Chicken karahi recipe the quick way - restaurant style flavour at home in 20 minutes.
Ingredients list and steps below. Subscribe for a new Pakistani recipe every Friday.

00:00 Intro
00:35 Ingredients
02:10 Cooking the chicken
07:45 Adding tomatoes and spices
11:20 Serving tips

Full recipe: https://example.pk/karahi?utm_source=youtube&utm_medium=video&utm_campaign=karahi
#chickenkarahi #pakistanirecipes #karahi""",
    "tags": ["chicken karahi", "karahi recipe", "pakistani food", "desi cooking", "20 minute recipe"],
    "thumbnail_text": "20 MIN KARAHI",
}

def check(v):
    kw = v["keyword"].lower()
    out = []
    t = v["title"]
    out.append(("Title length 40-70 chars", 40 <= len(t) <= 70, f"{len(t)} chars"))
    out.append(("Keyword in title", kw in t.lower(), ""))
    out.append(("Keyword in first 40 chars of title", kw in t.lower()[:40], ""))
    first_two = " ".join(v["description"].splitlines()[:2]).lower()
    out.append(("Keyword in first 2 lines of description", kw in first_two, ""))
    chapters = re.findall(r"^(\d{1,2}:\d{2})\s+\S", v["description"], re.M)
    out.append(("Chapters: 3+ timestamps starting 00:00", len(chapters) >= 3 and chapters[0] == "00:00", f"{len(chapters)} found"))
    out.append(("Tracked link (UTM) in description", "utm_source=" in v["description"], ""))
    tags = re.findall(r"#\w+", v["description"])
    out.append(("1-3 hashtags in description", 1 <= len(tags) <= 3, f"{len(tags)} found"))
    out.append(("Tags 5-15 and include the keyword theme", 5 <= len(v["tags"]) <= 15 and any("karahi" in x for x in v["tags"]), f"{len(v['tags'])} tags"))
    out.append(("Thumbnail text 4 words or fewer", len(v["thumbnail_text"].split()) <= 4, v["thumbnail_text"]))
    return out

res = check(video)
for name, ok, note in res:
    print(f"{'PASS' if ok else 'FIX '}  {name:<44}{note}")
print(f"\nScore {sum(ok for _, ok, _ in res)}/{len(res)}")
