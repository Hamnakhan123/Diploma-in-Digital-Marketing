# YouTube channel analytics: impressions CTR, views, average view duration, audience retention
# curve, watch time and estimated earnings. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Illustrative data for a Pakistani cooking channel ("Ammi Ka Kitchen"), three videos in PKR.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
RPM = 120   # assumed revenue per 1,000 views (PKR) after YouTube's share; varies widely by audience

videos = {  # title: (length s, impressions, views, avg view duration s, subs gained, likes, comments, shares)
    "Chicken Karahi in 20 min":    (720, 410_000, 28_700, 312, 640, 2_150, 380, 260),
    "Nihari - overnight recipe":   (1_260, 180_000, 7_200, 410, 150, 540, 95, 40),
    "5 lunchbox ideas for school": (540, 520_000, 46_800, 270, 1_120, 3_900, 610, 980),
}
print(f"{'Video':<29}{'CTR%':>6}{'AVD':>6}{'AVD%':>6}{'WatchHrs':>9}{'Eng%':>6}{'Est PKR':>9}")
for t, (L, imp, v, avd, subs, lk, cm, sh) in videos.items():
    ctr = v / imp * 100
    avd_pct = avd / L * 100
    hours = v * avd / 3600
    eng = (lk + cm + sh) / v * 100
    print(f"{t:<29}{ctr:>6.1f}{avd // 60:>3.0f}:{avd % 60:02.0f}{avd_pct:>6.0f}{hours:>9,.0f}{eng:>6.1f}{v / 1000 * RPM:>9,.0f}")
total_hours = sum(v[2] * v[3] / 3600 for v in videos.values())
print(f"\nTotal watch time: {total_hours:,.0f} hours (Partner Programme needs 4,000 public watch hours in 12 months + 1,000 subscribers)")

# Retention curve: % of viewers still watching at each point of the karahi video
points = [0, 5, 10, 15, 30, 60, 120, 240, 360, 480, 600, 720]
retained = [100, 82, 74, 70, 64, 58, 52, 45, 40, 36, 31, 12]
drop_first_10 = 100 - retained[2]
print(f"Karahi video: {drop_first_10}% of viewers leave in the first 10 seconds; {retained[-2]}% reach the 10-minute mark")
fig, ax = plt.subplots(figsize=(10, 4.2), facecolor=BG); ax.set_facecolor(BG)
ax.plot(points, retained, color=FIRE, lw=2.5, marker="o")
ax.fill_between(points, retained, color=FIRE, alpha=.15)
ax.axvspan(0, 15, color=GOLD, alpha=.12); ax.text(17, 95, "hook zone: first 15 s", color=GOLD, fontsize=8)
ax.annotate("end screen / outro drop", xy=(700, 14), xytext=(430, 25), color=TEXT, fontsize=8, arrowprops=dict(color=TEXT, arrowstyle="->"))
ax.set_ylim(0, 105); ax.set_xlabel("Seconds into video", color=TEXT); ax.set_ylabel("% of viewers still watching", color=TEXT)
ax.set_title("Audience retention - 'Chicken Karahi in 20 min' (12-minute video)", color=GOLD)
ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-05_youtube_retention.png", dpi=110, facecolor=BG)
print("Saved session-05_youtube_retention.png")
