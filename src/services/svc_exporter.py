import glob, pandas as pd
from rdflib import Graph


class Service:
    def read_turtle_data(self):
        return glob.glob("data/turtle/*.ttl")

    def parse_graph(self, graph):
        g = Graph()
        g.parse(data=graph, format="turtle")

        with open("src/queries/hazop.rq", "r") as f:
            qres = g.query(f.read())

        rows = []
        for row in qres:
            rows.append(row)

        return rows

    def create_hazop_dataframe(self, data, index):
        df = pd.DataFrame(data, columns=index)

        return df

    def export_to_excel(self, df):
        df.to_excel(f"data/excel/{df.name}", index=False)
