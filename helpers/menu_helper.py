import pygame
import os


class MenuHelper:
    def __init__(self):
        self.menu_items = ["PLAY", "ABOUT", "CREDITS"]
        self.menu_items_coord = []
        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)

    def make_button(self, surface, text_colour, x, y, width, height, text, colour=(66, 66, 66)):
        pygame.draw.rect(surface, colour, (x, y, width, height))

        label = self.font.render(text, 1, text_colour)
        self.menu_items_coord.append(str(text) + " " + str(x) + " " + str(y) + " " + str(width) + " " + str(height))
        surface.blit(label, (x + 2, y))  # Renders the label just above the bottom of the button

    def button_pressed(self, click_position):
        print("Click X: " + str(click_position[0]) + " Y: " + str(click_position[1]))
        for i in range(len(self.menu_items_coord)):
            coords_split = self.menu_items_coord[i].split()
            print("Menu coords: " + str(coords_split))
            print(int(coords_split[0]) + int(coords_split[2]))
            if int(click_position[0]) >= int(coords_split[0]) <= int(coords_split[2]) and\
               int(click_position[1]) >= int(coords_split[1]) <= int(coords_split[3]):
                print("You pressed a button, good job!")



    def draw_background_for_game(self, surface, game_name):
        bg_img = pygame.image.load(os.path.join("games", game_name + "/background.jpg"))
        image_rect = bg_img.get_rect()

        surface.blit(bg_img, image_rect)
