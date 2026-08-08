"""Generate SVG diagrams and markdown docs for design pattern tutorials."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CODE = ROOT / "code"
STATIC = ROOT / "static"
PYTHON = Path(sys.executable)

PATTERNS = [
    {
        "num": "1000",
        "slug": "singleton",
        "title": "Singleton",
        "category": "Creational",
        "analogy": "Only one engine control unit (ECU) exists—shared across the system.",
        "summary": "Singleton makes sure a class has only one shared instance. Every part of the car that talks to the ECU uses the same object.",
        "when": "Use it when exactly one shared resource must exist, such as configuration, logging, or a hardware controller.",
        "svg_title": "UML class diagram — one ECU class, one shared instance",
        "custom_svg": True,
        "svg_nodes": [("Dashboard", 80, 120), ("ECU", 320, 120), ("Engine Bay", 560, 120)],
        "svg_edges": [(0, 1), (2, 1)],
    },
    {
        "num": "1100",
        "slug": "prototype",
        "title": "Prototype",
        "category": "Creational",
        "analogy": "Clone and update an existing car design to make a new car design.",
        "summary": "Prototype copies an existing object instead of building from scratch. Start from a base design, clone it, then tweak the copy.",
        "when": "Use it when creating a new object is costly and small changes to an existing template are enough.",
        "svg_title": "Clone a base car design, then customize",
        "svg_nodes": [("Base Design", 120, 120), ("Clone", 320, 80), ("Sport Variant", 520, 80), ("Family Variant", 520, 160)],
        "svg_edges": [(0, 1), (1, 2), (1, 3)],
    },
    {
        "num": "1200",
        "slug": "factory_method",
        "title": "Factory Method",
        "category": "Creational",
        "analogy": "A car factory decides which model to produce based on order type.",
        "summary": "Factory Method lets subclasses decide which object to create. The factory receives an order and builds the right car model.",
        "when": "Use it when object creation depends on input type but the creation steps should stay in one place.",
        "svg_title": "Factory chooses sedan or SUV from order type",
        "svg_nodes": [("Order", 100, 120), ("Car Factory", 320, 120), ("Sedan", 540, 80), ("SUV", 540, 160)],
        "svg_edges": [(0, 1), (1, 2), (1, 3)],
    },
    {
        "num": "1300",
        "slug": "abstract_factory",
        "title": "Abstract Factory",
        "category": "Creational",
        "analogy": "A manufacturer picks sedan or SUV factory line; each factory builds matched parts.",
        "summary": "Abstract Factory creates families of related products. Pick sedan or SUV line, then get matching engine and body together.",
        "when": "Use it when you must create groups of related objects that must work together.",
        "svg_title": "Manufacturer picks a matching product family",
        "svg_nodes": [("Bulk Order", 90, 120), ("Manufacturer", 280, 120), ("Sedan Factory", 500, 70), ("SUV Factory", 500, 170)],
        "svg_edges": [(0, 1), (1, 2), (1, 3)],
    },
    {
        "num": "1400",
        "slug": "builder",
        "title": "Builder",
        "category": "Creational",
        "analogy": "Build a car step-by-step: chassis fitting, engine fitting, electric work, paint.",
        "summary": "Builder constructs a complex object step by step. The same builder can follow different recipes for city or sport cars.",
        "when": "Use it when an object has many optional parts and you want readable assembly steps.",
        "svg_title": "Step-by-step car assembly",
        "svg_nodes": [("Builder", 120, 120), ("Chassis", 300, 60), ("Engine", 300, 120), ("Paint", 300, 180), ("Car", 520, 120)],
        "svg_edges": [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4)],
    },
    {
        "num": "1500",
        "slug": "adapter",
        "title": "Adapter",
        "category": "Structural",
        "analogy": "Like an adapter between an Indian plug and a European socket.",
        "summary": "Adapter makes two incompatible interfaces work together. A travel adapter lets an Indian charger plug into a European socket.",
        "when": "Use it when existing code cannot be changed but must work with a different interface.",
        "svg_title": "Adapter connects incompatible plug and socket",
        "svg_nodes": [("Indian Plug", 80, 120), ("Adapter", 320, 120), ("EU Socket", 560, 120)],
        "svg_edges": [(0, 1), (1, 2)],
    },
    {
        "num": "1600",
        "slug": "composite",
        "title": "Composite",
        "category": "Structural",
        "analogy": "Repeating object structure like a tree (e.g., folder/file structure).",
        "summary": "Composite treats single parts and groups of parts the same way. A car assembly can contain sub-assemblies, each with its own weight.",
        "when": "Use it when you have tree structures and want one common operation across leaves and branches.",
        "svg_title": "Car assembly tree with parts and sub-assemblies",
        "svg_nodes": [("Car", 320, 60), ("Body", 180, 140), ("Powertrain", 460, 140), ("Door", 100, 220), ("Engine", 520, 220)],
        "svg_edges": [(0, 1), (0, 2), (1, 3), (2, 4)],
    },
    {
        "num": "1700",
        "slug": "proxy",
        "title": "Proxy",
        "category": "Structural",
        "analogy": "A remote system that simulates interaction with the real system.",
        "summary": "Proxy stands in front of a real object and controls access to it. A remote diagnostic tool can cache reads and check permissions before touching the real ECU.",
        "when": "Use it for lazy loading, access control, caching, or remote access.",
        "svg_title": "Proxy controls access to the real ECU",
        "svg_nodes": [("Client", 80, 120), ("Remote Proxy", 320, 120), ("Real ECU", 560, 120)],
        "svg_edges": [(0, 1), (1, 2)],
    },
    {
        "num": "1800",
        "slug": "facade",
        "title": "Facade",
        "category": "Structural",
        "analogy": "Auto-park feature encapsulates complex subsystems into one interface.",
        "summary": "Facade gives one simple button for a complex system. Auto-park hides sensors, steering, and braking behind a single interface.",
        "when": "Use it when many subsystems must be easy to use from one entry point.",
        "svg_title": "One auto-park button hides many subsystems",
        "svg_nodes": [("Driver", 80, 120), ("Auto Park", 320, 120), ("Sensors", 540, 60), ("Steering", 540, 120), ("Brakes", 540, 180)],
        "svg_edges": [(0, 1), (1, 2), (1, 3), (1, 4)],
    },
    {
        "num": "1900",
        "slug": "bridge",
        "title": "Bridge",
        "category": "Structural",
        "analogy": "Decouples engine from chassis so they can vary independently.",
        "summary": "Bridge splits abstraction from implementation. The same chassis platform can pair with different engine types without tight coupling.",
        "when": "Use it when two dimensions of variation must evolve independently.",
        "svg_title": "Chassis and engine vary independently",
        "svg_nodes": [("Vehicle", 320, 60), ("Chassis", 180, 150), ("Engine", 460, 150), ("SUV Frame", 100, 240), ("V8 Engine", 540, 240)],
        "svg_edges": [(0, 1), (0, 2), (1, 3), (2, 4)],
    },
    {
        "num": "2000",
        "slug": "decorator",
        "title": "Decorator",
        "category": "Structural",
        "analogy": 'Wraps a real object to change "access behavior" without altering the object.',
        "summary": "Decorator adds features by wrapping an object. You can stack sunroof, sound, and safety packages on a base car without changing the base class.",
        "when": "Use it when behavior should be added flexibly at runtime.",
        "svg_title": "Optional features wrap the base car",
        "svg_nodes": [("Base Car", 120, 120), ("Sunroof Wrap", 300, 120), ("Sound Wrap", 480, 120), ("Final Car", 660, 120)],
        "svg_edges": [(0, 1), (1, 2), (2, 3)],
    },
    {
        "num": "2100",
        "slug": "template_method",
        "title": "Template Method",
        "category": "Behavioral",
        "analogy": "Think of a car's overall design as a template—its rear design is a customizable step.",
        "summary": "Template Method defines fixed steps with customizable parts. Hatchback and sedan share the same build flow but implement rear design differently.",
        "when": "Use it when several classes share the same workflow but differ in specific steps.",
        "svg_title": "Shared build steps with custom rear design",
        "svg_nodes": [("Car Template", 320, 60), ("Build Frame", 180, 150), ("Install Engine", 320, 150), ("Design Rear", 460, 150), ("Hatchback", 400, 240), ("Sedan", 520, 240)],
        "svg_edges": [(0, 1), (0, 2), (0, 3), (3, 4), (3, 5)],
    },
    {
        "num": "2200",
        "slug": "observer",
        "title": "Observer",
        "category": "Behavioral",
        "analogy": "Sensors notify the dashboard when engine temperature increases.",
        "summary": "Observer lets objects subscribe to changes. When a sensor reading changes, every attached dashboard listener gets updated automatically.",
        "when": "Use it when one event source must notify many listeners without tight coupling.",
        "svg_title": "Sensors publish updates to the dashboard",
        "svg_nodes": [("Coolant Sensor", 120, 80), ("Oil Sensor", 120, 160), ("Dashboard", 520, 120)],
        "svg_edges": [(0, 2), (1, 2)],
    },
    {
        "num": "2300",
        "slug": "strategy",
        "title": "Strategy",
        "category": "Behavioral",
        "analogy": "Choose between eco, sport, or comfort driving modes while driving.",
        "summary": "Strategy swaps algorithms at runtime. The driver picks eco, sport, or comfort mode and the car changes behavior without rewriting the car class.",
        "when": "Use it when you have multiple interchangeable behaviors for the same task.",
        "svg_title": "Driving mode strategy can be swapped at runtime",
        "svg_nodes": [("Driver", 80, 120), ("Car", 320, 120), ("Eco", 540, 60), ("Sport", 540, 120), ("Comfort", 540, 180)],
        "svg_edges": [(0, 1), (1, 2), (1, 3), (1, 4)],
    },
    {
        "num": "2400",
        "slug": "command",
        "title": "Command",
        "category": "Behavioral",
        "analogy": "Pressing a button sends a command to start the engine.",
        "summary": "Command turns a request into an object. A start button does not start the engine directly—it sends a command object that can be queued, logged, or undone.",
        "when": "Use it for buttons, undo/redo, job queues, or remote actions.",
        "svg_title": "Button sends a start-engine command",
        "svg_nodes": [("Start Button", 100, 120), ("Command", 320, 120), ("Engine", 540, 120)],
        "svg_edges": [(0, 1), (1, 2)],
    },
    {
        "num": "2500",
        "slug": "state",
        "title": "State",
        "category": "Behavioral",
        "analogy": "Auto gear vehicles shift gear based on the vehicle's current state.",
        "summary": "State lets an object change behavior when its internal state changes. An automatic gearbox acts differently in park, drive, and reverse.",
        "when": "Use it when an object has many states and behavior changes with each state.",
        "svg_title": "Gearbox behavior depends on current state",
        "svg_nodes": [("Gearbox", 320, 60), ("Park", 120, 170), ("Drive", 320, 170), ("Reverse", 520, 170)],
        "svg_edges": [(0, 1), (0, 2), (0, 3)],
    },
    {
        "num": "2600",
        "slug": "iterator",
        "title": "Iterator",
        "category": "Behavioral",
        "analogy": "Cycle through music tracks or navigation waypoints.",
        "summary": "Iterator walks through a collection without exposing its internal structure. Next and previous buttons move through a playlist one track at a time.",
        "when": "Use it when clients should traverse a collection in a standard way.",
        "svg_title": "Iterator walks through playlist tracks",
        "svg_nodes": [("Playlist", 320, 80), ("Track 1", 160, 180), ("Track 2", 320, 180), ("Track 3", 480, 180), ("Iterator", 320, 260)],
        "svg_edges": [(0, 1), (0, 2), (0, 3), (4, 1), (4, 2), (4, 3)],
    },
    {
        "num": "2700",
        "slug": "interpreter",
        "title": "Interpreter",
        "category": "Behavioral",
        "analogy": 'Voice assistant interprets "Navigate to home" into GPS instructions.',
        "summary": "Interpreter evaluates sentences or expressions in a small language. A voice command is parsed into actions the navigation system understands.",
        "when": "Use it for simple rule languages, command parsers, or expression evaluators.",
        "svg_title": "Voice phrase interpreted into GPS actions",
        "svg_nodes": [("Voice Input", 100, 120), ("Interpreter", 320, 120), ("GPS Action", 540, 120)],
        "svg_edges": [(0, 1), (1, 2)],
    },
    {
        "num": "2800",
        "slug": "chain_of_responsibility",
        "title": "Chain of Responsibility",
        "category": "Behavioral",
        "analogy": "A service request passes through different service counters until one handles it.",
        "summary": "Chain of Responsibility passes a request along a chain until someone handles it. A service ticket may go through basic, specialist, and manager counters.",
        "when": "Use it when more than one handler might process a request and the sender should not know which one will.",
        "svg_title": "Service request moves through counters",
        "svg_nodes": [("Customer", 80, 120), ("Basic Counter", 240, 120), ("Specialist", 400, 120), ("Manager", 560, 120)],
        "svg_edges": [(0, 1), (1, 2), (2, 3)],
    },
]


def make_svg(pattern: dict) -> str:
    nodes = pattern["svg_nodes"]
    edges = pattern["svg_edges"]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="320" viewBox="0 0 720 320">',
        '  <rect width="720" height="320" fill="#f8fafc"/>',
        '  <defs>',
        '    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">',
        '      <path d="M0,0 L8,3 L0,6 Z" fill="#64748b"/>',
        '    </marker>',
        '  </defs>',
        f'  <text x="360" y="28" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="#0f172a">{pattern["svg_title"]}</text>',
    ]
    for start, end in edges:
        x1, y1 = nodes[start][1], nodes[start][2]
        x2, y2 = nodes[end][1], nodes[end][2]
        lines.append(
            f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>'
        )
    for label, x, y in nodes:
        lines.extend(
            [
                f'  <rect x="{x - 70}" y="{y - 24}" width="140" height="48" rx="10" fill="#dbeafe" stroke="#2563eb"/>',
                f'  <text x="{x}" y="{y + 6}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#1e3a8a">{label}</text>',
            ]
        )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def run_demo(code_dir: Path, slug: str) -> str:
    demo = code_dir / f"{slug}_demo.py"
    result = subprocess.run(
        [str(PYTHON), str(demo.name)],
        cwd=code_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout.strip()
    if result.returncode != 0:
        output += f"\n[stderr]\n{result.stderr.strip()}"
    return output


def nav_links(index: int) -> str:
    prev_link = ""
    next_link = ""
    if index > 0:
        prev_p = PATTERNS[index - 1]
        prev_link = f'    <a href="{prev_p["num"]}_{prev_p["slug"]}.md">Previous: {prev_p["title"]}</a>\n'
    else:
        prev_link = '    <a href="index.md">Previous: Index</a>\n'
    if index < len(PATTERNS) - 1:
        next_p = PATTERNS[index + 1]
        next_link = f'    <a href="{next_p["num"]}_{next_p["slug"]}.md">Next: {next_p["title"]}</a>'
    return f"<p align=\"right\">\n{prev_link}{next_link}\n</p>"


def make_markdown(pattern: dict, code_text: str, output: str, index: int) -> str:
    num = pattern["num"]
    slug = pattern["slug"]
    title = pattern["title"]
    demo_name = f"{slug}_demo.py"
    return f"""# {title} Design Pattern

<p align="center">
    <img src="../static/{num}_{slug}/{slug}_diagram.svg" width="90%">
</p>

<p align="center"><strong>Fig:</strong> {pattern["svg_title"]}</p>

## What is the {title} pattern?

{pattern["summary"]}

**Category:** {pattern["category"]} POV

## Car analogy

{pattern["analogy"]}

## When should you use it?

{pattern["when"]}

## Code example

```python
{code_text.strip()}
```

**Output:**
```
{output}
```

Source: [`{demo_name}`](../code/{num}_{slug}/{demo_name})

## Key idea

- The pattern solves a recurring design problem in a reusable way.
- In this example, the car analogy makes the roles of each class easy to remember.
- Run the demo yourself: `python {demo_name}` inside `code/{num}_{slug}/`.

{nav_links(index)}
"""


def main() -> None:
    for index, pattern in enumerate(PATTERNS):
        num = pattern["num"]
        slug = pattern["slug"]
        code_dir = CODE / f"{num}_{slug}"
        static_dir = STATIC / f"{num}_{slug}"
        static_dir.mkdir(parents=True, exist_ok=True)

        svg_path = static_dir / f"{slug}_diagram.svg"
        if not pattern.get("custom_svg"):
            svg_path.write_text(make_svg(pattern), encoding="utf-8")

        demo_path = code_dir / f"{slug}_demo.py"
        code_text = demo_path.read_text(encoding="utf-8")
        output = run_demo(code_dir, slug)

        md_path = DOCS / f"{num}_{slug}.md"
        md_path.write_text(make_markdown(pattern, code_text, output, index), encoding="utf-8")
        print(f"Generated {md_path.name}")


if __name__ == "__main__":
    main()
