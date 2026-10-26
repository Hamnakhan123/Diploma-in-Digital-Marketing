# Social media advertising reach in Pakistan by platform (late 2025) and what it means for a brand.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
# Source: DataReportal "Digital 2026: Pakistan" (Kepios, published 8 Nov 2025), figures from each
# platform's own ad-planning tools. Ad reach is NOT the same as unique monthly users.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
INTERNET_USERS = 117.0      # million, Oct 2025
POPULATION = 256.0          # million, Oct 2025

# platform: (ad reach in millions, % of adult ad audience that is female)
reach = {
    "TikTok (18+)":  (79.9, 28.8),
    "YouTube":       (54.3, 39.7),
    "Facebook":      (52.9, 19.5),
    "Snapchat":      (41.1, 26.4),
    "Instagram":     (22.4, 34.9),
    "LinkedIn*":     (18.0, 24.5),
    "Messenger":     (15.5, 15.9),
    "X":             (2.88, 17.4),
    "Reddit":        (2.05, None),
    "Threads":       (1.85, 26.5),
}

print(f"{'Platform':<14}{'Reach (M)':>10}{'% of internet users':>21}{'% female':>10}")
for name, (m, fem) in reach.items():
    share = m / INTERNET_USERS * 100
    f = f"{fem:.1f}" if fem is not None else "n/a"
    print(f"{name:<14}{m:>10.2f}{share:>20.1f}%{f:>10}")
print("* LinkedIn reports registered members, not monthly active users.")

# A planning question: a Lahore modest-fashion brand targets women.
print("\nEstimated FEMALE ad audience (reach x female share):")
female = {n: m * f / 100 for n, (m, f) in reach.items() if f is not None}
for n, v in sorted(female.items(), key=lambda kv: -kv[1])[:5]:
    print(f"  {n:<14}{v:>6.1f} M")

fig, ax = plt.subplots(figsize=(10, 4.8), facecolor=BG)
ax.set_facecolor(BG)
names = list(reach)[::-1]
vals = [reach[n][0] for n in names]
cols = [FIRE if v > 50 else (GOLD if v > 20 else VIOLET) for v in vals]
bars = ax.barh(names, vals, color=cols)
for b, v in zip(bars, vals):
    ax.text(v + 0.8, b.get_y() + b.get_height() / 2, f"{v:g} M", va="center", color=TEXT, fontsize=8)
ax.set_title("Pakistan: social media ad reach by platform, late 2025 (millions)", color=GOLD)
ax.set_xlabel("Ad reach in millions (platform ad tools)", color=TEXT)
ax.tick_params(colors=TEXT, labelsize=9)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Source: DataReportal Digital 2026 Pakistan · Prepared by Hamna Zahid Khan", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-01_platform_reach.png", dpi=110, facecolor=BG)
print("\nSaved session-01_platform_reach.png")
