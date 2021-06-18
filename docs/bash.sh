# required Pandoc, TeX Live

pandoc	--bibliography=bibliography/bibliography.bib \
		--metadata-file=metadata/metadata.yaml \
		markdown/*.md -o HAZOP2RDF_report.pdf \
		--from=markdown \
		--template=template/eisvogel.tex \
		--citeproc \
		--listings \
		--top-level-division=chapter \