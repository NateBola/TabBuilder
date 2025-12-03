from dataclasses import dataclass
from constants import *
from typing import NamedTuple

@dataclass
class window_settings():
    width: int = 700
    height: int = 500
    color_bg: tuple[int] = (255, 255, 255)

@dataclass
class tab_setting():
    padx: int = 20
    pady: int = 20

    line_width: int = 2
    line_height: int = 10
    line_padx: int  = 2

    line_color: tuple[int] = (0, 0, 0)
    color_bg: tuple[int] = (255, 255, 255)
