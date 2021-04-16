import logging, sys
from importer import Importer

fmt = "%(asctime)s [%(name)s] [%(levelname)s] %(message)s"
datefmt = "%d/%m/%Y %H:%M:%S"

logging.basicConfig(format=fmt,
                    datefmt=datefmt,
                    level=logging.INFO,
                    stream=sys.stdout)

log = logging.getLogger(__name__)

if __name__ == "__main__":
    log.info("Importer started")

    importer = Importer()
    importer.start()

    while True:
        try:
            hazop_path = input()
            importer.queue.put(hazop_path)

        except KeyboardInterrupt as e:
            importer.close()
            sys.exit(e)