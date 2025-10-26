import pygame as py
from pygame import Surface
from constants import *
from dataclasses import dataclass

class Main():
    """Main window of the program, handles events, and all input"""
    def __init__(self, screen_width: int, screen_height: int):
        """_summary_

        Args:
            screen_width (int): The width of the pygame window
            screen_height (int): The height of the pygame window
        """
        # Initalize
        py.init()
        py.display.set_caption("TabSnake")

        # Class Variables
        self.surface = py.display.set_mode((screen_width, screen_height))
        self.clock = py.time.Clock()
        self.draw_functions = list()

    def add_draw(self, draw_function):
        self.draw_functions.append(draw_function)

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

            #draw functions
            for func in self.draw_functions:
                func()
        
            # flip() updates the screen to make our changes visible
            py.display.flip()
            
            # how many updates per second
            self.clock.tick(60)

        py.quit()

class TabStaff():
    def __init__(self, master: Main):
        self.master = master
        self.surface = Surface((600, 60))

    def _draw_staff(self):
        self.surface.fill(ATOMIC_TANGERINE)
        self.master.surface.blit(self.surface, (0, 0))

