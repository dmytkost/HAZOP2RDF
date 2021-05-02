import unittest, warnings, glob, time

import pandas as pd

from src.importer import Importer


class TestImporter(unittest.TestCase):
    def setUp(self):
        self.importer = Importer()

    def test_read_hazop(self):
        samples = glob.glob("test/data/samples/*.xlsx")
        results = glob.glob("test/data/results/*.xlsx")

        for sample, result in zip(samples, results):
            config = {
                "path": sample,
                "engine": None,
                "header": 0,
                "sheet_name": 0
            }

            df_sample = self.importer.read_hazop(config)
            df_result = pd.read_excel(result)

            pd.testing.assert_frame_equal(df_sample,
                                          df_result,
                                          check_dtype=False)

    def test_graph_maker(self):
        samples = glob.glob("test/data/samples/*.xlsb")
        results = glob.glob("test/data/results/*.ttl")

        warnings.simplefilter("ignore", ResourceWarning)

        for sample, result in zip(samples, results):
            config = {
                "path": sample,
                "engine": "pyxlsb",
                "header": [2, 3],
                "sheet_name": 1
            }

            df_sample = self.importer.read_hazop(config)
            rdf_graph = self.importer.rdf_graph.make(df_sample)

            rdf_sample = rdf_graph.split("\n")

            with open(result) as file:
                rdf_result = file.read().splitlines()

            cond = set(rdf_sample).remove("") == set(rdf_result).remove("")
            self.assertTrue(cond)


def testImporterSuite():
    suite = unittest.TestSuite()
    suite.addTest(TestImporter("test_read_hazop"))
    suite.addTest(TestImporter("test_graph_maker"))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestImporterSuite())
