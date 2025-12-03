import pygame as py
from pygame import Surface
from constants import *
from dataclasses import dataclass
from math import floor

from gui_settings import window_settings

class Main():
    """Main window of the program, handles events, and all input"""

    def _event_loop(self):
        for event in py.event.get():
            if event.type == py.QUIT: self._running = False
            if event.type == py.MOUSEBUTTONDOWN: pass

    def _draw_loop(self):
        self._surface.fill(BLACK)
        for func in self._draw_functions:
            func()
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

    @property
    def surface(self):
        return self._surface

    def add_draw_function(self, draw_function):
        self._draw_functions.append(draw_function)

class TabStaff():

    def __init__(self, master: Main):
        self.master = master

        # Tab Staff Settings
        self.xpad = 20
        self.ypad = 40
        self.line_height = 10
        self.line_xpad = 2

        self.line_color = (255, 255, 255)
        self.bg_color = DIM_GRAY

    def draw_staff(self):
        screen_width, screen_height = py.display.get_window_size()
        tab_width = screen_width - (2 * self.xpad)
        tab_height = self.line_height * 5
        line_start = self.xpad + self.line_xpad
        line_end = screen_width - self.xpad - self.line_xpad
        rows = floor((screen_height - (2 * self.ypad)) / (tab_height + self.ypad))

        tab_rect = py.rect.Rect(self.xpad, 0, tab_width, tab_height)

        tab_yloc = self.ypad
        for i in range(rows):
            
            tab_rect.top = tab_yloc
            py.draw.rect(self.master.surface, self.bg_color, tab_rect)

            line_yloc = tab_yloc + self.line_height/2
            for i in range(5):
                py.draw.line(self.master.surface, WHITE, (line_start, line_yloc), (line_end, line_yloc))
                line_yloc += self.line_height

            tab_yloc = tab_yloc + tab_height + self.ypad




