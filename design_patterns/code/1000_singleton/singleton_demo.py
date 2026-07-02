"""
Singleton pattern demo: one ECU for the whole car.

Run:
    python singleton_demo.py

Only one engine control unit (ECU) exists—shared across the system.
"""

from __future__ import annotations


class ECU:
    """Single shared engine control unit for the vehicle."""

    _instance: ECU | None = None

    def __new__(cls) -> ECU:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self.firmware_version = "v2.1"
        self.engine_map = "eco"
        self._initialized = True

    def calibrate_sensors(self) -> str:
        return f"ECU {self.firmware_version} calibrating sensors ({self.engine_map} map)"

    def set_drive_mode(self, mode: str) -> None:
        self.engine_map = mode


class Dashboard:
    def __init__(self) -> None:
        self._ecu = ECU()

    def show_status(self) -> None:
        print(f"Dashboard reads ECU: {self._ecu.calibrate_sensors()}")


class EngineBay:
    def __init__(self) -> None:
        self._ecu = ECU()

    def sync_timing(self) -> None:
        print(f"Engine bay synced with ECU: {self._ecu.firmware_version}")


def main() -> None:
    print("=== Singleton: shared ECU ===\n")

    dashboard = Dashboard()
    engine_bay = EngineBay()

    dashboard.show_status()
    engine_bay.sync_timing()

    ecu_a = ECU()
    ecu_b = ECU()
    ecu_a.set_drive_mode("sport")

    print()
    print(f"Same ECU instance? {ecu_a is ecu_b}")
    print(f"Dashboard sees updated mode: {dashboard._ecu.calibrate_sensors()}")


if __name__ == "__main__":
    main()
