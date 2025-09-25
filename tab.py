import pygame as py

py.font.SysFont("Helvetica", 8, bold=True)

# PLAN

#   Create a long running tab that resizes to the screen
#   Make this into one large window

class TabChar():
    def __init__(self):
        self.character: str = None

    def draw(self, location: tuple[int]):
        pass

class TabStaff():
    def __init__(self, surface: py.Surface, location: tuple[int],  ):
        self.LINE_HEIGHT = 5
