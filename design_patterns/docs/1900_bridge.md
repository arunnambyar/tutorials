# Bridge Design Pattern

## On this page

- [What is the Bridge pattern?](#what-is-the-bridge-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Class diagram — Abstraction and Implementor](#class-diagram)
- [Sequence diagram](#sequence-diagram)
- [Code example](#code-example)

## What is the Bridge pattern?

Bridge keeps two parts of a design **separate so each can change on its own**.

One part is the **abstraction** — the thing the Client uses day to day (for example, a vehicle built on a chassis). The other part is the **implementation** — the detail that does the work (for example, the engine). A **bridge** is the link between them: the abstraction holds a reference to an implementation, instead of hard-coding one subclass for every mix.

Without Bridge, you often get an explosion of classes: SedanPetrol, SedanElectric, SUVPetrol, SUVElectric, and so on. With Bridge, chassis types and engine types stay in their own families. You mix them at runtime — same sedan chassis with petrol or electric, same SUV chassis with either engine — without rewriting the chassis hierarchy.

**Category:** Structural POV

## Car analogy

Decouples engine from chassis so they can vary independently.

## When should you use it?

Use it when two dimensions of variation must evolve independently.

## Class Diagram

```mermaid
classDiagram
    direction TB

    class Abstraction["Abstraction (ABC)"] {
        -implementor: Implementor
        +operation()
    }
    class RefinedAbstractionA {
        +operation()
    }
    class RefinedAbstractionB {
        +operation()
    }
    class Implementor["Implementor (ABC)"] {
        +operation_impl()
    }
    class ConcreteImplementorA {
        +operation_impl()
    }
    class ConcreteImplementorB {
        +operation_impl()
    }
    class Client {
        +run()
    }

    Client ..> Abstraction : uses
    Abstraction <|.. RefinedAbstractionA : extends
    Abstraction <|.. RefinedAbstractionB : extends
    Abstraction --> Implementor : has a bridge to Implementor
    Implementor <|.. ConcreteImplementorA : implements
    Implementor <|.. ConcreteImplementorB : implements

    note for Abstraction "Holds a reference to Implementor.<br>Mix any refined abstraction with any<br>concrete implementor at runtime."
    note for Client "Client uses Abstraction.<br>It does not depend on a concrete pair<br>like RefinedAbstractionA + ConcreteImplementorA."
```

<br/>

**Abstraction** is what the Client uses. **RefinedAbstractionA** and **RefinedAbstractionB** are two abstraction-side variants — the diagram shows two, but you can add more. **Implementor** is the separate side that does the real work. The **bridge** is the reference from Abstraction to Implementor — so you can combine any refined abstraction with `ConcreteImplementorA` or `ConcreteImplementorB` without multiplying subclasses.

<br/>

## Sequence Diagram

```mermaid
sequenceDiagram
    Actor Client
    participant Abstraction as RefinedAbstraction
    participant Implementor as ConcreteImplementor

    Client->>Implementor: new ConcreteImplementor()
    Implementor-->>Client: implementor

    Client->>Abstraction: new RefinedAbstraction(implementor)
    Note over Abstraction,Implementor: bridge is set
    Abstraction-->>Client: abstraction

    Client->>Abstraction: operation()
    Abstraction->>Implementor: operation_impl()
    Implementor-->>Abstraction: result
    Abstraction-->>Client: result
```

<br/>

Every step is a request with a response: create the **Implementor**, create the **RefinedAbstraction** with that implementor (the bridge), then call `operation()` → `operation_impl()` and return the result back through the same path. Swap either side — any refined abstraction with any concrete implementor — and the call path stays the same.

<br/>

## Code example

```python
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
```

**Output:**
```
=== Bridge pattern demo ===

Case 1 — Sedan + electric motor
City Sedan EV: Electric motor online
  Chassis: sedan unibody
  Power: 150 kW
  Payload limit: 450 kg

Case 2 — SUV + petrol engine
Family SUV: Petrol engine ignited
  Chassis: SUV ladder frame
  Power: 110 kW
  Payload limit: 750 kg

Case 3 — SUV + electric motor
Adventure SUV EV: Electric motor online
  Chassis: SUV ladder frame
  Power: 150 kW
  Payload limit: 750 kg
```

Source: [`bridge_demo.py`](../code/1900_bridge/bridge_demo.py)

<br/>
<p>
    <span style="float: left;">
        <a href="1800_facade.md">Previous: Facade</a>
        &nbsp;
        <a href="1910_bridge_vs_abstract_factory.md">Next: Bridge vs Abstract Factory</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
