# On-page SEO audit of an HTML page using only the Python standard library.
from html.parser import HTMLParser

html = """<!DOCTYPE html><html lang="en"><head>
<title>Home</title>
</head><body>
<h1>Welcome</h1><h1>Our Shawls</h1>
<img src="shawl-red.jpg"><img src="shawl-grey.jpg" alt="Grey pashmina shawl, hand-woven">
<p>Buy hand-woven wool shawls in Lahore. <a href="/contact">click here</a>
<a href="https://partner.example" rel="sponsored">Partner store</a></p>
</body></html>"""

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title, self.desc, self.h1 = "", None, 0
        self.imgs, self.no_alt, self.links, self.weak_anchors = 0, 0, 0, []
        self._in_title = self._in_a = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title": self._in_title = True
        if tag == "meta" and a.get("name") == "description": self.desc = a.get("content", "")
        if tag == "h1": self.h1 += 1
        if tag == "img":
            self.imgs += 1
            if not a.get("alt"): self.no_alt += 1
        if tag == "a": self.links += 1; self._in_a = True
    def handle_endtag(self, tag):
        if tag == "title": self._in_title = False
        if tag == "a": self._in_a = False
    def handle_data(self, data):
        if self._in_title: self.title += data
        if self._in_a and data.strip().lower() in ("click here", "read more", "here"):
            self.weak_anchors.append(data.strip())

p = Audit(); p.feed(html)
checks = [
    ("Title 30-60 characters", 30 <= len(p.title) <= 60, f"'{p.title}' ({len(p.title)} chars)"),
    ("Meta description present", bool(p.desc), p.desc or "missing"),
    ("Exactly one H1", p.h1 == 1, f"{p.h1} found"),
    ("All images have alt text", p.no_alt == 0, f"{p.no_alt} of {p.imgs} missing alt"),
    ("Descriptive anchor text", not p.weak_anchors, ", ".join(p.weak_anchors) or "ok"),
]
score = 0
for name, ok, detail in checks:
    score += ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:28} -> {detail}")
print(f"\nOn-page score: {score}/{len(checks)}")
