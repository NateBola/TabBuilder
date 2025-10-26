import pygame as py
from constants import *
from frames import Main, TabStaff

root = Main(screen_width=700, screen_height=500)
tab = TabStaff(root)
root.add_draw(tab._draw_staff)

root.start()