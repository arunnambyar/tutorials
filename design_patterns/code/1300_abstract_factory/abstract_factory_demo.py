"""
Abstract Factory pattern demo: manufacturer picks the right factory.

Run:
    python abstract_factory_demo.py

Each abstract factory creates a matched family of engine and body parts.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# --- Products ---


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


# --- Abstract Factory layer ---


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


# --- Client ---


class Manufacturer:
    _factories = {"city fleet": SedanFactory, "adventure fleet": SUVFactory}

    def select_factory(self, order_type: str) -> VehicleFactory:
        factory_cls = self._factories.get(order_type)
        if factory_cls is None:
            raise ValueError(f"Unknown order type: {order_type}")
        return factory_cls()

    def fulfill_order(self, order_type: str, model: str) -> str:
        factory = self.select_factory(order_type)
        print(f"Factory selected -> {factory.__class__.__name__}")
        return factory.assemble_car(model)


def main() -> None:
    print("=== Abstract Factory: matched part families ===\n")

    manufacturer = Manufacturer()
    for order_type, model in [("city fleet", "Metro Sedan"), ("adventure fleet", "Peak SUV")]:
        print(f"Order '{order_type}'")
        print(f"  {manufacturer.fulfill_order(order_type, model)}\n")


if __name__ == "__main__":
    main()
