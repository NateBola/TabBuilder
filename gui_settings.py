from dataclasses import dataclass
from constants import *
from typing import NamedTuple

@dataclass
class window_settings():
    width: int = 700
    height: int = 500

@dataclass
class tab_setting():
    padx: int = 0
    pady: int = 0
    line_height: int = 0
    line_padx: int  = 0
    color_fg: tuple[int] = (0, 0, 0)
    color_bg: tuple[int] = DIM_GRAY
