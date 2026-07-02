"""
Interpreter pattern demo: voice command to GPS instructions.

Run:
    python interpreter_demo.py

The voice assistant parses "navigate to home" into concrete navigation steps.
"""

from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict[str, str]) -> str:
        pass


class DestinationExpression(Expression):
    def __init__(self, keyword: str) -> None:
        self._keyword = keyword.lower()

    def interpret(self, context: dict[str, str]) -> str:
        destination = context.get(self._keyword)
        if not destination:
            return f"Unknown destination: {self._keyword}"
        return destination


class NavigateCommand(Expression):
    def __init__(self, destination: Expression) -> None:
        self._destination = destination

    def interpret(self, context: dict[str, str]) -> str:
        address = self._destination.interpret(context)
        return (
            f"Set GPS route to {address}; "
            "enable turn-by-turn; estimate ETA from traffic"
        )


class VoiceAssistant:
    def __init__(self, context: dict[str, str]) -> None:
        self._context = context
        self._phrases: dict[str, Expression] = {
            "navigate to home": NavigateCommand(DestinationExpression("home")),
            "navigate to office": NavigateCommand(DestinationExpression("office")),
        }

    def listen(self, phrase: str) -> None:
        print(f'[Voice] Heard: "{phrase}"')
        command = self._phrases.get(phrase.lower())
        if not command:
            print("  [GPS] Sorry, I did not understand that command")
            return
        result = command.interpret(self._context)
        print(f"  [GPS] {result}")


def main() -> None:
    print("=== Interpreter: voice navigation ===\n")

    assistant = VoiceAssistant(
        {
            "home": "42 Maple Street, Springfield",
            "office": "Tech Park, Block C, Floor 5",
        }
    )

    assistant.listen("navigate to home")
    print()
    assistant.listen("navigate to office")
    print()
    assistant.listen("navigate to mars")


if __name__ == "__main__":
    main()
