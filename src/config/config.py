"""The file containing parameters for reading and validating Excel data.

Excel configuration (excel)

    Parameters:
     excel[*]["engine"],
     excel[*]["header"],
     excel[*]["sheet_name"],
    are used in the function svc_importer.Service.read_hazop_dataframe to find and read the HAZOP dataframe in Excel workbook

     excel[*]["valid_header"],
    is a validation schema for the function svc_importer.Service.build_hazop_graph, the schema has to match the RDF schema in that function.

Output header (output_header) contains all the headers used for the output Excel data.

To update the program with another input data format (for exmaple .xsl). Make a new section ".xsl" with parameters in the excel configuration (excel) below and update src_importer.Service.read_excel_data to read and return a list of .xsl files.
"""

excel = {
    ".xlsb": {
        "engine": "pyxlsb",
        "header": [2, 3],
        "sheet_name": 1,
        "valid_header": [("Unnamed: 0_level_0", "ID HAZOP Case"),
                         ("Deviation", "HAZOPNode"),
                         ("Deviation", "Parameter"),
                         ("Deviation", "Guideword"),
                         ("Deviation", "Description"),
                         ("Cause", "HAZOPNode"),
                         ("Cause", "Parameter"),
                         ("Cause", "Guideword"),
                         ("Cause", "Description"),
                         ("Consequence", "HAZOPNode"),
                         ("Consequence", "Parameter"),
                         ("Consequence", "Guideword"),
                         ("Consequence", "Description"),
                         ("Risk Graph", "Severity"),
                         ("VDI/VDE 2180-1:2019", "Frequency of Presence "),
                         ("VDI/VDE 2180-1:2019", "Possibility of avoiding"),
                         ("VDI/VDE 2180-1:2019", "Probability"),
                         ("Safeguard", "HAZOPNode"),
                         ("Safeguard", "Description"),
                         ("Safeguard", "Recommendation"),
                         ("Safeguard", "Recommendation.1"),
                         ("Risk Graph", "Severity.1"),
                         ("Risk Graph", "Frequency of Presence "),
                         ("Risk Graph", "Possibility of avoiding"),
                         ("Risk Graph", "Probability")],
    },
    ".xlsx": {
        "engine": None,
        "header": [2, 3],
        "sheet_name": 0,
        "valid_header": [("Unnamed: 0_level_0", "ID HAZOP Case"),
                         ("Deviation", "HAZOPNode"),
                         ("Deviation", "Parameter"),
                         ("Deviation", "Guideword"),
                         ("Deviation", "Description"),
                         ("Cause", "HAZOPNode"),
                         ("Cause", "Parameter"),
                         ("Cause", "Guideword"),
                         ("Cause", "Description"),
                         ("Consequence", "HAZOPNode"),
                         ("Consequence", "Parameter"),
                         ("Consequence", "Guideword"),
                         ("Consequence", "Description"),
                         ("Risk Graph", "Severity"),
                         ("VDI/VDE 2180-1:2019", "Frequency of Presence "),
                         ("VDI/VDE 2180-1:2019", "Possibility of avoiding"),
                         ("VDI/VDE 2180-1:2019", "Probability"),
                         ("Safeguard", "HAZOPNode"),
                         ("Safeguard", "Description"),
                         ("Safeguard", "Recommendation"),
                         ("Safeguard", "Recommendation.1"),
                         ("Risk Graph", "Severity.1"),
                         ("Risk Graph", "Frequency of Presence "),
                         ("Risk Graph", "Possibility of avoiding"),
                         ("Risk Graph", "Probability")],
    }
}

output_header = ["ID HAZOP Case",
                 "Deviation HAZOPNode",
                 "Deviation Parameter",
                 "Deviation Guideword",
                 "Deviation Description",
                 "Cause HAZOPNode", "Cause Parameter",
                 "Cause Guideword", "Cause Description",
                 "Consequence HAZOPNode",
                 "Consequence Parameter",
                 "Consequence Guideword",
                 "Consequence Description",
                 "Risk Graph Severity",
                 "Risk Graph Frequency of Presence ",
                 "Risk Graph Possibility of avoiding",
                 "Risk Graph Probability",
                 "Safeguard HAZOPNode",
                 "Safeguard Description",
                 "Safeguard Recommendation",
                 "Safeguard Other info",
                 "Risk Graph Severity",
                 "Risk Graph Frequency of Presence ",
                 "Risk Graph Possibility of avoiding",
                 "Risk Graph Probability"]
