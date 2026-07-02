"""
Composite pattern demo: car assembly as a part tree.

Run:
    python composite_demo.py

Both single parts and assemblies share the same interface; weight rolls up the tree.
"""

from abc import ABC, abstractmethod


class CarPart(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def weight_kg(self) -> float:
        pass

    @abstractmethod
    def describe(self, indent: int = 0) -> None:
        pass


class Part(CarPart):
    def __init__(self, part_name: str, weight: float) -> None:
        self._name = part_name
        self._weight = weight

    def name(self) -> str:
        return self._name

    def weight_kg(self) -> float:
        return self._weight

    def describe(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}- {self._name} ({self._weight} kg)")


class Assembly(CarPart):
    def __init__(self, assembly_name: str) -> None:
        self._name = assembly_name
        self._children: list[CarPart] = []

    def add(self, part: CarPart) -> None:
        self._children.append(part)

    def name(self) -> str:
        return self._name

    def weight_kg(self) -> float:
        return sum(child.weight_kg() for child in self._children)

    def describe(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}+ {self._name} (total {self.weight_kg()} kg)")
        for child in self._children:
            child.describe(indent + 1)


def main() -> None:
    print("=== Composite: car assembly tree ===\n")

    car = Assembly("Complete Car")

    engine = Assembly("Engine Bay")
    engine.add(Part("Engine block", 85.0))
    engine.add(Part("Alternator", 6.5))

    body = Assembly("Body Shell")
    body.add(Part("Chassis frame", 120.0))
    body.add(Part("Doors (set of 4)", 48.0))

    car.add(engine)
    car.add(body)
    car.add(Part("Wheels (set of 4)", 32.0))

    car.describe(0)
    print(f"\nTotal vehicle weight: {car.weight_kg()} kg")


if __name__ == "__main__":
    main()
