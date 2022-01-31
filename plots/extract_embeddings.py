import yaml
import numpy as np

with open("vocab.encs.yml") as f:
    nmt_vocab = yaml.load(f)

variables = dict(
    np.load("/mounts/Users/cisintern/libovicky/work/char_level_marian/models/encs_bpew32k/model.npz"))
embeddings = variables['Wemb']

selected_embeddings = {}
with open("./most_freq_cs.tsv") as f:
    for line in f:
        word, _ = line.split()
        if word in nmt_vocab:
            selected_embeddings[word] = embeddings[nmt_vocab[word]]

np.savez("embeddings.npz", **selected_embeddings)

