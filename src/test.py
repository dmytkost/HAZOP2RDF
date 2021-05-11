from rdflib import Graph

g = Graph()
g.parse("data/mHAZOP_Dosier_PEA.ttl", format="turtle")

print(g)
print(len(g))
