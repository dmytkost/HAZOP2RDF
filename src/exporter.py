import logging

log = logging.getLogger(__name__)


class Exporter:
    def __init__(self, triple_store):
        self.triple_store = triple_store