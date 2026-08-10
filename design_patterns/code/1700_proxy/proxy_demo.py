"""
Proxy pattern demo: stand-in for the real ECU.

Run:
    python proxy_demo.py

The proxy creates the real ECU and checks access before calling it.
"""

from abc import ABC, abstractmethod


class EngineControlUnit(ABC):
    @abstractmethod
    def read_status(self) -> str:
        pass


class RealECU(EngineControlUnit):
    """The real object — slow or remote hardware."""

    def read_status(self) -> str:
        print("  [Real ECU] Reading sensors...")
        return "Engine OK"


class ECUProxy(EngineControlUnit):
    """Proxy — creates and owns RealECU; controls access to it."""

    def __init__(self) -> None:
        self._real_ecu = RealECU()
        self._locked = True

    def unlock(self) -> None:
        self._locked = False
        print("  [Proxy] Access unlocked")

    def read_status(self) -> str:
        if self._locked:
            print("  [Proxy] Blocked — unlock first")
            return "Access denied"

        print("  [Proxy] Forwarding to real ECU")
        return self._real_ecu.read_status()


def main() -> None:
    print("=== Proxy: ECU access ===\n")

    proxy = ECUProxy()

    print("Without unlock:", proxy.read_status())
    print()
    proxy.unlock()
    print("After unlock:", proxy.read_status())


if __name__ == "__main__":
    main()
