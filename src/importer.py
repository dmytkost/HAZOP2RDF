import logging, threading, queue

from pyxlsb import open_workbook

log = logging.getLogger(__name__)


class Importer(threading.Thread):
    SHEET = "PEA HAZOP"

    def __init__(self, triple_store):
        super(Importer, self).__init__()
        self.triple_store = triple_store
        self.queue = queue.Queue()
        self.daemon = True

    def run(self):
        while True:
            hazop = self.queue.get(True)
            self.print_hazop(hazop)

    def print_hazop(self, hazop):
        rows = []

        with open_workbook(hazop) as wb:
            with wb.get_sheet(self.SHEET) as sheet:
                for row in sheet.rows():
                    rows.append([item.v for item in row])

        for row in rows:
            log.info(f"{row}\n")
