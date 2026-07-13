# Chain of Responsibility Design Pattern

## On this page

- [What is the Chain of Responsibility pattern?](#what-is-the-chain-of-responsibility-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Code example](#code-example)
- [Key idea](#key-idea)

## What is the Chain of Responsibility pattern?

Chain of Responsibility passes a request along a chain until someone handles it. A service ticket may go through basic, specialist, and manager counters.

**Category:** Behavioral POV

## Car analogy

A service request passes through different service counters until one handles it.

## When should you use it?

Use it when more than one handler might process a request and the sender should not know which one will.

## Code example

```python
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
```

**Output:**
```
=== Chain of Responsibility: service counters ===

[Ticket] SR-101: tyre pressure low (minor)
  [Quick Service] Fixed tyre pressure low (SR-101)

[Ticket] SR-102: brake pad wear (moderate)
  [Quick Service] Escalating SR-102
  [Workshop] Scheduled brake pad wear (SR-102)

[Ticket] SR-103: engine control fault (critical)
  [Quick Service] Escalating SR-103
  [Workshop] Escalating SR-103
  [Manufacturer] Warranty claim for engine control fault
```

Source: [`chain_of_responsibility_demo.py`](../code/2800_chain_of_responsibility/chain_of_responsibility_demo.py)

## Key idea

- The pattern solves a recurring design problem in a reusable way.
- In this example, the car analogy makes the roles of each class easy to remember.
- Run the demo yourself: `python chain_of_responsibility_demo.py` inside `code/2800_chain_of_responsibility/`.

<br/>
<p>
    <span style="float: left;">
        <a href="2700_interpreter.md">Previous: Interpreter</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
