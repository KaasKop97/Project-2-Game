import pygame
import os

from games.DRON.MotorBike import MotorBike
from helpers import misc_helper, log_helper


class Dron:
    def __init__(self):
        self.game_name = "DRON"
        self.game_author = "Mitchel van Hamburg"

        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)
        self.misc = misc_helper.MiscHelper()
        self.log = log_helper.LogHelper()

        self.bike = MotorBike()

        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.bike)

    def update(self, surface):
        if self.bike.dead:
            self.player_dead()
        self.sprite_group.update()
        self.sprite_group.draw(surface)

    def load(self, surface):
        try:
            self.misc.set_background(surface, os.path.abspath("games/DRON/data/floor.png"))
            self.misc.play_music(os.path.abspath("games/DRON/data/music.ogg"))
        except pygame.error as e:
            self.log.write_log("ERROR", "Something died: " + str(e))
        return True

    def mousebutton_down(self, surface, position):
        # I do not need dis for my game
        pass

    def mousebutton_up(self, surface, position):
        # I do not need dis for my game
        pass

    def key_input(self, key):
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.bike.direction = "left"
        elif key == 119 or key == 273:
            # "W" or arrow up key
            self.bike.direction = "up"
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.bike.direction = "right"
        elif key == 115 or key == 274:
            # "S" or arrow down key
            self.bike.direction = "down"
        elif key == 27:
            self.stop_game()
            print("Should kill the game")

    def player_dead(self):
        print("Display a message saying that the user is dead and is able to try again or something")

    def stop_game(self):
        self.misc.stop_music()
        self.bike = None
        self.font = None
        self.sprite_group.empty()
