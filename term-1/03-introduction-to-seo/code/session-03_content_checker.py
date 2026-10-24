# SEO-friendly content checker: keyword placement, density and readability.
import re

keyword = "solar panels karachi"
title = "Solar Panels in Karachi: 2026 Price Guide for Homes"
text = """Solar panels in Karachi can cut a home's electricity bill sharply.
This guide explains prices, sizes and net metering. A 5 kW system suits most
three-bedroom homes. Ask installers for a written warranty. Compare at least
three quotes before you pay a deposit. Net metering lets you sell spare units
back to K-Electric. Clean the panels every two weeks because dust lowers output."""

words = re.findall(r"[A-Za-z0-9']+", text)
sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
kw_words = keyword.split()

def contains_kw(s):
    s = s.lower()
    return all(w in s for w in kw_words)

first_100 = " ".join(words[:100])
avg_sentence = len(words) / len(sentences)
# density = how often the main keyword word appears per 100 words
main_hits = sum(1 for w in words if w.lower() == "solar")
density = main_hits / len(words) * 100

print(f"Words: {len(words)}, sentences: {len(sentences)}")
print(f"Keyword in title:          {contains_kw(title)}")
print(f"Keyword in first 100 words: {contains_kw(first_100)}")
print(f"Average sentence length:   {avg_sentence:.1f} words ({'easy' if avg_sentence <= 20 else 'hard'} to read)")
print(f"'solar' density:           {density:.1f}% ({'natural' if density <= 3 else 'possible stuffing'})")
