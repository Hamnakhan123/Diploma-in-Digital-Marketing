# Plan a 6-week mobile campaign: split the budget across mobile channels, forecast results,
# and draw a timeline (Gantt chart). Prepared by Hamna Zahid Khan, Junior Lecturer.
# Illustrative launch of a food-delivery app in Faisalabad, PKR. Rates are assumptions to replace with your data.
import datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
BUDGET = 1_200_000
GOAL_INSTALLS = 20_000
# channel: (share of budget, cost per install or per result in PKR, install->first order rate)
channels = {
    "App install ads (Meta/TikTok)": (0.40, 55, 0.22),
    "Google App campaign":            (0.25, 60, 0.25),
    "Influencer Reels + promo code":  (0.15, 70, 0.30),
    "QR posters + campus activation": (0.08, 40, 0.35),
    "SMS to opted-in partner list":   (0.07, 90, 0.18),
    "Testing reserve":                (0.05, 60, 0.22),
}
assert abs(sum(c[0] for c in channels.values()) - 1) < 1e-9
tot_inst = tot_orders = 0
print(f"{'Channel':<32}{'Budget PKR':>12}{'CPI':>6}{'Installs':>10}{'1st orders':>11}")
for n, (share, cpi, rate) in channels.items():
    spend = BUDGET * share
    inst = spend / cpi
    orders = inst * rate
    tot_inst += inst; tot_orders += orders
    print(f"{n:<32}{spend:>12,.0f}{cpi:>6}{inst:>10,.0f}{orders:>11,.0f}")
print(f"{'TOTAL':<32}{BUDGET:>12,}{BUDGET / tot_inst:>6.0f}{tot_inst:>10,.0f}{tot_orders:>11,.0f}")
print(f"\nGoal {GOAL_INSTALLS:,} installs -> forecast {tot_inst:,.0f} ({tot_inst / GOAL_INSTALLS:.0%} of goal)")
print(f"Blended cost per first order: PKR {BUDGET / tot_orders:,.0f}")
aov, margin = 900, 0.20
print(f"First-order gross profit: {tot_orders:,.0f} x {aov} x {margin} = PKR {tot_orders * aov * margin:,.0f} "
      f"-> payback needs repeat orders (CLV), not first orders alone")

start = dt.date(2026, 11, 2)
tasks = [("Research and personas", 0, 7), ("Creatives and landing page", 5, 10), ("Tracking: MMP, UTMs, events", 7, 6),
         ("Soft launch and tests", 14, 7), ("Full launch: ads and influencers", 21, 21), ("QR and campus activation", 24, 10),
         ("Push and SMS re-engagement", 28, 14), ("Weekly optimisation and report", 14, 28)]
fig, ax = plt.subplots(figsize=(10, 4.2), facecolor=BG); ax.set_facecolor(BG)
cols = [VIOLET, GOLD, "#38BDF8", FIRE, EMBER, GOLD, VIOLET, FIRE]
for i, ((name, s, d), c) in enumerate(zip(tasks, cols)):
    ax.barh(i, d, left=mdates.date2num(start + dt.timedelta(days=s)), color=c, height=.6)
ax.set_yticks(range(len(tasks))); ax.set_yticklabels([t[0] for t in tasks], color=TEXT, fontsize=8)
ax.invert_yaxis(); ax.xaxis_date(); ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
ax.tick_params(colors=TEXT, labelsize=8)
ax.set_title("Mobile app launch campaign timeline (6 weeks)", color=GOLD)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative plan", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_campaign_timeline.png", dpi=110, facecolor=BG)
print("Saved session-02_campaign_timeline.png")
