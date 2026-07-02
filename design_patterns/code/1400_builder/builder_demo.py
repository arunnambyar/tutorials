"""
Builder pattern demo: assemble a car step by step.

Run:
    python builder_demo.py

Build a car step-by-step: chassis, engine, wiring, and paint.
"""

from __future__ import annotations


class Car:
    def __init__(self) -> None:
        self.chassis: str | None = None
        self.engine: str | None = None
        self.wiring: str | None = None
        self.paint: str | None = None

    def summary(self) -> str:
        parts = [self.chassis, self.engine, self.wiring, self.paint]
        return " | ".join(part for part in parts if part)


class CarBuilder:
    def __init__(self) -> None:
        self._car = Car()

    def fit_chassis(self, chassis_type: str) -> CarBuilder:
        self._car.chassis = f"chassis: {chassis_type}"
        return self

    def fit_engine(self, engine_type: str) -> CarBuilder:
        self._car.engine = f"engine: {engine_type}"
        return self

    def do_electric_work(self, wiring_package: str) -> CarBuilder:
        self._car.wiring = f"wiring: {wiring_package}"
        return self

    def apply_paint(self, color: str) -> CarBuilder:
        self._car.paint = f"paint: {color}"
        return self

    def build(self) -> Car:
        if not all([self._car.chassis, self._car.engine, self._car.wiring, self._car.paint]):
            raise ValueError("Car is incomplete—finish all build steps first")
        return self._car


class AssemblyLine:
    def build_city_car(self) -> Car:
        return (
            CarBuilder()
            .fit_chassis("compact frame")
            .fit_engine("1.2L efficient")
            .do_electric_work("basic dashboard")
            .apply_paint("pearl white")
            .build()
        )

    def build_sport_car(self) -> Car:
        return (
            CarBuilder()
            .fit_chassis("stiff sport frame")
            .fit_engine("2.5L turbo")
            .do_electric_work("digital cockpit")
            .apply_paint("racing red")
            .build()
        )


def main() -> None:
    print("=== Builder: step-by-step assembly ===\n")

    line = AssemblyLine()

    city_car = line.build_city_car()
    print(f"City car ready: {city_car.summary()}")

    print()
    sport_car = line.build_sport_car()
    print(f"Sport car ready: {sport_car.summary()}")


if __name__ == "__main__":
    main()
