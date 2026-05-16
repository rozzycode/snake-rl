PDF=main.pdf
TEX=main.tex

all:
	pdflatex -interaction=nonstopmode $(TEX)
	biber main
	pdflatex -interaction=nonstopmode $(TEX)
	pdflatex -interaction=nonstopmode $(TEX)

clean:
	rm -f *.aux *.bbl *.bcf *.blg *.log *.out *.run.xml *.toc *.lof *.lot $(PDF)
