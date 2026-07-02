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
