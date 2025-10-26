import pygame as py
from pygame import Surface
from constants import *
from dataclasses import dataclass
from math import floor

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
        self.surface = py.display.set_mode((screen_width, screen_height), flags=py.RESIZABLE)
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




