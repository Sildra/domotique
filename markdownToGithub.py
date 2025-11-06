#!/usr/bin/env python3
import re
import colorsys
from pathlib import Path

def strip_style_blocks(text: str) -> str:
    return re.sub(r"(?si)<style.*?>.*?</style\s*>", "", text)

def unwrap_html_tags(text: str, tag: str, pre: str = "", post: str = "") -> str:
    pattern = rf"(?si)<{tag}\b[^>]*>(.*?)</{tag}\s*>"
    return re.sub(pattern, lambda m: f"{pre}{m.group(1).strip()}{post}", text)

NAMED_COLORS = {
    "white": "#E7ECF2",
    "black": "#0D1117",
}

def invert_hex_color(hex_color: str) -> str:
    hex_color = NAMED_COLORS.get(hex_color, hex_color)
    if not hex_color.startswith('#'):
        return hex_color

    hex_color = hex_color.lstrip('#')
    r = 255 - int(hex_color[0:2], 16)
    g = 255 - int(hex_color[2:4], 16)
    b = 255 - int(hex_color[4:6], 16)
    return f"#{r:02X}{g:02X}{b:02X}"

def invert_luminosity(hex_color: str) -> str:
    hex_color = NAMED_COLORS.get(hex_color, hex_color)
    if not hex_color.startswith('#'):
        return hex_color

    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = 1 - l
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    r = int(r2 * 255)
    g = int(g2 * 255)
    b = int(b2 * 255)
    return f"#{r:02X}{g:02X}{b:02X}"


def invert_svg(input_path: Path, output_path: Path) -> None:
    svg_text = input_path.read_text(encoding="utf-8")
    pattern = r"#([0-9a-fA-F]{6})"
    svg_text = re.sub(pattern, lambda m: invert_luminosity(m.group(0)), svg_text)
    svg_text = re.sub(r"(white|black)", lambda m: invert_luminosity(m.group(0)), svg_text, flags=re.IGNORECASE)
    output_path.write_text(svg_text, encoding="utf-8")

def add_svg_theme(text: str) -> str:
    pattern = r'!\[([^\]]*)\]\((img/[^)]+\.svg)\)'
    
    def repl(match):
        alt_text, svg_path = match.groups()
        light_variant = Path(svg_path)
        name = light_variant.name
        idx = name.find('.') if not name.startswith('.') else name.find('.', 1)
        name = name[:idx] + "-dark" + name[idx:]
        dark_variant = Path(light_variant.parent / name)
        invert_svg(light_variant, dark_variant)
        return (
            f"![{alt_text}]({svg_path}#gh-light-mode-only)\n"
            f"![{alt_text}]({dark_variant.as_posix()}#gh-dark-mode-only)"
        )

    return re.sub(pattern, repl, text)

def main():
    input_path = Path("domotique.md")
    output_path = Path("README.md")

    text = input_path.read_text(encoding="utf-8")
    text = strip_style_blocks(text)
    text = unwrap_html_tags(text, "warning", "> [!WARNING]\n> ")
    text = unwrap_html_tags(text, "note", "> [!NOTE]\n> ")
    text = unwrap_html_tags(text, "important", "> [!IMPORTANT]\n> ")
    text = unwrap_html_tags(text, "tip", "> [!TIP]\n> ")
    text = unwrap_html_tags(text, "caution", "> [!CAUTION]\n> ")
    text = unwrap_html_tags(text, "success", "✅")
    text = unwrap_html_tags(text, "error", "❌ ")
    text = unwrap_html_tags(text, "s0", "☆")
    text = unwrap_html_tags(text, "s1", "★")
    text = unwrap_html_tags(text, "s2", "★★")
    text = unwrap_html_tags(text, "s3", "★★★")
    text = unwrap_html_tags(text, "s4", "★★★★")
    text = unwrap_html_tags(text, "s5", "★★★★★")
    text = unwrap_html_tags(text, "[^\\s]+")
    text = add_svg_theme(text)
    output_path.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()