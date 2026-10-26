# Email campaign KPI report: deliverability, opens, clicks, CTOR, conversions, unsubscribes,
# revenue per email and ROI, with a funnel chart. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Illustrative campaigns for a Karachi online bookstore, PKR. Opens are inflated by Apple Mail
# Privacy Protection, so clicks and conversions are the more reliable signals.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
MARGIN = 0.30
campaigns = {  # name: sent, hard bounces, soft bounces, unique opens, unique clicks, orders, revenue, unsubs, spam complaints, cost
    "Welcome series (3 emails)": (2_400, 12, 24, 1_380, 410, 96, 230_400, 6, 1, 4_000),
    "Weekly newsletter":         (15_000, 90, 210, 5_100, 690, 62, 136_400, 45, 6, 9_000),
    "11.11 promotion":           (15_000, 75, 180, 6_300, 1_470, 265, 662_500, 60, 9, 12_000),
    "Abandoned cart (auto)":     (1_100, 4, 8, 640, 260, 88, 246_400, 3, 0, 2_500),
    "Win-back (lapsed)":         (3_000, 60, 45, 540, 75, 9, 18_900, 51, 4, 3_000),
}
hdr = f"{'Campaign':<27}{'Deliv%':>7}{'Open%':>7}{'CTR%':>6}{'CTOR%':>7}{'Conv%':>6}{'Unsub%':>7}{'Rev/email':>10}{'ROI%':>8}"
print(hdr)
funnel_data = None
for n, (sent, hb, sb, op, cl, orders, rev, un, sp, cost) in campaigns.items():
    delivered = sent - hb - sb
    deliv = delivered / sent * 100
    open_r = op / delivered * 100
    ctr = cl / delivered * 100
    ctor = cl / op * 100
    conv = orders / cl * 100
    unsub = un / delivered * 100
    rpe = rev / delivered
    roi = (rev * MARGIN - cost) / cost * 100
    flag = "  <- spam rate above 0.1%" if sp / delivered > 0.001 else ""
    print(f"{n:<27}{deliv:>7.1f}{open_r:>7.1f}{ctr:>6.1f}{ctor:>7.1f}{conv:>6.1f}{unsub:>7.2f}{rpe:>10.1f}{roi:>8.0f}{flag}")
    if n == "11.11 promotion":
        funnel_data = [sent, delivered, op, cl, orders]
tot_rev = sum(c[6] for c in campaigns.values()); tot_cost = sum(c[9] for c in campaigns.values())
print(f"\nTotal revenue PKR {tot_rev:,} | cost PKR {tot_cost:,} | ROI on gross profit {(tot_rev * MARGIN - tot_cost) / tot_cost * 100:,.0f}%")
print("Formulas use DELIVERED emails as the base; CTOR = clicks / opens.")

fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=BG); ax.set_facecolor(BG)
labels = ["Sent", "Delivered", "Opened", "Clicked", "Ordered"]
cols = [VIOLET, "#38BDF8", GOLD, FIRE, EMBER]
bars = ax.barh(labels[::-1], funnel_data[::-1], color=cols[::-1])
for b, v in zip(bars, funnel_data[::-1]):
    ax.text(v + 150, b.get_y() + b.get_height() / 2, f"{v:,}", va="center", color=TEXT, fontsize=9)
ax.set_title("11.11 promotion email funnel", color=GOLD); ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-03_email_funnel.png", dpi=110, facecolor=BG)
print("Saved session-03_email_funnel.png")
