# Location-based marketing: decide which app users are inside a geofence around a store and
# should get a (consented) push offer, using the haversine distance. Prepared by Hamna Zahid Khan.
# Coordinates are approximate points in Lahore for practice.
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
STORE = ("Store - Gulberg", 31.5160, 74.3510)
RADIUS_M = 800

def haversine(lat1, lon1, lat2, lon2):
    r = 6_371_000
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))

users = [  # id, lat, lon, location consent, push opt-in, already got an offer today
    ("U1", 31.5185, 74.3490, True, True, False), ("U2", 31.5120, 74.3555, True, True, False),
    ("U3", 31.5290, 74.3480, True, True, False), ("U4", 31.5150, 74.3500, False, True, False),
    ("U5", 31.5172, 74.3532, True, False, False), ("U6", 31.5140, 74.3470, True, True, True),
    ("U7", 31.4990, 74.3600, True, True, False), ("U8", 31.5205, 74.3555, True, True, False),
]
fig, ax = plt.subplots(figsize=(6.5, 5.5), facecolor=BG); ax.set_facecolor(BG)
for uid, lat, lon, loc_ok, push_ok, capped in users:
    d = haversine(STORE[1], STORE[2], lat, lon)
    inside = d <= RADIUS_M
    send = inside and loc_ok and push_ok and not capped
    reason = ("SEND offer" if send else "outside fence" if not inside else
              "no location consent" if not loc_ok else "push not enabled" if not push_ok else "frequency cap reached")
    print(f"{uid}: {d:>6.0f} m from store -> {reason}")
    ax.scatter(lon, lat, color=GOLD if send else (EMBER if inside else VIOLET), s=70)
    ax.text(lon + 0.0006, lat, uid, color=TEXT, fontsize=8)
ax.scatter(STORE[2], STORE[1], marker="*", s=300, color=FIRE)
deg_lat = RADIUS_M / 111_320
deg_lon = RADIUS_M / (111_320 * math.cos(math.radians(STORE[1])))
ax.add_patch(plt.matplotlib.patches.Ellipse((STORE[2], STORE[1]), 2 * deg_lon, 2 * deg_lat, fill=False, color=FIRE, ls="--"))
ax.set_title("Geofence 800 m: gold = offer sent, red = inside but blocked", color=GOLD, fontsize=10)
ax.tick_params(colors=TEXT, labelsize=7)
for s in ax.spines.values(): s.set_color("#3b3355")
ax.set_xlabel("Longitude", color=TEXT); ax.set_ylabel("Latitude", color=TEXT)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · practice coordinates", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-03_geofence.png", dpi=110, facecolor=BG)
print("Saved session-03_geofence.png")
