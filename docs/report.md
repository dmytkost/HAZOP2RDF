# Projectreport HAZOP2RDF

- Dmytro Kostiuk
- Marcus Rothhaupt
- Artan Kabashi
- Vincenz Forkel
- project supervisor: Anselm Klose
- Herr Prof. Dr.-Ing. habil. Leon Urbas

## Table of contents

- Abstract(Marcus)
- Problem Analysis(Marcus)
- Concept Development(main part)
- Implementation(Dima)
- Validation(Dima)
- Summary and Outlook
- Sources
- Appendix

## Abstract

* Introduction to
* abstract of the project
* RDF problem description

## Problem Analysis

* Why Hazop 2 RDF?
* When can it help?
* Whom can it help?

## Concept Development(main part)

* How did we solve the problem(framework)
* How did we get to the concept?
* Why did we choose this method of implementing

## Implementation
    
We implemented an importer and exporter interface for the HAZOP2RDF project in Python. Using a command line 
interface users can interact with our software. 
     
Using our Importer API the user can import and validate incoming HAZOP data in Excel format and generate RDF 
graphs from it. They can be locally stored or uploaded to a Fuseki server. 
     
Using our Exporter API the user can export RDF Graphs containing HAZOP data to Excel format. The source for the 
Exporter API can either be a locally stored RDF file or an RDF file stored on a Fuseki server.
    
### Importer API
    
The main purpose of the Importer API is to build an RDF Graph from incoming Excel data. In order to build an 
RDF graph, we carefully read the incoming HAZOP Data and validate it. In order to validate correctly we 
implemented a config file, which stores all the metadata needed to describe the importing and validating process.
     
The main command of the Importer API is cmd-build-hazop-graphs, which reads the HAZOP data stored in a local 
directory and transforms it to an RDF Graph. The graph can be consequentially stored locally or uploaded to a 
Fuseki server. The two other commands cmd-list-excel-data and cmd-read-hazop-data make it possible for the user to 
perform steps of the main importer command individually.
     
The installation of a Fuseki server is optional. If the server is offline, the files can not be uploaded to the 
server resulting in an error message which is displayed to the user.
     
### Sequence Diagram: Importer API

* Diagram
    
### Exporter API
    
After the HAZOP data was successfully imported and stored, the user can convert the RDF Graph to Excel format again. 
     
There are two main commands in the Exporter API for the users to interact with. The user can either export data from 
an RDF file located in a local directory or from a file located online on a Fuseki server. In order for the export 
from Fuseki Server to function the server needs to be running and RDF Graphs need to be available. 
     
As a result the RDF Graphs will be stored locally in Excel format again.
     
### Sequence Diagram: Exporter API

* Diagram
    
### Remarks
    
We developed the HAZOP2RDF Project with version control on the online platform GitHub. The program is available for 
Windows and macOS platforms. We also included a detailed installation guide in the documentation on the GitHub platform.

## Validation

* Tests
* Measurements how to validate hazop data

## Summary and Outlook

* Discussion
* Future Work
* Future Projects
* Problems to be solved

## User manual for HAZOP2RDF

* HOW to install
* From github

## Sources

* HAZOP source
* Refernezimplementationen beachten und zitieren

## Appendix
* additional graphs, pictures...

--- END OF REPORT ---

//additional info
- source code digital abgeben
- zip im OPAL

// Diagrams:

* don't put diagrams in appendix
* [PlantUML](https://plantuml.com)
* [Mermaid](https://mermaid-js.github.io/mermaid/#/)
* [Guide for better Flowcharts](https://www.smartdraw.com/flowchart/flowchart-tips.htm)

//Abschlusspräsentation
- Überblick über problem(noch kürzer)
- Programm vorstellen (main part)
- Ergebnisse gut darstellen
- Diagramme nutzen(nicht zu groß, muss lesbar sein)
- Was ist der Mehrwert?
- Einfach und Klar erkennbar was der Mehrwert ist
- Mehr bilder als text

// TODO
- ontologie der importierten Hazop (png) an Anselm 
