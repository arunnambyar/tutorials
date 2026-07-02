"""
Decorator pattern demo: optional features wrapped around a base car.

Run:
    python decorator_demo.py

Each decorator adds behavior without modifying the underlying car class.
"""

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def price_inr(self) -> int:
        pass


class BaseCar(Car):
    def __init__(self, model: str, base_price: int) -> None:
        self._model = model
        self._base_price = base_price

    def description(self) -> str:
        return self._model

    def price_inr(self) -> int:
        return self._base_price


class CarFeatureDecorator(Car):
    def __init__(self, car: Car) -> None:
        self._car = car


class SunroofDecorator(CarFeatureDecorator):
    def description(self) -> str:
        return f"{self._car.description()} + panoramic sunroof"

    def price_inr(self) -> int:
        return self._car.price_inr() + 85000


class PremiumSoundDecorator(CarFeatureDecorator):
    def description(self) -> str:
        return f"{self._car.description()} + premium sound system"

    def price_inr(self) -> int:
        return self._car.price_inr() + 45000


class ADASDecorator(CarFeatureDecorator):
    def description(self) -> str:
        return f"{self._car.description()} + ADAS safety pack"

    def price_inr(self) -> int:
        return self._car.price_inr() + 120000


def main() -> None:
    print("=== Decorator: build-your-own car ===\n")

    car: Car = BaseCar("Compact Hatch", 650000)
    print(f"Base: {car.description()} - Rs {car.price_inr():,}")

    car = SunroofDecorator(car)
    car = PremiumSoundDecorator(car)
    car = ADASDecorator(car)

    print(f"\nConfigured: {car.description()}")
    print(f"Final price: Rs {car.price_inr():,}")


if __name__ == "__main__":
    main()
