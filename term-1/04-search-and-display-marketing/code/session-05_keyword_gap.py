# Keyword gap analysis - the idea behind Semrush "Keyword Gap" and SpyFu "Kombat".
# Prepared by Hamna Zahid Khan, Junior Lecturer. Rankings and volumes are illustrative.

# keyword: (monthly volume, keyword difficulty 0-100)
KW = {
    "online grocery karachi": (6600, 41), "grocery delivery near me": (9900, 55),
    "atta 10kg price": (4400, 18), "cooking oil price in pakistan": (8100, 24),
    "fresh vegetables home delivery": (2900, 22), "monthly ration list": (3600, 12),
    "organic honey pakistan": (1900, 20), "baby diapers price": (5400, 30),
    "same day grocery delivery lahore": (1300, 28), "best basmati rice brand": (2400, 26),
    "frozen chicken home delivery": (1600, 15), "ramzan ration bag price": (2900, 14),
}
# your site and two competitors: keyword -> ranking position
you = {"online grocery karachi": 7, "atta 10kg price": 14, "organic honey pakistan": 3,
       "fresh vegetables home delivery": 22}
comp_a = {"online grocery karachi": 2, "grocery delivery near me": 4, "atta 10kg price": 3,
          "cooking oil price in pakistan": 5, "monthly ration list": 6, "baby diapers price": 8}
comp_b = {"online grocery karachi": 5, "cooking oil price in pakistan": 2, "fresh vegetables home delivery": 4,
          "monthly ration list": 3, "best basmati rice brand": 7, "same day grocery delivery lahore": 9}
competitors = {"Competitor A": comp_a, "Competitor B": comp_b}

all_comp = set(comp_a) | set(comp_b)
missing = sorted(all_comp - set(you), key=lambda k: -KW[k][0])
weak = sorted([k for k in you if k in all_comp and you[k] > min(c.get(k, 99) for c in competitors.values())],
              key=lambda k: -KW[k][0])
strong = [k for k in you if all(you[k] <= c.get(k, 99) for c in competitors.values())]
untapped = sorted(set(KW) - set(you) - all_comp)

def show(title, keys):
    print(f"\n{title} ({len(keys)})")
    for k in keys:
        vol, kd = KW[k]
        ranks = "  ".join(f"{n[-1]}:#{c[k]}" if k in c else f"{n[-1]}:-" for n, c in competitors.items())
        print(f"  {k:<36}vol {vol:>5,}  KD {kd:>2}  you:{'#'+str(you[k]) if k in you else '-':<4} {ranks}")

show("MISSING - competitors rank, you don't", missing)
show("WEAK - you rank below a competitor", weak)
show("STRONG - you beat every competitor", strong)
show("UNTAPPED - nobody in this set ranks", untapped)

print("\nPriority score for missing keywords = volume / (KD + 10):")
for k in sorted(missing, key=lambda k: -KW[k][0] / (KW[k][1] + 10))[:4]:
    vol, kd = KW[k]
    print(f"  {k:<36}{vol / (kd + 10):>7.1f}")
