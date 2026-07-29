"""
Factory Method pattern demo: car factory picks the model to build.

Run:
    python factory_method_demo.py

A car factory decides which model to produce based on order type.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, seats: int) -> None:
        self.model = model
        self.seats = seats

    @abstractmethod
    def drive(self) -> str:
        pass


class Sedan(Car):
    def drive(self) -> str:
        return f"{self.model} sedan glides smoothly on the highway"


class SUV(Car):
    def drive(self) -> str:
        return f"{self.model} SUV climbs the rough trail with ease"


class CarFactory(ABC):
    @abstractmethod
    def create_car(self, model: str) -> Car:
        pass

    def fulfill_order(self, model: str) -> Car:
        car = self.create_car(model)
        print(f"Factory built: {car.model} ({car.seats} seats)")
        return car


class SedanFactory(CarFactory):
    def create_car(self, model: str) -> Car:
        return Sedan(model, seats=5)


class SUVFactory(CarFactory):
    def create_car(self, model: str) -> Car:
        return SUV(model, seats=7)


def main() -> None:
    print("=== Factory Method: model-specific factory ===\n")

    orders = [
        (SedanFactory(), "Aurora"),
        (SUVFactory(), "TrailBlazer"),
        (SedanFactory(), "Aurora LX"),
    ]

    for factory, model in orders:
        car = factory.fulfill_order(model)
        print(f"  -> {car.drive()}")
        print()


if __name__ == "__main__":
    main()
