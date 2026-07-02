"""
Template Method pattern demo: car body design with customizable rear.

Run:
    python template_method_demo.py

The overall design flow is fixed; hatchback and sedan customize the rear step.
"""

from abc import ABC, abstractmethod


class CarDesign(ABC):
    """Template: same build steps, subclasses customize rear design."""

    def build_car(self) -> None:
        print(f"[Design] Starting {self.model_name()} build")
        self.fit_chassis()
        self.mount_engine()
        self.design_rear()
        self.apply_paint()
        print(f"[Design] {self.model_name()} ready for production\n")

    def fit_chassis(self) -> None:
        print("  [Chassis] Frame welded and aligned")

    def mount_engine(self) -> None:
        print("  [Engine] Turbo unit mounted and calibrated")

    @abstractmethod
    def design_rear(self) -> None:
        pass

    @abstractmethod
    def model_name(self) -> str:
        pass

    def apply_paint(self) -> None:
        print("  [Paint] Base coat and clear coat applied")


class HatchbackDesign(CarDesign):
    def model_name(self) -> str:
        return "Hatchback"

    def design_rear(self) -> None:
        print("  [Rear] Liftgate with integrated spoiler and wide glass")


class SedanDesign(CarDesign):
    def model_name(self) -> str:
        return "Sedan"

    def design_rear(self) -> None:
        print("  [Rear] Trunk lid with chrome trim and LED tail lamps")


def main() -> None:
    print("=== Template Method: car body design ===\n")

    HatchbackDesign().build_car()
    SedanDesign().build_car()


if __name__ == "__main__":
    main()
