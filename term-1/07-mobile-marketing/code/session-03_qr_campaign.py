# Generate trackable QR codes for a poster campaign (one per location) and estimate results.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Needs: pip install qrcode pillow
import qrcode
from urllib.parse import urlencode

BASE = "https://example.pk/menu"
locations = {"dolmen-mall": 1_800, "lums-campus": 950, "packages-mall": 1_400}   # estimated daily passers-by
SCAN_RATE, ORDER_RATE, DAYS = 0.004, 0.18, 14

total_scans = total_orders = 0
for loc, footfall in locations.items():
    params = {"utm_source": "poster", "utm_medium": "qr", "utm_campaign": "winter_launch", "utm_content": loc}
    url = f"{BASE}?{urlencode(params)}"
    img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=8, border=4)
    fname = f"session-03_qr_{loc}.png"
    img.save(fname)
    scans = footfall * DAYS * SCAN_RATE
    orders = scans * ORDER_RATE
    total_scans += scans; total_orders += orders
    print(f"{loc:<14} {url}")
    print(f"{'':<14} saved {fname} | est. {scans:.0f} scans, {orders:.0f} orders in {DAYS} days")
print(f"\nTotal: ~{total_scans:.0f} scans and ~{total_orders:.0f} orders. GA4 shows the real numbers by utm_content.")
