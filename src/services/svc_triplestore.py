import os, json


class Service:
    url = "http://localhost:3030/ds"

    def upload_hazop_graph(self, filename, filepath):
        cmd = f"s-put {self.url} {filename} {filepath}"
        response = os.system(cmd)

        return response

    def get_hazop_graph(self, filename):
        cmd = f"s-get {self.url} {filename}"
        response = os.popen(cmd).read()

        return response

    def get_hazop_graph_bindings(self):
        rq = "src/queries/bindings.rq"
        cmd = f"s-query --service={self.url}/query --query={rq}"
        response = os.popen(cmd).read()
        response_dict = json.loads(response)

        bindings = []
        for g in response_dict["results"]["bindings"]:
            bindings.append(g["g"]["value"])

        return bindings