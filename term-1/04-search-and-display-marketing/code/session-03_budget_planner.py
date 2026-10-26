# Work backwards from a sales target to the Google Ads budget you need (reverse funnel).
# Prepared by Hamna Zahid Khan, Junior Lecturer.
import math

target_orders = 120          # orders wanted this month
conv_rate = 0.025            # 2.5% of clicks become orders (from past data)
cpc = 38                     # PKR average cost per click
ctr = 0.045                  # 4.5% click-through rate on search ads
avg_order_value = 5_200      # PKR
margin = 0.35                # gross margin
days = 30

clicks = math.ceil(target_orders / conv_rate)
budget = clicks * cpc
impressions = math.ceil(clicks / ctr)
revenue = target_orders * avg_order_value
cpa = budget / target_orders
roas = revenue / budget
profit = revenue * margin - budget
max_cpa = avg_order_value * margin

print(f"Target orders           : {target_orders}")
print(f"Clicks needed           : {target_orders} / {conv_rate:.1%} = {clicks:,}")
print(f"Impressions needed      : {clicks:,} / {ctr:.1%} = {impressions:,}")
print(f"Monthly budget          : {clicks:,} x PKR {cpc} = PKR {budget:,}")
print(f"Daily budget            : PKR {budget/days:,.0f}")
print(f"Expected CPA            : PKR {cpa:,.0f}  (break-even CPA = PKR {max_cpa:,.0f})")
print(f"Expected revenue / ROAS : PKR {revenue:,} / {roas:.1f}x")
print(f"Profit after ads        : PKR {profit:,.0f}")

print("\nWhat if conversion rate improves with a better landing page?")
for cr in (0.02, 0.025, 0.03, 0.04):
    c = math.ceil(target_orders / cr)
    print(f"  CR {cr:.1%}: {c:>5,} clicks -> budget PKR {c*cpc:>8,} -> CPA PKR {c*cpc/target_orders:,.0f}")
