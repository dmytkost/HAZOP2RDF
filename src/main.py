import logging, sys, glob

from importer import Importer
from exporter import Exporter
from triplestore import TripleStore

fmt = "%(asctime)s [%(name)s] [%(levelname)s] %(message)s"
datefmt = "%d/%m/%Y %H:%M:%S"

logging.basicConfig(format=fmt,
                    datefmt=datefmt,
                    level=logging.INFO,
                    stream=sys.stdout)

log = logging.getLogger(__name__)

if __name__ == "__main__":
    log.info("Main function started")

    triple_store = TripleStore()
    exporter = Exporter(triple_store)
    importer = Importer(triple_store)

    triple_store.start()
    importer.start()

    timeout = 1.0

    while True:
        try:
            hazop_files = glob.glob("data/*.xlsb")
            for file in hazop_files:
                hazop_config = {
                    "path": file,
                    "engine": "pyxlsb",
                    "header": [2, 3],
                    "sheet_name": 1
                }
                importer.queue.put(hazop_config)
            importer.join(timeout)
            sys.exit(f"Exit with timeout {timeout}")
        except KeyboardInterrupt as e:
            sys.exit(e)