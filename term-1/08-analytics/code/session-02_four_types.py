# The four types of analytics on one monthly dataset: descriptive, diagnostic, predictive, prescriptive.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Illustrative 12 months of an online store (PKR).
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sessions = np.array([41, 43, 46, 62, 48, 47, 45, 49, 52, 55, 78, 60]) * 1000
orders = np.array([820, 870, 880, 1380, 930, 890, 905, 940, 1010, 1060, 1650, 1120])
ad_spend = np.array([300, 300, 320, 520, 330, 320, 310, 340, 360, 380, 700, 420]) * 1000
cr = orders / sessions * 100

# 1. Descriptive - what happened?
print("DESCRIPTIVE: what happened?")
print(f"  Total orders {orders.sum():,}; best month {months[orders.argmax()]} ({orders.max():,}); avg conversion rate {cr.mean():.2f}%")

# 2. Diagnostic - why did it happen?
r = np.corrcoef(ad_spend, orders)[0, 1]
print("DIAGNOSTIC: why?")
print(f"  Correlation between ad spend and orders r = {r:.2f}; Apr (Ramadan/Eid) and Nov (11.11) had both the highest spend and conversion")
print(f"  Conversion rate in Apr {cr[3]:.2f}% and Nov {cr[10]:.2f}% vs normal months ~{np.median(cr):.2f}% -> demand peaks, not only more traffic")

# 3. Predictive - what will happen? (orders grow with the LOG of spend: diminishing returns)
b, a = np.polyfit(np.log(ad_spend), orders, 1)
plan = 450_000
print("PREDICTIVE: what will happen?")
print(f"  Model: orders = {a:,.0f} + {b:,.0f} x ln(spend)   (each doubling of spend adds about {b * np.log(2):,.0f} orders)")
print(f"  With PKR {plan:,} next month -> about {a + b * np.log(plan):,.0f} orders")

# 4. Prescriptive - what should we do?
aov, margin = 3_800, 0.35
print("PRESCRIPTIVE: what should we do?")
best = None
for spend in range(300_000, 1_700_001, 200_000):
    o = a + b * np.log(spend)
    profit = o * aov * margin - spend
    if best is None or profit > best[1]: best = (spend, profit)
    print(f"  spend PKR {spend:>7,} -> orders {o:>6,.0f}, profit after ads PKR {profit:>10,.0f}")
print(f"  Profit peaks where one more rupee of ads earns one rupee of profit: spend* = b x AOV x margin = PKR {b * aov * margin:,.0f}")
print(f"  Best in this grid: PKR {best[0]:,}. But we only ever spent PKR 300k-700k, so anything far above that is extrapolation:")
print("  raise spend step by step (e.g. +20% a month) and re-fit the model with the new data.")
print("  Caution: correlation is not causation - confirm with a holdout or geo test before trusting the slope.")
