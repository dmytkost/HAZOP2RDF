import threading, queue

class Importer(threading.Thread):
    def __init__(self):
        super(Importer, self).__init__()
        self.queue = queue.Queue()
        self.daemon = True

    def run(self):
        while True:
            hazop_path = self.queue.get()
            log.info(hazop_path)

    def close(self):
        self.queue.join()
        self.join(False)

