# Social media ROI for a quarter: full cost, attributed revenue, ROI, ROAS, cost per result,
# customer lifetime value effect, and a channel chart. Prepared by Hamna Zahid Khan, Junior Lecturer.
# Illustrative quarter for a Faisalabad home-textile brand ("Rangoli Linen"), PKR.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
MARGIN = 0.38
costs = {"Ad spend": 450_000, "Content production": 180_000, "Social media executive (3 months)": 270_000,
         "Tools (scheduler, listening, design)": 45_000, "Influencer fees": 150_000}
channels = {  # channel: (orders attributed in GA4, revenue)
    "Instagram": (310, 1_550_000), "Facebook": (240, 1_080_000), "TikTok": (180, 720_000),
    "Influencers": (95, 522_500), "YouTube": (40, 220_000)}

total_cost = sum(costs.values())
revenue = sum(r for _, r in channels.values())
orders = sum(o for o, _ in channels.values())
gross_profit = revenue * MARGIN
roi = (gross_profit - total_cost) / total_cost * 100
print("Costs:")
for k, v in costs.items(): print(f"  {k:<38}PKR {v:>9,}")
print(f"  {'TOTAL':<38}PKR {total_cost:>9,}")
print(f"\nAttributed revenue PKR {revenue:,} from {orders:,} orders (AOV PKR {revenue / orders:,.0f})")
print(f"Gross profit = {revenue:,} x {MARGIN} = PKR {gross_profit:,.0f}")
print(f"ROI = ({gross_profit:,.0f} - {total_cost:,}) / {total_cost:,} x 100 = {roi:.1f}%")
print(f"ROAS on ad spend only = {revenue:,} / {costs['Ad spend']:,} = {revenue / costs['Ad spend']:.2f}")
print(f"Cost per order (all-in) = PKR {total_cost / orders:,.0f}")

# Lifetime view: 35% of new customers buy again twice in a year
repeat_rate, repeat_orders = 0.35, 2
aov = revenue / orders
clv_extra = orders * repeat_rate * repeat_orders * aov * MARGIN
roi_clv = (gross_profit + clv_extra - total_cost) / total_cost * 100
print(f"\nWith repeat purchases (CLV view): extra gross profit PKR {clv_extra:,.0f} -> ROI {roi_clv:.1f}%")

fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=BG); ax.set_facecolor(BG)
names = list(channels)
ax.bar(names, [channels[n][1] / 1000 for n in names], color=[FIRE, VIOLET, EMBER, GOLD, "#38BDF8"])
for i, n in enumerate(names):
    ax.text(i, channels[n][1] / 1000 + 20, f"{channels[n][0]} orders", ha="center", color=TEXT, fontsize=8)
ax.set_ylabel("Attributed revenue (PKR thousands)", color=TEXT)
ax.set_title("Revenue attributed to each social channel - one quarter", color=GOLD)
ax.tick_params(colors=TEXT)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · illustrative data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-06_social_roi.png", dpi=110, facecolor=BG)
print("Saved session-06_social_roi.png")
