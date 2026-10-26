# Weekly social KPI report from post-level data: engagement rate (by reach and by impressions),
# saves/shares share, click-through, and the best-performing format. Prepared by Hamna Zahid Khan.
import csv, io
from collections import defaultdict

DATA = """post,format,reach,impressions,likes,comments,shares,saves,link_clicks
P1,Reel,42000,51000,1900,140,620,880,310
P2,Carousel,18000,22000,820,95,140,610,260
P3,Static,9000,10500,310,22,15,40,45
P4,Reel,56000,70000,2600,210,950,1200,420
P5,Story,7000,7600,0,35,0,0,150
P6,Carousel,21000,26000,990,130,180,720,300
P7,Static,8500,9800,280,18,10,35,40
"""
rows = list(csv.DictReader(io.StringIO(DATA)))
agg = defaultdict(lambda: defaultdict(int))
print(f"{'Post':<5}{'Format':<9}{'ER/reach':>9}{'ER/impr':>9}{'Save+Share%':>12}{'CTR%':>6}")
for r in rows:
    n = {k: int(v) for k, v in r.items() if k not in ("post", "format")}
    eng = n["likes"] + n["comments"] + n["shares"] + n["saves"]
    print(f"{r['post']:<5}{r['format']:<9}{eng / n['reach'] * 100:>8.2f}%{eng / n['impressions'] * 100:>8.2f}%"
          f"{(n['shares'] + n['saves']) / max(eng, 1) * 100:>11.1f}%{n['link_clicks'] / n['impressions'] * 100:>6.2f}")
    for k, v in n.items(): agg[r["format"]][k] += v
    agg[r["format"]]["eng"] += eng; agg[r["format"]]["posts"] += 1
print("\nBy format (averages per post):")
best = None
for f, a in agg.items():
    er = a["eng"] / a["reach"] * 100
    print(f"  {f:<9} posts {a['posts']}  avg reach {a['reach'] / a['posts']:>8,.0f}  ER by reach {er:5.2f}%  clicks/post {a['link_clicks'] / a['posts']:.0f}")
    if best is None or er > best[1]: best = (f, er)
print(f"\nBest format by engagement rate: {best[0]} ({best[1]:.2f}%) -> plan more of it next week.")
print("Note: Stories have no likes in this export; judge them by replies, taps and link clicks.")
