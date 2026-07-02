"""
Facade pattern demo: one-button auto-park interface.

Run:
    python facade_demo.py

AutoPark hides steering, sensors, and braking subsystems behind a single call.
"""

from dataclasses import dataclass


@dataclass
class ParkingSpot:
    label: str
    width_m: float


class UltrasonicSensors:
    def scan(self, spot: ParkingSpot) -> bool:
        fits = spot.width_m >= 2.1
        print(f"  [Sensors] Scanning {spot.label}: space {'OK' if fits else 'too tight'}")
        return fits


class PowerSteering:
    def turn_wheels(self, angle_deg: float) -> None:
        print(f"  [Steering] Turning wheels to {angle_deg} degrees")


class AutoBrake:
    def hold(self) -> None:
        print("  [Brake] Holding vehicle during maneuver")

    def release(self) -> None:
        print("  [Brake] Released - parking complete")


class AutoParkFacade:
    """Single button the driver presses; subsystems stay hidden."""

    def __init__(self) -> None:
        self._sensors = UltrasonicSensors()
        self._steering = PowerSteering()
        self._brake = AutoBrake()

    def park(self, spot: ParkingSpot) -> bool:
        print(f"[AutoPark] Starting park into {spot.label}")
        if not self._sensors.scan(spot):
            print("[AutoPark] Aborted - spot unavailable")
            return False

        self._brake.hold()
        self._steering.turn_wheels(-35)
        self._steering.turn_wheels(0)
        self._brake.release()
        print("[AutoPark] Success - vehicle parked")
        return True


def main() -> None:
    print("=== Facade: auto-park button ===\n")

    auto_park = AutoParkFacade()
    auto_park.park(ParkingSpot("Slot B12", 2.4))

    print()
    auto_park.park(ParkingSpot("Slot A03", 1.8))


if __name__ == "__main__":
    main()
