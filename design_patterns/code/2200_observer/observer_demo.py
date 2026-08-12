"""
Observer pattern demo: one sensor notifies the dashboard.

Run:
    python observer_demo.py
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temperature_c: float) -> None:
        pass


class Dashboard(Observer):
    def update(self, temperature_c: float) -> None:
        print(f"  [Dashboard] Coolant: {temperature_c}C")


class CoolantSensor:
    """Subject — notifies attached observers when temperature changes."""

    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature_c = 85.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def set_temperature(self, temperature_c: float) -> None:
        self._temperature_c = temperature_c
        print(f"[Sensor] Temperature is now {temperature_c}C")
        for observer in self._observers:
            observer.update(temperature_c)


def main() -> None:
    print("=== Observer: sensor -> dashboard ===\n")

    sensor = CoolantSensor()
    sensor.attach(Dashboard())

    sensor.set_temperature(85.0)
    sensor.set_temperature(108.0)


if __name__ == "__main__":
    main()
