from dataclasses import dataclass
from constants import *
from typing import NamedTuple

@dataclass
class WindowGui():
    width: int = 1024
    height: int = 768
    color_bg: tuple[int] = (255, 255, 255)

@dataclass
class GuitarTabLineGui():
    line_x_start = 20
    line_x_end = 900
    line_width = 2
    line_spacing = 10
    line_count = 6

    line_color: tuple[int] = (0, 0, 0)
    color_bg: tuple[int] = (255, 255, 255)

@dataclass
class GuitarTabGui():
    rect_start = WindowGui.width * 1/20
    rect_width = WindowGui.width * 18/20
    rect_height = GuitarTabLineGui.line_spacing * (GuitarTabLineGui.line_count + 1)