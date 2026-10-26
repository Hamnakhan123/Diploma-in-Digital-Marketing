# Draw a timeline of milestones in search and display advertising and save it as a PNG.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"

events = [
    (1994, "First clickable\nbanner ad", VIOLET),
    (1996, "Ad servers track\nimpressions", VIOLET),
    (1998, "GoTo.com: pay-per-click\nkeyword auction", FIRE),
    (2000, "Google AdWords\nlaunches", FIRE),
    (2002, "AdWords moves to\nCPC + quality", FIRE),
    (2003, "Yahoo buys Overture;\nAdSense launches", GOLD),
    (2005, "Quality Score\nintroduced", FIRE),
    (2008, "Google completes\nDoubleClick purchase", VIOLET),
    (2012, "Programmatic &\nreal-time bidding grow", VIOLET),
    (2016, "Smart Bidding\n(machine learning)", EMBER),
    (2018, "AdWords renamed Google Ads;\nGDPR in force", GOLD),
    (2021, "Performance Max\nlaunches", EMBER),
    (2022, "Responsive search ads\nbecome the standard", FIRE),
    (2024, "AI Overviews; Consent\nMode v2 in Europe", EMBER),
]

fig, ax = plt.subplots(figsize=(14, 5.2), facecolor=BG)
ax.set_facecolor(BG)
ax.axhline(0, color=TEXT, lw=1.5, alpha=0.6)
for i, (year, label, col) in enumerate(events):
    up = 1 if i % 2 == 0 else -1
    h = up * (1.1 if (i // 2) % 2 == 0 else 2.0)
    ax.vlines(year, 0, h, color=col, lw=1.4)
    ax.scatter(year, 0, s=70, color=col, zorder=3)
    ax.text(year, h + 0.15 * up, f"{year}\n{label}" if up > 0 else f"{label}\n{year}",
            ha="center", va="bottom" if up > 0 else "top", color=TEXT, fontsize=8.2)
ax.set_ylim(-3.3, 3.3)
ax.set_xlim(1992.5, 2025.5)
ax.axis("off")
ax.set_title("Thirty years of search and display advertising", color=GOLD, fontsize=14, pad=10)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout()
plt.savefig("session-01_search_ad_timeline.png", dpi=110, facecolor=BG)
print("Saved session-01_search_ad_timeline.png with", len(events), "milestones",
      f"from {events[0][0]} to {events[-1][0]}")
