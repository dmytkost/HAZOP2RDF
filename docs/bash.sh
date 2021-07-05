#!/bin/bash

pandoc \
	--bibliography=bibliography.bib \
	--metadata-file=metadata.yaml \
	--pdf-engine=xelatex \
	*.md -o HAZOP2RDF_report.pdf \
	--from=markdown \
	--template=eisvogel.tex \
	--citeproc \
	--listings \
