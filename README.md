# CAE-PA

## How to install
1. `git clone https://github.com/DimakDev/hazop.git`
1. `cd hazop`
1. `python3 -m venv ./venv`
1. `source venv/bin/activate`
1. `pip install .`
1. `cli [cmd]` See [API](#API) section for commands to run.
1. `pytest` Run tests
1. `deactivate`

## API

To see the list of available commands, run `cli`.

```cmd
Usage: cli [OPTIONS] COMMAND [ARGS]...

  Welcome to HAZOP CLI!

Options:
  --help  Show this message and exit.

Commands:
  exporter  Exporter interface for RDF-Graphs
  importer  Entry point for reading data and making RDF-Graphs
```

* `cli importer` - [Importer API](#importer)
* `cli exporter` - [Exporter API](#exporter)

### Importer

This API is an entry point for reading Excel data and building RDF-Graphs

Command: `cli importer`

```cmd
Usage: cli cli [OPTIONS] COMMAND [ARGS]...

  Entry point for reading data and making RDF-Graphs

Options:
  --help  Show this message and exit.

Commands:
  cmd-build-hazop-graphs  Make RDF-Graphs
  cmd-list-excel-data     List Excel data
  cmd-read-hazop-data     Read HAZOP data
 ```

* `cli importer cmd-list-excel-data`- to see the list of available Excel binary data
* `cli importer cmd-read-hazop-data`- to read the HAZOP data if its config is available
* `cli importer cmd-build-hazop-graphs`- to build HAZOP graphs, save it locally and upload to Fuseki server, if the server is up

### Exporter

This API exports RDF-Data either from local directory or from Fuseki server, if it is available.

Command: `cli exporter`

```cmd
Usage: cli cli [OPTIONS] COMMAND [ARGS]...

  Exporter interface for RDF-Graphs

Options:
  --help  Show this message and exit.

Commands:
  cmd-export-graphs-from-fuseki-server
                                  Export RDF-Graphs from Fuseki...
  cmd-export-graphs-from-local-directory
                                  Export RDF-Graphs from local...
```

* `cli exporter cmd-export-graphs-from-local-directory`- to convert graphs from Turtle in Excel format and save it locally
* `cli exporter cmd-export-graphs-from-fuseki-server`- to get graphs from Fuseki server, if the server is running, convert it to Excel format and save it locally