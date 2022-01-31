import numpy as np
from sklearn import datasets
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt


COLORS = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
    "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]

words = []
pos = {}

with open("./most_freq_cs.tsv") as f:
    for line in f:
        word, pos_num = line.rstrip().split()
        words.append(word)
        pos[word] = int(pos_num)

embeddings_dic = np.load("./embeddings.npz")

matrix = np.stack([embeddings_dic[w] for w in words])

tsne = TSNE(n_components=2, random_state=0)
words_2d = tsne.fit_transform(matrix)

plt.figure(figsize=(6.4, 3))
plt.axis('off')

for word, vec in zip(words, words_2d):

    plt.scatter(vec[0], vec[1], s=0)
    color = COLORS[pos[word]]
    plt.annotate(
        word[1:], xy=vec,
        xytext=(5, 2),
        textcoords='offset points',
        ha='center',
        va='center',
        fontsize=5,
        bbox={"boxstyle": "square,pad=0.3",
              "fc": f"{color}aa",
              "lw": .1})


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=COLORS[1], lw=4),
                Line2D([0], [0], color=COLORS[2], lw=4),
                Line2D([0], [0], color=COLORS[3], lw=4),
                Line2D([0], [0], color=COLORS[4], lw=4),
                Line2D([0], [0], color=COLORS[5], lw=4),
                Line2D([0], [0], color=COLORS[6], lw=4),
                Line2D([0], [0], color=COLORS[7], lw=4),
                Line2D([0], [0], color=COLORS[8], lw=4)]

pos_names = ["Podstatná jm.", "Přídavná jm.", "Zájmena", "Číslovky",
             "Slovesa", "Příslovce", "Předložky", "Spojky"]

plt.legend(custom_lines, pos_names, fontsize=6)

plt.tight_layout()
#plt.show()
plt.savefig("tsne.pdf")
