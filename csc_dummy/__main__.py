import sys
import logging

from .runner import run_from_file


def logging_setup():
    cur_logger = logging.getLogger(None)
    cur_logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    cur_logger.addHandler(handler)


def launch():
    logging_setup()
    scal = int(sys.argv[3])
    run_from_file(
        sys.argv[1], port=int(sys.argv[2]), require_hash_pinning=scal >= 2
    )


if __name__ == '__main__':
    launch()
