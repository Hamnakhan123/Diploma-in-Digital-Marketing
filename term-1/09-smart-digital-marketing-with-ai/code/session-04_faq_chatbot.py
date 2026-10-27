# A tiny customer-service chatbot: match the customer's message to an intent, answer, and hand over
# to a human when unsure. Real assistants use language models, but the flow is the same.
# Prepared by Hamna Zahid Khan, Junior Lecturer. Store details are fictional.
import re

INTENTS = {
    "delivery_time": ({"delivery", "kab", "when", "days", "arrive", "pohanch"},
                      "Karachi, Lahore and Islamabad: 2-3 working days. Other cities: 3-5 working days."),
    "cod":           ({"cod", "cash", "payment", "pay", "easypaisa", "jazzcash"},
                      "We accept cash on delivery, cards, JazzCash and Easypaisa."),
    "returns":       ({"return", "exchange", "wapis", "size", "refund"},
                      "Exchanges and returns are free within 7 days if tags are attached. Reply RETURN to start."),
    "order_status":  ({"order", "track", "status", "kahan", "where"},
                      "Please share your order number (e.g. ORD-12345) and I will check its status."),
    "greeting":      ({"hi", "hello", "salam", "aoa", "assalam"},
                      "Wa alaikum assalam! How can I help you today?"),
}
ORDERS = {"ORD-12345": "Dispatched from Lahore warehouse, with courier, expected tomorrow."}

def reply(msg):
    m = re.search(r"ORD-\d{5}", msg.upper())
    if m:
        return "order_lookup", ORDERS.get(m.group(), "I could not find that order. Connecting you to an agent.")
    words = set(re.findall(r"[a-z]+", msg.lower()))
    scores = {k: len(kw & words) for k, (kw, _) in INTENTS.items()}
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "handover", "I am not sure I understood. Connecting you to a human agent (avg wait 3 min)."
    return best, INTENTS[best][1]

chat = ["Assalam o alaikum", "Mera parcel kab pohanchega Multan mein?", "Can I pay with JazzCash?",
        "Size chota hai, exchange ho sakta hai?", "Where is my order", "ord-12345",
        "My shirt colour faded after one wash, very disappointed"]
handovers = 0
for msg in chat:
    intent, ans = reply(msg)
    handovers += intent == "handover"
    print(f"Customer: {msg}\nBot [{intent}]: {ans}\n")
print(f"Contained by bot: {len(chat) - handovers}/{len(chat)} messages ({(len(chat) - handovers) / len(chat):.0%})")
