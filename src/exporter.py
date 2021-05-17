import logging, threading, queue
import pandas as pd


from rdflib import Namespace, Graph, URIRef, BNode, Literal

log = logging.getLogger(__name__)



g = Graph()  
g.parse('mHAZOP_Dosier_PEA.ttl',format="turtle")
qres = g.query('''
            SELECT DISTINCT ?cases ?devNode ?devPara ?devGuide ?devDescri ?causeNode ?causePara ?causeGuide ?causeDescri ?conNode ?conPara ?conGuide ?conDescri ?safeNode ?safePara ?safeRec
            WHERE {
                ?cases HAZOPCase:Deviation ?object0.
                ?object0 HAZOPCase:HAZOPNode ?devNode;
                        HAZOPCase:Parameter ?devPara;
                        HAZOPCase:Guideword ?devGuide;
                        HAZOPCase:Description ?devDescri.
                        
                ?cases HAZOPCase:Cause ?object1.
                ?object1 HAZOPCase:HAZOPNode ?causeNode;
                        HAZOPCase:Parameter ?causePara;
                        HAZOPCase:Guideword ?causeGuide;
                        HAZOPCase:Description ?causeDescri.
                        
                ?cases HAZOPCase:Consequence ?object2.
                ?object2 HAZOPCase:HAZOPNode ?conNode;
                        HAZOPCase:Parameter ?conPara;
                        HAZOPCase:Guideword ?conGuide;
                        HAZOPCase:Description ?conDescri.
                        
                ?cases HAZOPCase:Safeguard ?object3.
                ?object3 HAZOPCase:HAZOPNode ?safeNode;
                        HAZOPCase:Parameter ?safePara;
                        HAZOPCase:Recommendation ?safeRec.       
                }
            GROUP BY ?cases
            ORDER BY ASC(?cases)
            ''')
'''
for cases,devNode,devPara,devGuide,devDescri, *_ in qres:
                print(cases,devNode,devPara,devGuide,devDescri)
'''                
df = pd.DataFrame.from_dict(qres)
df.columns = ['ID HAZOP Case','Deviation HAZOPNode','Parameter','Guideword','Description','Cause HAZOPNode','Parameter','Guideword','Description', 'Consequence HAZOPNode','Parameter','Guideword','Description', 'Safeguard HAZOPNode','Description','Recommendation']
df.to_excel('test.xlsx')
