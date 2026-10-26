# 📝 Practice Test · Analytics

> 🏠 [Diploma in Digital Marketing](../../README.md) › [Term 1](../README.md) › [Analytics](README.md) › **Practice test**

20 multiple-choice questions and 3 practical scenarios. Try every question before opening the answers.

[⬅ Back to module overview](README.md) · [Next module ➡](../09-smart-digital-marketing-with-ai/README.md)

---

## Part A · Multiple-choice questions

1. Which is a KPI?
   a) An order record b) "Cost per lead ≤ PKR 600 by March" c) 4,000 sessions d) A screenshot of a post
2. The first phase of the data analytics lifecycle is:
   a) visualise b) discover/define the business question c) collect d) act
3. Removing duplicate rows from a double export belongs to:
   a) discover b) clean and prepare c) visualise d) act
4. Data customers intentionally share in a quiz or preference centre is:
   a) third-party b) zero-party c) second-party d) unstructured
5. "We expect 60,000 sessions in December" is which type of analytics?
   a) Descriptive b) Diagnostic c) Predictive d) Prescriptive
6. In GA4, a 6-second session with 2 page views is:
   a) not engaged b) engaged c) a bounce d) invalid
7. GA4 shows 4,000 sessions, 2,800 engaged. The bounce rate is:
   a) 70% b) 30% c) 40% d) 28%
8. Which tool shows heatmaps and session recordings for free?
   a) Search Console b) Microsoft Clarity c) Looker Studio d) Google Ads
9. Which tool shows the actual Google search queries that led to your site?
   a) Search Console b) Clarity c) Hotjar d) Meta Business Suite
10. With AOV PKR 6,000 and a 30% gross margin, break-even CPA is:
    a) PKR 600 b) PKR 1,800 c) PKR 2,000 d) PKR 20,000
11. Break-even ROAS at a 25% margin is:
    a) 2.5 b) 4.0 c) 0.25 d) 25
12. Which attribution model gives 100% credit to the first touch?
    a) Last click b) First click c) Linear d) Time decay
13. Journey TikTok → Instagram → Google → sale of PKR 9,000. Under linear attribution Instagram gets:
    a) PKR 0 b) PKR 3,000 c) PKR 4,500 d) PKR 9,000
14. Budget should be moved towards the channel with the lowest:
    a) average CPA b) marginal CPA c) CPM d) bounce rate
15. A post: reach 25,000, followers 10,000, engagements 1,500. ER by reach is:
    a) 15% b) 6% c) 2.5% d) 60%
16. The same post's ER by followers is:
    a) 6% b) 15% c) 1.5% d) 0.6%
17. Why compare formats using medians as well as means?
    a) Medians are always higher b) To reduce the effect of viral outliers c) GA4 requires it d) Medians include paid posts
18. The best chart to show monthly revenue over a year is:
    a) pie b) line chart c) scatter d) histogram
19. A bar chart whose y-axis starts at 1.9% when comparing 2.0% and 2.2%:
    a) is accurate b) exaggerates the difference c) is required d) improves accessibility
20. In Looker Studio, ROAS for a blended Ads + GA4 source is created with a:
    a) connector b) calculated field c) theme d) date control

<details><summary>✅ Answers</summary>

1-b · 2-b · 3-b · 4-b · 5-c · 6-b · 7-b · 8-b · 9-a · 10-b · 11-b · 12-b · 13-b · 14-b · 15-b · 16-b · 17-b · 18-b · 19-b · 20-b

**Workings:** Q7: engagement 2,800 ÷ 4,000 = 70% → bounce **30%**. Q10: 6,000 × 0.30 = **PKR 1,800**. Q11: 1 ÷ 0.25 = **4.0**. Q13: 9,000 ÷ 3 = **3,000**. Q15: 1,500 ÷ 25,000 = **6%**. Q16: 1,500 ÷ 10,000 = **15%**.

</details>

## Part B · Scenarios

**Scenario 1 – "Is our marketing working?"** A Faisalabad home-textile brand's owner sends you three exports: Shopify orders (with a "how did you hear about us" field, often blank), GA4 traffic by source, and ad spend from Meta and Google (Meta in USD, Google in PKR). She asks, "Is our marketing working?"

(a) Turn the question into an analysis plan using the six lifecycle phases. (b) List at least five data-cleaning steps you expect. (c) Which KPIs and break-even guards would you report? (d) Name two limitations you'd mention in the report.

<details><summary>✅ Solution</summary>

(a) **Discover:** define "working" = profitable sales growth this quarter vs last quarter and the same quarter last year. **Collect:** Shopify orders, GA4 acquisition (sessions, key events, revenue by source/medium), Meta and Google spend, same date range. **Clean:** see (b). **Analyse:** revenue, orders, AOV, CPA and ROAS by channel; compare periods; break-even checks; funnel by device. **Visualise:** KPI tiles, revenue trend, sorted bar chart of ROAS by channel with a break-even line. **Act:** budget shifts, landing-page fixes, tracking improvements.
(b) Convert Meta USD to PKR at the period's rate; align time zones (Asia/Karachi); remove duplicate and test orders; exclude cancelled/refunded orders; standardise source names ("insta", "Instagram", "IG"); mark blank survey answers as "Unknown"; match date ranges; check that GA4 purchases roughly match Shopify orders.
(c) Revenue, orders, AOV, conversion rate, CPA and ROAS by channel, blended ROAS, repeat-purchase rate; break-even CPA = AOV × margin and break-even ROAS = 1 ÷ margin.
(d) Attribution differences between platforms and GA4 (and last-click undervaluing awareness); blank "how did you hear" answers and WhatsApp/COD orders without source; correlation vs causation (seasonality); currency conversion assumptions.

</details>

**Scenario 2 – Re-allocating a budget.** A Karachi retailer spends PKR 900,000 a month: Search 200k (average CPA 600, marginal CPA 750), Meta 400k (average CPA 800, marginal CPA 1,400), TikTok 300k (average CPA 950, marginal CPA 1,000). Last-click reports make TikTok look weakest.

(a) Which channel should lose budget first, and why? (b) Why might cutting TikTok entirely be a mistake? (c) Design a test to prove TikTok's real contribution.

<details><summary>✅ Solution</summary>

(a) **Meta** – its *marginal* CPA (PKR 1,400) is the highest, so the last rupees there buy the most expensive conversions. Move budget from Meta to Search (marginal 750) and TikTok (marginal 1,000) step by step until marginal CPAs converge, rechecking each week.
(b) TikTok often provides first touches that later convert via Search or direct; last click gives it little credit. Position-based/data-driven attribution and assisted-conversion reports may show a larger role; cutting it can shrink future branded searches.
(c) A **geo holdout**: pause TikTok in a set of comparable cities (or regions of Karachi via ad targeting) for 4 weeks while keeping it in matched control areas; compare total orders, branded searches and new customers between test and control. Alternatively use a platform conversion-lift study if eligible.

</details>

**Scenario 3 – A monthly dashboard for the CEO.** The CEO of a food-delivery startup complains that the current report is a 40-tab spreadsheet. She wants to know every Monday whether marketing is on track.

(a) Choose 5–6 KPIs and justify them. (b) Sketch the dashboard layout (what goes where and which chart types). (c) Which data sources would you connect in Looker Studio and what calculated fields would you create? (d) Write an example insight title and a "what we'll do" note.

<details><summary>✅ Solution</summary>

(a) Orders vs target (core outcome); revenue (scale); blended CPA vs break-even (efficiency); ROAS (return on ads); new customers (growth); Day-30 retention or repeat-order rate (long-term health).
(b) **Top row:** scorecards for orders vs target (% achieved), revenue, CPA (with break-even), new customers – each compared with last week. **Middle:** line chart of daily orders and spend (last 8 weeks), with campaign annotations. **Bottom:** sorted bar chart of CPA by channel with a break-even line; funnel (app opens → menu views → cart → orders); small table of top 5 campaigns. Filters: date range, city, platform (iOS/Android).
(c) GA4/Firebase (sessions, funnel events, orders, revenue), Google Ads, Meta Ads (via connector or a Sheet export), order database/Sheet (including COD/WhatsApp orders), and a targets Sheet. Calculated fields: `CPA = Cost / Orders`, `ROAS = Revenue / Cost`, `Target achievement = Orders / Target orders`, a custom channel grouping with CASE.
(d) Title: "Orders 8% behind target because Android checkout conversion fell after Tuesday's update." Note: "Engineering is rolling back the payment screen today; we've paused 20% of Android install spend until conversion recovers and will review on Thursday."

</details>

---

<sub>Prepared by **Hamna Zahid Khan**, Junior Lecturer · Diploma in Digital Marketing</sub>
