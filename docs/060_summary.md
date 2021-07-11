# Summary

Our software lays the groundwork for our vision of a modular HAZOP for a modular plant. It is easily integratable into the traditional HAZOP workflow, by allowing the engineering team to continue conducting the HAZOP studies in Excel. However, it solves the many follow up problems associated with that format. The user is able to overcome the storage and reusability issues, while also having his HAZOP studies available in a machine readable format. The queriable nature of the RDF format allows for the seperate future building of a HAZOP-to-HAZOP interface.

The user is provided with a Command Line Interface that enables the input validation of Excel HAZOP data and the lossless back-and-forth transformation of Excel and RDF formats.
A possible storage solution, in the form of a Fuseki server, is also provided. Alternatively, all work can be conducted in the local directory.


## Future Work

The application provides essential functionality for the HAZOP transformation. There is still room left for future adoptions, tests and experiments.

* The import of the HAZOP data can be improved and adopted with fixed constrains. It can be conditional statements, which parse different shapes of the incoming data and serve them for the RDF transformation.

* Fuseki servers offer HTTP access. Currently, we use a set of command line scripts[^2] to work with SPARQL. This API can be extended with the Requests[^3] or SPARQLWrapper[^4] package to perform HTTP requests internally and customise them.

Other ideas and improvements have their place. We focused on the basic functionalities, needed to transform the HAZOPs. To provide a richer experience for the client, the application can be extended to meet their individual requirements.

With HAZOP data now readily available in RDF graphs, working on a HAZOP-to-HAZOP interface can begin.

[^2]: Set of scripts: [SOH (SPARQL over HTTP)](https://jena.apache.org/documentation/fuseki2/soh.html)
[^3]: Python package: [Requests](https://docs.python-requests.org/en/master/)
[^4]: Python package: [SPARQLWrapper](https://rdflib.dev/sparqlwrapper/)

 
