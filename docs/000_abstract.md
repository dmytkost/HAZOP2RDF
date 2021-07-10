# Abstract

A Hazard and Operability (HAZOP) study is a widely used safety related document in the process manufacturing industry.
Creating such a document is a time and labor-intensive process. This document is hand-crafted and written,  
thus human error cannot be avoided. In order to avoid such errors computer-aided HAZOP systems can be used to support human experts.

In this research paper, we propose such a computer aided HAZOP system.
The system we propose is able to handle HAZOP data in the Excel and RDF format and allows for an easy-to-handle, back-and-forth 
conversion. Furthermore, a verification of the HAZOP data is integrated and can be configured further.

The program features a command line interface which allows access to an Importer and Exporter. The Importer can be used to import and validate 
incoming HAZOP data in Excel and generate RDF graphs from it, these can then be stored locally or uploaded to a 
Fuseki server. The Exporter can export RDF graphs containing HAZOP data to Excel. The RDF file for the Exporter can either be locally stored or on a Fuseki server.

Our findings show that our proposed computer-aided HAZOP system is able to effectivly create RDF ontologies for manually created HAZOP studies.
These RDF ontologies, not only enable better storage for HAZOP studies, they are also machine readible, queriable, and therefore allow for further automation.

**Keywords:**  HAZOP to RDF transformation, computer-aided  HAZOP  studies,  safety  engineering  ontologies, 
handling HAZOP studies, Excel to RDF transformation, converting HAZOP studies
