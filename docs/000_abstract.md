\newpage

# Abstract

A Hazard and Operability (HAZOP) study is a widely used safety related document in the process manufacturing industry. Creating such a document is a time and labor-intensive process. This document is hand-crafted and written, thus human error cannot be avoided. To avoid such errors computer-aided HAZOP systems can be used to support human experts.

In this research paper, we propose a key part of such a computer aided HAZOP system. This key part is able to handle HAZOP data in the Excel and RDF format and allows for an easy-to-handle, back-and-forth transformation. Furthermore, a verification of the HAZOP data is integrated and can be configured further.

The idea for this system has its root in a college project task. After choosing the task to create such a "HAZOP transformation program" which should include an importer, exporter and a Triplestore we quickly began to do research about the main elements of the task. 

We started by reading about how HAZOP studies are conducted and how ontologies can be formed with RDF. After the first success with a powerful python library named rdf2lib we kept adding on elements like a verification algorithm for the Excel HAZOP, a command line interface for easy access to the components of our software and a Fuseki Server integration for allowing a better storage of imported HAZOP RDF files.

Our findings show that our proposed computer-aided HAZOP system can effectively create RDF ontologies for manually created HAZOP studies. These RDF ontologies, not only enable better storage for HAZOP studies, but they are also machine readable, queryable, and therefore allow for further automation.

**Keywords:** HAZOP to RDF transformation, computer-aided HAZOP studies, safety engineering ontologies, handling HAZOP studies, Excel to RDF transformation, converting HAZOP studies
