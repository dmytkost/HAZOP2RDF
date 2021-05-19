import glob, pandas as pd

from rdflib import Namespace, Graph, URIRef, BNode, Literal

class Service:
    def __init__(self):
        self.config = {
            "data/PEA-HAZOP-Dosiermodul_v07.xlsb": {
                "engine": "pyxlsb",
                "header": [2, 3],
                "sheet_name": 1
            }
        }

    def read_excel_data(self):
        return glob.glob("data/*.xlsb")

    def read_hazop_data(self, excel_data):
        hazop_data = []

        for file in excel_data:
            if file in self.config:
                df = pd.read_excel(file,
                                   engine=self.config[file]["engine"],
                                   header=self.config[file]["header"],
                                   sheet_name=self.config[file]["sheet_name"])

                df_filtered = df[df.iloc[:, 0].notnull()]
                hazop_data.append(df_filtered)

        return hazop_data

    def make_rdf_graphs(self, hazop_data):
        rdf_graphs = []

        for df in hazop_data:
            rdf_graphs.append(self.make_rdf_graph(df))

        return rdf_graphs

    def make_rdf_graph(self, df):
        g = Graph()
        n = Namespace("HAZOPCase/")
        g.bind("HAZOPCase", n)

        for i, row in df.iterrows():
            hazop_case = str(row[0]).replace(" ", "_")
            uri = "http://www.cae-pa.de/HAZOPCase/" + hazop_case

            reference   = URIRef(uri)
            deviation   = BNode()
            cause       = BNode()
            consequence = BNode()
            riskgraph   = BNode()
            safeguard   = BNode()
            restrisiko  = BNode()

            g.add((reference, n.Deviation, deviation))
            g.add((reference, n.Cause, cause))
            g.add((reference, n.Consequence, consequence))
            g.add((reference, n.Riskgraph, riskgraph))
            g.add((reference, n.Safeguard, safeguard))
            g.add((reference, n.Restrisiko, restrisiko))

            g.add((deviation, n.HAZOPNode, Literal(row[1])))
            g.add((deviation, n.Parameter, Literal(row[2])))
            g.add((deviation, n.Guideword, Literal(row[3])))
            g.add((deviation, n.Description, Literal(row[4])))

            g.add((cause, n.HAZOPNode, Literal(row[5])))
            g.add((cause, n.Parameter, Literal(row[6])))
            g.add((cause, n.Guideword, Literal(row[7])))
            g.add((cause, n.Description, Literal(row[8])))

            g.add((consequence, n.HAZOPNode, Literal(row[9])))
            g.add((consequence, n.Parameter, Literal(row[10])))
            g.add((consequence, n.Guideword, Literal(row[11])))
            g.add((consequence, n.Description, Literal(row[12])))

            g.add((riskgraph, n.Severity, Literal(row[13])))
            g.add((riskgraph, n.FrequencyOfPresence, Literal(row[14])))
            g.add((riskgraph, n.PossibilityOfAvoiding, Literal(row[15])))
            g.add((riskgraph, n.Probability, Literal(row[16])))

            g.add((safeguard, n.HAZOPNode, Literal(row[17])))
            g.add((safeguard, n.Parameter, Literal(row[18])))
            g.add((safeguard, n.Recommendation, Literal(row[19])))
            g.add((safeguard, n.Recommendation, Literal(row[20])))

            g.add((restrisiko, n.Severity, Literal(row[21])))
            g.add((restrisiko, n.FrequencyOfPresence, Literal(row[22])))
            g.add((restrisiko, n.PossibilityOfAvoiding, Literal(row[23])))
            g.add((restrisiko, n.Probability, Literal(row[24])))

        return g
