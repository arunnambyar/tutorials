# Composite Design Pattern

## On this page

- [What is the Composite pattern?](#what-is-the-composite-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Code example](#code-example)
- [Key idea](#key-idea)

## What is the Composite pattern?

Composite treats single parts and groups of parts the same way. A car assembly can contain sub-assemblies, each with its own weight.

**Category:** Structural POV

## Car analogy

Repeating object structure like a tree (e.g., folder/file structure).

## When should you use it?

Use it when you have tree structures and want one common operation across leaves and branches.

## Code example

```python
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
```

**Output:**
```
=== Composite: car assembly tree ===

+ Complete Car (total 291.5 kg)
  + Engine Bay (total 91.5 kg)
    - Engine block (85.0 kg)
    - Alternator (6.5 kg)
  + Body Shell (total 168.0 kg)
    - Chassis frame (120.0 kg)
    - Doors (set of 4) (48.0 kg)
  - Wheels (set of 4) (32.0 kg)

Total vehicle weight: 291.5 kg
```

Source: [`composite_demo.py`](../code/1600_composite/composite_demo.py)

## Key idea

- The pattern solves a recurring design problem in a reusable way.
- In this example, the car analogy makes the roles of each class easy to remember.
- Run the demo yourself: `python composite_demo.py` inside `code/1600_composite/`.

<br/>
<p>
    <span style="float: left;">
        <a href="1500_adapter.md">Previous: Adapter</a>
        &nbsp;
        <a href="1700_proxy.md">Next: Proxy</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
