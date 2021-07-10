# Concept

## Program Component Design

We decided to structure our solution into separate elements. The  elements should have their own communication interfaces to perform certain actions with the incoming HAZOP data.

- The Importer should take the HAZOPs, validate them and convert them into the RDF format. Finally, the created RDF-Graph with all metadata is stored either locally or uploaded on the Fuseki server.
- The Exporter should take the RDF-Graphs, parse the information and metadata, and store them in an Excel file.
- The TripleStore module is a Fuseki server API. It stores HAZOP data in RDF-Triples. Acting as a central database for machine-readable, completed HAZOP-Analysis with easy accessibility.

We planned to integrate the modules to allow simultaneously operation. So, we can perform the complete cycle of HAZOP format conversion from and to Excel format. 

![Program components](plantuml/program_components.png)

## User interaction scenario

Through the communication with the program the user should have the opportunity to load, read and store the HAZOPs in either format. 

The concept allows the interaction with up to two interfaces, the importer and exporter.

![User interaction](plantuml/user_interaction.png)

## Design Command Line Interface

We choose a Command Line Interface (CLI) as a fundament for our project. The CLI should be able to provide the complete functionality spectrum of the importer and exporter to the user.

The diagram below shows the functionalities available to the user.

![Design of Command Line Interface](plantuml/cli_design.png)
