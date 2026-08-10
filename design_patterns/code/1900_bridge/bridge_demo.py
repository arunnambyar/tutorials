"""
Bridge pattern demo — GoF roles (vehicle context).

Run:
    python bridge_demo.py

AbstractionVehicle holds an ImplementorEngine reference (the bridge).
RefinedAbstraction subclasses add chassis details; engine types stay separate.
"""

from abc import ABC, abstractmethod


class ImplementorEngine(ABC):
    """Implementor — engine side of the bridge."""

    @abstractmethod
    def operation_impl(self) -> tuple[str, int]:
        pass


class ConcreteImplementorAPetrolEngine(ImplementorEngine):
    def operation_impl(self) -> tuple[str, int]:
        return "Petrol engine ignited", 110


class ConcreteImplementorBElectricMotor(ImplementorEngine):
    def operation_impl(self) -> tuple[str, int]:
        return "Electric motor online", 150


class AbstractionVehicle(ABC):
    """Abstraction — holds the bridge to an ImplementorEngine."""

    def __init__(self, model: str, implementor: ImplementorEngine) -> None:
        self.model = model
        self._implementor = implementor

    @abstractmethod
    def operation(self) -> None:
        pass


class RefinedAbstractionSedanVehicle(AbstractionVehicle):
    """RefinedAbstraction — sedan chassis; delegates engine work to Implementor."""

    def operation(self) -> None:
        start_msg, power_kw = self._implementor.operation_impl()
        print(f"{self.model}: {start_msg}")
        print("  Chassis: sedan unibody")
        print(f"  Power: {power_kw} kW")
        print("  Payload limit: 450 kg")


class RefinedAbstractionSUVVehicle(AbstractionVehicle):
    """RefinedAbstraction — SUV chassis; same bridge, different abstraction."""

    def operation(self) -> None:
        start_msg, power_kw = self._implementor.operation_impl()
        print(f"{self.model}: {start_msg}")
        print("  Chassis: SUV ladder frame")
        print(f"  Power: {power_kw} kW")
        print("  Payload limit: 750 kg")


class ClientVehicleShowroom:
    """Client — uses AbstractionVehicle only; not a concrete pair."""

    def __init__(self, vehicle: AbstractionVehicle) -> None:
        self._vehicle = vehicle

    def run(self) -> None:
        self._vehicle.operation()


def main() -> None:
    print("=== Bridge pattern demo ===\n")

    configs: list[tuple[str, AbstractionVehicle]] = [
        (
            "Sedan + electric motor",
            RefinedAbstractionSedanVehicle(
                "City Sedan EV", ConcreteImplementorBElectricMotor()
            ),
        ),
        (
            "SUV + petrol engine",
            RefinedAbstractionSUVVehicle(
                "Family SUV", ConcreteImplementorAPetrolEngine()
            ),
        ),
        (
            "SUV + electric motor",
            RefinedAbstractionSUVVehicle(
                "Adventure SUV EV", ConcreteImplementorBElectricMotor()
            ),
        ),
    ]

    for label, vehicle in configs:
        print(f"Case — {label}")
        print(f"  ClientVehicleShowroom uses {vehicle.__class__.__name__}")
        ClientVehicleShowroom(vehicle).run()
        print()


if __name__ == "__main__":
    main()
