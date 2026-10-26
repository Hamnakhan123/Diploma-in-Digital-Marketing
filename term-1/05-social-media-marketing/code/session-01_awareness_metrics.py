# Measuring the effect of social media on brand awareness: share of voice, reach growth,
# engagement rate and an awareness-lift survey. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Figures are an illustrative quarter for a Karachi chai cafe chain ("Chai Adda") and two rivals.

mentions = {"Chai Adda": 1_840, "Rival A": 2_600, "Rival B": 1_160}   # brand mentions in the quarter
total = sum(mentions.values())
print("Share of voice (SOV) = brand mentions / all mentions in the category")
for b, m in mentions.items():
    print(f"  {b:<10}{m:>6,} mentions -> SOV {m / total * 100:5.1f}%")

# Reach and engagement before vs after a 3-month content plan
before = dict(followers=12_400, reach=96_000, engagements=2_300)
after = dict(followers=19_850, reach=310_000, engagements=11_160)
for label, d in (("Before", before), ("After", after)):
    er_reach = d["engagements"] / d["reach"] * 100
    er_fol = d["engagements"] / d["followers"] * 100
    print(f"\n{label}: followers {d['followers']:,}, monthly reach {d['reach']:,}, engagements {d['engagements']:,}")
    print(f"  Engagement rate by reach     = {d['engagements']:,} / {d['reach']:,} x 100 = {er_reach:.2f}%")
    print(f"  Engagement rate by followers = {d['engagements']:,} / {d['followers']:,} x 100 = {er_fol:.2f}%")
growth = (after["followers"] - before["followers"]) / before["followers"] * 100
print(f"\nFollower growth = ({after['followers']:,} - {before['followers']:,}) / {before['followers']:,} x 100 = {growth:.1f}%")

# Brand-lift survey: two random groups of 400 people in Karachi
exposed, exposed_aware = 400, 172
control, control_aware = 400, 112
pe, pc = exposed_aware / exposed, control_aware / control
print(f"\nAided awareness: exposed {pe:.0%} vs control {pc:.0%}")
print(f"Absolute lift = {pe - pc:.0%} points; relative lift = {(pe - pc) / pc * 100:.1f}%")
