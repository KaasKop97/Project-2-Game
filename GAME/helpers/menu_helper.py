from handlers import config_handler

from helpers import misc_helper

import pygame
import os


# TODO: Back functionality
class MenuHelper:
    def __init__(self, surface):
        self.main_menu_items = ["PLAY", "QUIT"]
        self.game_names = [
            "DRON",
            "Galaxy Trespassers",
            "Race",
            "Dodge the Fangirls"
        ]
        self.rectangles = {}
        self.currently_drawn = ""

        self.font = pygame.font.init()
        self.font = pygame.font.SysFont("Inconsolata", 15)

        self.surface = surface
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.test = ""

    def create_button(self, text, x, y, width, height, text_colour, rect_colour=(66, 66, 66)):
        rect = pygame.draw.rect(
            self.surface, rect_colour, (x, y, width, height))
        label = self.font.render(text, 1, text_colour)

        self.rectangles[text] = rect

        self.surface.blit(label, (x + 2, y))

    def get_button_pressed(self, click_position):
        for key, value in self.rectangles.items():
            try:
                if value.collidepoint(click_position[0], click_position[1]):
                    return key
            except KeyError:
                print("Key does not exists!")

    def draw_menu(self, menu_name):
        self.reset_menu()
        self.misc.set_background(self.surface, os.path.join(os.getcwd(), "menu", "background.jpg"))

        if menu_name == self.currently_drawn:
            return False

        if menu_name == "main":

            for i in range(len(self.main_menu_items)):
                self.create_button(self.main_menu_items[i], 50, 10 + (40 * i), 85, 30, (255, 255, 255))
            # TODO:
            # self.misc.play_music("")
        elif menu_name == "PLAY":
            for i in range(len(self.game_names)):
                self.create_button(self.game_names[i], 50, 10 + (40 * i), 150, 30, (255, 255, 255))

    def get_hover(self, hover_pos):
        controls = ""
        hover_author = ""
        for key, value in self.rectangles.items():
            try:
                if value.collidepoint(hover_pos[0], hover_pos[1]):
                    print(key)
                    if key == "DRON":
                        hover_author = "Game made by: Mitchel"
                        display_text_hover = "Controls: WASD or the arrow keys. Press R to rety."
                    elif key == "Galaxy Trespassers":
                        hover_author = "Game made by: Cherie"
                        display_text_hover = "Controls: WASD or the arrow keys. Press space to shoot."
                    elif key == "Race":
                        hover_author = "Game made by: Aman"
                        display_text_hover = "Controls: WASD or the arrow keys."
                    elif key == "Dodge the Fangirls":
                        hover_author = "Game made by: Charone"
                        display_text_hover = "Controls: WASD or the arrow keys."
                    else:
                        display_text_hover = ""
                        hover_author = ""
                    self.misc.draw_text("Verdana", 15, hover_author, (255, 255, 255), self.surface, 275, 20)
                    self.misc.draw_text("Verdana", 15, display_text_hover, (255, 255, 255), self.surface, 275, 40)

            except KeyError:
                print("Key does not exists!")

    def reset_menu(self):
        self.surface.fill((0, 0, 0))
        self.rectangles.clear()
