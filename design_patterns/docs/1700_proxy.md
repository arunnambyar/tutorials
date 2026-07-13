# Proxy Design Pattern

## On this page

- [What is the Proxy pattern?](#what-is-the-proxy-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Code example](#code-example)
- [Key idea](#key-idea)

## What is the Proxy pattern?

Proxy stands in front of a real object and controls access to it. A remote diagnostic tool can cache reads and check permissions before touching the real ECU.

**Category:** Structural POV

## Car analogy

A remote system that simulates interaction with the real system.

## When should you use it?

Use it for lazy loading, access control, caching, or remote access.

## Code example

```python
"""
Proxy pattern demo: remote diagnostic stand-in for the real ECU.

Run:
    python proxy_demo.py

The proxy adds access control and caching before talking to the real ECU.
"""

from abc import ABC, abstractmethod


class EngineControlUnit(ABC):
    @abstractmethod
    def read_diagnostics(self) -> dict[str, str]:
        pass


class RealECU(EngineControlUnit):
    """Expensive or remote hardware — simulated here with a slow read."""

    def read_diagnostics(self) -> dict[str, str]:
        print("  [Real ECU] Running full onboard scan...")
        return {
            "engine_temp": "92C",
            "battery": "78%",
            "fault_codes": "none",
        }


class RemoteDiagnosticProxy(EngineControlUnit):
    def __init__(self, real_ecu: RealECU) -> None:
        self._real_ecu = real_ecu
        self._cache: dict[str, str] | None = None
        self._authorized = False

    def authorize(self, mechanic_id: str) -> None:
        ok = mechanic_id.startswith("MECH-")
        self._authorized = ok
        status = "granted" if ok else "denied"
        print(f"  [Proxy] Workshop access {status} for {mechanic_id}")

    def read_diagnostics(self) -> dict[str, str]:
        if not self._authorized:
            print("  [Proxy] Blocked: mechanic not authorized")
            return {}

        if self._cache is not None:
            print("  [Proxy] Returning cached diagnostic snapshot")
            return dict(self._cache)

        print("  [Proxy] Forwarding request to real ECU")
        self._cache = self._real_ecu.read_diagnostics()
        return dict(self._cache)


def main() -> None:
    print("=== Proxy: remote ECU diagnostics ===\n")

    proxy = RemoteDiagnosticProxy(RealECU())

    print("First request (unauthorized):")
    print("Result:", proxy.read_diagnostics())

    print("\nAuthorize mechanic and query twice:")
    proxy.authorize("MECH-204")
    print("Result:", proxy.read_diagnostics())
    print("Result:", proxy.read_diagnostics())


if __name__ == "__main__":
    main()
```

**Output:**
```
=== Proxy: remote ECU diagnostics ===

First request (unauthorized):
  [Proxy] Blocked: mechanic not authorized
Result: {}

Authorize mechanic and query twice:
  [Proxy] Workshop access granted for MECH-204
  [Proxy] Forwarding request to real ECU
  [Real ECU] Running full onboard scan...
Result: {'engine_temp': '92C', 'battery': '78%', 'fault_codes': 'none'}
  [Proxy] Returning cached diagnostic snapshot
Result: {'engine_temp': '92C', 'battery': '78%', 'fault_codes': 'none'}
```

Source: [`proxy_demo.py`](../code/1700_proxy/proxy_demo.py)

## Key idea

- The pattern solves a recurring design problem in a reusable way.
- In this example, the car analogy makes the roles of each class easy to remember.
- Run the demo yourself: `python proxy_demo.py` inside `code/1700_proxy/`.

<br/>
<p>
    <span style="float: left;">
        <a href="1600_composite.md">Previous: Composite</a>
        &nbsp;
        <a href="1800_facade.md">Next: Facade</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
