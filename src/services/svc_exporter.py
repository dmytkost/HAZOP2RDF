import os
import glob
import pandas as pd
from rdflib import Graph


class Service:
    def read_turtle_data(self):
        path = os.path.join("data", "turtle", "*.ttl")

        return glob.glob(path)

    def parse_graph(self, graph):
        g = Graph()
        g.parse(data=graph, format="turtle")

        query_path = os.path.join("src", "queries", "hazop.rq")
        with open(query_path, "r") as f:
            qres = g.query(f.read())

        rows = []
        for row in qres:
            rows.append(row)

        return rows

    def create_hazop_dataframe(self, data, index):
        df = pd.DataFrame(data, columns=index)

        return df

    def export_to_excel(self, df):
        df.replace(r"\bnan\b", "", regex=True, inplace=True)
        df[df.columns[0]] = df[df.columns[0]].astype("int32")
        df.sort_values(by=df.columns[0], ascending=True, inplace=True)
        filepath = os.path.join("data", "excel", df.name)
        df.to_excel(filepath,
                    columns=df.columns,
                    index=False,
                    sheet_name="HAZOP")
