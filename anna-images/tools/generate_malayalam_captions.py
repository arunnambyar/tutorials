"""Generate Malayalam story captions for Anna park frames using Gemini."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
STORY = ROOT / "story.md"

FRAMES: list[str] = [
    "anna_park_frame1.png",
    "anna_park_frame2.png",
    "anna_park_frame5_throw_ready.png",
    "anna_park_frame6_throw_release.png",
    "anna_park_frame7_dog_catch.png",
    "anna_park_frame8_dog_return.png",
    "anna_park_frame4.png",
    "anna_park_frame9_throw_again.png",
    "anna_park_frame10_puppy_chase.png",
    "anna_park_frame11_puppy_pickup.png",
    "anna_park_frame12_together.png",
    "anna_park_frame13_goodbye.png",
]

PROMPT = """You are writing short story captions in Malayalam for a children's picture book.

Look at this illustration of little Anna and her golden puppy Puppy at the park.

Write ONE sentence in Malayalam that describes what is happening in this scene.
- Keep Anna and Puppy as English names (do not translate them).
- Use simple, warm language suitable for young children.
- Return ONLY the Malayalam sentence, no quotes, numbering, or explanation."""


def caption_frame(client: genai.Client, image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                    types.Part.from_text(text=PROMPT),
                ],
            )
        ],
    )
    return (response.text or "").strip()


def build_story(captions: list[str]) -> str:
    blocks: list[str] = ["# Anna and Puppy at the Park", ""]
    for filename, caption in zip(FRAMES, captions, strict=True):
        blocks.extend([caption, "", f"![](./assets/{filename})", ""])
    return "\n".join(blocks).rstrip() + "\n"


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Set GEMINI_API_KEY or GOOGLE_API_KEY.", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    captions: list[str] = []

    for filename in FRAMES:
        path = ASSETS / filename
        print(f"Captioning {filename}...")
        captions.append(caption_frame(client, path))
        print(f"  -> {captions[-1]}")

    STORY.write_text(build_story(captions), encoding="utf-8")
    cache = ASSETS / "malayalam_captions.json"
    cache.write_text(
        json.dumps(dict(zip(FRAMES, captions, strict=True)), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Updated {STORY.name} and {cache.name}")


if __name__ == "__main__":
    main()
