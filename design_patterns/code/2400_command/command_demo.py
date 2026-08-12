"""
Command pattern demo. Run: python command_demo.py
"""

from abc import ABC, abstractmethod


# --- Receiver ---

class Engine:
    def __init__(self) -> None:
        self.running = False

    def start(self) -> None:
        if self.running:
            print("  [Engine] Already running")
            return
        self.running = True
        print("  [Engine] Ignition on - engine started")

    def stop(self) -> None:
        if not self.running:
            print("  [Engine] Already stopped")
            return
        self.running = False
        print("  [Engine] Engine stopped")


# --- Command ---

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class EngineCommand(Command):
    def __init__(self, engine: Engine) -> None:
        self._engine = engine


class StartEngineCommand(EngineCommand):
    def execute(self) -> None:
        print("[Command] StartEngine.execute()")
        self._engine.start()


class StopEngineCommand(EngineCommand):
    def execute(self) -> None:
        print("[Command] StopEngine.execute()")
        self._engine.stop()


# --- Invoker ---

class StartStopButton:
    def __init__(self) -> None:
        self._command: Command | None = None

    def set_command(self, command: Command) -> None:
        self._command = command

    def press(self) -> None:
        print("[Button] Pressed")
        if self._command:
            self._command.execute()


# --- Demo ---

def main() -> None:
    print("=== Command: start/stop button ===\n")

    engine = Engine()
    button = StartStopButton()

    button.set_command(StartEngineCommand(engine))
    button.press()

    print()
    button.set_command(StopEngineCommand(engine))
    button.press()


if __name__ == "__main__":
    main()
