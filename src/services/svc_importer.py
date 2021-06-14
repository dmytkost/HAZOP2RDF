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
        s_ref = uri + "subject/"
        p_ref = uri + "predicate/"
        g = Graph()

        hazopcase = URIRef(f"{s_ref}hazopcase/")
        predicate_deviation = URIRef(f"{p_ref}deviation")
        predicate_cause = URIRef(f"{p_ref}cause")
        predicate_consequence = URIRef(f"{p_ref}consequence")
        predicate_riskgraph = URIRef(f"{p_ref}riskgraph")
        predicate_safeguard = URIRef(f"{p_ref}safegurd")
        predicate_restrisiko = URIRef(f"{p_ref}restrisiko")
        predicate_hazopnode = URIRef(f"{p_ref}hazopnode")
        predicate_parameter = URIRef(f"{p_ref}parameter")
        predicate_guideword = URIRef(f"{p_ref}guideword")
        predicate_description = URIRef(f"{p_ref}description")
        predicate_recommendation = URIRef(f"{p_ref}recommendation")
        predicate_otherinfo = URIRef(f"{p_ref}otherinfo")
        predicate_severity = URIRef(f"{p_ref}severity")
        predicate_presence = URIRef(f"{p_ref}frequencyofpresence")
        predicate_avoiding = URIRef(f"{p_ref}possibilityofavoiding")
        predicate_probability = URIRef(f"{p_ref}probability")

        g.bind("hazopcase", hazopcase)
        g.bind("deviation", predicate_deviation)
        g.bind("cause", predicate_cause)
        g.bind("consequence", predicate_consequence)
        g.bind("riskgraph", predicate_riskgraph)
        g.bind("safeguard", predicate_safeguard)
        g.bind("restrisiko", predicate_restrisiko)
        g.bind("hazopnode", predicate_hazopnode)
        g.bind("parameter", predicate_parameter)
        g.bind("guideword", predicate_guideword)
        g.bind("description", predicate_description)
        g.bind("recommendation", predicate_recommendation)
        g.bind("otherinfo", predicate_otherinfo)
        g.bind("severity", predicate_severity)
        g.bind("frequencyofpresence", predicate_presence)
        g.bind("possibilityofavoiding", predicate_avoiding)
        g.bind("probability", predicate_probability)

        for i, row in df.iterrows():
            if not str(row[0]).isdigit():
                continue

            case = URIRef(str(row[0]))
            node_deviation = BNode()
            node_cause = BNode()
            node_consequence = BNode()
            node_riskgraph = BNode()
            node_safeguard = BNode()
            node_restrisiko = BNode()

            g.add((hazopcase + case, predicate_deviation, node_deviation))
            g.add((hazopcase + case, predicate_cause, node_cause))
            g.add((hazopcase + case, predicate_consequence, node_consequence))
            g.add((hazopcase + case, predicate_riskgraph, node_riskgraph))
            g.add((hazopcase + case, predicate_safeguard, node_safeguard))
            g.add((hazopcase + case, predicate_restrisiko, node_restrisiko))

            g.add((node_deviation, predicate_hazopnode, Literal(row[1])))
            g.add((node_deviation, predicate_parameter, Literal(row[2])))
            g.add((node_deviation, predicate_guideword, Literal(row[3])))
            g.add((node_deviation, predicate_description, Literal(row[4])))

            g.add((node_cause, predicate_hazopnode, Literal(row[5])))
            g.add((node_cause, predicate_parameter, Literal(row[6])))
            g.add((node_cause, predicate_guideword, Literal(row[7])))
            g.add((node_cause, predicate_description, Literal(row[8])))

            g.add((node_consequence, predicate_hazopnode, Literal(row[9])))
            g.add((node_consequence, predicate_parameter, Literal(row[10])))
            g.add((node_consequence, predicate_guideword, Literal(row[11])))
            g.add((node_consequence, predicate_description, Literal(row[12])))

            g.add((node_riskgraph, predicate_severity, Literal(row[13])))
            g.add((node_riskgraph, predicate_presence, Literal(row[14])))
            g.add((node_riskgraph, predicate_avoiding, Literal(row[15])))
            g.add((node_riskgraph, predicate_probability, Literal(row[16])))

            g.add((node_safeguard, predicate_hazopnode, Literal(row[17])))
            g.add((node_safeguard, predicate_parameter, Literal(row[18])))
            g.add((node_safeguard, predicate_recommendation, Literal(row[19])))
            g.add((node_safeguard, predicate_otherinfo, Literal(row[20])))

            g.add((node_restrisiko, predicate_severity, Literal(row[21])))
            g.add((node_restrisiko, predicate_presence, Literal(row[22])))
            g.add((node_restrisiko, predicate_avoiding, Literal(row[23])))
            g.add((node_restrisiko, predicate_probability, Literal(row[24])))

        graph_str = g.serialize(format="turtle").decode("utf-8")

        return graph_str
