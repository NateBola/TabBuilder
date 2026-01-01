from dataclasses import dataclass
from typing import NamedTuple
from color_pallet import *


@dataclass
class WindowGui():
    width: int = 1024
    height: int = 768
    color_bg: tuple[int] = (255, 255, 255)

@dataclass
class GuitarTabGui():
    line_width = 2
    line_space = 14
    line_count = 6

    rect_start = WindowGui.width * 1/20
    rect_width = WindowGui.width * 18/20
    rect_height = line_space * (line_count + 1)
    rect_padding = 20

    line_color: tuple[int] = "purple"
    rect_color: tuple[int] = "white"

SCROLL_FACTOR = 20