import pygame as py
from pygame import Surface
from constants import *
from dataclasses import dataclass
from math import floor

from gui_settings import window_settings, tab_setting

class Main():
    """Main window of the program, handles events, and all input"""

    def _event_loop(self):
        for event in py.event.get():
            if event.type == py.QUIT: self._running = False
            if event.type == py.MOUSEBUTTONDOWN: pass

    def _draw_loop(self):
        self._surface.fill(window_settings.color_bg)
        for i, func in enumerate(self._draw_functions):
            func(self._surface, self._draw_parameters[i])
        py.display.flip()

    def start(self):
        while self._running:
            self._event_loop()
            self._draw_loop()
            self._clock.tick(60)
        py.quit()

    def __init__(self):
        """_summary_
        """
        # Initalize
        py.init()
        py.display.set_caption("TabSnake")

        # Class Variables
        self._running = True
        self._surface = py.display.set_mode((window_settings.width, window_settings.height), flags=py.RESIZABLE)
        self._clock = py.time.Clock()
        self._draw_functions = list()
        self._draw_parameters = dict()

    @property
    def surface(self):
        return self._surface

    def add_draw_function(self, draw_function, func_parameters):
        """_summary_

        Args:
            draw_function (_type_): _description_
            func_parameters (_type_): _description_
        """
        self._draw_functions.append(draw_function)
        self._draw_parameters[len(self._draw_functions)-1] = func_parameters

def draw_tab_staff(surface: Surface, parameters):
    """_summary_

    Args:
        surface (Surface): _description_
        parameters (_type_): _description_
    """
    screen_width, screen_height = py.display.get_window_size()
    tab_width = screen_width - (2 * tab_setting.padx)
    tab_height = tab_setting.line_height * 5
    line_start = tab_setting.padx + tab_setting.line_padx
    line_end = screen_width - tab_setting.padx - tab_setting.line_padx
    rows = floor((screen_height - (2 * tab_setting.pady)) / (tab_height + tab_setting.pady))

    tab_rect = py.rect.Rect(tab_setting.padx, 0, tab_width, tab_height)

    tab_yloc = tab_setting.pady
    for i in range(rows):
        
        tab_rect.top = tab_yloc
        py.draw.rect(surface, tab_setting.color_bg, tab_rect)

        line_yloc = tab_yloc + tab_setting.line_height/2
        for i in range(5):
            py.draw.line(
                surface,
                tab_setting.line_color,
                (line_start, line_yloc),
                (line_end, line_yloc),
                width=tab_setting.line_width
            )
            line_yloc += tab_setting.line_height

        tab_yloc = tab_yloc + tab_height + tab_setting.pady
        




