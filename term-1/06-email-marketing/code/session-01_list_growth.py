# Model 12 months of email list growth and decay: new opt-ins, unsubscribes, bounces and
# inactive contacts, and chart the result. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Illustrative figures for a Karachi online bookstore.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
start = 8_000
signups = [600, 650, 700, 1_400, 900, 750, 700, 800, 850, 950, 1_800, 1_100]   # Apr = Ramadan offer, Nov = 11.11
UNSUB, BOUNCE, DECAY = 0.004, 0.003, 0.030    # monthly rates: unsubscribes, hard bounces, contacts going inactive
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

size, active, sizes, actives = start, start * 0.75, [], []
print(f"{'Month':<6}{'New':>6}{'Lost':>7}{'List':>8}{'Engaged':>9}")
for m, new in zip(months, signups):
    lost = round(size * (UNSUB + BOUNCE))
    size = size + new - lost
    active = active * (1 - DECAY - UNSUB - BOUNCE) + new * 0.85
    sizes.append(size); actives.append(active)
    print(f"{m:<6}{new:>6}{lost:>7}{size:>8,}{active:>9,.0f}")
growth = (sizes[-1] - start) / start * 100
print(f"\nNet list growth in the year: {growth:.1f}%  |  engaged share at year end: {actives[-1] / sizes[-1]:.0%}")
print("Lesson: list size grows, but without re-engagement campaigns the engaged share slowly falls.")

fig, ax = plt.subplots(figsize=(10, 4.2), facecolor=BG); ax.set_facecolor(BG)
ax.plot(months, sizes, color=FIRE, lw=2.5, marker="o", label="Total list")
ax.plot(months, actives, color=GOLD, lw=2.5, marker="s", label="Engaged contacts (opened/clicked in 90 days)")
ax.bar(months, signups, color=VIOLET, alpha=.45, label="New sign-ups")
ax.set_title("Email list growth over 12 months (illustrative)", color=GOLD)
ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8, loc="upper left")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-01_list_growth.png", dpi=110, facecolor=BG)
print("Saved session-01_list_growth.png")
