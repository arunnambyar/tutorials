"""
Strategy pattern demo. Run: python strategy_demo.py
"""

from abc import ABC, abstractmethod


# --- Strategy ---

class DrivingMode(ABC):
    @abstractmethod
    def accelerate(self) -> str:
        pass

    @abstractmethod
    def fuel_use(self) -> str:
        pass


class EcoMode(DrivingMode):
    def accelerate(self) -> str:
        return "Gentle throttle, early upshift"

    def fuel_use(self) -> str:
        return "18 km/l estimated"


class SportMode(DrivingMode):
    def accelerate(self) -> str:
        return "Sharp throttle, holds lower gears"

    def fuel_use(self) -> str:
        return "11 km/l estimated"


class ComfortMode(DrivingMode):
    def accelerate(self) -> str:
        return "Smooth power delivery, soft suspension"

    def fuel_use(self) -> str:
        return "15 km/l estimated"


# --- Context ---

class Car:
    def __init__(self, mode: DrivingMode) -> None:
        self._mode = mode

    def set_mode(self, mode: DrivingMode) -> None:
        self._mode = mode

    def drive(self) -> None:
        print(f"  Acceleration: {self._mode.accelerate()}")
        print(f"  Fuel economy: {self._mode.fuel_use()}")


# --- Demo ---

def main() -> None:
    print("=== Strategy: driving modes ===\n")

    car = Car(EcoMode())
    print("[Mode] Eco")
    car.drive()

    print("\n[Mode] Sport")
    car.set_mode(SportMode())
    car.drive()

    print("\n[Mode] Comfort")
    car.set_mode(ComfortMode())
    car.drive()


if __name__ == "__main__":
    main()
