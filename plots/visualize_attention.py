#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


with open("./attention.tsv") as f:
    for i, line in enumerate(f):
        src_str, tgt_str, attention_str = line.strip().split("\t")
        src = src_str.split() + ["</s>"]
        tgt = tgt_str.split() + ["</s>"]

        # shape is src x tgt
        attention = np.array([
            [float(x) for x in row.split(",")]
            for row in attention_str.split()])

        plt.imshow(attention.T, cmap='hot', interpolation='nearest')

        plt.xlabel("→ Vygenerovaný překlad →", weight="bold")
        plt.ylabel("← Zdrojová věta ←", weight="bold")

        plt.yticks(range(len(src)), src)
        plt.xticks(range(len(tgt)), tgt, rotation=45, ha="right", va="top")

        plt.tight_layout()
        plt.show()
        plt.savefig(f"attention{i + 1}.pdf")

