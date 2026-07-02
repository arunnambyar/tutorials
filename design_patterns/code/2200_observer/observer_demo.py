"""
Observer pattern demo: sensors notify the dashboard.

Run:
    python observer_demo.py

Engine sensors publish readings; the dashboard updates automatically.
"""

from abc import ABC, abstractmethod


class DashboardObserver(ABC):
    @abstractmethod
    def update(self, sensor: str, value: float, unit: str) -> None:
        pass


class DigitalDashboard(DashboardObserver):
    def update(self, sensor: str, value: float, unit: str) -> None:
        print(f"  [Dashboard] {sensor}: {value}{unit}")


class CoolantSensor:
    def __init__(self) -> None:
        self._observers: list[DashboardObserver] = []
        self._temperature_c = 85.0

    def attach(self, observer: DashboardObserver) -> None:
        self._observers.append(observer)

    def _notify(self, sensor: str, value: float, unit: str) -> None:
        for observer in self._observers:
            observer.update(sensor, value, unit)

    def read_temperature(self) -> None:
        print(f"[CoolantSensor] Reading {self._temperature_c}C")
        self._notify("Coolant temp", self._temperature_c, "C")

    def simulate_overheat(self) -> None:
        self._temperature_c = 108.0
        print("[CoolantSensor] Overheat detected!")
        self._notify("Coolant temp", self._temperature_c, "C")


class OilPressureSensor:
    def __init__(self) -> None:
        self._observers: list[DashboardObserver] = []

    def attach(self, observer: DashboardObserver) -> None:
        self._observers.append(observer)

    def read_pressure(self, psi: float) -> None:
        print(f"[OilSensor] Reading {psi} psi")
        for observer in self._observers:
            observer.update("Oil pressure", psi, " psi")


def main() -> None:
    print("=== Observer: sensors and dashboard ===\n")

    dashboard = DigitalDashboard()
    coolant = CoolantSensor()
    oil = OilPressureSensor()
    coolant.attach(dashboard)
    oil.attach(dashboard)

    coolant.read_temperature()
    oil.read_pressure(32.5)
    print()
    coolant.simulate_overheat()


if __name__ == "__main__":
    main()
