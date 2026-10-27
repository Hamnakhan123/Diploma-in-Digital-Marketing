# 📝 Practice Test · Smart Digital Marketing with AI

> 🏠 [Diploma in Digital Marketing](../../README.md) › [Term 1](../README.md) › [Smart Digital Marketing with AI](README.md) › **Practice test**

20 multiple-choice questions and 3 practical scenarios. Try every question before opening the answers.

[⬅ Back to module overview](README.md) · [Next module ➡](../../capstone/README.md)

---

## Part A · Multiple-choice questions

1. Which statement is correct?
   a) Machine learning includes all of AI b) Deep learning is a type of machine learning c) Generative AI cannot create images d) AI and automation rules are the same thing
2. Grouping customers into segments without labels is:
   a) supervised learning b) unsupervised learning c) reinforcement learning d) data entry
3. A churn model flags 200 customers; 150 really churn. Its precision is:
   a) 50% b) 75% c) 133% d) 25%
4. Overall response rate is 2%; the top-scored 10% of customers respond at 8%. The lift is:
   a) 4 b) 6 c) 0.25 d) 10
5. Which tool is a visual drag-and-drop platform for building ML workflows?
   a) RapidMiner b) Brand24 c) OneTrust d) Adzooma
6. Salesforce Einstein and Adobe Sensei are best described as:
   a) cookie banners b) AI layers built into enterprise marketing clouds c) web hosts d) ad networks
7. AOV PKR 3,000, 4 orders a year, 3 years, 25% margin. Simple CLV is:
   a) PKR 9,000 b) PKR 36,000 c) PKR 3,000 d) PKR 12,000
8. The main job of a customer data platform (CDP) such as Segment is to:
   a) design logos b) stitch data from many sources into unified customer profiles c) host videos d) send invoices
9. "Customers who bought this also bought…" is usually powered by:
   a) collaborative filtering b) k-means only c) a cookie banner d) a lexicon
10. A personalised email converts at 3.0%, the control at 2.4%. The personalisation lift is:
    a) 0.6% b) 25% c) 20% d) 125%
11. Surfer SEO-style tools help marketers by:
    a) scoring content against top-ranking pages for a keyword b) running chatbots c) managing consent d) forecasting stock
12. In the RCTFC prompt pattern, "max 60 characters, numbered list" is the:
    a) Role b) Context c) Format d) Constraints
13. A bot receives 10,000 chats and hands 3,000 to humans. Containment is:
    a) 30% b) 70% c) 3,000 d) 7%
14. A multi-armed bandit in advertising:
    a) splits traffic equally forever b) shifts traffic towards better-performing ads while still exploring c) needs no clicks d) only works for SEO
15. Which is an example of **manipulation** in AI marketing?
    a) A preference centre b) A fake countdown timer c) A bot disclosure d) A bias audit
16. BigID is mainly used to:
    a) discover and classify personal data across systems b) write ad copy c) schedule posts d) build landing pages
17. An ad reaches 40% of men and 28% of women. The disparate-impact ratio is:
    a) 0.70 – fails the four-fifths rule b) 1.43 – passes c) 0.12 – passes d) 0.80 – borderline pass
18. A smart reputation alert should fire when:
    a) any mention appears b) mention volume spikes and sentiment drops together c) a competitor posts d) followers grow
19. Our brand has 4,000 mentions; competitors have 3,500 and 2,500. Our share of voice is:
    a) 40% b) 53% c) 4,000 d) 62%
20. "Privacy by design" means:
    a) adding a privacy policy after a complaint b) building consent, minimisation and security into a campaign from the start c) never using data d) storing all data forever

<details><summary>✅ Answers</summary>

1-b · 2-b · 3-b · 4-a · 5-a · 6-b · 7-a · 8-b · 9-a · 10-b · 11-a · 12-c · 13-b · 14-b · 15-b · 16-a · 17-a · 18-b · 19-a · 20-b

**Workings:** Q3: 150 ÷ 200 = **75%**. Q4: 8 ÷ 2 = **4**. Q7: 3,000 × 4 × 3 × 0.25 = **PKR 9,000** (PKR 36,000 is lifetime revenue before margin). Q10: (3.0 − 2.4) ÷ 2.4 = **25%**. Q13: (10,000 − 3,000) ÷ 10,000 = **70%**. Q17: 28 ÷ 40 = **0.70**. Q19: 4,000 ÷ 10,000 = **40%**.

</details>

## Part B · Scenarios

**Scenario 1 – AI for a Lahore fashion e-store.** A lawn and pret brand has 25,000 customers, a Shopify store, an Instagram shop and a WhatsApp order line. Sales are flat, repeat purchases are low and the owner wants "to use AI".

(a) Propose three AI use cases in order of priority, each with the data needed and a KPI. (b) How would you prove that personalised emails actually work? (c) Name two risks and how you would manage them.

<details><summary>✅ Solution</summary>

(a) **1. Segmentation and CLV** – order history (RFM), channel, city → identify high-value and at-risk customers; KPI repeat-purchase rate. **2. Personalised recommendations and emails** – browsing and purchase data in a CDP-style profile → "complete the look" emails and site widgets; KPI revenue per email, AOV. **3. WhatsApp chatbot** for order status, sizes and returns with human handover; KPI containment rate, response time, CSAT.
(b) Hold out a random **control group** (e.g. 10–20%) that receives the generic email; compare conversion rate and revenue per recipient; calculate lift = (personalised − control) ÷ control; run for at least one full sale cycle.
(c) **Privacy** – use only consented data, honour opt-outs, never ask for CNIC in chat. **Creepy or wrong personalisation** – cap frequency, avoid sensitive inferences, check recommendations for out-of-stock items. Also: bots giving wrong answers on complaints → always hand over to a human.

</details>

**Scenario 2 – Generative AI and ad automation for a restaurant chain.** A Karachi chain wants 40 social captions a month and wants an AI tool (Adzooma-style) to manage its Google and Meta ads with PKR 600,000 monthly spend. Last month an AI-written post listed the wrong price and drew angry comments.

(a) Design a safe generative-AI content workflow. (b) Which automation rules would you set, with limits? (c) How would you test four new ad creatives?

<details><summary>✅ Solution</summary>

(a) Brand Voice and Knowledge base (menu, prices, branches, timings) → RCTFC prompts from a prompt library → generate and shortlist → **human fact-check** of prices, timings, offers and religious/cultural sensitivity → approval by a named person → publish → save winners. A price-check step against the current menu would have stopped last month's error.
(b) Examples: pause keywords with spend > 2× target CPA and zero conversions after 14 days; reduce bids 10–15% if CPA > target for 7 days (max one change per week); add negative keywords weekly from search terms ("recipe", "jobs"); alert, not auto-act, when spend jumps > 30% in a day. Weekly human review of every automated change.
(c) Make four **genuinely different** creatives (different hook, visual and offer), let a bandit or the platform's automated allocation shift spend to winners, track CPA and orders not just CTR, and confirm the winner with enough conversions before scaling.

</details>

**Scenario 3 – An ethics and reputation crisis.** A Peshawar microfinance app uses an AI model to choose who sees its loan ads. A journalist finds women see the ad far less often. The next day mentions jump from 150 to 900 and sentiment turns sharply negative. The app's lead sheets, containing phone numbers and CNICs, are also shared with an agency over WhatsApp.

(a) How would you check whether the model is biased? (b) Outline your response for the first 48 hours. (c) What privacy fixes are needed, and which tools could help?

<details><summary>✅ Solution</summary>

(a) Compare **selection rates** by gender among equally eligible people; calculate the **disparate-impact ratio** (lower ÷ higher) and flag anything below 0.80; compare how many eligible women versus eligible men were reached (TPR); look for proxy features (e.g. occupation or neighbourhood) and biased training history.
(b) Brand24-style monitoring confirms the spike; verify the facts within the first hour; publish a holding statement within hours acknowledging the issue; pause the biased targeting; fix and re-audit the model; publish a transparent update with what changed; brief customer support; afterwards hold a post-mortem and set up regular fairness audits. No deleting criticism or buying praise.
(c) Stop sharing files over WhatsApp; use access-controlled storage; **remove CNICs** from marketing files (not needed for ads); mask phone numbers when sharing; sign a data-processing agreement with the agency; set retention limits. **BigID-style discovery** finds personal data across files and systems; **OneTrust-style consent and governance** records consent, manages preferences and documents a privacy impact assessment.

</details>

---

<sub>Prepared by **Hamna Zahid Khan**, Junior Lecturer · Diploma in Digital Marketing</sub>
