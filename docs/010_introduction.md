# Introduction

* Introduction

* abstract

This research paper describes a program that handles HAZOP data from an excel spreadsheet. 
With the described program an easy to handle back-and-fourth conversion from HAZOP data in excel Format 
to RDF format is possible. Furthermore a verification of the HAZOP data takes 
place and can also be configured. 

By analysing the needs of the faculty and working together with process control engineers we 
developed this application. 

Our solution features a command line interface to give users an easy access to our software.

Using our Importer interface the user can import and validate incoming HAZOP data in 
Excel format and generate RDF graphs from it. They can be locally stored or uploaded to a Fuseki server.

Using our Exporter interface the user can export RDF graphs containing HAZOP data to 
Excel format. The source for the Exporter interface can either be a locally stored RDF 
file or an RDF file stored on a Fuseki server.

As a result of our research we conclude that handling HAZOP data in RDF Format is much more convenient than 
working with excel data because the descriptive format largely increases compatibility between different 
modular plants.

* RDF problem description