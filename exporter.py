import logging

log = logging.getLogger(__name__)


class Exporter:
    def __init__(self, triple_store):
        log.info("Hello I am Exporter")
        self.triple_store = triple_store