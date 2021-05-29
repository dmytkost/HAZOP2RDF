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

        query_path = os.path.join("src", "queries", "hazop.rq")
        with open(query_path, "r") as f:
            qres = g.query(f.read())

        data_list = []
        for row in qres:
            data_list.append(row)

        return data_list

    def create_hazop_dataframe(self, data, columns):
        """Creates HAZOP dataframe

        Args:
            data (list): HAZOP data
            columns (list): Columns of HAZOP dataframe

        Returns:
            pandas.DataFrame: HAZOP dataframe
        """
        df = pd.DataFrame(data, columns=columns)

        return df

    def export_to_excel(self, df, filename):
        """Exports HAZOP dataframe in excel format

        Args:
            df (pandas.DataFrame): HAZOP dataframe
            filename (str): Name of the file
        """
        df.replace(r"\bnan\b", "", regex=True, inplace=True)
        df[df.columns[0]] = df[df.columns[0]].astype("int32")
        df.sort_values(by=df.columns[0], ascending=True, inplace=True)
        filepath = os.path.join("data", "excel", filename)
        df.to_excel(filepath, index=False, sheet_name="HAZOP")
