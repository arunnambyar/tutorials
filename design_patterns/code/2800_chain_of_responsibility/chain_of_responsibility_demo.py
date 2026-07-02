"""
Chain of Responsibility demo: service request through counters.

Run:
    python chain_of_responsibility_demo.py

A service ticket passes along counters until one can handle it.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ServiceRequest:
    ticket_id: str
    issue: str
    severity: str


class ServiceCounter(ABC):
    def __init__(self, desk_name: str) -> None:
        self.desk_name = desk_name
        self._next: ServiceCounter | None = None

    def set_next(self, counter: "ServiceCounter") -> "ServiceCounter":
        self._next = counter
        return counter

    def handle(self, request: ServiceRequest) -> None:
        if self._can_handle(request):
            self._resolve(request)
            return
        if self._next:
            print(f"  [{self.desk_name}] Escalating {request.ticket_id}")
            self._next.handle(request)
        else:
            print(f"  [{self.desk_name}] No desk available for {request.ticket_id}")

    @abstractmethod
    def _can_handle(self, request: ServiceRequest) -> bool:
        pass

    @abstractmethod
    def _resolve(self, request: ServiceRequest) -> None:
        pass


class SeverityDesk(ServiceCounter):
    def __init__(self, desk_name: str, severity: str, action: str) -> None:
        super().__init__(desk_name)
        self._severity = severity
        self._action = action

    def _can_handle(self, request: ServiceRequest) -> bool:
        return request.severity == self._severity

    def _resolve(self, request: ServiceRequest) -> None:
        print(f"  [{self.desk_name}] {self._action.format(**request.__dict__)}")


def main() -> None:
    print("=== Chain of Responsibility: service counters ===\n")

    front_desk = SeverityDesk("Quick Service", "minor", "Fixed {issue} ({ticket_id})")
    front_desk.set_next(
        SeverityDesk("Workshop", "moderate", "Scheduled {issue} ({ticket_id})")
    ).set_next(
        SeverityDesk("Manufacturer", "critical", "Warranty claim for {issue}")
    )

    tickets = [
        ServiceRequest("SR-101", "tyre pressure low", "minor"),
        ServiceRequest("SR-102", "brake pad wear", "moderate"),
        ServiceRequest("SR-103", "engine control fault", "critical"),
    ]

    for ticket in tickets:
        print(f"[Ticket] {ticket.ticket_id}: {ticket.issue} ({ticket.severity})")
        front_desk.handle(ticket)
        print()


if __name__ == "__main__":
    main()
