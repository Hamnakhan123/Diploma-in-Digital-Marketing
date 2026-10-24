# Media metrics for two Instagram ad creatives - Session 4
ads = {
    "Video A": {"cost": 45000, "impressions": 150000, "reach": 50000,
                "likes": 1200, "comments": 90, "shares": 60, "saves": 150},
    "Video B": {"cost": 45000, "impressions": 112500, "reach": 45000,
                "likes": 2300, "comments": 310, "shares": 280, "saves": 510},
}

for name, a in ads.items():
    frequency = a["impressions"] / a["reach"]
    cpm = a["cost"] / a["impressions"] * 1000
    engagements = a["likes"] + a["comments"] + a["shares"] + a["saves"]
    er = engagements / a["reach"] * 100
    cost_per_eng = a["cost"] / engagements
    print(f"{name}: frequency={frequency:.2f}  CPM=PKR {cpm:.0f}  "
          f"engagements={engagements:,}  ER={er:.2f}%  cost/engagement=PKR {cost_per_eng:.2f}")
