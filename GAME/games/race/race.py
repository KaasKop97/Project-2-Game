                                # # Installations # #
import pygame
import os
import random
from handlers import config_handler
from games.race import Player, Truck


                                # # Class Race # #

class race:
    def __init__(self, surface):
        self.game_name      =   "Insane Driver!"
        self.author         =   "Amanpreet Singh"
        self.GameDisplay    =   surface
        self.conf           =   config_handler.ConfigHandler()
        self.game_width     =   int(self.conf.get_value ("game", "width"))
        self.game_height    =   int(self.conf.get_value("game", "height"))
        self.player         =   Player.Player(self.game_width * 0.45, self.game_height * 0.9, 43, 55,
                                              os.path.join("games", "race", "data", "car.png"))
        self.truck          =   Truck.Truck(random.randrange (0, self.game_width), -600, 196, 57,
                                             os.path.join("games", "race", "data", "Truckobstacle.png"), 1)
        self.sprite_group   =   pygame.sprite.Group()
        self.sprite_group.add(self.player, self.truck)

    def load (self, surface):
        return True

    def update (self):
        self.sprite_group.update()
        self.sprite_group.draw(self.GameDisplay)

    def mousebutton_down(self, surface, event):
        pass

    def mousebutton_up (self, surface, event):
        pass

    def key_up(self, key):
        if key == 97 or key == 276:
            self.Player.changeX = 0
        elif key == 100 or key == 275:
            self.Player.ChangeX = 0

    def key_down(self, key):
        if key == 97 or key == 276:
            self.Player.changeX = -5
        elif key == 100 or key == 275:
            self.Player.changeX = 5


    def stop_game(self):
        pass


























































