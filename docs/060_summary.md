# Summary

* Discussion
  
With increasing complexity of systems, the
amount of generated data increases proportionally and easily
exceeds the human capabilities for interpretation.

Therefore, we propose an approach for data compression and
models for correlations of causes, deviations and consequences.

The result are enriched HAZOP studies that are
designed to be conducive for human interpretation and also
support machine-readability
The HAZOP-data was stored as Resource Description Framework (RDF). An import and export was implemented to support the original
documentation of the used HAZOPs

* Future Work
  
The vision would be to support humans in the decision-making in such a way
that, based on HAZOPs from experts, even novices could also
decide whether a plant is safe or not. Since safety scenarios
are always critical, this aspect needs to be analysed in more
detail and is focus of future research

* Future Projects
  


* Problems to be solved


PROBLEM: We use a fixed schema to validate the input data, by pattern mismatch the data will be skipped.\
TODO: Dynamic schema for accepting dynamic changes.\
NEED: Dynamic changes constrains.

PROBLEM: We don't validate the logic of the HAZOP data.\
TODO: Validation schema.\
NEED: Rules, what are acceptable in HAZOP and what are not.

IMPROVEMENT: TripleStore SOH API (SPARQL over HTML) to an API using Requests or SPARQLWrapper packages.\
ADVANTAGES: better control over request/response operations, customization.