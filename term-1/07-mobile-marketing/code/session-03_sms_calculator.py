# SMS campaign calculator: detect GSM-7 vs Unicode (Urdu), count segments, estimate cost and
# results. Prepared by Hamna Zahid Khan, Junior Lecturer. Price per segment is an assumption -
# use your bulk SMS provider's quote.
GSM7 = set("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà")
GSM7_EXT = set("^{}\\[~]|€")          # count as 2 characters

def segments(text):
    if all(c in GSM7 or c in GSM7_EXT for c in text):
        length = sum(2 if c in GSM7_EXT else 1 for c in text)
        single, multi, enc = 160, 153, "GSM-7"
    else:
        length = len(text.encode("utf-16-le")) // 2
        single, multi, enc = 70, 67, "Unicode (UCS-2)"
    n = 1 if length <= single else -(-length // multi)
    return enc, length, n

messages = {
    "English offer": "GarmChai: Karak chai flask PKR 650, free delivery over 1000 tonight. Order: wa.me/920000000000 Reply STOP to opt out",
    "Roman Urdu offer": "GarmChai: Aaj raat karak chai flask sirf PKR 650! Free delivery 1000 se upar. Order: wa.me/920000000000 STOP likh kar opt-out karein",
    "Urdu script offer": "گرم چائے: آج رات کڑک چائے فلاسک صرف 650 روپے! آرڈر کے لیے واٹس ایپ کریں۔ بند کرنے کے لیے STOP لکھیں",
    "Emoji offer": "GarmChai ☕ Karak chai flask PKR 650 tonight! Order on WhatsApp. Reply STOP to opt out",
}
LIST = 25_000            # opted-in subscribers
PRICE = 0.60             # PKR per segment (assumption)
DELIVERY, CLICK, CONVERT, AOV, MARGIN = 0.95, 0.04, 0.20, 700, 0.35
for name, msg in messages.items():
    enc, length, n = segments(msg)
    cost = LIST * n * PRICE
    orders = LIST * DELIVERY * CLICK * CONVERT
    profit = orders * AOV * MARGIN - cost
    print(f"{name:<18} {enc:<16} {length:>3} chars -> {n} segment(s) | cost PKR {cost:>7,.0f} | "
          f"~{orders:.0f} orders | profit after SMS PKR {profit:,.0f}")
print("\nTip: one emoji or Urdu letter switches the WHOLE message to Unicode (70 chars per segment).")
