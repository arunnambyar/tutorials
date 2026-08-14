"""
Interpreter pattern demo. Run: python interpreter_demo.py
"""

from abc import ABC, abstractmethod


# --- Context ---

class Context:
    """GoF Context: global info used while interpreting (variable bindings)."""

    def __init__(self) -> None:
        self._bindings: dict[str, bool] = {}

    def assign(self, name: str, value: bool) -> None:
        self._bindings[name.lower()] = value

    def lookup(self, name: str) -> bool:
        return self._bindings.get(name.lower(), False)


# --- AbstractExpression ---

class AbstractExpression(ABC):
    """GoF AbstractExpression: interpret(context) for one grammar node."""

    @abstractmethod
    def interpret(self, context: Context) -> bool:
        pass


# --- TerminalExpression ---

class TerminalExpression(AbstractExpression):
    """GoF TerminalExpression: a variable / leaf (e.g. rain, fog, night)."""

    def __init__(self, name: str) -> None:
        self._name = name.lower()

    def interpret(self, context: Context) -> bool:
        return context.lookup(self._name)


# --- NonterminalExpression ---

class OrExpression(AbstractExpression):
    """
    GoF NonterminalExpression: aggregates child AbstractExpressions.
    Grammar: <expr> OR <expr> OR ...
    """

    def __init__(self, *children: AbstractExpression) -> None:
        self._children: list[AbstractExpression] = list(children)

    def interpret(self, context: Context) -> bool:
        return any(child.interpret(context) for child in self._children)


class AndExpression(AbstractExpression):
    """
    GoF NonterminalExpression: aggregates child AbstractExpressions.
    Grammar: <expr> AND <expr> AND ...
    """

    def __init__(self, *children: AbstractExpression) -> None:
        self._children: list[AbstractExpression] = list(children)

    def interpret(self, context: Context) -> bool:
        return all(child.interpret(context) for child in self._children)


# --- Client ---

class Client:
    """GoF Client: builds the AST, then calls interpret(context)."""

    def get_context_from_string(self, text: str) -> Context:
        """Split tokens like rain=true fog=false and build a Context."""
        context = Context()
        for token in text.split():
            name, raw_value = token.split("=", 1)
            context.assign(name, raw_value.lower() in ("true", "1", "yes"))
        return context

    def run(self, expression: AbstractExpression, context: Context) -> None:
        result = expression.interpret(context)
        print(f"    [Expression] Evaluates to {result}")


# --- Demo ---

def main() -> None:
    print("=== Interpreter: boolean driving rules ===\n")

    client = Client()

    # Same AST rules, different Context values → different results
    fog_lamps = OrExpression(
        TerminalExpression("rain"),
        TerminalExpression("fog"),
    )
    slow_down = AndExpression(
        TerminalExpression("rain"),
        TerminalExpression("night"),
    )

    print("--- Set 1: rain=true fog=false night=true ---")
    context1 = client.get_context_from_string("rain=true fog=false night=true")
    print("  FOG LAMP")
    client.run(fog_lamps, context1)
    print("  SLOW DOWN")
    client.run(slow_down, context1)

    print()
    print("--- Set 2: rain=false fog=false night=true ---")
    context2 = client.get_context_from_string("rain=false fog=false night=true")
    print("  FOG LAMP")
    client.run(fog_lamps, context2)
    print("  SLOW DOWN")
    client.run(slow_down, context2)


if __name__ == "__main__":
    main()
