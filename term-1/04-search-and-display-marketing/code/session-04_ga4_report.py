# Build GA4-style channel and funnel reports from a small event log, then chart the funnel.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Data is generated with a fixed seed so output repeats.
import random
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(7)
BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"

# channel: (share of sessions, chance of each funnel step continuing, avg seconds)
CHANNELS = {
    "Paid Search":    (0.30, (0.70, 0.22, 0.55, 0.60), 95),
    "Organic Search": (0.28, (0.65, 0.18, 0.55, 0.62), 110),
    "Paid Social":    (0.20, (0.45, 0.10, 0.45, 0.50), 40),
    "Display":        (0.12, (0.30, 0.06, 0.40, 0.45), 18),
    "Email":          (0.10, (0.75, 0.30, 0.60, 0.70), 130),
}
STEPS = ["session_start", "view_item", "add_to_cart", "begin_checkout", "purchase"]
AOV = 4_800  # PKR average order value

sessions = []
for i in range(6000):
    r, acc = random.random(), 0
    for ch, (share, probs, secs) in CHANNELS.items():
        acc += share
        if r <= acc: break
    reached = 1
    for p in probs:
        if random.random() < p: reached += 1
        else: break
    pages = reached if random.random() < 0.65 else reached + 1
    mean = secs if reached > 1 else secs * 0.25      # one-page visits are usually short
    seconds = max(1, int(random.expovariate(1 / mean)))
    engaged = seconds > 10 or pages >= 2 or reached == 5      # GA4 engaged-session rule
    sessions.append((ch, reached, engaged, seconds))

rep = defaultdict(lambda: [0, 0, 0, 0])
for ch, reached, engaged, secs in sessions:
    r = rep[ch]; r[0] += 1; r[1] += engaged; r[2] += reached == 5; r[3] += secs
print(f"{'Channel':<16}{'Sessions':>9}{'Engaged':>9}{'Eng.rate':>9}{'Bounce':>8}{'Purch.':>7}{'CR%':>6}{'Revenue PKR':>13}")
for ch in CHANNELS:
    s, e, p, secs = rep[ch]
    print(f"{ch:<16}{s:>9,}{e:>9,}{e/s:>9.1%}{1-e/s:>8.1%}{p:>7}{p/s*100:>6.2f}{p*AOV:>13,}")
S = len(sessions); E = sum(x[2] for x in sessions); P = sum(x[1] == 5 for x in sessions)
print(f"{'All':<16}{S:>9,}{E:>9,}{E/S:>9.1%}{1-E/S:>8.1%}{P:>7}{P/S*100:>6.2f}{P*AOV:>13,}")

print("\nPurchase funnel (all channels):")
counts = [sum(x[1] >= k for x in sessions) for k in range(1, 6)]
for i, (step, c) in enumerate(zip(STEPS, counts)):
    drop = "" if i == 0 else f"  ({c/counts[i-1]:.0%} of previous step, drop-off {1-c/counts[i-1]:.0%})"
    print(f"  {step:<15}{c:>6,}{drop}")

fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=BG)
ax.set_facecolor(BG)
cols = [VIOLET, "#8B7CF6", GOLD, FIRE, EMBER]
for i, (step, c) in enumerate(zip(STEPS, counts)):
    w = c / counts[0]
    ax.barh(len(STEPS) - 1 - i, w, left=(1 - w) / 2, color=cols[i], height=0.8)
    label = f"{step}  {c:,}  ({c/counts[0]:.1%})"
    if w > 0.45:   # wide bar: label inside
        ax.text(0.5, len(STEPS) - 1 - i, label, ha="center", va="center", color=BG, fontsize=10, fontweight="bold")
    else:          # narrow bar: label to the right so it stays readable
        ax.text(0.5 + w / 2 + 0.02, len(STEPS) - 1 - i, label, ha="left", va="center", color=TEXT, fontsize=10, fontweight="bold")
ax.set_xlim(0, 1.05)
ax.axis("off")
ax.set_title("Purchase funnel built from GA4-style events", color=GOLD, fontsize=13)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · simulated data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-04_ga4_funnel.png", dpi=110, facecolor=BG)
print("Saved session-04_ga4_funnel.png")
