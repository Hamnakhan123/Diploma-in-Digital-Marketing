# "Customers who bought this also bought": an item-to-item recommender (collaborative filtering)
# using cosine similarity. Prepared by Hamna Zahid Khan, Junior Lecturer. Fictional baskets of an online bookshop.
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FIRE, GOLD, VIOLET, EMBER, TEXT = "#0A0716", "#FF6B1A", "#FCD34D", "#A78BFA", "#F43F5E", "#F5EEFF"

items = ["Urdu novel", "Poetry collection", "Kids story book", "Colouring book",
         "Exam guide", "Past papers", "Cookbook", "Islamic history"]
baskets = [  # one row per customer, 1 = bought
    [1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0],
]
M = np.array(baskets, dtype=float)
norms = np.linalg.norm(M, axis=0)
sim = (M.T @ M) / np.outer(norms, norms)
np.fill_diagonal(sim, 0)

print("Item-to-item similarity (cosine, 0 = never together, 1 = always together):")
print(" " * 18 + " ".join(f"{i[:6]:>6}" for i in items))
for i, row in zip(items, sim):
    print(f"{i:<18}" + " ".join(f"{v:6.2f}" for v in row))

def recommend(owned, k=2):
    scores = sim[:, owned].sum(axis=1)
    scores[owned] = -1
    return [(items[j], round(float(scores[j]), 2)) for j in np.argsort(-scores)[:k]]

for who, owned in [("Ayesha (bought Urdu novel)", [0]), ("Hamza (bought Exam guide)", [4]),
                   ("Fatima (bought Kids story book + Cookbook)", [2, 6])]:
    print(f"\n{who} -> recommend {recommend(owned)}")

fig, ax = plt.subplots(figsize=(7.5, 5.6), facecolor=BG); ax.set_facecolor(BG)
im = ax.imshow(sim, cmap="inferno", vmin=0, vmax=1)
ax.set_xticks(range(len(items))); ax.set_xticklabels(items, rotation=40, ha="right", color=TEXT, fontsize=8)
ax.set_yticks(range(len(items))); ax.set_yticklabels(items, color=TEXT, fontsize=8)
for i in range(len(items)):
    for j in range(len(items)):
        if sim[i, j] > 0:
            ax.text(j, i, f"{sim[i, j]:.2f}", ha="center", va="center", fontsize=7, color=BG if sim[i, j] > 0.6 else TEXT)
ax.set_title("Which books are bought together? (cosine similarity)", color=GOLD)
cb = fig.colorbar(im, ax=ax, fraction=0.046); cb.ax.tick_params(colors=TEXT)
fig.text(0.99, 0.01, "Prepared by Hamna Zahid Khan · fictional baskets", color=TEXT, alpha=0.5, ha="right", fontsize=7)
plt.tight_layout(); plt.savefig("session-03_similarity_heatmap.png", dpi=110, facecolor=BG)
print("\nSaved session-03_similarity_heatmap.png")
