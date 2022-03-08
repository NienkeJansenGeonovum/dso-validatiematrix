all: Validatiematrix.md
clean:
	rm -f Validatiematrix.md

Validatiematrix.md: Validatiematrix2markdown.py Validatiematrix.xlsx
	python3 ./Validatiematrix2markdown.py Validatiematrix.xlsx > Validatiematrix.md
