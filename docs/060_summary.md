# Summary
  
With increasing complexity of systems, the
amount of generated data increases proportionally and easily
exceeds the human capabilities for interpretation.

Therefore, we propose an approach for data compression and
models for correlations of causes, deviations and consequences.

The result are enriched HAZOP studies that are
designed to be conducive for human interpretation and also
support machine-readability
The HAZOP-data was stored as Resource Description Framework (RDF). An import and export was implemented to support the original
documentation of the used HAZOP studies
  
The vision would be to support humans in the decision-making in such a way
that, based on HAZOP studies from experts, even novices could also
decide whether a plant is safe or not. Since safety scenarios
are always critical, this aspect needs to be analysed in more
detail and is focus of future research

## Future Work

The application provides essential functionality for the HAZOP transformation. There is still room left for future adoptions, tests and experiments.

* The import of the HAZOP data can be improved and adopted with fixed constrains. It can be conditional statements, which parse different shapes of the incoming data and serve them for the RDF transformation.

* Fuseki servers offer HTTP access. Currently, we use a set of command line scripts[^2] to work with SPARQL. This API can be extended with the Requests[^3] or SPARQLWrapper[^4] package to perform HTTP requests internally and customise them.

Other ideas and improvements have their place. We focused on the basic functionalities, needed to transform the HAZOPs. To provide a richer experience for the client, the application can be extended to meet their individual requirements.

[^2]: Set of scripts: [SOH (SPARQL over HTTP)](https://jena.apache.org/documentation/fuseki2/soh.html)
[^3]: Python package: [Requests](https://docs.python-requests.org/en/master/)
[^4]: Python package: [SPARQLWrapper](https://rdflib.dev/sparqlwrapper/)

 
