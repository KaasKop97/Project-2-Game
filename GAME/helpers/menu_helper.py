import pygame
import os

from handlers import config_handler, game_handler
from helpers import log_helper, misc_helper


class MenuHelper:
    def __init__(self):
        self.main_menu_items = ["PLAY", "ABOUT", "SETTINGS", "CREDITS", "QUIT GAME"]
        self.menu_selected = []
        self.menu_item_name = []
        self.rectangles = []
        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)
        self.config = config_handler.ConfigHandler()
        self.game_loader = game_handler.GameHandler()
        self.game_names = self.game_loader.game_names
        self.misc_helper = misc_helper.MiscHelper()

        self.log = log_helper.LogHelper()

    def create_button(self, surface, text_colour, x, y, width, height, text, colour=(66, 66, 66)):
        rect = pygame.draw.rect(surface, colour, (x, y, width, height))
        self.rectangles.append(rect)

        label = self.font.render(text, 1, text_colour)
        self.menu_item_name.append(str(text))
        surface.blit(label, (x + 2, y))  # Renders the label just above the bottom of the button

    def button_pressed(self, click_position):
        for i in range(len(self.rectangles)):
            if self.rectangles[i].collidepoint(click_position[0], click_position[1]):
                return self.menu_item_name[i]

    def draw_main_menu(self, surface):
        self.misc_helper.set_background(surface, os.path.join("menu", "background.png"))
        self.add_to_back("main")
        for i in range(len(self.main_menu_items)):
            self.create_button(surface, (255, 255, 255), int(self.config.get_value("game", "width")) // 2 - 55,
                               10 + (40 * i), 85, 30, self.main_menu_items[i])

    def draw_game_selection(self, surface):
        self.add_to_back("game_selection")
        self.reset(surface, (255, 255, 255))
        for i in range(len(self.game_names)):
            self.create_button(surface, (255, 255, 255), int(self.config.get_value("game", "width")) // 2 - 55,
                               10 + (40 * i), 85, 30, self.game_names[i])
            if i == len(self.game_names) - 1:
                self.create_button(surface, (255, 255, 255), 10, 10 + (80 * i), 85, 30, "BACK")

    def draw_pop_up(self, surface, text, button_text):
        print(str(surface) + " " + str(text) + " " + str(button_text))

    def go_back(self, surface):
        self.log.write_log("DEBUG", str(self.menu_selected))
        self.reset(surface)
        menu_selected_length = len(self.menu_selected)
        #TODO Add all menu selections and their methods
        if self.menu_selected[menu_selected_length - 1] and menu_selected_length == "main":
            self.draw_main_menu(surface)
        elif self.menu_selected[menu_selected_length - 1] == "game_selection":
            self.draw_game_selection(surface)


    def add_to_back(self, menu_name):
        if self.menu_selected and not self.menu_selected[len(self.menu_selected)] == menu_name:
            self.menu_selected.append(menu_name)
        print(self.menu_selected)

    def get_last_button_coords(self):
        return self.menu_item_name[-1]

    def reset(self, surface, colour=(255, 255, 255)):
        self.menu_item_name.clear()
        self.rectangles.clear()
        surface.fill(colour)
