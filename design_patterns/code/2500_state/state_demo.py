"""
State pattern demo. Run: python state_demo.py
"""

from abc import ABC, abstractmethod


# --- State ---

class CarState(ABC):
    @abstractmethod
    def start(self, car: "Car") -> None:
        pass

    @abstractmethod
    def accelerate(self, car: "Car") -> None:
        pass

    @abstractmethod
    def stop(self, car: "Car") -> None:
        pass


class OffState(CarState):
    def start(self, car: "Car") -> None:
        print("  [Car] Engine started (Off -> Idle)")
        car.set_state(IdleState())

    def accelerate(self, car: "Car") -> None:
        print("  [Car] Can't move - engine is off")

    def stop(self, car: "Car") -> None:
        print("  [Car] Already off")


class IdleState(CarState):
    def start(self, car: "Car") -> None:
        print("  [Car] Already running")

    def accelerate(self, car: "Car") -> None:
        print("  [Car] Moving (Idle -> Driving)")
        car.set_state(DrivingState())

    def stop(self, car: "Car") -> None:
        print("  [Car] Engine stopped (Idle -> Off)")
        car.set_state(OffState())


class DrivingState(CarState):
    def start(self, car: "Car") -> None:
        print("  [Car] Already driving")

    def accelerate(self, car: "Car") -> None:
        print("  [Car] Already moving")

    def stop(self, car: "Car") -> None:
        print("  [Car] Slowed to idle (Driving -> Idle)")
        car.set_state(IdleState())


# --- Context ---

class Car:
    def __init__(self) -> None:
        self._state: CarState = OffState()

    def set_state(self, state: CarState) -> None:
        self._state = state

    def start(self) -> None:
        self._state.start(self)

    def accelerate(self) -> None:
        self._state.accelerate(self)

    def stop(self) -> None:
        self._state.stop(self)


# --- Demo ---

def main() -> None:
    print("=== State: car power (Off / Idle / Driving) ===\n")

    car = Car()

    car.accelerate()   # ignored - still Off
    car.start()        # Off -> Idle
    car.accelerate()   # Idle -> Driving
    car.accelerate()   # already Driving
    car.stop()         # Driving -> Idle
    car.stop()         # Idle -> Off


if __name__ == "__main__":
    main()
