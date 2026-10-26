# Send-time optimisation: pick each user's best hour for a push notification from their past
# app opens, respecting quiet hours. This is the simple idea behind AI "smart send" features.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Open hours are in PKT (UTC+5), invented.
from collections import Counter

QUIET = set(range(0, 9))        # no pushes 00:00-08:59 PKT
DEFAULT = 20                    # fall back to 8 pm when there is too little history
history = {
    "Ayesha": [13, 13, 14, 21, 13, 22, 13],
    "Bilal":  [23, 23, 0, 1, 23, 22, 23],       # night owl - quiet hours push him to the edge
    "Hira":   [9, 9, 10, 9, 18, 9],
    "Usman":  [20],                             # too little data
    "Zara":   [17, 18, 18, 19, 18, 18, 17, 18],
}
for user, hours in history.items():
    if len(hours) < 3:
        best, why = DEFAULT, "default (less than 3 opens)"
    else:
        allowed = [h for h in hours if h not in QUIET]
        if not allowed:
            best, why = DEFAULT, "all opens in quiet hours - default"
        else:
            best, cnt = Counter(allowed).most_common(1)[0]
            why = f"{cnt} of {len(hours)} opens at this hour"
    print(f"{user:<7} best send hour {best:02d}:00 PKT  ({why})")
print("\nAI tools do the same at scale, learning from millions of opens and re-learning every week.")
