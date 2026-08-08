"""
Adapter pattern demo — GoF Object Adapter (vehicle context).

Run:
    python adapter_demo.py

ClientCarDashboard expects TargetSpeedSensor (km/h).
AdapteeImperialSpeedSensor reports mph.
AdapterImperialToMetric wraps it so the dashboard needs no changes.
"""

from abc import ABC, abstractmethod

MPH_TO_KMH = 1.60934


class TargetSpeedSensor(ABC):
    """Target — interface ClientCarDashboard expects."""

    @abstractmethod
    def read_speed_kmh(self) -> float:
        pass


class ConcreteTargetMetricSpeedSensor(TargetSpeedSensor):
    """ConcreteTarget — already reports km/h."""

    def read_speed_kmh(self) -> float:
        return 100.0


class AdapteeImperialSpeedSensor:
    """Adaptee — existing sensor that reports mph instead."""

    def read_speed_mph(self) -> float:
        return 60.0


class AdapterImperialToMetric(TargetSpeedSensor):
    """Adapter — wraps AdapteeImperialSpeedSensor and exposes km/h."""

    def __init__(self, sensor: AdapteeImperialSpeedSensor) -> None:
        self._sensor = sensor

    def read_speed_kmh(self) -> float:
        mph = self._sensor.read_speed_mph()
        return mph * MPH_TO_KMH


class ClientCarDashboard:
    """Client — works only with TargetSpeedSensor."""

    def __init__(self, sensor: TargetSpeedSensor) -> None:
        self._sensor = sensor

    def show_speed(self) -> None:
        kmh = self._sensor.read_speed_kmh()
        print(f"Dashboard shows: {kmh:.0f} km/h")


def main() -> None:
    print("=== Adapter pattern demo ===\n")

    print("Case 1 - compatible sensor (no adapter)")
    print("  ClientCarDashboard uses ConcreteTargetMetricSpeedSensor directly")
    ClientCarDashboard(ConcreteTargetMetricSpeedSensor()).show_speed()

    print("\nCase 2 - incompatible sensor (adapter in the middle)")
    print("  ClientCarDashboard still calls read_speed_kmh() only")
    legacy_sensor = AdapteeImperialSpeedSensor()
    print(f"  AdapteeImperialSpeedSensor returns: {legacy_sensor.read_speed_mph():.0f} mph")

    adapted_sensor = AdapterImperialToMetric(legacy_sensor)
    print(
        "  AdapterImperialToMetric translates mph -> km/h "
        f"({legacy_sensor.read_speed_mph():.0f} mph -> {adapted_sensor.read_speed_kmh():.0f} km/h)"
    )
    ClientCarDashboard(adapted_sensor).show_speed()


if __name__ == "__main__":
    main()
