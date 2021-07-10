# Abstract

A Hazard and Operability (HAZOP) study is a widely used safety related document in the process industry.
Designing such a document is a time and labor-intensive process. Because this document is hand crafted and written  
human error cannot be avoided. Computer-aided HAZOP systems can be used to support human experts.

This research paper describes a program which is able handle HAZOP data from an excel spreadsheet and thus 
provide such a much-needed computer-aided HAZOP system. With the described program an easy-to-handle back-and-forth 
conversion from HAZOP data(described in an excel spreadsheet) to RDF format is possible. Furthermore, a verification 
of the HAZOP data takes place and can also be configured. 

The program features a command line interface to give users an easy access to its software features.

Using our Importer interface, the user can import and validate incoming HAZOP data in 
Excel format and generate RDF graphs from it. They can be locally stored or uploaded to a Fuseki server.

Using our Exporter interface, the user can export RDF graphs containing HAZOP data to 
Excel format. The source for the Exporter interface can either be a locally stored RDF file or an RDF file 
stored on a Fuseki server.

The results of our findings show the largely increased compatibility of RDF files over excel files when storing, 
transforming, or manipulating HAZOP studies.


**Keywords:**  HAZOP to RDF transformation, computer-aided  HAZOP  studies,  safety  engineering  ontologies, 
handling HAZOP studies, EXCEL to RDF transformation, converting HAZOP studies