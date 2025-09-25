import pygame as py
from pygame import Surface
from constants import *
from dataclasses import dataclass

class Main():
    """Main window of the program, handles events, and all input"""
    def __init__(self, screen_width: int, screen_height: int):
        # Initalize
        py.init()
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

class TabStaff():
    def __init__(self, master):
        super().__init__(master)
        self.line_width = 2
        self.line_spacing = 5

    def _draw_staff(self):
        pass

