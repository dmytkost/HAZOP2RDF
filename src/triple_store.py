import logging, threading, queue

log = logging.getLogger(__name__)


class TripleStore(threading.Thread):
    def __init__(self):
        super(TripleStore, self).__init__()
        self.queue = queue.Queue()
        self.daemon = True

    def run(self):
        while True:
            rdf_graph = self.queue.get(True)

	        with open("data/mHAZOP_Dosier_PEA.ttl", "w") as file:
	            file.write(rdf_graph)

            log.info(rdf_graph)

