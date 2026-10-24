# 📝 Practice Test · Essentials of Website Design and Development

> 🏠 [Diploma in Digital Marketing](../../README.md) › [Term 1](../README.md) › [Essentials of Website Design and Development](README.md) › **Practice test**

20 multiple-choice questions and 3 practical scenarios. Try every question before opening the answers.

[⬅ Back to module overview](README.md) · [Next module ➡](../03-introduction-to-seo/README.md)

---

## Part A · Multiple-choice questions

1. Which line tells the browser to render a page in HTML5 standards mode?
   a) `<html5>` b) `<!DOCTYPE html>` c) `<meta html="5">` d) `<head>`
2. Which of these is a void (standalone) tag?
   a) `<p>` b) `<li>` c) `<img>` d) `<a>`
3. Which meta tag makes a page scale correctly on phones?
   a) `charset` b) `description` c) `viewport` d) `keywords`
4. Which tag marks text as strongly important, not just bold?
   a) `<b>` b) `<strong>` c) `<mark>` d) `<big>`
5. To show `<h1>` as visible text on a page, you write:
   a) `<h1>` b) `&lt;h1&gt;` c) `"h1"` d) `\h1`
6. From `blog/post.html`, the relative link to `index.html` in the root folder is:
   a) `index.html` b) `/blog/index.html` c) `../index.html` d) `./blog/index.html`
7. A paid influencer link should carry which `rel` value?
   a) `ugc` b) `sponsored` c) `noopener` d) `author`
8. `href="services.html#pricing"` links to:
   a) a file named pricing b) the element with `id="pricing"` on services.html c) a pricing website d) the top of services.html
9. Which part of a URL tells analytics that a visit came from a newsletter?
   a) `#newsletter` b) `utm_source=newsletter` c) `rel="newsletter"` d) `target="newsletter"`
10. The recommended way to style a 50-page website is:
    a) Inline styles b) An internal `<style>` on each page c) One external style sheet d) `<font>` tags
11. Which selector has the highest specificity?
    a) `nav ul li a` b) `.menu .link` c) `#main` d) `a:hover`
12. Two rules with equal specificity set different colours on the same element. Which applies?
    a) The first one b) The last one c) Neither d) The browser picks randomly
13. Which property is inherited by child elements?
    a) `padding` b) `border` c) `font-family` d) `margin`
14. `padding: 10px 20px;` means:
    a) 10px left/right, 20px top/bottom b) 10px top/bottom, 20px left/right c) 10px top, 20px bottom d) 10px all sides
15. A box has `width: 200px; padding: 10px; border: 2px` and default `box-sizing`. Its visible width is:
    a) 200px b) 212px c) 224px d) 220px
16. Which `display` value lays out children in a single flexible row?
    a) `block` b) `inline` c) `flex` d) `none`
17. A "Chat on WhatsApp" button that stays in the corner while scrolling uses:
    a) `position: static` b) `position: relative` c) `position: fixed` d) `float: right`
18. Which element is meant for self-contained content such as a product card or blog post?
    a) `<aside>` b) `<article>` c) `<span>` d) `<nav>`
19. Which form method should send a customer's phone number and email?
    a) `get` b) `post` c) `link` d) `href`
20. White text on a yellow `#ffb703` button has a contrast ratio of about 1.75:1. This:
    a) passes WCAG AA b) fails WCAG AA – use dark text c) only matters for print d) improves conversion

<details><summary>✅ Answers</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|
| 1 | b | 6 | c | 11 | c | 16 | c |
| 2 | c | 7 | b | 12 | b | 17 | c |
| 3 | c | 8 | b | 13 | c | 18 | b |
| 4 | b | 9 | b | 14 | b | 19 | b |
| 5 | b | 10 | c | 15 | c | 20 | b |

Q11: `#main` = (1,0,0) beats `.menu .link` (0,2,0), `a:hover` (0,1,1) and `nav ul li a` (0,0,4). Q15: 200 + 2×10 + 2×2 = 224px. Q20: WCAG AA needs 4.5:1 for normal text.

</details>

## Part B · Practical / scenario questions

**Scenario 1 – Fix a broken landing page head.** A clothing brand's landing page ranks poorly, looks tiny on phones and shows "Ã©" instead of "é". Its head is:

```html
<html>
<head>
  <title>Home</title>
</head>
```

(a) Name the four problems. (b) Rewrite the head correctly for a page selling winter shawls in Lahore.

<details><summary>✅ Solution</summary>

(a) No doctype or `lang`; no `charset` (garbled characters); no viewport tag (tiny on phones); a generic title and no meta description (weak SEO and search snippet).
(b)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pure Wool Winter Shawls | Free Delivery in Lahore</title>
  <meta name="description" content="Hand-woven wool shawls from PKR 4,500. Free delivery across Lahore in 48 hours.">
  <link rel="stylesheet" href="css/style.css">
</head>
```

</details>

**Scenario 2 – Debug the CSS and the layout.** A developer complains: "My `.btn { background: green; }` rule doesn't work, the button stays blue." The style sheet also contains `#hero a { background: blue; }` and the button is a link inside `<section id="hero">`. Separately, three product cards set to `width: 33.33%; padding: 20px; border: 1px solid` wrap onto two lines. (a) Explain both problems. (b) Give a fix for each.

<details><summary>✅ Solution</summary>

(a) `#hero a` has specificity (1,0,1), which beats `.btn` (0,1,0), so blue wins regardless of order. The cards use the default `content-box`, so each is 33.33% **plus** 40px padding and 2px border – together they exceed 100% and wrap.
(b) Raise specificity to match the context, e.g. `#hero .btn { background: green; }` (1,1,0), or better, remove the ID selector and style with classes only; avoid `!important`. Add `* { box-sizing: border-box; }` (or use `display: flex; gap: 1rem;` with `flex: 1` on each card).

</details>

**Scenario 3 – Design a lead form and measure it.** A driving school's landing page gets 3,000 visits a month and 60 enquiries from a 12-field form (including address, CNIC, date of birth and "how did you hear about us"). (a) Calculate the current conversion rate. (b) Redesign the form: list the fields you would keep, their input types and validation. (c) If conversion rises to 4%, how many extra enquiries per month is that? (d) How would you know which ad brought each enquiry?

<details><summary>✅ Solution</summary>

(a) 60 ÷ 3,000 × 100 = **2%**.
(b) Keep only what's needed for a first call: Name (`type="text"`, `required`, `autocomplete="name"`), Mobile (`type="tel"`, `required`, `pattern="03[0-9]{9}"`), Area (`<select>` of branches, `required`), Preferred course (radio: Car / Motorbike), consent checkbox (`required`). Collect CNIC, address and date of birth later at enrolment. Button text: "Book my free trial lesson". Use `<label for>` on every field and `method="post"`.
(c) 3,000 × 4% = 120 → **60 extra enquiries** per month.
(d) Use **UTM-tagged links** on each ad and pass `utm_source`/`utm_campaign` into **hidden inputs** so every submission records its source; report enquiries by source in analytics.

</details>

---

<sub>Prepared by **Hamna Zahid Khan**, Junior Lecturer · Diploma in Digital Marketing</sub>
