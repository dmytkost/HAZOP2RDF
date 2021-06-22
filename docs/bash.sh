# required Pandoc, TeX Live

pandoc \
	--bibliography=bibliography.bib \
	--metadata-file=metadata.yaml \
	*.md -o HAZOP2RDF_report.pdf \
	--from=markdown \
	--template=eisvogel.tex \
	--citeproc \
	--listings \
	--top-level-division=chapter \