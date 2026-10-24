# Estimate monthly clicks from rankings using an illustrative CTR curve.
# Real CTRs vary by query, SERP features and device; use Search Console data for your site.
ctr = {1: 0.28, 2: 0.15, 3: 0.10, 4: 0.07, 5: 0.05, 6: 0.04, 7: 0.03, 8: 0.025, 9: 0.02, 10: 0.018}

def clicks(volume, position):
    return volume * ctr.get(position, 0.005)

volume = 1300
for now, target in [(9, 3), (4, 1), (15, 8)]:
    gain = clicks(volume, target) - clicks(volume, now)
    print(f"Move from #{now:>2} to #{target}: {clicks(volume, now):6.0f} -> {clicks(volume, target):6.0f} clicks/month (+{gain:.0f})")
