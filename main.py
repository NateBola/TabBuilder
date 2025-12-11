import pygame as py
from pygame import Surface
from constants import *
from gui_settings import window_settings, tab_setting
from math import floor

# Global Variables
main_surface = py.display.set_mode((window_settings.width, window_settings.height), flags=py.RESIZABLE)
main_clock = py.time.Clock()

def pygame_event_loop():
    for event in py.event.get():
        if event.type == py.QUIT: pygame_quit()
        if event.type == py.MOUSEBUTTONDOWN: pass

def pygame_draw_loop(main_surface: Surface):

    def draw_tab_staff(surface: Surface):
        screen_width, screen_height = py.display.get_window_size()
        tab_width = screen_width - (2 * tab_setting.padx)
        tab_height = tab_setting.line_height * 5
        line_start = tab_setting.padx + tab_setting.line_padx
        line_end = screen_width - tab_setting.padx - tab_setting.line_padx
        rows = floor((screen_height - (2 * tab_setting.pady)) / (tab_height + tab_setting.pady))

        tab_rect = py.rect.Rect(tab_setting.padx, 0, tab_width, tab_height)

        tab_yloc = tab_setting.pady
        for i in range(rows):
        
            tab_rect.top = tab_yloc
            py.draw.rect(surface, tab_setting.color_bg, tab_rect)

            line_yloc = tab_yloc + tab_setting.line_height/2
            for i in range(5):
                py.draw.line(
                    surface,
                    tab_setting.line_color,
                    (line_start, line_yloc),
                    (line_end, line_yloc),
                    width=tab_setting.line_width
                )
                line_yloc += tab_setting.line_height

            tab_yloc = tab_yloc + tab_height + tab_setting.pady

    main_surface.fill(window_settings.color_bg)
    draw_tab_staff(main_surface)
    py.display.flip()

def pygame_quit():
    py.quit()
    exit()

# Setup Pygame
py.init()
py.display.set_caption("TabSnake")

while True:
    pygame_event_loop()
    pygame_draw_loop(main_surface)
    main_clock.tick(60)