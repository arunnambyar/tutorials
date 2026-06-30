"""Non-blocking HTTP POST on one thread — event loop using nonblock.http helpers."""

import json
from collections.abc import Generator

from nonblock.http import nb_connect, nb_recv, nb_send


HOST = "jsonplaceholder.typicode.com"
PORT = 80
PAYLOAD = {"title": "demo", "body": "hi"}
BODY = json.dumps(PAYLOAD)
REQUEST = (
    f"POST /posts HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    f"Content-Type: application/json\r\n"
    f"Content-Length: {len(BODY)}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
    f"{BODY}"
)


def nb_request(
    host: str,
    port: int,
    request: bytes
) -> Generator[None, None, bytes]:
    print("\n")
    print("Is connected to server ? >")
    connect_gen = nb_connect(HOST, PORT)
    while True:
        try:
            next(connect_gen)
            yield None
        except StopIteration as stopped:
            sock = stopped.value
            break
    print("Connected to server <")
    print("\n")

    print("Sending POST >")
    data = REQUEST.encode()
    send_gen = nb_send(sock, data)
    while True:
        try:
            next(send_gen)
            yield None
        except StopIteration as stopped:
            break
    print("Request sent <")
    print("\n")

    print("Waiting for response >")
    response_gen = nb_recv(sock)
    while True:
        try:
            next(response_gen)
            yield None
        except StopIteration as stopped:
            response = stopped.value
            break
    print("Response received <")
    print("\n")

    return response


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
    event_loop.add_task(nb_request(HOST, PORT, REQUEST.encode()))
    event_loop.add_task(nb_request(HOST, PORT, REQUEST.encode()))
    event_loop.add_task(nb_request(HOST, PORT, REQUEST.encode()))
    event_loop.run()

    for result in event_loop.results:
        for line in result.split(b"\r\n"):
            if line:
                print(line.decode())