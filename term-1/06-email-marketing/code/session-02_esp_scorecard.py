# Weighted decision matrix for choosing an Email Service Provider (ESP).
# Prepared by Hamna Zahid Khan, Junior Lecturer. Scores (1-5) are an example team's judgement for a
# small Pakistani online store with 5,000 contacts - re-score with your own needs and current prices.
criteria = {  # criterion: weight (sums to 100)
    "Price at 5,000 contacts": 20, "Ease of use / templates": 15, "Automation (welcome, cart)": 20,
    "Deliverability reputation": 15, "E-commerce integration (Shopify/WooCommerce)": 15,
    "Segmentation and personalisation": 10, "Support and local payment options": 5}
esps = {
    "Option A (budget newsletter tool)": [5, 4, 2, 3, 2, 2, 3],
    "Option B (e-commerce automation tool)": [2, 4, 5, 4, 5, 5, 3],
    "Option C (all-in-one CRM suite)": [1, 3, 5, 4, 4, 5, 4],
    "Option D (developer API service)": [4, 1, 3, 4, 3, 3, 2],
}
w = list(criteria.values())
assert sum(w) == 100
print("Weighted score = sum(score x weight) / 100  (max 5.00)\n")
results = []
for name, scores in esps.items():
    total = sum(s * wt for s, wt in zip(scores, w)) / 100
    results.append((total, name))
    print(f"{name:<40}{total:.2f}")
best = max(results)
print(f"\nRecommended: {best[1]} ({best[0]:.2f}/5)")
print("Check before signing: free trial, contact-based vs send-based pricing, SPF/DKIM/DMARC setup help, data export.")
