"""
Adapter pattern demo: plug adapter for an EV charger.

Run:
    python adapter_demo.py

Indian and European plugs differ; an adapter lets one charger work everywhere.
"""

from abc import ABC, abstractmethod


class EuropeanSocket(ABC):
    @abstractmethod
    def supply_230v(self) -> str:
        pass


class EuropeanWallSocket(EuropeanSocket):
    def supply_230v(self) -> str:
        return "230V AC from European socket"


class IndianPlug:
    def connect_240v(self) -> str:
        return "240V AC from Indian plug"


class IndianToEuropeanAdapter(EuropeanSocket):
    """Adapts an Indian plug to fit a European socket interface."""

    def __init__(self, plug: IndianPlug) -> None:
        self._plug = plug

    def supply_230v(self) -> str:
        raw = self._plug.connect_240v()
        return f"Adapted {raw} -> 230V for car charger"


class CarCharger:
    def __init__(self, socket: EuropeanSocket) -> None:
        self._socket = socket

    def start_charging(self) -> None:
        power = self._socket.supply_230v()
        print(f"Car charger connected: {power}")
        print("Charging started...")


def main() -> None:
    print("=== Adapter: EV charger plug ===\n")

    native_socket = EuropeanWallSocket()
    CarCharger(native_socket).start_charging()

    print()
    indian_plug = IndianPlug()
    adapter = IndianToEuropeanAdapter(indian_plug)
    CarCharger(adapter).start_charging()


if __name__ == "__main__":
    main()
