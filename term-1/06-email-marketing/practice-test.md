# 📝 Practice Test · Email Marketing

> 🏠 [Diploma in Digital Marketing](../../README.md) › [Term 1](../README.md) › [Email Marketing](README.md) › **Practice test**

20 multiple-choice questions and 3 practical scenarios. Try every question before opening the answers.

[⬅ Back to module overview](README.md) · [Next module ➡](../07-mobile-marketing/README.md)

---

## Part A · Multiple-choice questions

1. Email is called an "owned" channel because:
   a) it is free b) the business controls the list, not a platform's algorithm c) only owners can send it d) it never bounces
2. Double opt-in means:
   a) asking twice for a phone number b) the subscriber confirms by clicking a link before being added c) sending every email twice d) two lists
3. Which list-building practice is unacceptable?
   a) A quiz lead magnet b) An unticked checkout box c) A purchased list of 30,000 addresses d) A QR code at the shop counter
4. SPF's job is to:
   a) sign the email digitally b) list which servers are allowed to send for your domain c) set a policy for failures d) count clicks
5. A DMARC policy of `p=none` means:
   a) reject all failing mail b) monitor only and send reports c) quarantine failing mail d) disable email
6. A hard bounce should be:
   a) retried daily b) removed from the list immediately c) moved to VIP d) ignored
7. "Your order #2231 has shipped" is a:
   a) promotional email b) transactional email c) newsletter d) win-back email
8. The recommended subject-line length for mobile is roughly:
   a) 5–10 characters b) 30–50 characters c) 120 characters d) unlimited
9. A preheader is:
   a) the logo b) the preview text shown after the subject line in the inbox c) the footer d) the sender address
10. Which is a SMART goal?
    a) "Send better emails" b) "Raise newsletter click rate from 2.5% to 3.5% in 12 weeks by testing personalised subjects" c) "Grow the list" d) "Be more engaging"
11. In RFM segmentation, a customer who spent a lot but hasn't bought for 250 days is best described as:
    a) Champion b) At risk c) New d) Never a customer
12. The best way to choose an ESP is:
    a) the most famous brand b) a weighted scorecard against your needs, then free trials c) always the cheapest d) the one a competitor uses
13. A frequency cap is:
    a) a limit on marketing emails per person per period b) a limit on list size c) the maximum subject length d) a bounce threshold
14. A campaign was sent to 8,000 addresses; 200 bounced. Delivered emails = 7,800. 312 people clicked. Click rate is:
    a) 3.9% b) 4.0% c) 2.5% d) 39%
15. 1,950 unique opens and 312 unique clicks give a CTOR of:
    a) 6% b) 16% c) 25% d) 62%
16. Open rates became less reliable mainly because of:
    a) GDPR b) Apple Mail Privacy Protection c) DKIM d) Shorter subject lines
17. Good opens but very low CTOR point to a problem with:
    a) authentication b) the email content and call to action c) the landing page d) list size
18. A healthy spam complaint rate is below about:
    a) 0.1% b) 2% c) 5% d) 10%
19. A/B test on click rate: A 4.0% vs B 5.0% with 7,400 delivered each gives z ≈ 2.93. At 95% confidence:
    a) not significant b) B is significantly better c) A is significantly better d) cannot tell
20. A responsible use of AI in email marketing is:
    a) uploading the customer list to a public chatbot b) letting AI invent customer reviews c) drafting subject lines with AI, fact-checking them and A/B testing d) sending AI copy without review

<details><summary>✅ Answers</summary>

1-b · 2-b · 3-c · 4-b · 5-b · 6-b · 7-b · 8-b · 9-b · 10-b · 11-b · 12-b · 13-a · 14-b · 15-b · 16-b · 17-b · 18-a · 19-b · 20-c

**Workings:** Q14: 312 ÷ 7,800 × 100 = **4.0%**. Q15: 312 ÷ 1,950 × 100 = **16%**. Q19: |z| = 2.93 > 1.96 → significant.

</details>

## Part B · Scenarios

**Scenario 1 – Fixing a broken email programme.** A Karachi electronics store emails its whole list of 40,000 contacts three times a week from `karachielectronics@gmail.com`. The list combines website sign-ups, an exhibition spreadsheet and a list bought from a vendor. Last campaign: delivery 88%, open rate 9%, click rate 0.4%, unsubscribe 1.2%, spam complaints 0.5%. Many customers say emails land in spam.

(a) Identify at least six problems. (b) Write a 30-day recovery plan in order. (c) What metrics would show the recovery is working?

<details><summary>✅ Solution</summary>

(a) Free Gmail sender address (no domain authentication); purchased list (no consent, spam traps); exhibition data with unclear consent; no list cleaning (12% not delivered); far too frequent (3/week to everyone); no segmentation; spam complaints 0.5% exceed Gmail/Yahoo's 0.3% limit; probably no one-click unsubscribe; content not relevant (low clicks).
(b) **Week 1:** stop all bulk sends; set up a domain sender (`news@karachielectronics.pk`) with SPF, DKIM, DMARC (`p=none`); add a visible one-click unsubscribe and physical address. **Week 1–2:** delete the purchased list; clean the rest (invalid, duplicates, bounces, unsubscribes); keep only contacts with consent; verify addresses. **Week 2:** send a re-permission email to exhibition contacts ("Do you still want our offers?") – keep only those who click. **Week 3:** restart sending **only to engaged contacts** (opened/clicked in 90 days, recent buyers), once a week, segmented by interest (phones, appliances, accessories); launch welcome and abandoned-cart automations. **Week 4:** gradually add more contacts as reputation improves; create a preference centre (frequency, topics).
(c) Delivery rate > 97%, spam complaints < 0.1%, inbox placement in Gmail tests, click rate rising towards 2–3%, unsubscribe < 0.5%, revenue per email and email-attributed sales in GA4 rising.

</details>

**Scenario 2 – Strategy for a new online tutoring academy.** A Lahore academy sells O/A-Level online tutoring (PKR 12,000/month per subject). It has 2,500 subscribers from a free "past papers" download, a Shopify-like website and a team of two. Goal: 80 new enrolments in the next 3 months.

(a) Create one buyer persona. (b) Write two SMART goals. (c) Design a 5-email nurture sequence (timing, subject, purpose, CTA). (d) If the sequence reaches 2,400 delivered contacts with a 6% click rate per email and 4% of clickers enrol, how many enrolments come from one email? Is the 80-enrolment goal realistic from email alone?

<details><summary>✅ Solution</summary>

(a) **"Exam-Worried Parent Farah"** – 42, Lahore (Johar Town), child in O-Level year 2; goal: better grades in maths and physics; pains: tuition centre commute, traffic, inconsistent tutors; objections: online quality, tutor credentials, fees; reads email on phone 9–11 pm; message: "Top-graded tutors, from home, with weekly progress reports".
(b) "Enrol 80 new students by 31 January 2027 through the past-papers nurture sequence and webinar." · "Increase the nurture sequence's click rate from 4% to 6% by 15 December 2026 by testing personalised subject lines."
(c) Day 0: "Your past papers + a 2-minute study plan" – deliver the lead magnet, set expectations – CTA *Download*. Day 2: "Why most students lose marks in Paper 2" – educational value – CTA *Read the guide*. Day 4: "Meet the tutors (A* graduates)" – credibility – CTA *See profiles*. Day 7: "Free trial class this Saturday" – event – CTA *Book a seat*. Day 10: "Last 12 seats for January" – honest urgency, fees, FAQ – CTA *Enrol now / WhatsApp us*.
(d) 2,400 × 6% = 144 clicks; 144 × 4% ≈ **5.8 enrolments per email**. Even if every one of the 5 emails performed this well (≈ 29 enrolments, fewer in practice because the same people click repeatedly), email alone won't reach 80. The plan needs list growth (more lead magnets, social lead ads), the free trial class to raise conversion, and follow-up by WhatsApp/phone for interested parents.

</details>

**Scenario 3 – Reading a monthly report and using AI.** A fashion brand's monthly email report: Welcome series RPE PKR 85; newsletter RPE PKR 6, CTOR 8%; promotional emails RPE PKR 30, unsubscribe 0.9%; open rate rose from 32% to 48% after many subscribers switched to iPhones, but clicks stayed flat. The manager wants to use AI to "write all emails from now on".

(a) Explain the open-rate rise. (b) What should improve in the newsletter and promotional emails? (c) Write rules for using AI safely in this team (at least five).

<details><summary>✅ Solution</summary>

(a) Apple Mail Privacy Protection pre-loads emails, recording opens that didn't happen. Flat clicks show real engagement didn't change – stop using open rate as the main KPI.
(b) Newsletter: CTOR 8% is weak – one featured story/product, fewer links, one clear button, segment by interest (women's/men's/kids), test subject lines on clicks. Promotional: 0.9% unsubscribe suggests too many or irrelevant promotions – reduce frequency, send to segments based on browsing/purchase, add a preference centre, and give VIPs early access instead of blanket discounts.
(c) AI rules: (1) AI drafts, humans approve every email; (2) never paste customer data into public tools – use the ESP's built-in AI; (3) fact-check prices, dates, stock and claims; (4) edit into the brand voice and avoid generic phrases; (5) no invented reviews, scarcity or urgency; (6) A/B test AI suggestions against human versions on click rate; (7) check cultural and religious sensitivity, especially around Ramadan and Muharram; (8) keep a log of prompts that work.

</details>

---

<sub>Prepared by **Hamna Zahid Khan**, Junior Lecturer · Diploma in Digital Marketing</sub>
