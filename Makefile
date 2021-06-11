ds:
	fuseki-server --update --mem /ds

cli:
	pip install --editable .

test_report:
	pytest --cov=src --cov-report term-missing

test_report_html:
	pytest --cov=src --cov-report html