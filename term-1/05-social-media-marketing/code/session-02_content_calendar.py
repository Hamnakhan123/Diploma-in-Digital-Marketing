# Build a 4-week social media content calendar from content pillars and a posting plan,
# save it as CSV and draw a weekly heat-map. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Example brand: "Sukoon Skincare", a Lahore D2C brand selling on Instagram, TikTok and Facebook.
import csv, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
START = dt.date(2026, 11, 2)                      # a Monday
PILLARS = [("Educate", 0.40), ("Entertain", 0.25), ("Community/UGC", 0.20), ("Promote", 0.15)]
# platform -> (posts per week, best local posting time, preferred formats)
PLAN = {
    "Instagram": (4, "20:30", ["Reel", "Carousel", "Story poll"]),
    "TikTok":    (5, "21:30", ["Short video", "Trend remix"]),
    "Facebook":  (3, "13:00", ["Photo post", "Live Q&A", "Video"]),
}
IDEAS = {
    "Educate": ["Skin type quiz", "SPF myths in Lahore heat", "Night routine in 3 steps", "Ingredient explainer: niacinamide"],
    "Entertain": ["Behind the scenes at packing", "Before Eid glow trend", "Staff try-on challenge", "Expectation vs reality"],
    "Community/UGC": ["Customer review repost", "Ask me anything", "Dermatologist answers DMs", "Feature a follower routine"],
    "Promote": ["New serum launch", "Free delivery weekend", "Bundle offer", "Limited stock alert"],
}

total_posts = sum(p[0] for p in PLAN.values()) * 4
quota = {name: round(total_posts * share) for name, share in PILLARS}
diff = total_posts - sum(quota.values()); quota["Educate"] += diff
print(f"Total posts in 4 weeks: {total_posts}")
for k, v in quota.items():
    print(f"  {k:<14}{v:>3} posts ({v / total_posts:.0%})")

# Spread pillars evenly: build a cyclic sequence weighted by quota
seq, left = [], dict(quota)
while sum(left.values()):
    for name, _ in PILLARS:
        if left[name]:
            seq.append(name); left[name] -= 1
rows, i = [], 0
days_for = {4: [0, 2, 4, 6], 5: [0, 1, 3, 4, 6], 3: [1, 3, 5]}
for week in range(4):
    for plat, (n, time, formats) in PLAN.items():
        for j, d in enumerate(days_for[n]):
            date = START + dt.timedelta(days=week * 7 + d)
            pillar = seq[i % len(seq)]
            idea = IDEAS[pillar][(week + j) % 4]
            rows.append([date.isoformat(), date.strftime("%a"), time, plat, formats[j % len(formats)], pillar, idea])
            i += 1
rows.sort()
with open("session-02_content_calendar.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["date", "day", "time_pkt", "platform", "format", "pillar", "idea"]); w.writerows(rows)
print("\nFirst 8 rows of session-02_content_calendar.csv:")
for r in rows[:8]:
    print("  " + " | ".join(r))

# heat-map: posts per weekday per platform
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
grid = [[sum(1 for r in rows if r[3] == p and r[1] == d) for d in days] for p in PLAN]
fig, ax = plt.subplots(figsize=(9, 2.8), facecolor=BG)
ax.imshow(grid, cmap="inferno", aspect="auto")
ax.set_xticks(range(7)); ax.set_xticklabels(days, color=TEXT)
ax.set_yticks(range(len(PLAN))); ax.set_yticklabels(list(PLAN), color=TEXT)
for y, row in enumerate(grid):
    for x, v in enumerate(row):
        ax.text(x, y, v, ha="center", va="center", color=GOLD if v < 3 else BG, fontsize=10, weight="bold")
ax.set_title("Posts per weekday over 4 weeks", color=GOLD)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_content_calendar.png", dpi=110, facecolor=BG)
print("\nSaved session-02_content_calendar.csv and session-02_content_calendar.png")
