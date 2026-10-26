# Web analytics from raw events, the way GA4 thinks: users, sessions, engaged sessions,
# engagement rate, traffic sources, top pages and a purchase funnel.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Events are synthetic (fixed seed).
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(11)
sources = ["google / organic", "instagram / paid_social", "direct / (none)", "newsletter / email", "tiktok / paid_social"]
rows = []
for s_id in range(1, 2001):
    user = f"u{rng.integers(1, 1300)}"
    src = rng.choice(sources, p=[.34, .25, .18, .1, .13])
    t = 0
    steps = ["page_view"]
    dur = int(rng.exponential(14))
    if rng.random() < (.75 if "email" in src else .55): steps.append("view_item")
    if "view_item" in steps and rng.random() < .30: steps.append("add_to_cart")
    if "add_to_cart" in steps and rng.random() < .45: steps.append("begin_checkout")
    if "begin_checkout" in steps and rng.random() < .55 + (.15 if "email" in src else 0): steps.append("purchase")
    for e in steps:
        page = {"page_view": rng.choice(["/", "/sale", "/blog/winter-care"]), "view_item": "/product", "add_to_cart": "/product",
                "begin_checkout": "/checkout", "purchase": "/thank-you"}[e]
        rows.append((s_id, user, src, e, page, t)); t += rng.integers(5, 40)
    rows.append((s_id, user, src, "session_end", "", dur if len(steps) == 1 else max(dur, t)))
ev = pd.DataFrame(rows, columns=["session_id", "user_id", "source_medium", "event", "page", "sec"])
ev.to_csv("session-02_events.csv", index=False)

s = ev.groupby("session_id").agg(user=("user_id", "first"), src=("source_medium", "first"),
                                 dur=("sec", "max"), views=("event", lambda x: (x.isin(["page_view", "view_item"])).sum()),
                                 purchase=("event", lambda x: (x == "purchase").any()))
s["engaged"] = (s.dur > 10) | (s.views >= 2) | s.purchase       # GA4 engaged-session rule
print(f"Events: {len(ev):,} | Sessions: {len(s):,} | Users: {s.user.nunique():,}")
print(f"Engagement rate: {s.engaged.mean():.1%}  |  'Bounce rate' (100 - engagement): {1 - s.engaged.mean():.1%}")
print(f"Purchases: {s.purchase.sum()}  |  Session conversion rate: {s.purchase.mean():.2%}\n")
by = s.groupby("src").agg(sessions=("user", "count"), engaged=("engaged", "mean"), purchases=("purchase", "sum"))
by["conv_rate_%"] = (by.purchases / by.sessions * 100).round(2)
by["engaged"] = (by.engaged * 100).round(1)
print(by.sort_values("sessions", ascending=False).rename(columns={"engaged": "engaged_%"}).to_string())
print("\nTop landing pages:")
print(ev[ev.event == "page_view"].page.value_counts().to_string())

steps = ["page_view", "view_item", "add_to_cart", "begin_checkout", "purchase"]
counts = [ev[ev.event == e].session_id.nunique() for e in steps]
print("\nFunnel (sessions reaching each step):")
for i, (e, c) in enumerate(zip(steps, counts)):
    drop = "" if i == 0 else f"  ({c / counts[i - 1]:.0%} of previous step)"
    print(f"  {e:<15}{c:>6}{drop}")
fig, ax = plt.subplots(figsize=(9, 4), facecolor=BG); ax.set_facecolor(BG)
ax.bar(steps, counts, color=[VIOLET, "#38BDF8", GOLD, FIRE, EMBER])
for i, c in enumerate(counts): ax.text(i, c + 25, f"{c:,}", ha="center", color=TEXT)
ax.set_title("Purchase funnel from raw events", color=GOLD); ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic events", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_funnel.png", dpi=110, facecolor=BG)
print("Saved session-02_events.csv and session-02_funnel.png")
