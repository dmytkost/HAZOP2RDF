import logging, threading, queue

log = logging.getLogger(__name__)

class Importer(threading.Thread):
    def __init__(self, triple_store):
        super(Importer, self).__init__()
        log.info("Hello I am Importer")
        self.triple_store = triple_store
        self.queue = queue.Queue()
        self.daemon = True

    def run(self):
        while True:
            hazop_path = self.queue.get(True)
            log.info(hazop_path)
