"""
Generate a GIF showing what happens when a coroutine uses a **blocking** I/O call.

Same layout and arrow motion as control_flow_animation.py, but when A1 hits
blocking HTTP the entire event loop freezes — no pause/resume, no switching
to B or C until the call returns (~10 s hold with blinking waiting nodes).

Run:
    pip install matplotlib pillow
    python blocking_flow_animation.py

Output:
    ../../static/3100_asyncio_coroutines/blocking_flow_demo.gif
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import patheffects as pe
from PIL import Image

OUTPUT = (
    Path(__file__).resolve().parents[2]
    / "static/3100_asyncio_coroutines/blocking_flow_demo.gif"
)

C_BG = "#f8fafc"
C_TEXT = "#0f172a"
C_MUTED = "#64748b"
C_LOOP = "#1d4ed8"
C_WIRE = "#cbd5e1"
C_ARROW = "#dc2626"
C_BLOCK = "#b45309"

STATE_STYLE = {
    "pending": ("#e2e8f0", "#94a3b8", "not run"),
    "running": ("#dbeafe", "#2563eb", "running"),
    "waiting": ("#fef9c3", "#ca8a04", "waiting"),
    "done": ("#dcfce7", "#16a34a", "completed"),
    "blocking": ("#ffedd5", "#c2410c", "blocking"),
}

CORO_KEYS = ("a", "a1", "a2", "b", "b1", "c")
IO_KEYS = ("http", "file", "db", "log")

FRAMES_PER_SEGMENT = 2
SEGMENT_MS = 1300
BLOCK_HOLD_MS = 10000
BLOCK_HOLD_FRAMES = 10
FINAL_HOLD_MS = 4000
FINAL_HOLD_FRAMES = 6


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
    loop_state: str = "running"


@dataclass(frozen=True)
class IntroHold:
    caption: str
    coro: dict[str, str]
    io: dict[str, str]
    loop_state: str = "running"


@dataclass(frozen=True)
class BlockHold:
    src: str
    dst: str
    caption: str
    coro: dict[str, str]
    io: dict[str, str]
    loop_state: str = "waiting"


NODES: dict[str, Node] = {
    "loop": Node("loop", Point(1.45, 3.85), "Event\nLoop", "loop", 0),
    "a": Node("a", Point(4.25, 6.25), "Coro A", "coro", 1),
    "a1": Node("a1", Point(6.85, 6.55), "Coro A1", "coro", 2),
    "http": Node("http", Point(9.85, 6.55), "blocking\nHTTP", "io", 3),
    "a2": Node("a2", Point(6.85, 5.25), "Coro A2", "coro", 2),
    "file": Node("file", Point(9.85, 5.25), "read\nfile", "io", 3),
    "b": Node("b", Point(4.25, 3.85), "Coro B", "coro", 1),
    "b1": Node("b1", Point(6.85, 3.85), "Coro B1", "coro", 2),
    "db": Node("db", Point(9.85, 3.85), "blocking\nDB", "io", 3),
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
B = "blocking"

INTRO_HOLD_MS = 900
INTRO_HOLD_FRAMES = 2

# Sequential blocking flow — no pause/resume to other coroutines during a block.
CONTROL_STEPS: list[ControlStep | BlockHold | IntroHold] = [
    IntroHold(
        "All coroutines not run yet — event loop idle",
        {"a": P, "a1": P, "a2": P, "b": P, "b1": P, "c": P},
        {"http": P, "file": P, "db": P, "log": P},
    ),
    ControlStep(
        "loop", "a",
        "Loop hands control to Coro A",
        {"a": R, "a1": P, "a2": P, "b": P, "b1": P, "c": P},
        {"http": P, "file": P, "db": P, "log": P},
    ),
    ControlStep(
        "a", "a1",
        "Coro A calls Coro A1 — A1 running",
        {"a": W, "a1": R, "a2": P, "b": P, "b1": P, "c": P},
        {"http": P, "file": P, "db": P, "log": P},
    ),
    ControlStep(
        "a1", "http",
        "A1 calls blocking HTTP — thread enters the call",
        {"a": W, "a1": W, "a2": P, "b": P, "b1": P, "c": P},
        {"http": B, "file": P, "db": P, "log": P},
        loop_state=W,
    ),
    BlockHold(
        "a1", "http",
        "Blocking HTTP — loop frozen, no other coroutine runs (10 s)",
        {"a": W, "a1": W, "a2": P, "b": P, "b1": P, "c": P},
        {"http": B, "file": P, "db": P, "log": P},
        loop_state=W,
    ),
    ControlStep(
        "http", "a1",
        "Blocking HTTP returns — control back to A1",
        {"a": W, "a1": R, "a2": P, "b": P, "b1": P, "c": P},
        {"http": D, "file": P, "db": P, "log": P},
    ),
    ControlStep(
        "a1", "a",
        "Return: Coro A1 completed — control back to Coro A",
        {"a": R, "a1": D, "a2": P, "b": P, "b1": P, "c": P},
        {"http": D, "file": P, "db": P, "log": P},
    ),
    ControlStep(
        "a", "a2",
        "Coro A calls Coro A2 — A2 running",
        {"a": W, "a1": D, "a2": R, "b": P, "b1": P, "c": P},
        {"http": D, "file": P, "db": P, "log": P},
    ),
    ControlStep(
        "a2", "file",
        "A2 calls blocking read file — thread enters the call",
        {"a": W, "a1": D, "a2": W, "b": P, "b1": P, "c": P},
        {"http": D, "file": B, "db": P, "log": P},
        loop_state=W,
    ),
    BlockHold(
        "a2", "file",
        "Blocking read file — loop frozen again (10 s)",
        {"a": W, "a1": D, "a2": W, "b": P, "b1": P, "c": P},
        {"http": D, "file": B, "db": P, "log": P},
        loop_state=W,
    ),
    ControlStep(
        "file", "a2",
        "Blocking read returns — control back to A2",
        {"a": W, "a1": D, "a2": R, "b": P, "b1": P, "c": P},
        {"http": D, "file": D, "db": P, "log": P},
    ),
    ControlStep(
        "a2", "a",
        "Return: Coro A2 completed — control back to Coro A",
        {"a": R, "a1": D, "a2": D, "b": P, "b1": P, "c": P},
        {"http": D, "file": D, "db": P, "log": P},
    ),
    ControlStep(
        "a", "loop",
        "Return: Coro A completed — control back to event loop",
        {"a": D, "a1": D, "a2": D, "b": P, "b1": P, "c": P},
        {"http": D, "file": D, "db": P, "log": P},
    ),
    ControlStep(
        "loop", "b",
        "Loop hands control to Coro B — B running",
        {"a": D, "a1": D, "a2": D, "b": R, "b1": P, "c": P},
        {"http": D, "file": D, "db": P, "log": P},
    ),
    ControlStep(
        "b", "b1",
        "Coro B calls Coro B1 — B1 running",
        {"a": D, "a1": D, "a2": D, "b": W, "b1": R, "c": P},
        {"http": D, "file": D, "db": P, "log": P},
    ),
    ControlStep(
        "b1", "db",
        "B1 calls blocking DB — thread enters the call",
        {"a": D, "a1": D, "a2": D, "b": W, "b1": W, "c": P},
        {"http": D, "file": D, "db": B, "log": P},
        loop_state=W,
    ),
    BlockHold(
        "b1", "db",
        "Blocking DB — loop frozen again (10 s)",
        {"a": D, "a1": D, "a2": D, "b": W, "b1": W, "c": P},
        {"http": D, "file": D, "db": B, "log": P},
        loop_state=W,
    ),
    ControlStep(
        "db", "b1",
        "Blocking DB returns — control back to B1",
        {"a": D, "a1": D, "a2": D, "b": W, "b1": R, "c": P},
        {"http": D, "file": D, "db": D, "log": P},
    ),
    ControlStep(
        "b1", "b",
        "Return: Coro B1 completed — control back to Coro B",
        {"a": D, "a1": D, "a2": D, "b": R, "b1": D, "c": P},
        {"http": D, "file": D, "db": D, "log": P},
    ),
    ControlStep(
        "b", "loop",
        "Return: Coro B completed — control back to event loop",
        {"a": D, "a1": D, "a2": D, "b": D, "b1": D, "c": P},
        {"http": D, "file": D, "db": D, "log": P},
    ),
    ControlStep(
        "loop", "c",
        "Loop hands control to Coro C — C running",
        {"a": D, "a1": D, "a2": D, "b": D, "b1": D, "c": R},
        {"http": D, "file": D, "db": D, "log": P},
    ),
    ControlStep(
        "c", "log",
        "Coro C calls print()",
        {"a": D, "a1": D, "a2": D, "b": D, "b1": D, "c": R},
        {"http": D, "file": D, "db": D, "log": R},
    ),
    ControlStep(
        "log", "c",
        "Return: control back to Coro C",
        {"a": D, "a1": D, "a2": D, "b": D, "b1": D, "c": R},
        {"http": D, "file": D, "db": D, "log": D},
    ),
    ControlStep(
        "c", "loop",
        "Return: Coro C completed — all coroutines done",
        {"a": D, "a1": D, "a2": D, "b": D, "b1": D, "c": D},
        {"http": D, "file": D, "db": D, "log": D},
    ),
]

def _lerp(a: Point, b: Point, t: float) -> Point:
    return Point(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t)


def _draw_legend(ax) -> None:
    y = 8.05
    items = [
        ("pending", 0.5),
        ("running", 2.4),
        ("waiting", 4.3),
        ("blocking", 6.2),
        ("done", 8.1),
    ]
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


def _draw_loop(ax, node: Node, state: str, blink: bool) -> None:
    size = 1.25
    x, y = node.center.x - size / 2, node.center.y - size / 2
    face, edge, _ = STATE_STYLE[state]
    lw = 3.4 if blink and state == W else 2.5
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (x, y),
            size,
            size,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=lw,
            edgecolor=edge,
            facecolor=face,
        )
    )
    ax.text(
        node.center.x,
        node.center.y,
        node.label,
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
        color=C_LOOP if state == "running" else C_TEXT,
    )


def _draw_coro(ax, node: Node, state: str, blink: bool) -> None:
    face, edge, _ = STATE_STYLE[state]
    lw = 3.6 if blink and state == W else 2.2
    ax.add_patch(
        mpatches.Circle(
            (node.center.x, node.center.y),
            CORO_RADIUS,
            linewidth=lw,
            edgecolor=edge,
            facecolor=face if not (blink and state == W) else "#fde68a",
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


def _draw_io(ax, node: Node, state: str, blink: bool, blocking: bool = False) -> None:
    if state == B:
        face, edge = STATE_STYLE[B][:2]
    else:
        face, edge, _ = STATE_STYLE[state]
    x, y = node.center.x - IO_W / 2, node.center.y - IO_H / 2
    lw = 3.4 if blink and state in (W, B) else 2
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (x, y),
            IO_W,
            IO_H,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            linewidth=lw,
            edgecolor=edge,
            facecolor=face if not (blink and state == B) else "#fed7aa",
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
    tag = "blocking" if blocking or state == B else "non-blocking"
    ax.text(
        node.center.x,
        tag_y,
        tag,
        ha="center",
        fontsize=6.5,
        color=C_BLOCK if tag == "blocking" else C_MUTED,
        fontstyle="italic",
        fontweight="bold" if tag == "blocking" else "normal",
    )


def _draw_wires(ax) -> None:
    for a_key, b_key in EDGES:
        a, b = NODES[a_key], NODES[b_key]
        ax.plot(
            [a.center.x, b.center.x],
            [a.center.y, b.center.y],
            color=C_WIRE,
            lw=1.5,
            zorder=1,
        )


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


def render_frame(
    step: ControlStep | BlockHold | IntroHold,
    step_idx: int,
    total_steps: int,
    t: float,
    blink: bool = False,
) -> Image.Image:
    loop_state = step.loop_state

    fig, ax = plt.subplots(figsize=(11.5, 7.8), dpi=120)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.05, 8.75)
    ax.axis("off")

    ax.text(
        5.6,
        8.55,
        "Blocking I/O freezes the event loop",
        ha="center",
        fontsize=12,
        fontweight="bold",
        color=C_TEXT,
    )
    _draw_legend(ax)
    ax.text(
        0.55,
        7.45,
        "square = event loop   ·   circles = coroutines   ·   dashed = I/O",
        fontsize=7.5,
        color=C_MUTED,
    )

    _draw_wires(ax)
    _draw_loop(ax, NODES["loop"], loop_state, blink)
    for key in CORO_KEYS:
        _draw_coro(ax, NODES[key], step.coro[key], blink)
    for key in IO_KEYS:
        blocking = step.io[key] == B
        _draw_io(ax, NODES[key], step.io[key], blink, blocking=blocking)

    if isinstance(step, IntroHold):
        pass  # no arrow — all tasks not run yet
    else:
        src, dst = NODES[step.src], NODES[step.dst]
        _draw_arrow(ax, src, dst, t)

    footer = ax.text(
        5.6,
        0.22,
        f"[{step_idx + 1}/{total_steps}]  {step.caption}",
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
    total = len(CONTROL_STEPS)

    for step_idx, step in enumerate(CONTROL_STEPS):
        if isinstance(step, IntroHold):
            for _ in range(INTRO_HOLD_FRAMES):
                images.append(render_frame(step, step_idx, total, 0.0))
                durations.append(INTRO_HOLD_MS // INTRO_HOLD_FRAMES)
            continue

        if isinstance(step, BlockHold):
            for frame in range(BLOCK_HOLD_FRAMES):
                blink = frame % 2 == 0
                images.append(render_frame(step, step_idx, total, 1.0, blink=blink))
                durations.append(BLOCK_HOLD_MS // BLOCK_HOLD_FRAMES)
            continue

        for frame in range(FRAMES_PER_SEGMENT):
            t = (frame + 1) / FRAMES_PER_SEGMENT
            images.append(render_frame(step, step_idx, total, t))
            durations.append(SEGMENT_MS // FRAMES_PER_SEGMENT)

    final = render_frame(CONTROL_STEPS[-1], total - 1, total, 1.0)
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
    print(f"Saved {path} ({len(images)} frames, {total} steps)")


if __name__ == "__main__":
    build_gif(OUTPUT)
