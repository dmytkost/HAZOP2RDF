import os
import glob
import pandas as pd

from rdflib import Namespace, Graph, URIRef, BNode, Literal


class Service:
    """Importer utilities
    """

    def read_excel_data(self):
        """Reads Excel data with .xlsb and .xlsx extensions

        Returns:
            list: list of files with .xlsb and .xlsx extensions
        """
        xlsb_list_path = os.path.join("data", "*.xlsb")
        xlsx_list_path = os.path.join("data", "*.xlsx")

        excel_xlsb_list = glob.glob(xlsb_list_path)
        excel_xlsx_list = glob.glob(xlsx_list_path)

        return excel_xlsb_list + excel_xlsx_list

    def get_hazop_dataframe(self, args):
        """Gets HAZOP dataframe

        Args:
            args (tuple): excel reading parameters

        Returns:
            pandas.DataFrame: HAZOP dataframe
        """
        df = pd.read_excel(args[0],
                           engine=args[1],
                           header=args[2],
                           sheet_name=args[3])

        df_filtered = df[df.iloc[:, 0].notnull()].drop_duplicates()

        return df_filtered

    def build_hazop_graph(self, df):
        """Builds HAZOP graph

        Args:
            df (pandas.DataFrame): HAZOP dataframe

        Returns:
            str: Graph in string format
        """
        uri = "http://www.hazop2rdf.de/hazop/"
        g = Graph()

        uriref = URIRef(f"{uri}hazopcase/")
        blanknode = Namespace(f"{uri}blanknode/")
        predicate = Namespace(f"{uri}predicate/")

        g.bind("hazopcase", uriref)
        g.bind("blanknode", blanknode)
        g.bind("predicate", predicate)

        for i, row in df.iterrows():
            if not str(row[0]).isdigit():
                continue

            hazopcase = uriref + URIRef(str(row[0]))
            deviation = BNode()
            cause = BNode()
            consequence = BNode()
            riskgraph = BNode()
            safeguard = BNode()
            restrisiko = BNode()

            g.add((hazopcase, blanknode.deviation, deviation))
            g.add((hazopcase, blanknode.cause, cause))
            g.add((hazopcase, blanknode.consequence, consequence))
            g.add((hazopcase, blanknode.riskgraph, riskgraph))
            g.add((hazopcase, blanknode.safeguard, safeguard))
            g.add((hazopcase, blanknode.restrisiko, restrisiko))

            g.add((deviation, predicate.hazopnode, Literal(row[1])))
            g.add((deviation, predicate.parameter, Literal(row[2])))
            g.add((deviation, predicate.guideword, Literal(row[3])))
            g.add((deviation, predicate.description, Literal(row[4])))

            g.add((cause, predicate.hazopnode, Literal(row[5])))
            g.add((cause, predicate.parameter, Literal(row[6])))
            g.add((cause, predicate.guideword, Literal(row[7])))
            g.add((cause, predicate.description, Literal(row[8])))

            g.add((consequence, predicate.hazopnode, Literal(row[9])))
            g.add((consequence, predicate.parameter, Literal(row[10])))
            g.add((consequence, predicate.guideword, Literal(row[11])))
            g.add((consequence, predicate.description, Literal(row[12])))

            g.add((riskgraph, predicate.severity, Literal(row[13])))
            g.add((riskgraph, predicate.presence, Literal(row[14])))
            g.add((riskgraph, predicate.avoiding, Literal(row[15])))
            g.add((riskgraph, predicate.probability, Literal(row[16])))

            g.add((safeguard, predicate.hazopnode, Literal(row[17])))
            g.add((safeguard, predicate.parameter, Literal(row[18])))
            g.add((safeguard, predicate.recommendation, Literal(row[19])))
            g.add((safeguard, predicate.otherinfo, Literal(row[20])))

            g.add((restrisiko, predicate.severity, Literal(row[21])))
            g.add((restrisiko, predicate.presence, Literal(row[22])))
            g.add((restrisiko, predicate.avoiding, Literal(row[23])))
            g.add((restrisiko, predicate.probability, Literal(row[24])))

        graph_str = g.serialize(format="turtle").decode("utf-8")

        return graph_str
