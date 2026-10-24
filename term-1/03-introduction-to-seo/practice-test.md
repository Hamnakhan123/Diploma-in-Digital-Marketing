# 📝 Practice Test · Introduction to SEO

> 🏠 [Diploma in Digital Marketing](../../README.md) › [Term 1](../README.md) › [Introduction to SEO](README.md) › **Practice test**

20 multiple-choice questions and 3 practical scenarios. Try every question before opening the answers.

[⬅ Back to module overview](README.md) · [Next module ➡](../04-search-and-display-marketing/README.md)

---

## Part A · Multiple-choice questions

1. In which order does a search engine process web pages?
   a) Rank → crawl → index b) Crawl → index → rank c) Index → rank → crawl d) Crawl → rank → index
2. The query "daraz login" has which search intent?
   a) Informational b) Commercial c) Navigational d) Transactional
3. Showing Googlebot different content from what users see is called:
   a) Canonicalisation b) Cloaking c) Crawling d) Clustering
4. Which on-page element is **not** a direct ranking factor but strongly affects click-through rate?
   a) Title tag b) H1 heading c) Meta description d) Internal links
5. A recommended title tag length is roughly:
   a) 10–20 characters b) 50–60 characters c) 150–160 characters d) 250+ characters
6. Which backlink is most valuable to a Lahore bakery?
   a) 200 links from unrelated foreign directories b) A feature on a respected Lahore food blog c) A bought link on a gambling site d) A link hidden in a widget on 5,000 pages
7. An affiliate or paid link should be marked with:
   a) `rel="ugc"` b) `rel="canonical"` c) `rel="sponsored"` d) no attribute
8. Under mobile-first indexing, Google mainly uses which version of a page for ranking?
   a) Desktop b) Mobile c) Printer-friendly d) Cached
9. Which is **not** one of Google's three main local ranking factors?
   a) Relevance b) Distance c) Prominence d) Number of social media followers
10. NAP consistency refers to matching:
    a) Name, Address, Phone b) Network, Authority, PageRank c) News, Articles, Posts d) Name, Area, Price
11. Which keyword is a long-tail keyword?
    a) "shoes" b) "running shoes" c) "waterproof running shoes for women size 38" d) "nike"
12. Two pages on your site compete for the same keyword and neither ranks well. This is:
    a) Keyword cannibalisation b) Cloaking c) Link building d) Faceted navigation
13. Which free tool shows the real search queries, impressions and clicks for your own site?
    a) Semrush b) Google Search Console c) Moz Domain Authority d) Google Trends
14. A `Disallow: /cart/` line in robots.txt:
    a) removes cart pages from the index immediately b) asks crawlers not to crawl `/cart/` URLs c) deletes the cart d) adds cart pages to the sitemap
15. A product page moves permanently to a new URL. Which status code should the old URL return?
    a) 200 b) 301 c) 302 d) 404
16. Which Core Web Vitals result is "good"?
    a) LCP 3.8 s b) INP 450 ms c) CLS 0.05 d) LCP 5 s
17. Compared with typed queries, voice queries are typically:
    a) shorter keyword fragments b) longer, conversational questions, often local c) only about shopping d) never answered by featured snippets
18. Which Google system (2019) improved understanding of how words in a sentence relate to each other?
    a) Panda b) Penguin c) BERT d) PageRank
19. Google's position on AI-generated content is that:
    a) all AI content is penalised b) content is judged on helpfulness, but mass-producing low-value pages is spam c) AI content always ranks higher d) AI content must use special schema
20. In GA4, bounce rate is:
    a) the share of single-page sessions b) 100% minus engagement rate c) average engagement time d) clicks ÷ impressions

<details><summary>✅ Answers</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|
| 1 | b | 6 | b | 11 | c | 16 | c |
| 2 | c | 7 | c | 12 | a | 17 | b |
| 3 | b | 8 | b | 13 | b | 18 | c |
| 4 | c | 9 | d | 14 | b | 19 | b |
| 5 | b | 10 | a | 15 | b | 20 | b |

Q14: robots.txt controls crawling, not indexing – to keep a page out of results, allow crawling and use `noindex`. Q16: the "good" thresholds are LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1. Q20: GA4 defines bounce rate as the share of sessions that were **not** engaged, the opposite of engagement rate.

</details>

## Part B · Practical / scenario questions

**Scenario 1 – Audit a clinic's home page.** A dental clinic in Clifton, Karachi has this page head and opening:

```html
<title>Home</title>
<h1>Welcome</h1><h1>Our Services</h1>
<img src="IMG_0042.jpg">
<p>We are the best dentist best dentist Karachi best dentist Clifton. <a href="/book">Click here</a></p>
```

Its Google Business Profile is named "Smile Clinic Best Dentist Karachi", its Facebook page lists an old phone number, and it has 9 reviews with no replies. (a) List the on-page problems. (b) Rewrite the head and opening. (c) List the local SEO problems and fixes.

<details><summary>✅ Solution</summary>

(a) Generic title; no meta description; two H1s with no keywords; image with a meaningless file name and no `alt`; keyword stuffing; "Click here" anchor text.
(b)

```html
<title>Dentist in Clifton, Karachi | Smile Dental Clinic</title>
<meta name="description" content="Family and cosmetic dentistry in Clifton, Karachi. Check-ups, whitening and braces. Open Mon–Sat 10am–8pm. Book on WhatsApp today.">
<h1>Dentist in Clifton, Karachi</h1>
<img src="smile-dental-clinic-clifton-reception.webp" alt="Reception area of Smile Dental Clinic in Clifton" width="800" height="533">
<p>Smile Dental Clinic offers check-ups, whitening and braces for the whole family in Block 5, Clifton.
<a href="/book">Book your dental appointment</a></p>
```

(c) Keyword-stuffed GBP name breaks Google's guidelines → use the real name "Smile Dental Clinic". Inconsistent NAP → update the Facebook phone number and check every directory. Few reviews and no replies → ask each patient (QR code, WhatsApp link), reply to every review, never buy reviews. Also: correct category (Dentist), opening hours including holidays, photos, services with prices, `Dentist` structured data on the website.

</details>

**Scenario 2 – Keyword strategy and traffic forecast for a new store.** A new online store selling school uniforms in Pakistan has almost no backlinks. A keyword tool shows:

| Keyword | Volume | KD | Intent |
|---|---|---|---|
| school uniform | 12,000 | 78 | Mixed |
| buy school uniform online pakistan | 1,000 | 22 | Transactional |
| beaconhouse uniform price | 1,600 | 25 | Transactional |
| how to remove ink stains from white shirt | 2,400 | 30 | Informational |

(a) Which keywords should the store target first, and with what type of page? (b) The store ranks #9 for "beaconhouse uniform price". Using CTRs of 2% at #9 and 10% at #3, how many extra monthly clicks would reaching #3 bring? (c) Name two seasonal timing decisions using Google Trends.

<details><summary>✅ Solution</summary>

(a) Start with the low-KD, high-intent terms: "buy school uniform online pakistan" (category/home page) and "beaconhouse uniform price" (a school-specific product page with clear prices – only if the store genuinely stocks it). Use "how to remove ink stains from white shirt" for a helpful blog guide that links to the shirts – it builds topical relevance and earns links. Park "school uniform" (KD 78, mixed intent) until the site has authority.
(b) At #9: 1,600 × 2% = 32 clicks. At #3: 1,600 × 10% = 160 clicks. Extra = **128 clicks/month**.
(c) Interest peaks before the school year starts (around March–April and again before August), so publish and optimise pages several weeks before each peak; run content and promotions on stain removal and uniform care during term time.

</details>

**Scenario 3 – Fix a slow, unsatisfying service page.** A web-design agency's service page has:

- Search Console: 9,000 impressions, 140 clicks, average position 6
- GA4: engagement rate 38%, average engagement time 22 s, 3 enquiries a month
- PageSpeed Insights (mobile, field data): LCP 4.3 s, INP 180 ms, CLS 0.28
- robots.txt contains `Disallow: /portfolio/` and the portfolio page is linked from the service page

(a) Calculate CTR and diagnose each problem. (b) Give a prioritised fix list covering technical, content, UX and voice/AI. (c) Design one A/B test for the page and explain how to keep it SEO-safe.

<details><summary>✅ Solution</summary>

(a) CTR = 140 ÷ 9,000 × 100 = **1.6%** – low for position 6, so the title and description are weak. LCP 4.3 s is **poor** (> 4 s) and CLS 0.28 is **poor** (> 0.25); INP is good. Engagement of 38% and 22 s suggest the page doesn't deliver what searchers want. Blocking `/portfolio/` stops Google crawling the agency's strongest proof of expertise.
(b) 1. **Technical:** remove `Disallow: /portfolio/`; compress and preload the hero image, use WebP, better caching/CDN to fix LCP; set width/height on images and reserve space for banners to fix CLS. 2. **Content/intent:** put a one-line value statement, starting prices, three portfolio examples and a "Get a free quote" button above the fold; add client results and team credentials (E-E-A-T). 3. **On-page:** rewrite the title ("Web Design in Karachi | Packages from PKR 60,000 – AgencyName") and meta description with benefits; add `Service`/`LocalBusiness` schema. 4. **UX:** short 4-field form, WhatsApp button, reviews near the CTA. 5. **Voice/AI:** an FAQ answering "How much does a website cost in Karachi?" and "How long does it take?" in ~30-word answers.
(c) Test: version A (current form at the bottom) vs version B (4-field form beside the headline). Metric: enquiry conversion rate, run for at least two full weeks. Keep it SEO-safe: same URL with a testing tool, or variant URLs with `rel="canonical"` to the original and 302 redirects; never show Googlebot a different version; end the test and roll out the winner.

</details>

---

<sub>Prepared by **Hamna Zahid Khan**, Junior Lecturer · Diploma in Digital Marketing</sub>
