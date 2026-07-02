"""
Bridge pattern demo: engine and chassis vary independently.

Run:
    python bridge_demo.py

Vehicle ties an Engine implementation to a Chassis without inheritance explosion.
"""

from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def power_kw(self) -> int:
        pass


class PetrolEngine(Engine):
    def start(self) -> str:
        return "Petrol engine ignited"

    def power_kw(self) -> int:
        return 110


class ElectricMotor(Engine):
    def start(self) -> str:
        return "Electric motor online"

    def power_kw(self) -> int:
        return 150


class Chassis(ABC):
    @abstractmethod
    def frame_type(self) -> str:
        pass

    @abstractmethod
    def max_payload_kg(self) -> int:
        pass


class SedanChassis(Chassis):
    def frame_type(self) -> str:
        return "sedan unibody"

    def max_payload_kg(self) -> int:
        return 450


class SUVChassis(Chassis):
    def frame_type(self) -> str:
        return "SUV ladder frame"

    def max_payload_kg(self) -> int:
        return 750


class Vehicle:
    """Bridge between engine and chassis - mix any pair at runtime."""

    def __init__(self, model: str, engine: Engine, chassis: Chassis) -> None:
        self.model = model
        self._engine = engine
        self._chassis = chassis

    def drive_off(self) -> None:
        print(f"{self.model}: {self._engine.start()}")
        print(f"  Chassis: {self._chassis.frame_type()}")
        print(f"  Power: {self._engine.power_kw()} kW")
        print(f"  Payload limit: {self._chassis.max_payload_kg()} kg")


def main() -> None:
    print("=== Bridge: engine + chassis combos ===\n")

    configs = [
        Vehicle("City Sedan EV", ElectricMotor(), SedanChassis()),
        Vehicle("Family SUV", PetrolEngine(), SUVChassis()),
        Vehicle("Adventure SUV EV", ElectricMotor(), SUVChassis()),
    ]

    for car in configs:
        car.drive_off()
        print()


if __name__ == "__main__":
    main()
