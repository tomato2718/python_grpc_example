from multiprocessing import Process

from ._arg_parser import arg_parser
from ._starter import start_server


def main() -> None:
    args = arg_parser.parse_args()
    ADDRESS = f"{args.host}:{args.port}"
    WORKERS_COUNT = args.workers
    print(f"Service is listening on {ADDRESS}")
    WORKERS: list[Process] = []
    for _ in range(WORKERS_COUNT):
        worker = Process(target=start_server, kwargs={"address": ADDRESS})
        worker.start()
        WORKERS.append(worker)
    for worker in WORKERS:
        worker.join()


if __name__ == "__main__":
    main()
