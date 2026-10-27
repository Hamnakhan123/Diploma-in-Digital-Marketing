# Spotting customer trends: decompose weekly search interest into trend + seasonality and forecast ahead.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Synthetic weekly interest (0-100) for "lawn suit" in Pakistan.
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"
rng = np.random.default_rng(5)
weeks = np.arange(156)                      # three years of weekly data
season = 30 * np.exp(-((weeks % 52 - 14) ** 2) / 40)   # peak around week 14 (spring lawn launches)
trend = 30 + 0.12 * weeks
y = trend + season + rng.normal(0, 3, len(weeks))

# Fit trend with least squares on a straight line + average seasonal pattern by week-of-year
A = np.column_stack([np.ones_like(weeks), weeks])
coef, *_ = np.linalg.lstsq(A, y, rcond=None)
resid = y - A @ coef
seasonal = np.array([resid[weeks % 52 == w].mean() for w in range(52)])
fit = A @ coef + seasonal[weeks % 52]
mape = np.mean(np.abs((y - fit) / y)) * 100
print(f"Trend: +{coef[1]:.2f} interest points per week ({coef[1] * 52:.1f} per year)")
print(f"Seasonal peak week-of-year: {seasonal.argmax()} (+{seasonal.max():.1f} above trend)")
print(f"Seasonal low week-of-year:  {seasonal.argmin()} ({seasonal.min():.1f})")
print(f"In-sample error (MAPE): {mape:.1f}%")

future = np.arange(156, 182)
fc = coef[0] + coef[1] * future + seasonal[future % 52]
peak = future[fc.argmax()]
print(f"\nForecast next 26 weeks: peak at week {peak} (week-of-year {peak % 52}) with interest {fc.max():.0f}")
print(f"Plan: creatives ready by week-of-year {peak % 52 - 6}, budget ramp from week-of-year {peak % 52 - 3}")

fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=BG); ax.set_facecolor(BG)
ax.plot(weeks, y, color=VIOLET, lw=1.2, label="Actual interest")
ax.plot(weeks, A @ coef, color=GOLD, ls="--", label="Trend")
ax.plot(future, fc, color=FIRE, lw=2.5, label="Forecast")
ax.axvline(156, color=TEXT, alpha=0.3)
ax.set_xlabel("Week", color=TEXT); ax.set_ylabel("Search interest (0-100)", color=TEXT)
ax.set_title("Seasonal demand with a rising trend, and the next peak", color=GOLD)
ax.tick_params(colors=TEXT)
for sp in ax.spines.values(): sp.set_color("#3b3355")
ax.legend(facecolor=BG, labelcolor=TEXT, fontsize=8)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · synthetic data", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-02_trend_forecast.png", dpi=110, facecolor=BG)
print("Saved session-02_trend_forecast.png")
