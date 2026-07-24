"""Build Anna park GIF with Malayalam captions and slide numbers."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT_PATH = Path(r"C:\Windows\Fonts\Nirmala.ttc")

SLIDES: list[tuple[str, str]] = [
    (
        "anna_park_frame1.png",
        "പാർക്കിൽ Anna-ക്ക് Puppy എന്ന ചെറിയ നായ്ക്കുട്ടിയെ കണ്ടു.",
    ),
    (
        "anna_park_frame2.png",
        "Anna Puppy-യെ സ്നേഹത്തോടെ തലോടിച്ചു.",
    ),
    (
        "anna_park_frame5_throw_ready.png",
        "Anna ചുവന്ന പന്ത് കയ്യിൽ പിടിച്ച് എറിയാൻ തയ്യാറായി.",
    ),
    (
        "anna_park_frame6_throw_release.png",
        "Anna പന്ത് ഉയർത്തി എറിഞ്ഞു; അത് അകലേക്ക് പോയി.",
    ),
    (
        "anna_park_frame7_dog_catch.png",
        "Puppy ഓടിവന്ന് പന്ത് വായിൽ പിടിച്ചു.",
    ),
    (
        "anna_park_frame8_dog_return.png",
        "Puppy പന്തുമായി Anna-യുടെ അടുത്തേക്ക് വന്നു.",
    ),
    (
        "anna_park_frame4.png",
        "Anna സന്തോഷത്തോടെ കൈയടിച്ചു; Puppy-യും സന്തോഷിച്ചു!",
    ),
    (
        "anna_park_frame9_throw_again.png",
        "Anna വീണ്ടും പന്ത് എറിഞ്ഞു.",
    ),
    (
        "anna_park_frame10_puppy_chase.png",
        "Puppy വേഗത്തിൽ പന്തിന്റെ പുറകെ ഓടി.",
    ),
    (
        "anna_park_frame11_puppy_pickup.png",
        "Puppy പുല്ലിൽ നിന്ന് പന്ത് വായിൽ എടുത്തു.",
    ),
    (
        "anna_park_frame12_together.png",
        "Anna-യും Puppy-യും പുല്ലിൽ ഒരുമിച്ച് ഇരുന്നു.",
    ),
    (
        "anna_park_frame13_goodbye.png",
        "Anna വീട്ടിലേക്ക് പോകുമ്പോൾ Puppy-യോട് വിട പറഞ്ഞു.",
    ),
]

FRAME_MS = 10_000


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if FONT_PATH.exists():
        return ImageFont.truetype(str(FONT_PATH), size=size)
    return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if font.getlength(trial) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [text]


def caption_frame(image: Image.Image, slide_no: int, total: int, caption: str) -> Image.Image:
    base = image.convert("RGBA")
    draw = ImageDraw.Draw(base)
    width, height = base.size

    slide_font = load_font(max(28, width // 45))
    caption_font = load_font(max(34, width // 32))

    slide_label = f"{slide_no} / {total}"
    slide_pad = 24
    slide_box = draw.textbbox((0, 0), slide_label, font=slide_font)
    slide_w = slide_box[2] - slide_box[0]
    slide_h = slide_box[3] - slide_box[1]
    slide_x = width - slide_w - slide_pad
    slide_y = slide_pad

    draw.rounded_rectangle(
        (slide_x - 16, slide_y - 8, slide_x + slide_w + 16, slide_y + slide_h + 8),
        radius=14,
        fill=(0, 0, 0, 170),
    )
    draw.text((slide_x, slide_y), slide_label, font=slide_font, fill=(255, 255, 255, 255))

    lines = wrap_text(caption, caption_font, width - 80)
    line_heights = [draw.textbbox((0, 0), line, font=caption_font)[3] for line in lines]
    line_gap = 10
    caption_block_h = sum(line_heights) + line_gap * (len(lines) - 1)
    bar_pad_y = 24
    bar_top = height - caption_block_h - bar_pad_y * 2
    draw.rectangle((0, bar_top, width, height), fill=(0, 0, 0, 175))

    y = bar_top + bar_pad_y
    for line, line_h in zip(lines, line_heights):
        line_w = draw.textlength(line, font=caption_font)
        draw.text(((width - line_w) / 2, y), line, font=caption_font, fill=(255, 255, 255, 255))
        y += line_h + line_gap

    return base


def main() -> None:
    total = len(SLIDES)
    captioned: list[Image.Image] = []

    for index, (filename, caption) in enumerate(SLIDES, start=1):
        source = ASSETS / filename
        image = Image.open(source)
        captioned.append(caption_frame(image, index, total, caption))

        out_frame = ASSETS / f"anna_park_slide{index:02d}.png"
        captioned[-1].convert("RGB").save(out_frame, optimize=True)

    target = captioned[0].size
    palette_frames: list[Image.Image] = []
    for image in captioned:
        if image.size != target:
            image = image.resize(target, Image.Resampling.LANCZOS)
        palette_frames.append(image.convert("P", palette=Image.ADAPTIVE, colors=256))

    gif_path = ASSETS / "anna_park_playing_with_dog.gif"
    palette_frames[0].save(
        gif_path,
        save_all=True,
        append_images=palette_frames[1:],
        duration=FRAME_MS,
        loop=0,
        disposal=2,
        optimize=True,
    )
    print(f"Built {gif_path.name} with {total} captioned slides ({FRAME_MS} ms each)")


if __name__ == "__main__":
    main()
