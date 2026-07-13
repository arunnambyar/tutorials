# Command Design Pattern

## On this page

- [What is the Command pattern?](#what-is-the-command-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Code example](#code-example)
- [Key idea](#key-idea)

## What is the Command pattern?

Command turns a request into an object. A start button does not start the engine directly—it sends a command object that can be queued, logged, or undone.

**Category:** Behavioral POV

## Car analogy

Pressing a button sends a command to start the engine.

## When should you use it?

Use it for buttons, undo/redo, job queues, or remote actions.

## Code example

```python
"""
Command pattern demo: button sends start-engine command.

Run:
    python command_demo.py

The start button does not start the engine directly; it invokes a command object.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


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


class StartEngineCommand(Command):
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def execute(self) -> None:
        print("[Command] StartEngine.execute()")
        self._engine.start()


class StopEngineCommand(Command):
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def execute(self) -> None:
        print("[Command] StopEngine.execute()")
        self._engine.stop()


class StartStopButton:
    def __init__(self) -> None:
        self._command: Command | None = None

    def set_command(self, command: Command) -> None:
        self._command = command

    def press(self) -> None:
        print("[Button] Pressed")
        if self._command:
            self._command.execute()


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
```

**Output:**
```
=== Command: start/stop button ===

[Button] Pressed
[Command] StartEngine.execute()
  [Engine] Ignition on - engine started

[Button] Pressed
[Command] StopEngine.execute()
  [Engine] Engine stopped
```

Source: [`command_demo.py`](../code/2400_command/command_demo.py)

## Key idea

- The pattern solves a recurring design problem in a reusable way.
- In this example, the car analogy makes the roles of each class easy to remember.
- Run the demo yourself: `python command_demo.py` inside `code/2400_command/`.

<br/>
<p>
    <span style="float: left;">
        <a href="2300_strategy.md">Previous: Strategy</a>
        &nbsp;
        <a href="2500_state.md">Next: State</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
