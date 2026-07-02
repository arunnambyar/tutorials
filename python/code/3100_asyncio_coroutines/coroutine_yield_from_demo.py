import random
import time

from collections.abc import Generator


def nonblocking_sleep(
    seconds: float,
) -> Generator[None, None, None]:
    """Nonblocking sleep for a random number of seconds"""
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        yield None
    return None


def mock_server_connect(
    server_name: str,
) -> Generator[None, None, str]:
    """Mock server connection"""

    # START: mocked server connection
    # by non-blocking sleep for a random seconds
    mock_delay = random.randint(5, 20)
    yield from nonblocking_sleep(mock_delay)
    # DONE: mocked server connection

    return f"RESULT:{server_name}"


def process_server_data(
    server_name: str,
) -> Generator[None, None, str]:
    print(f"{time.strftime('%H:%M:%S')} STARTED: {server_name} >")

    data = yield from mock_server_connect(server_name)

    print(f"{time.strftime('%H:%M:%S')} COMPLETED: {server_name} <")
    return data


def process_db_data(
    server_name: str,
) -> Generator[None, None, str]:
    print(f"{time.strftime('%H:%M:%S')} STARTED: {server_name} >")

    data = yield from mock_server_connect(server_name)

    print(f"{time.strftime('%H:%M:%S')} COMPLETED: {server_name} <")
    return data


class EventLoop:
    def __init__(self):
        self.tasks = []
        self.results = []

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:
            try:
                task = self.tasks.pop(0)
                next(task)
                self.tasks.append(task)
            except StopIteration as stopped:
                self.results.append(stopped.value)


if __name__ == "__main__":
    event_loop = EventLoop()

    event_loop.add_task(process_server_data("SERVER-A"))
    event_loop.add_task(process_server_data("SERVER-B"))
    event_loop.add_task(process_server_data("SERVER-C"))
    event_loop.add_task(process_db_data("DB-A"))
    event_loop.add_task(process_db_data("DB-B"))
    event_loop.add_task(process_db_data("DB-C"))

    print()
    print("Running event loop: >>>>>>>>>>>>>>>>")
    print()
    event_loop.run()
    print()
    print("Event loop completed: <<<<<<<<<<<<<<<")
    print("Results:", event_loop.results)
    print()
