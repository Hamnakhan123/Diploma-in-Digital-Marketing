# Technical SEO: test robots.txt rules and generate an XML sitemap (standard library only).
from urllib import robotparser
from xml.sax.saxutils import escape

robots_txt = """User-agent: *
Disallow: /cart/
Disallow: /search
Allow: /

Sitemap: https://shop.example.pk/sitemap.xml"""

rp = robotparser.RobotFileParser()
rp.parse(robots_txt.splitlines())
for path in ["/", "/products/lawn-suit-3pc", "/cart/checkout", "/search?q=lawn"]:
    ok = rp.can_fetch("Googlebot", "https://shop.example.pk" + path)
    print(f"{'ALLOW' if ok else 'BLOCK'}  {path}")

pages = [("/", "2026-10-20"), ("/products/lawn-suit-3pc", "2026-10-18"), ("/blog/lawn-care-tips", "2026-09-30")]
urls = "\n".join(
    f"  <url><loc>{escape('https://shop.example.pk' + p)}</loc><lastmod>{d}</lastmod></url>" for p, d in pages)
sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>'
print("\n" + sitemap)
