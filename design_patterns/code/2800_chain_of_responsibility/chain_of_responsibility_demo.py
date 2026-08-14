"""
Chain of Responsibility pattern demo. Run: python chain_of_responsibility_demo.py
"""

from abc import ABC
from dataclasses import dataclass


# --- Request ---

@dataclass
class Request:
    """The request passed along the chain."""

    ticket_id: str
    issue: str
    severity: str


# --- Handler ---

class Handler(ABC):
    """GoF Handler: defines handle_request and maintains the successor link."""

    def __init__(self) -> None:
        self._successor: Handler | None = None

    def set_successor(self, successor: "Handler") -> "Handler":
        self._successor = successor
        return successor

    def handle_request(self, request: Request) -> None:
        """Default: do not handle here — forward to successor (if any)."""
        if self._successor is not None:
            self._successor.handle_request(request)
        else:
            print(f"  [Handler] Unhandled request {request.ticket_id}")


# --- ConcreteHandler ---

class ConcreteHandler1(Handler):
    """GoF ConcreteHandler: Quick Service — handles minor requests."""

    def handle_request(self, request: Request) -> None:
        if request.severity == "minor":
            # Handle the request, then return (stop the chain).
            print(f"  [Quick Service] Fixed {request.issue} ({request.ticket_id})")
            return
        # Cannot handle — forward to successor.
        print(f"  [Quick Service] Escalating {request.ticket_id}")
        super().handle_request(request)


class ConcreteHandler2(Handler):
    """GoF ConcreteHandler: Workshop — handles moderate requests."""

    def handle_request(self, request: Request) -> None:
        if request.severity == "moderate":
            # Handle the request, then return (stop the chain).
            print(f"  [Workshop] Scheduled {request.issue} ({request.ticket_id})")
            return
        # Cannot handle — forward to successor.
        print(f"  [Workshop] Escalating {request.ticket_id}")
        super().handle_request(request)


class ConcreteHandler3(Handler):
    """GoF ConcreteHandler: Manufacturer — handles critical requests."""

    def handle_request(self, request: Request) -> None:
        if request.severity == "critical":
            # Handle the request, then return (stop the chain).
            print(f"  [Manufacturer] Warranty claim for {request.issue}")
            return
        # Cannot handle — forward to successor.
        print(f"  [Manufacturer] Escalating {request.ticket_id}")
        super().handle_request(request)


# --- Client ---

class Client:
    """GoF Client: builds the chain and initiates the request."""

    def build_chain(self) -> Handler:
        handler1 = ConcreteHandler1()
        handler2 = ConcreteHandler2()
        handler3 = ConcreteHandler3()
        handler1.set_successor(handler2).set_successor(handler3)
        return handler1

    def run(self, handler: Handler, request: Request) -> None:
        print(f"[Client] {request.ticket_id}: {request.issue} ({request.severity})")
        handler.handle_request(request)


# --- Demo ---

def main() -> None:
    print("=== Chain of Responsibility: service counters ===\n")

    client = Client()
    chain = client.build_chain()

    requests = [
        Request("SR-101", "tyre pressure low", "minor"),
        Request("SR-102", "brake pad wear", "moderate"),
        Request("SR-103", "engine control fault", "critical"),
    ]

    for request in requests:
        client.run(chain, request)
        print()


if __name__ == "__main__":
    main()
