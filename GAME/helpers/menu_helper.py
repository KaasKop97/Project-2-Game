from handlers import config_handler

from helpers import misc_helper

import pygame


# TODO: Back functionality
class MenuHelper:
    def __init__(self, surface):
        self.main_menu_items = ["PLAY", "SETTINGS", "CREDITS", "QUIT"]
        self.game_names = [
            "DRON",
            "Galaxy Trespasser",
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

    def create_button(self, text, x, y, width, height, text_colour, rect_colour=(66, 66, 66)):
        rect = pygame.draw.rect(
            self.surface, rect_colour, (x, y, width, height))
        label = self.font.render(text, 1, text_colour)

        self.rectangles[text] = rect

        self.surface.blit(label, (x + 2, y))

    def get_button_pressed(self, click_position):
        for key, value in self.rectangles.items():
            if value.collidepoint(click_position[0], click_position[1]):
                return key
            else:
                return "Dodge the Fangirls"

    def draw_menu(self, menu_name):
        self.reset_menu()

        if menu_name == self.currently_drawn:
            return False

        if menu_name == "main":
            for i in range(len(self.main_menu_items)):
                self.create_button(self.main_menu_items[i], int(self.conf.get_value("game", "width")) // 2 - 55, 10 + (40 * i), 85, 30, (255, 255, 255))
            self.currently_drawn = "main"
            # TODO:
            # self.misc.play_music("")
        elif menu_name == "PLAY":
            for i in range(len(self.game_names)):
                self.create_button(self.game_names[i], int(self.conf.get_value("game", "width")) // 2 - 55,
                                   10 + (40 * i), 85, 30, (255, 255, 255))
            self.currently_drawn = "play"

    def reset_menu(self):
        self.surface.fill((0, 0, 0))
        self.rectangles.clear()
