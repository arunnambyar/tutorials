# Abstract Factory Design Pattern

## On this page

- [What is the Abstract Factory pattern?](#what-is-the-abstract-factory-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Code example](#code-example)
- [Key idea](#key-idea)

## What is the Abstract Factory pattern?

Abstract Factory creates families of related products. One manufacturer picks a sedan line or SUV line and gets matching parts together.

**Category:** Creational POV

## Car analogy

A manufacturer decides which factory to use based on a bulk order.

## When should you use it?

Use it when you must create groups of related objects that must work together.

## Code example

```python
"""
Abstract Factory pattern demo: manufacturer picks the right factory.

Run:
    python abstract_factory_demo.py

A manufacturer decides which factory to use based on a bulk order.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def spec(self) -> str:
        pass


class Body(ABC):
    @abstractmethod
    def spec(self) -> str:
        pass


class SedanEngine(Engine):
    def spec(self) -> str:
        return "1.5L turbo sedan engine"


class SedanBody(Body):
    def spec(self) -> str:
        return "low-profile sedan body"


class SUVEngine(Engine):
    def spec(self) -> str:
        return "2.0L VVT SUV engine"


class SUVBody(Body):
    def spec(self) -> str:
        return "high-clearance SUV body"


class VehicleFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_body(self) -> Body:
        pass

    def assemble_car(self, model: str) -> str:
        return f"{model}: {self.create_body().spec()} + {self.create_engine().spec()}"


class SedanFactory(VehicleFactory):
    def create_engine(self) -> Engine:
        return SedanEngine()

    def create_body(self) -> Body:
        return SedanBody()


class SUVFactory(VehicleFactory):
    def create_engine(self) -> Engine:
        return SUVEngine()

    def create_body(self) -> Body:
        return SUVBody()


class Manufacturer:
    _factories = {"city fleet": SedanFactory, "adventure fleet": SUVFactory}

    def select_factory(self, order_type: str) -> VehicleFactory:
        factory_cls = self._factories.get(order_type)
        if factory_cls is None:
            raise ValueError(f"Unknown order type: {order_type}")
        return factory_cls()


def main() -> None:
    print("=== Abstract Factory: matched part families ===\n")

    manufacturer = Manufacturer()
    for order_type, model in [("city fleet", "Metro Sedan"), ("adventure fleet", "Peak SUV")]:
        factory = manufacturer.select_factory(order_type)
        print(f"Order '{order_type}' -> {factory.__class__.__name__}")
        print(f"  {factory.assemble_car(model)}\n")


if __name__ == "__main__":
    main()
```

**Output:**
```
=== Abstract Factory: matched part families ===

Order 'city fleet' -> SedanFactory
  Metro Sedan: low-profile sedan body + 1.5L turbo sedan engine

Order 'adventure fleet' -> SUVFactory
  Peak SUV: high-clearance SUV body + 2.0L VVT SUV engine
```

Source: [`abstract_factory_demo.py`](../code/1300_abstract_factory/abstract_factory_demo.py)

## Key idea

- The pattern solves a recurring design problem in a reusable way.
- In this example, the car analogy makes the roles of each class easy to remember.
- Run the demo yourself: `python abstract_factory_demo.py` inside `code/1300_abstract_factory/`.

<br/>
<p>
    <span style="float: left;">
        <a href="1200_factory_method.md">Previous: Factory Method</a>
        &nbsp;
        <a href="1400_builder.md">Next: Builder</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
