import pygame as py
from pygame import Surface
from constants import *
from dataclasses import dataclass

_GRID_STYLE = 10
_PACK_STYLE = 20
_NONE_STYLE = 30

class _MasterFrame():
    """Class that contains functions and data for master frames"""
    def __init__(self, width: int, height: int):
        self._place_style = _NONE_STYLE
        self.width = width
        self.height = height
            
    def _check_grid(self) -> int:
        if self._place_style == _PACK_STYLE:
            raise TypeError("Cannot use grid placement in the same frame where an object is packed")
        return self._place_style
        
    def _set_grid(self, row: int, col: int):
        self._place_style = _GRID_STYLE
        self.rows = row
        self.cols = col

    def _check_pack(self) -> int:
        if self._place_style == _GRID_STYLE:
            raise TypeError("Cannot use pack placement in the same frame that uses a grid")
        return self._place_style
        
    def _set_pack(self):
        self._place_style = _PACK_STYLE

class _ChildFrame():
    """Class that contains functions for child frames"""

    def __init__(self, master: _MasterFrame):
        self.master = master

    def grid_place(self, row: int, col: int):
        if self.master._check_grid() != _GRID_STYLE:
            self.master._set_grid(row=row, col=col)
        pass

    def pack_place(self, side: int):
        if self.master._check_pack() != _PACK_STYLE:
            self.master._set_pack()

        pass

class Main(_MasterFrame):
    """Main window of the program, handles events, and all input"""
    def __init__(self, screen_width: int, screen_height: int):
        # Initalize
        py.init()
        super().__init__(width=screen_width, height=screen_height)
        py.display.set_caption("TabSnake")

        # Class Variables
        self.surface = py.display.set_mode((screen_width, screen_height))
        self.clock = py.time.Clock()

    def start(self):
        running = True
        while running:

            # Event Loop
            for event in py.event.get():
                # Allows the user to quit the program
                if event.type == py.QUIT:
                    running = False

                # Detects user input
                if event.type == py.MOUSEBUTTONDOWN:
                    pass
        
            #clear the screen
            self.surface.fill(BLACK)
        
            # flip() updates the screen to make our changes visible
            py.display.flip()
            
            # how many updates per second
            self.clock.tick(60)

        py.quit()

class TabStaff(_ChildFrame):
    def __init__(self, master):
        super().__init__(master)
        self.line_width = 2
        self.line_spacing = 5

    def grid_place(self, row, col):
        super().grid_place(row, col)

    def pack_place(self, side):
        super().pack_place(side)

    def _draw_staff(self):
        pass

