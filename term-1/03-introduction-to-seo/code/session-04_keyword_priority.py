# Prioritise keywords: opportunity = volume x intent value / difficulty,
# but only for keywords a young site can realistically win (KD at or below its reach).
keywords = [  # keyword, monthly searches, difficulty 0-100, intent
    ("online quran classes", 9900, 72, "commercial"),
    ("online quran classes for kids uk", 880, 28, "transactional"),
    ("how to learn tajweed at home", 1300, 22, "informational"),
    ("quran academy fees", 590, 18, "transactional"),
    ("quran", 450000, 98, "navigational"),
]
intent_value = {"transactional": 3, "commercial": 2, "informational": 1, "navigational": 0.2}
SITE_MAX_KD = 40   # a new site with few backlinks

rows = []
for kw, vol, kd, intent in keywords:
    score = vol * intent_value[intent] / max(kd, 1)
    plan = "target now" if kd <= SITE_MAX_KD else "later (too hard)"
    rows.append((kd > SITE_MAX_KD, -score, kw, vol, kd, intent, score, plan))

print(f"{'Keyword':34}{'Vol':>8}{'KD':>4}  {'Intent':14}{'Score':>6}  Plan")
for _, _, kw, vol, kd, intent, score, plan in sorted(rows):
    print(f"{kw:34}{vol:>8}{kd:>4}  {intent:14}{score:>6.0f}  {plan}")
