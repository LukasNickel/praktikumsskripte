all: build/Protokoll999.tex

build/plot999-1.pdf: plot999-1.py data999.txt |build
	python plot999-1.py #savefig('build/plot999-1.pdf')

build/Protokoll999.pdf: Protokoll999.tex build/plot999-1.pdf |build
	lualatex --output-directory=build Protokoll999.tex

build:
	mkdir -p build
	
.PHONY: all clean
