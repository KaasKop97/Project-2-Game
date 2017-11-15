import pygame

from handlers import config_handler, game_handler
from helpers import log_helper


class MenuHelper:
    def __init__(self):
        self.menu_items = ["PLAY", "ABOUT", "SETTINGS", "CREDITS", "QUIT"]
        self.menu_items_coord = []
        self.menu_selected = []
        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)
        self.config = config_handler.ConfigHandler()
        self.game_loader = game_handler.GameHandler()

        self.log = log_helper.LogHelper()

    def create_button(self, surface, text_colour, x, y, width, height, text, colour=(66, 66, 66)):
        pygame.draw.rect(surface, colour, (x, y, width, height))

        label = self.font.render(text, 1, text_colour)
        self.menu_items_coord.append(str(text) + " " + str(x) + " " + str(y) + " " + str(width) + " " + str(height))
        surface.blit(label, (x + 2, y))  # Renders the label just above the bottom of the button

    def button_pressed(self, click_position):
        for i in range(len(self.menu_items_coord)):
            coords_split = self.menu_items_coord[i].split()

            if int(coords_split[1]) <= int(click_position[0]) <= int(coords_split[1]) + int(coords_split[3]) and \
                                    int(coords_split[2]) <= int(click_position[1]) <= int(coords_split[2]) + int(
                        coords_split[4]):
                return coords_split[0]

    def draw_main_menu(self, surface):
        self.menu_selected = "MAIN"
        for i in range(len(self.menu_items)):
            self.create_button(surface, (255, 255, 255), int(self.config.get_value("game", "width")) // 2 - 55,
                               10 + (40 * i), 85, 30, self.menu_items[i])

    def draw_game_selection(self, surface):
        self.menu_selected = "PLAY"
        self.reset(surface, (255, 255, 255))
        for i in range(len(self.game_loader.games_in_path)):
            self.create_button(surface, (255, 255, 255), int(self.config.get_value("game", "width")) // 2 - 55,
                               10 + (40 * i), 85, 30, self.game_loader.games_in_path[i])
            if i == len(self.game_loader.games_in_path) - 1:
                self.create_button(surface, (255, 255, 255), 10, 10 + (80 * i), 85, 30, "BACK")

    def draw_pop_up(self, surface, text, button_text):
        print(str(surface) + " " + str(text) + " " + str(button_text))

    def go_back(self, surface):
        self.log.write_log("DEBUG", str(self.menu_selected))
        if self.menu_selected in self.menu_items:
            if self.menu_selected == "MAIN":
                self.draw_main_menu(surface)
            elif self.menu_selected == "PLAY":
                self.draw_game_selection(surface)
            elif self.menu_selected == "ABOUT":
                self.draw_about(surface)
            elif self.menu_selected == "SETTINGS":
                self.draw_settings(surface)
            elif self.menu_selected == "CREDITS":
                self.draw_credits(surface)
        else:
            return False

    def set_background(self, surface, image):
        bg_img = pygame.image.load(image)
        bg_img = pygame.transform.scale(bg_img, (
        int(self.config.get_value("game", "width")), int(self.config.get_value("game", "height"))))
        image_rect = bg_img.get_rect()

        surface.blit(bg_img, image_rect)

    def get_last_button_coords(self):
        return self.menu_items_coord[-1]

    def reset(self, surface, colour=(255, 255, 255)):
        self.menu_items_coord.clear()
        surface.fill(colour)
