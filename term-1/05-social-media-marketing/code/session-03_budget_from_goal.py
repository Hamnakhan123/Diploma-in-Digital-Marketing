# Work backwards from a sales goal to a paid social budget, then check frequency.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
goal_orders = 300          # orders wanted in 30 days
aov = 4_500                # average order value, PKR
margin = 0.40
cr = 0.012                 # landing page conversion rate from link clicks (1.2%)
ctr = 0.011                # link-click-through rate (1.1%)
cpm = 210                  # expected CPM, PKR
audience = 1_200_000       # estimated audience size in the ad tool

clicks = goal_orders / cr
impressions = clicks / ctr
budget = impressions / 1000 * cpm
cpa = budget / goal_orders
breakeven_cpa = aov * margin
reach_est = min(audience * 0.45, impressions)      # assume ~45% of audience reachable in a month
freq = impressions / reach_est
print(f"Clicks needed      = {goal_orders} / {cr} = {clicks:,.0f}")
print(f"Impressions needed = {clicks:,.0f} / {ctr} = {impressions:,.0f}")
print(f"Budget             = {impressions:,.0f} / 1000 x PKR {cpm} = PKR {budget:,.0f} (PKR {budget / 30:,.0f}/day)")
print(f"Expected CPA       = PKR {cpa:,.0f}  vs break-even CPA PKR {breakeven_cpa:,.0f}")
print(f"Estimated reach    = {reach_est:,.0f}; frequency = {freq:.1f} per person per month")
print("Verdict:", "profitable" if cpa < breakeven_cpa else "unprofitable - improve CR/CTR or raise AOV",
      "|", "frequency OK" if freq <= 6 else "frequency too high - widen audience or refresh creatives weekly")
