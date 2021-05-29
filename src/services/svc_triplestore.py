import os


class Service:
    """Triplestore SOH (SPARQL over HTTP) API

    Attributes:
        url (str): Fuseki server URL
    """

    url = "http://localhost:3030/ds"

    def upload_hazop_graph(self, filename, filepath):
        """Uploads HAZOP graph to the server

        Args:
            filename (str): Name of the file
            filepath (str): Path of the file

        Returns:
            bytes: HTTP response
        """
        cmd = f"s-put {self.url} {filename} {filepath}"
        response = os.system(cmd)

        return response

    def get_hazop_graph(self, filename):
        """Gets HAZOP graph from the server

        Args:
            filename (str): Name of the file

        Returns:
            bytes: HTTP response
        """
        cmd = f"s-get {self.url} {filename}"
        response = os.popen(cmd).read()

        return response

    def get_dataset_information(self):
        """Gets dataset information

        Returns:
            bytes: HTTP response
        """
        rq = "src/queries/bindings.rq"
        cmd = f"s-query --service={self.url}/query --query={rq}"
        response = os.popen(cmd).read()

        return response
