# # Installations # #
import pygame
import os
import random
from handlers import config_handler
from games.race import Player, Truck
from helpers import misc_helper


# # Class Race # #

class race:
    def __init__(self, surface):
        self.game_name = "Race"
        self.author = "Amanpreet Singh"
        self.GameDisplay = surface
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))
        self.player = Player.Player(self.game_width * 0.45, 450, 43, 55,
                                    os.path.join("games", "race", "data", "car.png"))
        self.truck = Truck.Truck(random.randrange(0, self.game_width), -50, 196, 57,
                                 os.path.join("games", "race", "data", "Truckobstacle.png"), 1)
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.player, self.truck)
        self.misc = misc_helper.MiscHelper()

    def load(self):
        self.misc.set_background(self.GameDisplay, os.path.join("games", "race", "data", "road2.png"))
        self.misc.play_music(os.path.join("games", "race", "data", "RDsound.wav"), -1)
        return True

    def update(self):
        self.sprite_group.update()
        self.misc.set_background(self.GameDisplay, os.path.join("games", "race", "data", "road2.png"))

        if self.truck.rect.colliderect(self.player.rect):
            self.dead()

        if self.misc.is_out_of_bounds(self.player.rect):
            self.dead()

        self.sprite_group.update()
        self.sprite_group.draw(self.GameDisplay)

        # def score (self):
        # self.misc.draw_text("freesanbold.ttf", 21, "Dodged:%d", (255, 255, 255), self.GameDisplay,
        # self.X +(self.game_width / 2), self.Y + (self.game_height))


        # textRect.center = ((x + (w / 2), y + (h / 2)))

    def dead(self):
        self.misc.draw_text("freesanbold.ttf", 50, "DEAD", (255, 0, 0), self.GameDisplay,
                            self.game_width / 2, self.game_height / 2)
        self.misc.draw_text("freesanbold.ttf", 30, "Press ESC to play another game", (255,255,255), self.GameDisplay,
                            self.game_width / 2, self.game_height / 2)

        self.truck.speed = 0
        self.player.changeX = 0
        self.misc.stop_music()
        self.dead = False

    def mousebutton_down(self, surface, event):
        pass

    def mousebutton_up(self, surface, event):
        pass

    def key_up(self, key):
        if key == 97 or key == 276:
            self.player.changeX = 0
        elif key == 100 or key == 275:
            self.player.ChangeX = 0

    def key_down(self, key):
        #if not self.player.dead:
            if key == 97 or key == 276:
                self.player.changeX = -5
            elif key == 100 or key == 275:
                self.player.changeX = 5

    def stop_game(self):
        pass
