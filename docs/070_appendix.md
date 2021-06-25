# Appendix

* turtle data, output ontology in excel, documentation

```ttl
@prefix blanknode: <http://www.hazop2rdf.de/hazop/blanknode/> .
@prefix hazopcase: <http://www.hazop2rdf.de/hazop/hazopcase/> .
@prefix predicate: <http://www.hazop2rdf.de/hazop/predicate/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hazopcase:1 blanknode:cause [ predicate:description "Zugeführtes Prozessmedium zu heiß (>200°C)" ;
            predicate:guideword "Mehr" ;
            predicate:hazopnode "In 1 - Feed-Eingang" ;
            predicate:parameter "Temperatur" ] ;
    blanknode:consequence [ predicate:description "Materialversagen der Dichtungen, Leckage" ;
            predicate:guideword "NaN"^^xsd:double ;
            predicate:hazopnode "Speicherbehälter" ;
            predicate:parameter "NaN"^^xsd:double ] ;
    blanknode:deviation [ predicate:description "Überschreitung der zulässigen Temperatur im Behälter" ;
            predicate:guideword "Mehr" ;
            predicate:hazopnode "Speicherbehälter" ;
            predicate:parameter "Temperatur" ] ;
    blanknode:restrisiko [ predicate:avoiding "G2 - fast unmöglich" ;
            predicate:presence "A2 - häufig bis andauernd" ;
            predicate:probability "W2 - gering" ;
            predicate:severity "S1 - minimale " ] ;
    blanknode:riskgraph [ predicate:avoiding "G2 - fast unmöglich" ;
            predicate:presence "A2 - häufig bis andauernd" ;
            predicate:probability "W2 - gering" ;
            predicate:severity "S2 - geringe" ] ;
    blanknode:safeguard [ predicate:hazopnode "Speicherbehälter" ;
            predicate:otherinfo "NaN"^^xsd:double ;
            predicate:parameter "Hochwertige Dichtungen für Temp. über 200°C (bei 25bar)" ;
            predicate:recommendation "NaN"^^xsd:double ] .
```

![Graph ontology in Excel](images/graph_ontology_excel.png)