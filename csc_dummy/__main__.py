import sys

from .runner import run_from_file


def launch():
    scal = int(sys.argv[3])
    run_from_file(
        sys.argv[1], port=int(sys.argv[2]), require_hash_pinning=scal >= 2
    )


if __name__ == '__main__':
    launch()
