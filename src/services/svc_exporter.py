import glob, pandas as pd
from rdflib import Graph


class Service:
    def read_turtle_data(self):
        return glob.glob("data/turtle/*.ttl")

    def create_hazop_dataframe(self, graph, index):
        df = pd.DataFrame(columns=index)

        g = Graph()
        g.parse(data=graph, format="turtle")

        with open("src/queries/hazop.rq", "r") as f:
            qres = g.query(f.read())

        for i, row in enumerate(qres):
            df.loc[i] = row

        return df

    def export_to_excel(self, df, filename):
        df.to_excel(f"data/excel/{filename}", index=False)
