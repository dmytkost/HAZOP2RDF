# required: pandoc, basictex

pandoc:
	pandoc --standalone \
	--citeproc \
	--strip-comments \
	--bibliography=references.bib \
	--metadata-file=metadata.yaml \
	*.md -o HAZOP2RDF_report.pdf