import pygame as py
from pygame.math import Vector2
from gui_settings import *

def pygame_quit():
    py.quit()
    exit()

# Setup Pygame
py.init()
py.display.set_caption("TabSnake")

# Pygame Variables
MAIN_SURFACE = py.display.set_mode((WindowGui.width, WindowGui.height), flags=py.RESIZABLE)
MAIN_CLOCK = py.time.Clock()

while True:

    # Event Loop
    for event in py.event.get():
        # Event, Handles Quiting
        if event.type == py.QUIT: pygame_quit()

    # Graphics Loops
    MAIN_SURFACE.fill(WindowGui.color_bg)
    
    py.display.flip()

    # Tick Clock
    MAIN_CLOCK.tick(60)