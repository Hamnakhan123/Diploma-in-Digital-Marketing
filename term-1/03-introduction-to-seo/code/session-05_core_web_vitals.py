# Rate pages against Core Web Vitals thresholds (75th percentile of real-user visits).
THRESHOLDS = {  # metric: (good up to, poor above)
    "LCP_s":  (2.5, 4.0),    # Largest Contentful Paint, seconds
    "INP_ms": (200, 500),    # Interaction to Next Paint, milliseconds
    "CLS":    (0.1, 0.25),   # Cumulative Layout Shift, unitless
}

def rate(metric, value):
    good, poor = THRESHOLDS[metric]
    return "good" if value <= good else ("needs improvement" if value <= poor else "poor")

pages = {
    "/":                 {"LCP_s": 1.9, "INP_ms": 120, "CLS": 0.05},
    "/products/lawn":    {"LCP_s": 4.6, "INP_ms": 180, "CLS": 0.31},
    "/blog/care-tips":   {"LCP_s": 2.8, "INP_ms": 260, "CLS": 0.02},
}
for url, m in pages.items():
    ratings = {k: rate(k, v) for k, v in m.items()}
    passed = all(r == "good" for r in ratings.values())
    print(f"{url:18} " + "  ".join(f"{k}={m[k]} ({r})" for k, r in ratings.items()) + f"  -> {'PASS' if passed else 'FAIL'}")
