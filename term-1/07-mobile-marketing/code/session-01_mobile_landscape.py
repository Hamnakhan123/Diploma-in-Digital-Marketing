# Pakistan's mobile landscape in late 2025 and what it means for marketers.
# Prepared by Hamna Zahid Khan, Junior Lecturer.
# Source: DataReportal "Digital 2026: Pakistan" (Kepios, 8 Nov 2025): GSMA Intelligence for mobile
# connections, Kepios for internet and social users, Ookla for speeds, UN for population.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
population = 256.0            # million
connections = 194.0           # cellular mobile connections, million
broadband_share = 0.795       # share of connections on 3G/4G/5G networks
internet_users = 117.0        # million
social_ids = 79.9             # million
mobile_speed, fixed_speed = 24.32, 16.28   # median download Mbps

print(f"Mobile connections : {connections:.0f} M = {connections / population:.1%} of population")
print(f"Broadband (3G/4G/5G): {connections * broadband_share:.0f} M connections ({broadband_share:.1%})")
print(f"Internet users     : {internet_users:.0f} M = {internet_users / population:.1%} of population")
print(f"Social media IDs   : {social_ids:.1f} M = {social_ids / population:.1%} of population")
print(f"Offline population : {population - internet_users:.0f} M ({(population - internet_users) / population:.1%})")
print(f"Median mobile download {mobile_speed} Mbps vs fixed {fixed_speed} Mbps -> mobile is faster than the typical fixed line")
print("\nMarketing implications:")
print(" 1. Design every page, ad and email for phones first.")
print(" 2. SMS still reaches people who are not online - over half the population.")
print(" 3. Keep pages light: speeds vary by city and network.")

fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=BG); ax.set_facecolor(BG)
labels = ["Population", "Mobile connections", "Broadband connections", "Internet users", "Social media IDs"]
vals = [population, connections, connections * broadband_share, internet_users, social_ids]
bars = ax.bar(labels, vals, color=[VIOLET, FIRE, GOLD, "#38BDF8", EMBER])
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 3, f"{v:.0f} M", ha="center", color=TEXT, fontsize=9)
ax.set_title("Pakistan's mobile and digital audience, late 2025 (millions)", color=GOLD)
ax.tick_params(colors=TEXT, labelsize=8)
for s in ax.spines.values(): s.set_color("#3b3355")
fig.text(0.99, 0.01, "Source: DataReportal Digital 2026 Pakistan · Prepared by Hamna Zahid Khan", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-01_mobile_landscape.png", dpi=110, facecolor=BG)
print("Saved session-01_mobile_landscape.png")
