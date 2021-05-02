import logging, threading, queue

log = logging.getLogger(__name__)


class TripleStore(threading.Thread):
    def __init__(self):
        super(TripleStore, self).__init__()
        self.queue = queue.Queue()
        self.daemon = True

    def run(self):
        while True:
            graph = self.queue.get(True)
            log.info(graph)

