import os
import glob
import pandas as pd

from rdflib import Graph


class Service:
    """Exporter utilities
    """

    def read_turtle_data(self):
        """Reads turtle data from data directory

        Returns:
            list: List of turtle data
        """
        path = os.path.join("data", "turtle", "*.ttl")
        turtle_data_list = glob.glob(path)

        return turtle_data_list

    def get_graph_data(self, graph):
        """Gets graph data

        Args:
            graph (str): Graph in string format

        Returns:
            list: Graph data as list
        """
        g = Graph()
        g.parse(data=graph, format="turtle")

        query_path = os.path.join("src", "sparql", "hazop.rq")
        with open(query_path, "r") as f:
            qres = g.query(f.read())

        data_list = []
        for row in qres:
            data_list.append(row)

        return data_list

    def export_graph_to_excel(self, args):
        """Exports graph to Excel

        Workflow:
            * replace all NaNs to blank cells
            * convert HazopCase type to int32
            * sort by HazopCase, reset index
            * assign MultiIndex header
            * export graph to Excel

        Args:
            args (tuple): graph data, header and filename
        """
        df = pd.DataFrame(args[0])
        df.replace(r"\bnan\b", "", regex=True, inplace=True)
        df[df.columns[0]] = df[df.columns[0]].astype("int32")
        df.sort_values(by=df.columns[0], ascending=True, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.columns = pd.MultiIndex.from_tuples(args[1])
        filepath = os.path.join("data", "excel", args[2])
        df.to_excel(filepath, index_label="Index", sheet_name="HAZOP")
