# CAE-PA

## How to install
1. `git clone https://github.com/DimakDev/hazop.git`
1. `cd hazop`
1. `python3 -m venv ./venv`
1. `source venv/bin/activate`
1. `pip install .`
1. `cli [cmd]` See [API](#API) section for commands to run.
2. `deactivate`

## API
Below is a list of the currently support API commands.

* [`cli importer`](#importer) - Importer functions.

### Importer (outdated)
This interface is made as an entry point for reading data and making RDF-Graphs. Below you can see the command's description.

```cmd
Usage: cli cli [OPTIONS] COMMAND [ARGS]...

  Entry point for reading data and making RDF-Graphs

Options:
  --help  Show this message and exit.

Commands:
  list-excel-data  List Excel data
  make-rdf-graphs  Make RDF-Graphs
  read-hazop-data  Read HAZOP data
 ```

To use a function from the commands list use: ***`cli importer list-excel-data`***
