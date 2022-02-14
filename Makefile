SHELL=bash
NAME=main
LATEX=xelatex
SVGFILES := $(wildcard img/*.svg)
# GNUFILES := $(wildcard plots/*.gnu)
#PY_PLOTS := $(wildcard plots/*.py)

FILES=$(NAME).tex odkazy.bib $(SVGFILES:%.svg=%.pdf) #$(PY_PLOTS:%.py=%.pgf) #
all: $(NAME).pdf

$(NAME).pdf: $(FILES)
	latexmk -pdflatex="$(LATEX) %O %S" -pdf -dvi- -ps- -halt-on-error $(NAME)

watch:
	latexmk -pdflatex="$(LATEX) %O %S" -pdf -dvi- -ps- -interaction=nonstopmode -synctex=1 -pvc $(NAME)

view:
	xdg-open $(NAME).pdf

force: $(FILES)
	latexmk -pdflatex="$(LATEX) %O %S" -pdf -dvi- -ps- $(NAME)

clean:
	rm -f $(NAME).{aux,bbl,log,out,pdf}
	rm -r html

%.pdf: %.svg
	inkscape -A $*.pdf $*.svg

%.pgf: %.py
	PYTHONPATH=${PWD}/plots:${PYTHONPATH} python3 $*.py
