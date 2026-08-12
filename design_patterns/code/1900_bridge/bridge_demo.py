"""
Bridge pattern demo. Run: python bridge_demo.py
"""

from abc import ABC, abstractmethod


# --- Implementor ---

class ImplementorEngine(ABC):
    @abstractmethod
    def operation_impl(self) -> tuple[str, int]:
        pass


class ConcreteImplementorAPetrolEngine(ImplementorEngine):
    def operation_impl(self) -> tuple[str, int]:
        return "Petrol engine ignited", 110


class ConcreteImplementorBElectricMotor(ImplementorEngine):
    def operation_impl(self) -> tuple[str, int]:
        return "Electric motor online", 150


# --- Abstraction ---

class AbstractionVehicle(ABC):
    def __init__(self, model: str, implementor: ImplementorEngine) -> None:
        self.model = model
        self._implementor = implementor

    @abstractmethod
    def operation(self) -> None:
        pass


class RefinedAbstractionSedanVehicle(AbstractionVehicle):
    def operation(self) -> None:
        start_msg, power_kw = self._implementor.operation_impl()
        print(f"{self.model}: {start_msg}")
        print("  Chassis: sedan unibody")
        print(f"  Power: {power_kw} kW")
        print("  Payload limit: 450 kg")


class RefinedAbstractionSUVVehicle(AbstractionVehicle):
    def operation(self) -> None:
        start_msg, power_kw = self._implementor.operation_impl()
        print(f"{self.model}: {start_msg}")
        print("  Chassis: SUV ladder frame")
        print(f"  Power: {power_kw} kW")
        print("  Payload limit: 750 kg")


# --- Client ---

class ClientVehicleShowroom:
    def run(self, vehicle: AbstractionVehicle) -> None:
        vehicle.operation()


# --- Demo ---

def main() -> None:
    print("=== Bridge pattern demo ===\n")
    client = ClientVehicleShowroom()

    # Case 1: Sedan + electric
    print("Case 1 — Sedan + electric motor")
    electric = ConcreteImplementorBElectricMotor()
    sedan_ev = RefinedAbstractionSedanVehicle("City Sedan EV", electric)
    client.run(sedan_ev)
    print()

    # Case 2: SUV + petrol
    print("Case 2 — SUV + petrol engine")
    petrol = ConcreteImplementorAPetrolEngine()
    family_suv = RefinedAbstractionSUVVehicle("Family SUV", petrol)
    client.run(family_suv)
    print()

    # Case 3: SUV + electric
    print("Case 3 — SUV + electric motor")
    electric_again = ConcreteImplementorBElectricMotor()
    adventure_suv = RefinedAbstractionSUVVehicle("Adventure SUV EV", electric_again)
    client.run(adventure_suv)
    print()


if __name__ == "__main__":
    main()
