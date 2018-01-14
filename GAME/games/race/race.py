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
        self.misc = misc_helper.MiscHelper()

        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))
        self.bg, self.bg_rect = self.misc.load_background(os.path.join("games", "race", "data", "road2.png"))

        self.player = Player.Player(self.game_width * 0.45, self.game_height - 100, 43, 55,
                                    os.path.join("games", "race", "data", "car.png"))
        self.truck = Truck.Truck(random.randrange(0, self.game_width), -50, 196, 57,
                                 os.path.join("games", "race", "data", "Truckobstacle.png"), 1)
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.player, self.truck)

    def load(self):
        self.misc.play_music(os.path.join("games", "race", "data", "RDsound.wav"), -1)

        return True

    def update(self):
        self.GameDisplay.blit(self.bg, (0, 0))
        self.player.score = self.truck.dodge_count
        self.sprite_group.update()

        if self.truck.rect.colliderect(self.player.rect):
            self.dead()

        if self.misc.is_out_of_bounds(self.player.rect):
            self.dead()

        self.sprite_group.update()
        self.sprite_group.draw(self.GameDisplay)
        self.misc.draw_text("freesansbold", 30, "Score: " + str(self.player.score), (0, 0, 0), self.GameDisplay, 10,
                            10)

    def dead(self):
        self.misc.draw_text("freesansbold", 50, "DEAD", (255, 0, 0), self.GameDisplay, 200, 200)
        self.misc.draw_text("verdana", 63, "Your score: " + str(self.player.score), (0, 0, 0), self.GameDisplay, 200,
                            225)
        self.misc.draw_text("freesansbold", 50, "Press ESC to play another game.", (0, 0, 0), self.GameDisplay, 200,
                            300)

        self.truck.speed = 0
        self.player.changeX = 0
        self.player.dead = True
        self.misc.stop_music()

    def mousebutton_down(self, surface, event):
        pass

    def mousebutton_up(self, surface, event):
        pass

    def key_up(self, key):
        if key == 97 or key == 276:
            self.player.changeX = 0
        elif key == 100 or key == 275:
            self.player.changeX = 0

    def key_down(self, key):
        if not self.player.dead:
            if key == 97 or key == 276:
                self.player.changeX = -5
            elif key == 100 or key == 275:
                self.player.changeX = 5

    def stop_game(self):
        self.misc.stop_music()
        self.sprite_group.empty()
        self.player = None
        self.truck = None
