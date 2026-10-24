# Funnel conversion calculator - Session 3, Foundations of Digital Marketing
stages = [
    ("Website visits", 20000),
    ("Free sign-ups", 1600),
    ("Started trial lesson", 720),
    ("Paid for course", 216),
    ("Referred a friend", 43),
]

top = stages[0][1]
print(f"{'Stage':<22}{'People':>8}{'Step CVR':>10}{'From top':>10}")
for i, (name, n) in enumerate(stages):
    step = "-" if i == 0 else f"{n / stages[i-1][1]:.1%}"
    print(f"{name:<22}{n:>8,}{step:>10}{n / top:>10.2%}")

# find the leakiest step (lowest step conversion)
steps = [(stages[i][0], stages[i+1][0], stages[i+1][1] / stages[i][1]) for i in range(len(stages) - 1)]
worst = min(steps, key=lambda s: s[2])
print(f"\nLeakiest step: {worst[0]} -> {worst[1]} ({worst[2]:.1%})")

# what if we lift the leakiest step from 8% to 10%?
new_signups = int(20000 * 0.10)
new_paid = new_signups * (720 / 1600) * (216 / 720)
print(f"If sign-up rate rises to 10%: {new_signups} sign-ups -> about {new_paid:.0f} paid customers (was 216)")
