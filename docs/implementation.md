## Implementation
    
We implemented the Command Line Interface using Click package. It is highly configurable and can build very complex applications. The ComplexCLI utility, we used in our project, combines multiple interfaces in a single Command Line Interface.

The following diagram shows the structure of the Command Line Interface. It contains Importer and Exporter interface, which use services. The services contain utilities needed for the interfaces to perform lower level actions.

![](plantuml/cli_structure.png)

Using the Command Line Interface users can interact with our software.
     
Using our Importer interface the user can import and validate incoming HAZOP data in Excel format and generate RDF
graphs from it. They can be locally stored or uploaded to a Fuseki server. 
     
Using our Exporter interface the user can export RDF graphs containing HAZOP data to Excel format. The source for the
Exporter interface can either be a locally stored RDF file or an RDF file stored on a Fuseki server.
    
### Importer interface
    
The main purpose of the Importer interface is to build an RDF graph from incoming Excel data. To build an RDF graph, we carefully read the incoming HAZOP Data and validate it. To validate the data correctly we implemented a config file, which stores all the metadata needed to describe the importing and validating process.

The main command of the Importer interface is cmd-build-hazop-graphs, which reads the HAZOP data stored in a local directory and transforms it to an RDF graph. The graph can be consequentially stored locally or uploaded to a Fuseki server. The two other commands cmd-read-excel-data and cmd-read-hazop-data make it possible for the user to perform steps of the main importer command individually.

The installation of a Fuseki server is optional. If the server is offline, the files cannot be uploaded to the server resulting in an error message which is displayed to the user.

### Sequence Diagram: Importer interface

![](plantuml/sequence_importer.png)
    
### Exporter interface

After the HAZOP data was successfully imported and stored, the user can convert the RDF graph to Excel format again.

There are two main commands in the Exporter interface for the users to interact with. The user can either export data from an RDF file located in a local directory or from a file located online on a Fuseki server. For the successful export from the Fuseki Server the server needs to be running.

As a result, the RDF graphs will be stored locally in Excel format again.

### Sequence Diagram: Exporter interface

![](plantuml/sequence_exporter.png)
    
### Remarks
    
We developed the HAZOP2RDF Project with version control on GitHub. The program is available for Windows and macOS. We also included a detailed installation guide in the documentation.