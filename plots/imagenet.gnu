#!/usr/bin/gnuplot

set term lua tikz latex createstyle size 13,7
set output "plots/imagenet.tex"

set boxwidth 0.75
set style fill solid
set key off
set xrange [2010.2:2018.4]
set xtics autofreq 2011, 1, 2017
set xtics scale 0
set yrange [0:0.30]
set format y "%.2f"
set ytics scale 0.15
set ylabel "5-best error rate" offset -1.5
plot "plots/imagenet.dat" using 1:2 with boxes linecolor rgb "#1d3075", \
     "" u 1:2:3 with labels offset char -4.0,1 left, \
     "" u 1:2:4 with labels offset char -4.0,2.2 left, \
     "" u 1:2:5 with labels offset char -4.0,3.4 left
