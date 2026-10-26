# A simplified Google Ads auction: Ad Rank = max CPC bid x Quality Score.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
# Google's real Ad Rank also uses ad-rank thresholds, context (device, location, time) and expected
# impact of assets, so treat this as a teaching model of the core idea, not the exact formula.

keyword = "ac repair karachi"
advertisers = [  # name, max CPC bid (PKR), Quality Score (1-10)
    ("CoolFix Services", 120, 9),
    ("AC Wala Express", 180, 5),
    ("Gulshan Cooling Co", 140, 7),
    ("Budget AC Repairs", 200, 3),
    ("Arctic Home Care", 90, 8),
]
AD_RANK_THRESHOLD = 650   # illustrative minimum Ad Rank needed to show at all

rows = [(name, bid, qs, bid * qs) for name, bid, qs in advertisers]
rows.sort(key=lambda r: r[3], reverse=True)

print(f'Auction for "{keyword}"\n')
print(f"{'Pos':<4}{'Advertiser':<22}{'Bid':>6}{'QS':>4}{'Ad Rank':>9}{'Actual CPC':>12}")
for i, (name, bid, qs, rank) in enumerate(rows):
    if rank < AD_RANK_THRESHOLD:
        print(f"{'--':<4}{name:<22}{bid:>6}{qs:>4}{rank:>9}{'not shown':>12}")
        continue
    nxt = rows[i + 1][3] if i + 1 < len(rows) else AD_RANK_THRESHOLD
    nxt = max(nxt, AD_RANK_THRESHOLD)
    actual = min(bid, nxt / qs + 1)       # pay just enough to beat the next Ad Rank, never above your bid
    print(f"{i+1:<4}{name:<22}{bid:>6}{qs:>4}{rank:>9}{actual:>12.2f}")

best = rows[0]
print(f"\n{best[0]} bids PKR {best[1]} but wins position 1 because its Quality Score is {best[2]}.")
budget = [r for r in rows if r[0] == "Budget AC Repairs"][0]
print(f"{budget[0]} bids the most (PKR {budget[1]}) yet Ad Rank {budget[3]} is too low to show.")

# What a Quality Score improvement is worth for one advertiser
name, bid, qs = "AC Wala Express", 180, 5
target_rank = rows[0][3] + 1
for new_qs in (5, 7, 9):
    need = target_rank / new_qs
    print(f"{name} with QS {new_qs}: needs a bid of about PKR {need:,.1f} to take position 1")
