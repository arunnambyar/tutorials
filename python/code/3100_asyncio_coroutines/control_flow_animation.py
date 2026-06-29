"""
Generate a GIF showing control flow: event loop (left square) → multi-level
coroutines (right circles) → non-blocking I/O endpoints (leaf boxes).

Only the red arrow animates — it travels forward into coroutines and returns
when control passes back to a parent or the event loop.

Coroutine colors:
  grey   = not run yet
  blue   = running
  yellow = waiting (paused at await / I/O)
  green  = completed

Run:
    pip install matplotlib pillow
    python control_flow_animation.py

Output:
    ../../static/3100_asyncio_coroutines/control_flow_demo.gif
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import patheffects as pe
from PIL import Image

OUTPUT = Path(__file__).resolve().parents[2] / "static/3100_asyncio_coroutines/control_flow_demo.gif"

C_BG = "#f8fafc"
C_TEXT = "#0f172a"
C_MUTED = "#64748b"
C_LOOP = "#1d4ed8"
C_WIRE = "#cbd5e1"
C_ARROW = "#dc2626"

STATE_STYLE = {
    "pending": ("#e2e8f0", "#94a3b8", "not run"),
    "running": ("#dbeafe", "#2563eb", "running"),
    "waiting": ("#fef9c3", "#ca8a04", "waiting"),
    "done": ("#dcfce7", "#16a34a", "completed"),
}

CORO_KEYS = ("a", "a1", "a2", "b", "b1", "c")
IO_KEYS = ("http", "file", "db", "log")

FRAMES_PER_SEGMENT = 2
SEGMENT_MS = 1300
FINAL_HOLD_MS = 9000
FINAL_HOLD_FRAMES = 10


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Node:
    key: str
    center: Point
    label: str
    kind: str  # loop | coro | io
    level: int = 0


@dataclass(frozen=True)
class ControlStep:
    src: str
    dst: str
    caption: str
    coro: dict[str, str]
    io: dict[str, str]


NODES: dict[str, Node] = {
    "loop": Node("loop", Point(1.45, 3.85), "Event\nLoop", "loop", 0),
    "a": Node("a", Point(4.25, 6.25), "Coro A", "coro", 1),
    "a1": Node("a1", Point(6.85, 6.55), "Coro A1", "coro", 2),
    "http": Node("http", Point(9.85, 6.55), "await\nHTTP", "io", 3),
    "a2": Node("a2", Point(6.85, 5.25), "Coro A2", "coro", 2),
    "file": Node("file", Point(9.85, 5.25), "await\nfile", "io", 3),
    "b": Node("b", Point(4.25, 3.85), "Coro B", "coro", 1),
    "b1": Node("b1", Point(6.85, 3.85), "Coro B1", "coro", 2),
    "db": Node("db", Point(9.85, 3.85), "await\nDB", "io", 3),
    "c": Node("c", Point(4.25, 2.05), "Coro C", "coro", 1),
    "log": Node("log", Point(6.85, 2.05), "print()", "io", 2),
}

CORO_RADIUS = 0.30
IO_W, IO_H = 0.95, 0.50
LEVEL_ABOVE = 0.50
IO_TAG_BELOW = 0.62
IO_TAG_ABOVE = 0.30

EDGES: list[tuple[str, str]] = [
    ("loop", "a"),
    ("loop", "b"),
    ("loop", "c"),
    ("a", "a1"),
    ("a1", "http"),
    ("a", "a2"),
    ("a2", "file"),
    ("b", "b1"),
    ("b1", "db"),
    ("c", "log"),
]

P = "pending"
R = "running"
W = "waiting"
D = "done"

CONTROL_STEPS: list[ControlStep] = [
    # --- forward: A chain starts, pauses on I/O ---
    ControlStep("loop", "a", "Loop hands control to Coro A (level 1)", {"a": R, "a1": P, "a2": P, "b": P, "b1": P, "c": P}, {"http": P, "file": P, "db": P, "log": P}),
    ControlStep("a", "a1", "Coro A awaits nested Coro A1 (level 2)", {"a": W, "a1": R, "a2": P, "b": P, "b1": P, "c": P}, {"http": P, "file": P, "db": P, "log": P}),
    ControlStep("a1", "http", "A1 reaches non-blocking HTTP I/O — pauses", {"a": W, "a1": W, "a2": P, "b": P, "b1": P, "c": P}, {"http": W, "file": P, "db": P, "log": P}),
    ControlStep("a1", "a", "Return: A1 at await — control back to Coro A", {"a": W, "a1": W, "a2": P, "b": P, "b1": P, "c": P}, {"http": W, "file": P, "db": P, "log": P}),
    ControlStep("a", "loop", "Return: A at await — control back to event loop", {"a": W, "a1": W, "a2": P, "b": P, "b1": P, "c": P}, {"http": W, "file": P, "db": P, "log": P}),
    # --- forward: B chain while A waits ---
    ControlStep("loop", "b", "Loop switches to Coro B while A1 waits", {"a": W, "a1": W, "a2": P, "b": R, "b1": P, "c": P}, {"http": W, "file": P, "db": P, "log": P}),
    ControlStep("b", "b1", "Coro B awaits nested Coro B1 (level 2)", {"a": W, "a1": W, "a2": P, "b": W, "b1": R, "c": P}, {"http": W, "file": P, "db": P, "log": P}),
    ControlStep("b1", "db", "B1 reaches non-blocking DB I/O — pauses", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": P}, {"http": W, "file": P, "db": W, "log": P}),
    ControlStep("b1", "b", "Return: B1 at await — control back to Coro B", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": P}, {"http": W, "file": P, "db": W, "log": P}),
    ControlStep("b", "loop", "Return: B at await — control back to event loop", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": P}, {"http": W, "file": P, "db": W, "log": P}),
    # --- forward + return: C runs and only C completes ---
    ControlStep("loop", "c", "Loop switches to Coro C", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": R}, {"http": W, "file": P, "db": W, "log": P}),
    ControlStep("c", "log", "Coro C calls non-blocking print()", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": R}, {"http": W, "file": P, "db": W, "log": R}),
    ControlStep("log", "c", "Return: control leaves print() back to Coro C", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": R}, {"http": W, "file": P, "db": W, "log": D}),
    ControlStep("c", "loop", "Return: Coro C completes — only C is done so far", {"a": W, "a1": W, "a2": P, "b": W, "b1": W, "c": D}, {"http": W, "file": P, "db": W, "log": D}),
    # --- resume A chain: A1 then A2 then A ---
    ControlStep("loop", "a", "Loop resumes Coro A", {"a": R, "a1": W, "a2": P, "b": W, "b1": W, "c": D}, {"http": W, "file": P, "db": W, "log": D}),
    ControlStep("a", "a1", "Coro A awaits Coro A1 again", {"a": W, "a1": R, "a2": P, "b": W, "b1": W, "c": D}, {"http": W, "file": P, "db": W, "log": D}),
    ControlStep("http", "a1", "Return: HTTP I/O done — control back to A1", {"a": W, "a1": R, "a2": P, "b": W, "b1": W, "c": D}, {"http": D, "file": P, "db": W, "log": D}),
    ControlStep("a1", "a", "Return: Coro A1 completes — control back to A", {"a": R, "a1": D, "a2": P, "b": W, "b1": W, "c": D}, {"http": D, "file": P, "db": W, "log": D}),
    ControlStep("a", "a2", "Coro A awaits nested Coro A2 (level 2)", {"a": W, "a1": D, "a2": R, "b": W, "b1": W, "c": D}, {"http": D, "file": P, "db": W, "log": D}),
    ControlStep("a2", "file", "A2 reaches non-blocking file I/O — pauses", {"a": W, "a1": D, "a2": W, "b": W, "b1": W, "c": D}, {"http": D, "file": W, "db": W, "log": D}),
    ControlStep("file", "a2", "Return: file I/O done — control back to A2", {"a": W, "a1": D, "a2": R, "b": W, "b1": W, "c": D}, {"http": D, "file": D, "db": W, "log": D}),
    ControlStep("a2", "a", "Return: Coro A2 completes — control back to A", {"a": R, "a1": D, "a2": D, "b": W, "b1": W, "c": D}, {"http": D, "file": D, "db": W, "log": D}),
    ControlStep("a", "loop", "Return: Coro A completes — control back to loop", {"a": D, "a1": D, "a2": D, "b": W, "b1": W, "c": D}, {"http": D, "file": D, "db": W, "log": D}),
    # --- resume B chain: B1 then B ---
    ControlStep("loop", "b", "Loop resumes Coro B", {"a": D, "a1": D, "a2": D, "b": R, "b1": W, "c": D}, {"http": D, "file": D, "db": W, "log": D}),
    ControlStep("b", "b1", "Coro B awaits Coro B1 again", {"a": D, "a1": D, "a2": D, "b": W, "b1": R, "c": D}, {"http": D, "file": D, "db": W, "log": D}),
    ControlStep("db", "b1", "Return: DB I/O done — control back to B1", {"a": D, "a1": D, "a2": D, "b": W, "b1": R, "c": D}, {"http": D, "file": D, "db": D, "log": D}),
    ControlStep("b1", "b", "Return: Coro B1 completes — control back to B", {"a": D, "a1": D, "a2": D, "b": R, "b1": D, "c": D}, {"http": D, "file": D, "db": D, "log": D}),
    ControlStep("b", "loop", "Return: Coro B completes — all coroutines done", {"a": D, "a1": D, "a2": D, "b": D, "b1": D, "c": D}, {"http": D, "file": D, "db": D, "log": D}),
]


def _lerp(a: Point, b: Point, t: float) -> Point:
    return Point(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t)


def _draw_legend(ax) -> None:
    y = 8.05
    items = [("pending", 0.9), ("running", 3.2), ("waiting", 5.5), ("done", 7.8)]
    for state, x in items:
        face, edge, label = STATE_STYLE[state]
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (x, y - 0.12),
                0.35,
                0.24,
                boxstyle="round,pad=0.01,rounding_size=0.04",
                facecolor=face,
                edgecolor=edge,
                linewidth=1.5,
            )
        )
        ax.text(x + 0.48, y, label, va="center", fontsize=8, color=C_TEXT)


def _draw_loop(ax, node: Node) -> None:
    size = 1.25
    x, y = node.center.x - size / 2, node.center.y - size / 2
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (x, y),
            size,
            size,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=2.5,
            edgecolor=C_LOOP,
            facecolor="#dbeafe",
        )
    )
    ax.text(node.center.x, node.center.y, node.label, ha="center", va="center", fontsize=9, fontweight="bold", color=C_LOOP)


def _draw_coro(ax, node: Node, state: str) -> None:
    face, edge, _ = STATE_STYLE[state]
    ax.add_patch(
        mpatches.Circle(
            (node.center.x, node.center.y),
            CORO_RADIUS,
            linewidth=2.2,
            edgecolor=edge,
            facecolor=face,
        )
    )
    ax.text(
        node.center.x,
        node.center.y + LEVEL_ABOVE,
        f"L{node.level}",
        ha="center",
        fontsize=7,
        color=C_MUTED,
    )
    ax.text(
        node.center.x,
        node.center.y,
        node.label,
        ha="center",
        va="center",
        fontsize=7.5,
        fontweight="bold",
        color=C_TEXT,
    )


def _draw_io(ax, node: Node, state: str) -> None:
    face, edge, _ = STATE_STYLE[state]
    x, y = node.center.x - IO_W / 2, node.center.y - IO_H / 2
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (x, y),
            IO_W,
            IO_H,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            linewidth=2,
            edgecolor=edge,
            facecolor=face,
            linestyle="--",
        )
    )
    ax.text(
        node.center.x,
        node.center.y,
        node.label,
        ha="center",
        va="center",
        fontsize=7,
        fontweight="bold",
        color=C_TEXT,
    )
    if node.key == "log":
        tag_y = node.center.y + IO_H / 2 + IO_TAG_ABOVE
    else:
        tag_y = node.center.y - IO_H / 2 - IO_TAG_BELOW
    ax.text(
        node.center.x,
        tag_y,
        "non-blocking",
        ha="center",
        fontsize=6.5,
        color=C_MUTED,
        fontstyle="italic",
    )


def _draw_wires(ax) -> None:
    for a_key, b_key in EDGES:
        a, b = NODES[a_key], NODES[b_key]
        ax.plot([a.center.x, b.center.x], [a.center.y, b.center.y], color=C_WIRE, lw=1.5, zorder=1)


def _edge_point(node: Node, toward: Point) -> Point:
    dx = toward.x - node.center.x
    dy = toward.y - node.center.y
    dist = (dx * dx + dy * dy) ** 0.5
    if dist == 0:
        return node.center
    if node.kind == "loop":
        radius = 0.68
    elif node.kind == "coro":
        radius = CORO_RADIUS + 0.06
    else:
        radius = IO_W / 2 + 0.08
    return Point(node.center.x + dx / dist * radius, node.center.y + dy / dist * radius)


def _draw_arrow(ax, start_node: Node, end_node: Node, t: float) -> None:
    start = _edge_point(start_node, end_node.center)
    end = _edge_point(end_node, start_node.center)
    head = _lerp(start, end, t)
    tail = _lerp(start, end, max(0.0, t - 0.38))
    ax.annotate(
        "",
        xy=(head.x, head.y),
        xytext=(tail.x, tail.y),
        arrowprops=dict(
            arrowstyle="-|>",
            color=C_ARROW,
            lw=3.2,
            shrinkA=0,
            shrinkB=0,
            mutation_scale=16,
        ),
        zorder=10,
    )


def render_frame(step: ControlStep, step_idx: int, t: float) -> Image.Image:
    src, dst = NODES[step.src], NODES[step.dst]

    fig, ax = plt.subplots(figsize=(11.5, 7.8), dpi=120)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.05, 8.75)
    ax.axis("off")

    ax.text(
        5.6,
        8.55,
        "Control flow through multi-level coroutines",
        ha="center",
        fontsize=12,
        fontweight="bold",
        color=C_TEXT,
    )
    _draw_legend(ax)
    ax.text(
        0.55,
        7.45,
        "square = event loop   ·   circles = coroutines   ·   dashed = non-blocking I/O",
        fontsize=7.5,
        color=C_MUTED,
    )

    _draw_wires(ax)
    _draw_loop(ax, NODES["loop"])
    for key in CORO_KEYS:
        _draw_coro(ax, NODES[key], step.coro[key])
    for key in IO_KEYS:
        _draw_io(ax, NODES[key], step.io[key])

    _draw_arrow(ax, src, dst, t)

    footer = ax.text(
        5.6,
        0.22,
        f"[{step_idx + 1}/{len(CONTROL_STEPS)}]  {step.caption}",
        ha="center",
        fontsize=8.5,
        color=C_TEXT,
        fontstyle="italic",
    )
    footer.set_path_effects([pe.withStroke(linewidth=2, foreground=C_BG)])

    fig.canvas.draw()
    rgba = fig.canvas.buffer_rgba()
    image = Image.frombytes("RGBA", fig.canvas.get_width_height(), rgba)
    plt.close(fig)
    return image.convert("P", palette=Image.ADAPTIVE)


def build_gif(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    images: list[Image.Image] = []
    durations: list[int] = []

    for step_idx, step in enumerate(CONTROL_STEPS):
        for frame in range(FRAMES_PER_SEGMENT):
            t = (frame + 1) / FRAMES_PER_SEGMENT
            images.append(render_frame(step, step_idx, t))
            durations.append(SEGMENT_MS // FRAMES_PER_SEGMENT)

    final = render_frame(CONTROL_STEPS[-1], len(CONTROL_STEPS) - 1, 1.0)
    for _ in range(FINAL_HOLD_FRAMES):
        images.append(final)
        durations.append(FINAL_HOLD_MS // FINAL_HOLD_FRAMES)

    images[0].save(
        path,
        save_all=True,
        append_images=images[1:],
        duration=durations,
        loop=0,
        optimize=True,
    )
    print(f"Saved {path} ({len(images)} frames, {len(CONTROL_STEPS)} control steps)")


if __name__ == "__main__":
    build_gif(OUTPUT)
