# Simulate one real-time bidding (RTB) auction and scale it to a campaign.
# Prepared by Hamna Zahid Khan, Junior Lecturer. All bids are illustrative (PKR per 1,000 impressions).

bids = {               # DSP bidding on one ad slot on a Pakistani news site, in PKR CPM
    "DSP-A (mobile phone brand)": 420,
    "DSP-B (food delivery app)": 365,
    "DSP-C (bank credit card)": 390,
    "DSP-D (clothing retailer)": 210,
}
floor_cpm = 250        # minimum price the publisher (via its SSP) will accept

eligible = {k: v for k, v in bids.items() if v >= floor_cpm}
ranked = sorted(eligible.items(), key=lambda kv: kv[1], reverse=True)
winner, top_bid = ranked[0]
runner_up = ranked[1][1]

second_price = runner_up + 1          # classic second-price: pay 1 rupee more than runner-up
first_price = top_bid                 # first-price: pay what you bid

print("Eligible bids (floor PKR %d CPM):" % floor_cpm)
for name, bid in ranked:
    print(f"  {name:<30} PKR {bid:>4} CPM")
print(f"Removed by floor: {[k for k in bids if k not in eligible]}")
print(f"\nWinner: {winner}")
print(f"  Second-price auction clears at PKR {second_price} CPM -> PKR {second_price/1000:.3f} per impression")
print(f"  First-price auction clears at  PKR {first_price} CPM -> PKR {first_price/1000:.3f} per impression")

# Scale to a campaign
impressions = 500_000
for label, cpm in [("second-price", second_price), ("first-price", first_price)]:
    spend = impressions / 1000 * cpm
    print(f"\n{label}: {impressions:,} impressions x PKR {cpm} CPM = PKR {spend:,.0f}")

# Frequency cap: how many people can we reach at 3 impressions per person per week?
cap = 3
print(f"\nWith a frequency cap of {cap}/week, 500,000 impressions reach at least {impressions // cap:,} different people")

# Viewability: only viewable impressions count under a vCPM deal
viewable_rate = 0.62
print(f"At {viewable_rate:.0%} viewability, {int(impressions * viewable_rate):,} impressions were actually viewable")
print(f"Effective cost per 1,000 viewable impressions (first-price): PKR {first_price / viewable_rate:,.0f}")
