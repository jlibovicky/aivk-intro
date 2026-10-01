#!/bin/bash

for ARXIV in AI CL; do
    for Y in {2000..2026}; do
        for M in {01..12}; do
            curl https://arxiv.org/list/cs.${ARXIV}/${Y}-${M} | \
                grep 'Total of' | head -n1 | \
                sed 's/^.*Total of //;s/ .*//' | sed "s/^/${M}\/${Y},/"
                sleep 1s
        done
    done | tee -a arxiv_stats_${ARXIV}.csv
done