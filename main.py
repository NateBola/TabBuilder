import pygame as py
from pygame import Surface
from color_pallet import *
from gui_settings import *
from math import floor

class GuitarTab():

    def __init__(self, surface: Surface, y_start_pos: int):
        self._surface = surface
        self._rect = py.Rect(
            (GuitarTabGui.rect_start, y_start_pos),
            (GuitarTabGui.rect_width, GuitarTabGui.rect_height)
        )

        self._line_rect_list = list()

    def draw(self):
        py.draw.rect(self._surface, GuitarTabGui.rect_color, self._rect)

        y_pos = self._rect.top
        for i in range(GuitarTabGui.line_count):
            py.draw.line(
                self._surface,
                GuitarTabGui.line_color,
                (self._rect.left, y_pos),
                (self._rect.right, y_pos),
                GuitarTabGui.line_width
            )
            y_pos += GuitarTabGui.line_space

    def update(self, y_delta: int):
        self._rect.move_ip(0, y_delta*SCROLL_FACTOR)

def pygame_quit():
    py.quit()
    exit()

# Setup Pygame
py.init()
py.display.set_caption("TabSnake")

# Pygame Variables
MAIN_SURFACE = py.display.set_mode((WindowGui.width, WindowGui.height), flags=py.RESIZABLE)
MAIN_CLOCK = py.time.Clock()

# Variables
start_height = GuitarTabGui.rect_padding
guitar_tab_list = list()
for i in range(3):
    guitar_tab_list.append(GuitarTab(MAIN_SURFACE, start_height))
    start_height += (GuitarTabGui.rect_height + GuitarTabGui.rect_padding)

while True:

    # Event Loop
    for event in py.event.get():
        # Event, Handles Quiting
        if event.type == py.QUIT: pygame_quit()

        # Event, User click
        if event.type == py.MOUSEBUTTONDOWN: pass

        # Event, User Scroll
        if event.type == py.MOUSEWHEEL:
            for gui_element in guitar_tab_list: gui_element.update(event.y)

    # Graphics Loops
    MAIN_SURFACE.fill(WindowGui.color_bg)
    for gui_element in guitar_tab_list: gui_element.draw()
    py.display.flip()

    # Tick Clock
    MAIN_CLOCK.tick(60)
    