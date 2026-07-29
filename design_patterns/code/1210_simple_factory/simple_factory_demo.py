"""
Simple (Parameterized) Factory demo: createProduct + factory operations.

Run:
    python simple_factory_demo.py

Matches the sequence: instantiate factory, createProduct(product_type),
then run pre/operation/post steps on the product.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, model: str, seats: int) -> None:
        self.model = model
        self.seats = seats

    @abstractmethod
    def operation(self) -> str:
        pass


class Sedan(Product):
    def operation(self) -> str:
        return f"{self.model} sedan glides smoothly on the highway"


class SUV(Product):
    def operation(self) -> str:
        return f"{self.model} SUV climbs the rough trail with ease"


class SimpleFactory:
    def create_product(self, product_type: str, model: str) -> Product:
        if product_type == "sedan":
            return Sedan(model, seats=5)
        if product_type == "suv":
            return SUV(model, seats=7)
        raise ValueError(f"Unknown product type: {product_type}")

    def run_factory_operations(self, product: Product) -> str:
        print("  perform pre operations")
        result = product.operation()
        print("  perform post operations")
        return result


def main() -> None:
    print("=== Simple Factory: parameter picks the product ===\n")

    factory = SimpleFactory()
    orders = [
        ("sedan", "Aurora"),
        ("suv", "TrailBlazer"),
        ("sedan", "Aurora LX"),
    ]

    for product_type, model in orders:
        print(f"Order: {product_type} / {model}")
        product = factory.create_product(product_type, model)
        print(f"  product creation completed -> {product.__class__.__name__} ({product.seats} seats)")

        print("  trigger factory operations")
        outcome = factory.run_factory_operations(product)
        print(f"  factory operations achieved -> {outcome}\n")


if __name__ == "__main__":
    main()
