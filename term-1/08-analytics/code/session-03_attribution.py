# Compare attribution models on customer journeys: last click, first click, linear,
# time decay and position-based (40/20/40). Prepared by Hamna Zahid Khan, Junior Lecturer.
from collections import defaultdict

journeys = [  # (touchpoints in order, revenue PKR)
    (["TikTok", "Instagram", "Google Search"], 6_000),
    (["Google Search"], 3_500),
    (["Instagram", "Email", "Email"], 4_800),
    (["TikTok", "Google Search", "Email"], 7_200),
    (["YouTube", "Instagram", "Google Search", "Email"], 9_000),
    (["Instagram", "Google Search"], 5_000),
    (["TikTok", "Instagram"], 2_800),
]

def weights(n, model):
    if model == "Last click": return [0] * (n - 1) + [1]
    if model == "First click": return [1] + [0] * (n - 1)
    if model == "Linear": return [1 / n] * n
    if model == "Time decay":                      # each step back counts half
        w = [0.5 ** (n - 1 - i) for i in range(n)]; s = sum(w); return [x / s for x in w]
    if model == "Position (40/20/40)":
        if n == 1: return [1]
        if n == 2: return [.5, .5]
        mid = 0.2 / (n - 2); return [.4] + [mid] * (n - 2) + [.4]

models = ["Last click", "First click", "Linear", "Time decay", "Position (40/20/40)"]
channels = sorted({t for j, _ in journeys for t in j})
table = {m: defaultdict(float) for m in models}
for m in models:
    for path, rev in journeys:
        for ch, w in zip(path, weights(len(path), m)):
            table[m][ch] += rev * w
print(f"{'Channel':<15}" + "".join(f"{m:>21}" for m in models))
for ch in channels:
    print(f"{ch:<15}" + "".join(f"{table[m][ch]:>21,.0f}" for m in models))
print(f"{'TOTAL':<15}" + "".join(f"{sum(table[m].values()):>21,.0f}" for m in models))
print("\nNotice: TikTok and YouTube get almost nothing under last click but real credit under first-click and position-based models.")
