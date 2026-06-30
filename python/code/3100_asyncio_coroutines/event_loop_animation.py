"""
Generate a GIF showing a simple event loop managing coroutines at multiple levels.

Run:
    pip install matplotlib pillow
    python event_loop_animation.py

Output:
    ../../static/3100_asyncio_coroutines/event_loop_demo.gif
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import patheffects as pe
from PIL import Image

OUTPUT = Path(__file__).resolve().parents[2] / "static/3100_asyncio_coroutines/event_loop_demo.gif"

# Colors
C_LOOP = "#2563eb"
C_PENDING = "#94a3b8"
C_RUNNING = "#2563eb"
C_WAITING = "#ca8a04"
C_DONE = "#16a34a"
C_BG = "#f8fafc"
C_TEXT = "#0f172a"
C_MUTED = "#64748b"
C_ARROW = "#dc2626"

FRAMES_PER_SEGMENT = 2
SEGMENT_MS = 2500
FINAL_HOLD_MS = 5000
FINAL_HOLD_FRAMES = 4


STATUS_STYLE = {
    "ready": ("#e2e8f0", "#94a3b8", "NOT RUN"),
    "running": ("#dbeafe", "#2563eb", "RUNNING"),
    "waiting": ("#fef9c3", "#ca8a04", "WAITING"),
    "done": ("#dcfce7", "#16a34a", "DONE"),
}


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class CoroutineState:
    name: str
    level: int
    status: str  # ready | running | waiting | done
    step: str = ""


@dataclass(frozen=True)
class Frame:
    tick: int
    caption: str
    coroutines: tuple[CoroutineState, ...]


FRAMES: list[Frame] = [
    Frame(
        1,
        "Event loop starts Coro A (level 1)",
        (
            CoroutineState("Coro A", 1, "running", "step 1: start"),
            CoroutineState("Coro B", 1, "ready"),
            CoroutineState("Coro C", 1, "ready"),
        ),
    ),
    Frame(
        2,
        "Coro A runs until it must wait for I/O",
        (
            CoroutineState("Coro A", 1, "running", "step 2: await I/O"),
            CoroutineState("Coro B", 1, "ready"),
            CoroutineState("Coro C", 1, "ready"),
        ),
    ),
    Frame(
        3,
        "Coro A pauses at await — moved to waiting bench",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "ready"),
            CoroutineState("Coro C", 1, "ready"),
        ),
    ),
    Frame(
        4,
        "Loop picks Coro B (level 1)",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "running", "step 1: fetch"),
            CoroutineState("Coro C", 1, "ready"),
        ),
    ),
    Frame(
        5,
        "Coro B starts a nested coroutine B1 (level 2)",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "running", "await B1"),
            CoroutineState("Coro B1", 2, "running", "step 1: query DB"),
            CoroutineState("Coro C", 1, "ready"),
        ),
    ),
    Frame(
        6,
        "B1 hits await — loop switches while I/O runs",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "waiting", "await B1"),
            CoroutineState("Coro B1", 2, "waiting", "await DB"),
            CoroutineState("Coro C", 1, "ready"),
        ),
    ),
    Frame(
        7,
        "Loop runs quick Coro C (level 1) — no waiting",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "waiting", "await B1"),
            CoroutineState("Coro B1", 2, "waiting", "await DB"),
            CoroutineState("Coro C", 1, "running", "step 1: log"),
        ),
    ),
    Frame(
        8,
        "Coro C finishes — loop checks waiting bench",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "waiting", "await B1"),
            CoroutineState("Coro B1", 2, "waiting", "await DB"),
            CoroutineState("Coro C", 1, "done", "finished"),
        ),
    ),
    Frame(
        9,
        "B1 I/O done — loop resumes nested coroutine (level 2)",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "waiting", "await B1"),
            CoroutineState("Coro B1", 2, "running", "step 2: parse"),
            CoroutineState("Coro C", 1, "done", "finished"),
        ),
    ),
    Frame(
        10,
        "B1 completes — control returns to Coro B (level 1)",
        (
            CoroutineState("Coro A", 1, "waiting", "await network"),
            CoroutineState("Coro B", 1, "running", "step 2: save"),
            CoroutineState("Coro B1", 2, "done", "finished"),
            CoroutineState("Coro C", 1, "done", "finished"),
        ),
    ),
    Frame(
        11,
        "Coro A I/O ready — loop resumes where it paused",
        (
            CoroutineState("Coro A", 1, "running", "step 3: use data"),
            CoroutineState("Coro B", 1, "done", "finished"),
            CoroutineState("Coro B1", 2, "done", "finished"),
            CoroutineState("Coro C", 1, "done", "finished"),
        ),
    ),
    Frame(
        12,
        "All coroutines done — event loop exits",
        (
            CoroutineState("Coro A", 1, "done", "finished"),
            CoroutineState("Coro B", 1, "done", "finished"),
            CoroutineState("Coro B1", 2, "done", "finished"),
            CoroutineState("Coro C", 1, "done", "finished"),
        ),
    ),
]

# Red arrow path per tick: (source, destination) — shows where control moves
ARROW_PATH: list[tuple[str, str]] = [
    ("loop", "a"),      # tick 1
    ("loop", "a"),      # tick 2
    ("a", "bench"),     # tick 3 — A pauses at await
    ("loop", "b"),      # tick 4
    ("b", "b1"),        # tick 5
    ("b1", "bench"),    # tick 6 — B1 pauses at await
    ("loop", "c"),      # tick 7
    ("c", "loop"),      # tick 8 — C completes
    ("loop", "b1"),     # tick 9 — resume B1
    ("b1", "b"),        # tick 10 — return to B
    ("loop", "a"),      # tick 11 — resume A
    ("a", "loop"),      # tick 12 — all done
]

# Layout constants (shared by drawing and arrow routing)
LOOP_CX, LOOP_CY = 5.0, 5.725
BOX_W, BOX_H, GAP = 2.55, 1.1, 0.45
L1_Y = 3.35
SUB_W, SUB_H = 2.05, 0.9
SUB_Y = 1.75
BENCH_CX, BENCH_CY = 5.0, 1.15


def _l1_center(index: int) -> Point:
    n1 = 3
    total_w = n1 * BOX_W + (n1 - 1) * GAP
    start_x = 5 - total_w / 2
    x = start_x + index * (BOX_W + GAP)
    return Point(x + BOX_W / 2, L1_Y + BOX_H / 2)


def _node_center(key: str) -> Point:
    if key == "loop":
        return Point(LOOP_CX, LOOP_CY)
    if key == "a":
        return _l1_center(0)
    if key == "b":
        return _l1_center(1)
    if key == "c":
        return _l1_center(2)
    if key == "b1":
        b = _l1_center(1)
        return Point(b.x, SUB_Y + SUB_H / 2)
    if key == "bench":
        return Point(BENCH_CX, BENCH_CY)
    raise KeyError(key)


def _lerp(a: Point, b: Point, t: float) -> Point:
    return Point(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t)


def _edge_point(center: Point, toward: Point, kind: str) -> Point:
    dx = toward.x - center.x
    dy = toward.y - center.y
    dist = (dx * dx + dy * dy) ** 0.5
    if dist == 0:
        return center
    if kind == "loop":
        radius = 0.45
    elif kind == "bench":
        radius = 0.42
    elif kind == "b1":
        radius = 0.52
    else:
        radius = 0.58
    return Point(center.x + dx / dist * radius, center.y + dy / dist * radius)


def _draw_control_arrow(ax, src_key: str, dst_key: str, t: float) -> None:
    src_c = _node_center(src_key)
    dst_c = _node_center(dst_key)
    start = _edge_point(src_c, dst_c, src_key if src_key != "bench" else "bench")
    end = _edge_point(dst_c, src_c, dst_key if dst_key != "bench" else "bench")
    head = _lerp(start, end, t)
    tail = _lerp(start, end, max(0.0, t - 0.35))
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


def _draw_legend(ax) -> None:
    y = 6.35
    items = [
        ("ready", 0.6),
        ("running", 2.6),
        ("waiting", 4.6),
        ("done", 6.6),
    ]
    for state, x in items:
        face, edge, label = STATUS_STYLE[state]
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
        ax.text(x + 0.45, y, label.lower(), va="center", fontsize=8, color=C_TEXT)


def _draw_box(ax, x, y, w, h, face, edge=C_TEXT, lw=1.5, radius=0.08):
    box = mpatches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(box)
    return box


def render_frame(frame: Frame, tick_idx: int, t: float) -> Image.Image:
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=120)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.0)
    ax.axis("off")

    ax.text(
        5,
        6.75,
        "Event loop managing coroutines (multi-level)",
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        color=C_TEXT,
    )
    _draw_legend(ax)

    # Event loop
    loop_w, loop_h = 3.6, 0.75
    loop_x = 5 - loop_w / 2
    loop_y = 5.35
    _draw_box(ax, loop_x, loop_y, loop_w, loop_h, "#dbeafe", edge=C_LOOP, lw=2.5)
    ax.text(
        5,
        loop_y + loop_h / 2,
        f"EVENT LOOP  ·  tick {frame.tick}",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color=C_LOOP,
    )

    level1 = [c for c in frame.coroutines if c.level == 1]
    level2 = [c for c in frame.coroutines if c.level == 2]

    ax.text(0.35, 4.65, "Level 1", fontsize=9, color=C_MUTED, fontweight="bold")
    n1 = len(level1)
    box_w, box_h, gap = 2.55, 1.1, 0.45
    total_w = n1 * box_w + (n1 - 1) * gap
    start_x = 5 - total_w / 2

    parent_positions: dict[str, float] = {}

    for i, coro in enumerate(level1):
        x = start_x + i * (box_w + gap)
        y = 3.35
        face, edge, label = STATUS_STYLE[coro.status]
        lw = 2.8 if coro.status == "running" else 1.5
        _draw_box(ax, x, y, box_w, box_h, face, edge=edge, lw=lw)
        ax.text(x + box_w / 2, y + box_h - 0.24, coro.name, ha="center", fontsize=10, fontweight="bold", color=C_TEXT)
        ax.text(x + box_w / 2, y + 0.62, label, ha="center", fontsize=8.5, color=edge, fontweight="bold")
        step = coro.step or "—"
        ax.text(x + box_w / 2, y + 0.3, step, ha="center", fontsize=7.5, color=C_MUTED)
        parent_positions[coro.name] = x + box_w / 2

    if level2:
        ax.text(0.35, 2.85, "Level 2", fontsize=9, color=C_MUTED, fontweight="bold")
        parent_x = parent_positions.get("Coro B", 5)
        n2 = len(level2)
        sub_w, sub_h = 2.05, 0.9
        sub_gap = 0.3
        sub_total = n2 * sub_w + (n2 - 1) * sub_gap
        sub_start = parent_x - sub_total / 2
        sub_y = 1.75

        ax.plot([parent_x, parent_x], [3.35, sub_y + sub_h + 0.2], color=C_MUTED, lw=1.2, ls="--")

        for coro in level2:
            sx = sub_start
            face, edge, label = STATUS_STYLE[coro.status]
            lw = 2.8 if coro.status == "running" else 1.5
            _draw_box(ax, sx, sub_y, sub_w, sub_h, face, edge=edge, lw=lw)
            ax.text(sx + sub_w / 2, sub_y + sub_h - 0.2, coro.name, ha="center", fontsize=9, fontweight="bold", color=C_TEXT)
            ax.text(sx + sub_w / 2, sub_y + 0.45, label, ha="center", fontsize=8, color=edge, fontweight="bold")
            ax.text(sx + sub_w / 2, sub_y + 0.16, coro.step or "—", ha="center", fontsize=7, color=C_MUTED)

    waiting = [c for c in frame.coroutines if c.status == "waiting"]
    bench_y = 0.75
    _draw_box(ax, 0.4, bench_y, 9.2, 0.8, "#fef9c3", edge=C_WAITING, lw=1.5)
    ax.text(0.6, bench_y + 0.56, "Waiting bench (await)", fontsize=8.5, fontweight="bold", color=C_WAITING)
    if waiting:
        bench_text = "  ·  ".join(f"{c.name}: {c.step}" for c in waiting)
    else:
        bench_text = "empty — no coroutine is paused"
    ax.text(5, bench_y + 0.24, bench_text, ha="center", fontsize=8, color=C_TEXT)

    caption = ax.text(
        5,
        0.2,
        frame.caption,
        ha="center",
        va="bottom",
        fontsize=9.5,
        color=C_TEXT,
        fontstyle="italic",
    )
    caption.set_path_effects([pe.withStroke(linewidth=2, foreground=C_BG)])

    src, dst = ARROW_PATH[tick_idx]
    _draw_control_arrow(ax, src, dst, t)

    fig.canvas.draw()
    rgba = fig.canvas.buffer_rgba()
    image = Image.frombytes("RGBA", fig.canvas.get_width_height(), rgba)
    plt.close(fig)
    return image.convert("P", palette=Image.ADAPTIVE)


def build_gif(frames: list[Frame], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    images: list[Image.Image] = []
    durations: list[int] = []

    for tick_idx, frame in enumerate(frames):
        for sub in range(FRAMES_PER_SEGMENT):
            t = (sub + 1) / FRAMES_PER_SEGMENT
            images.append(render_frame(frame, tick_idx, t))
            durations.append(SEGMENT_MS // FRAMES_PER_SEGMENT)

    final = render_frame(frames[-1], len(frames) - 1, 1.0)
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
    print(f"Saved {path} ({len(images)} frames, {len(frames)} ticks)")


if __name__ == "__main__":
    build_gif(FRAMES, OUTPUT)
