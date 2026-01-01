from dataclasses import dataclass
from typing import NamedTuple
from color_pallet import *


@dataclass
class WindowGui():
    width: int = 1024
    height: int = 768
    color_bg: tuple[int] = (255, 255, 255)

@dataclass
class GuitarTabLineGui():
    x_start = WindowGui.width * 1/20
    x_width = WindowGui.width * 18/20

    line_width = 2
    line_space = 10
    line_count = 6

    line_color: tuple[int] = "purple"

@dataclass
class GuitarTabGui():
    rect_start = WindowGui.width * 1/20
    rect_width = WindowGui.width * 18/20
    rect_height = GuitarTabLineGui.line_space * (GuitarTabLineGui.line_count + 1)

SCROLL_FACTOR = 20