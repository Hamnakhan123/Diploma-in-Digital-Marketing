# A tiny search engine: crawl (a dict of pages), index (inverted index), rank (TF-IDF style score).
import math, re
from collections import Counter, defaultdict

pages = {
    "/biryani-recipe":   "Karachi biryani recipe step by step biryani masala rice chicken",
    "/best-biryani-khi": "Best biryani restaurants in Karachi ranked by price and taste biryani",
    "/nihari-guide":     "Nihari guide Karachi breakfast slow cooked beef nihari",
    "/rice-types":       "Basmati rice types for pulao and biryani cooking guide",
}

def tokens(text):
    return re.findall(r"[a-z]+", text.lower())

# 1) Indexing: word -> {page: count}
index = defaultdict(dict)
for url, text in pages.items():
    for word, n in Counter(tokens(text)).items():
        index[word][url] = n
print("Index entries for 'biryani':", index["biryani"])

# 2) Ranking: sum of tf * idf for each query word
def search(query):
    N = len(pages)
    scores = Counter()
    for word in tokens(query):
        postings = index.get(word, {})
        if not postings:
            continue
        idf = math.log((N + 1) / len(postings)) + 1   # rare words count more
        for url, tf in postings.items():
            scores[url] += tf * idf
    return scores.most_common()

for q in ["best biryani karachi", "nihari"]:
    print(f"\nQuery: {q}")
    for rank, (url, s) in enumerate(search(q), 1):
        print(f"  {rank}. {url:18} score={s:.2f}")
