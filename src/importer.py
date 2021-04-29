import logging, threading, queue

import pandas as pd

from rdflib import Namespace, Graph, URIRef, BNode, Literal

log = logging.getLogger(__name__)


class Importer(threading.Thread):
    def __init__(self, triple_store):
        super(Importer, self).__init__()
        self.triple_store = triple_store
        self.queue = queue.Queue()
        self.daemon = True

    def run(self):
        while True:
            hazop_path = self.queue.get(True)
            df_hazop = self.read_hazop(hazop_path)

            # log.info(df_hazop["Deviation"]["HAZOPNode"])

            maker = GraphMaker()
            maker.make(df_hazop)

    def read_hazop(self, hazop_path):
        df = pd.read_excel(hazop_path,
                           engine="pyxlsb",
                           header=[2, 3],
                           sheet_name=1)

        return df


class GraphMaker:
    def make(self, df):
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
            safeguard   = BNode()

            g.add((reference, n.Deviation, deviation))
            g.add((reference, n.Cause, cause))
            g.add((reference, n.Consequence, consequence))
            g.add((reference, n.Safeguard, safeguard))

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

            g.add((safeguard, n.HAZOPNode, Literal(row[13])))
            g.add((safeguard, n.Parameter, Literal(row[14])))
            g.add((safeguard, n.Guideword, Literal(row[15])))
            g.add((safeguard, n.Description, Literal(row[16])))

        with open("data/mHAZOP_Dosier_PEA.ttl", "w") as file:
            file.write(g.serialize(format="turtle").decode("utf-8"))

        log.info(g.serialize(format="turtle").decode("utf-8"))
