# UX + SEO scorecard: flag pages where engagement signals suggest the page fails the searcher.
# Data shaped like a GA4 export joined with Search Console (illustrative numbers).
pages = [  # url, impressions, clicks, engagement rate, avg engagement time (s), mobile LCP (s)
    ("/blog/how-to-start-freelancing", 42000, 1890, 0.71, 145, 2.1),
    ("/services/web-design",            9000,  140, 0.38,  22, 4.3),
    ("/blog/best-laptops-students",    30000,  450, 0.44,  31, 2.4),
    ("/contact",                        1200,   90, 0.80,  50, 1.6),
]

def diagnose(impr, clicks, eng, secs, lcp):
    ctr = clicks / impr
    issues = []
    if ctr < 0.02:  issues.append(f"low CTR {ctr:.1%}: rewrite title/description")
    if eng < 0.50:  issues.append(f"engagement {eng:.0%}: content may not match intent")
    if secs < 40:   issues.append(f"{secs}s engaged: add answer near the top, improve layout")
    if lcp > 2.5:   issues.append(f"LCP {lcp}s: compress hero image, lazy-load below the fold")
    return ctr, issues

for url, impr, clicks, eng, secs, lcp in pages:
    ctr, issues = diagnose(impr, clicks, eng, secs, lcp)
    status = "HEALTHY" if not issues else f"{len(issues)} ISSUE(S)"
    print(f"{url:34} CTR {ctr:5.1%}  {status}")
    for i in issues:
        print(f"    - {i}")
