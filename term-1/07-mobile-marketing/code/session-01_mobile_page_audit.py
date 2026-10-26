# A simple mobile-friendliness audit of an HTML page: viewport, font size, tap targets,
# image weight, click-to-call/WhatsApp links and page weight. Prepared by Hamna Zahid Khan.
import re, os

def audit(path, image_sizes_kb):
    html = open(path, encoding="utf-8").read()
    checks = []
    checks.append(("Viewport meta tag present", 'name="viewport"' in html))
    sizes = [int(x) for x in re.findall(r"font-size:\s*(\d+)px", html)]
    checks.append((f"All font sizes >= 14px (found {sorted(set(sizes))})", all(s >= 14 for s in sizes)))
    pads = [int(x) for x in re.findall(r"min-height:\s*(\d+)px", html)]
    checks.append(("Buttons have min-height >= 44px (tap targets)", bool(pads) and all(p >= 44 for p in pads)))
    checks.append(("Click-to-call link (tel:)", "href=\"tel:" in html))
    checks.append(("WhatsApp chat link (wa.me)", "wa.me/" in html))
    checks.append(("Images lazy-loaded", "loading=\"lazy\"" in html or "<img" not in html))
    total_img = sum(image_sizes_kb.values())
    checks.append((f"Images total under 500 KB (planned {total_img} KB)", total_img <= 500))
    page_kb = os.path.getsize(path) / 1024
    checks.append((f"HTML under 100 KB ({page_kb:.1f} KB)", page_kb < 100))
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FIX '}  {name}")
    print(f"Score: {sum(ok for _, ok in checks)}/{len(checks)}")

audit("session-01_mobile_landing.html", {"hero.webp": 140, "product1.webp": 60, "product2.webp": 60})
