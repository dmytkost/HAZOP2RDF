# Description

The project HAZOP2RDF is part of the course Projektierung von Automatisierungssystem. The main goal of the project is to transform the HAZOP data, which is stored in Excel format into RDF format and visa versa.

We implemented a command line interface (CLI) using ComplexCLI, which means CLI in CLI to combine all interfaces in a single interface.


# How to install

## Windows

1. `git clone https://github.com/DimakDev/hazop.git`
1. `cd hazop`
1. `python -m venv .\venv`
1. `venv\Scripts\activate`
1. `pip install --upgrade pip`
1. `pip install .`
1. `venv\Scripts\cli [cmd]` See [API](#API) section for commands to run
1. `pytest` See [Tests](#Tests) section for commands to run
1. `deactivate`

## macOS

1. `git clone https://github.com/DimakDev/hazop.git`
1. `cd hazop`
1. `python3 -m venv ./venv`
1. `source venv/bin/activate`
1. `pip install --upgrade pip`
1. `pip install .`
1. `cli [cmd]` See [API](#API) section for commands to run
1. `pytest` See [Tests](#Tests) section for commands to run
1. `deactivate`


# API

To see the list of available commands, run `cli`.

```cmd
Usage: cli [OPTIONS] COMMAND [ARGS]...

  Welcome to HAZOP CLI!

Options:
  --help  Show this message and exit.

Commands:
  exporter  Exporter interface
  importer  Importer interface
```

* `cli importer` - [Importer API](#importer)
* `cli exporter` - [Exporter API](#exporter)

## Importer

This API is an entry point for reading Excel data and building RDF-Graphs.

Command: `cli importer`

```cmd
Usage: cli cli [OPTIONS] COMMAND [ARGS]...

  Importer interface

Options:
  --help  Show this message and exit.

Commands:
  cmd-build-hazop-graphs  Build HAZOP graphs
  cmd-read-excel-data     Read excel data
  cmd-read-hazop-data     Read hazop data
```

* `cli importer cmd-read-excel-data`- to see the list of available Excel binary data
* `cli importer cmd-read-hazop-data`- to read the HAZOP data if its config is available
* `cli importer cmd-build-hazop-graphs`- to build HAZOP graphs, save it locally and upload to Fuseki server, if the server is up

## Exporter

This API exports RDF-Graphs to Excel either from local directory or from Fuseki server, if it is available.

Command: `cli exporter`

```cmd
Usage: cli cli [OPTIONS] COMMAND [ARGS]...

  Exporter interface

Options:
  --help  Show this message and exit.

Commands:
  cmd-export-graphs-from-fuseki-server
                                  Export HAZOP graphs...
  cmd-export-graphs-from-local-directory
                                  Export HAZOP graphs...
```

* `cli exporter cmd-export-graphs-from-local-directory`- to convert graphs from Turtle in Excel format and save it locally
* `cli exporter cmd-export-graphs-from-fuseki-server`- to get graphs from Fuseki server, if the server is running, convert it to Excel format and save it locally


# Tests

You can use the following commands to get quick results or customize the tests' configuration using pytest and pytest-cov flags:

* `pytest`- to run quick test
* `pytest --cov=src --cov-report term-missing`-to run a test with coverage report and missing statements
* `pytest --cov=src --cov-report html`-to run a test with coverage report and missing statements in html format (by default open htmlcov/index.html to see the results)