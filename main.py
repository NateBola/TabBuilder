import pygame as py
from pygame import Surface
from constants import *
from gui import Main, draw_tab_staff

root = Main()
root.add_draw_function(draw_tab_staff, None)
root.start()