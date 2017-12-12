import pygame
import os
import random

from games.DRON.MotorBike import MotorBike
from helpers import misc_helper, log_helper


class Dron:
    def __init__(self, surface):
        self.game_name = "DRON"
        self.game_author = "Mitchel van Hamburg"

        self.surface = surface
        self.misc = misc_helper.MiscHelper()
        self.log = log_helper.LogHelper()

        self.bike = MotorBike((10, 10), -90, (255, 0, 0), 1, self.surface)
        self.opponent = MotorBike((500, 500), 90, (0, 255, 0), 3, self.surface)

        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.bike, self.opponent)

    def update(self):
        if self.bike.dead:
            self.player_dead()
        elif self.opponent.dead:
            self.victory()
        # Somehow need to fix being able to draw the background every frame without lag.
        # Or remove the last position of the sprite with something?
        self.handle_cpu_players()
        self.sprite_group.update()
        self.sprite_group.draw(self.surface)

    def load(self):
        try:
            #self.misc.set_background(surface, os.path.abspath("games/DRON/data/floor.png"))
            self.misc.play_music(os.path.abspath("games/DRON/data/music.ogg"))
        except pygame.error as e:
            self.log.write_log("ERROR", "Something died fix it you idiot: " + str(e))
            return False
        return True

    def mousebutton_down(self, surface, position):
        # I do not need dis for my game so I pass it
        pass

    def mousebutton_up(self, surface, position):
        # I do not need dis for my game so I pass it
        pass

    def key_down(self, key):
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.bike.direction = 3
        elif key == 119 or key == 273:
            # "W" or arrow up key
            self.bike.direction = 0
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.bike.direction = 1
        elif key == 115 or key == 274:
            # "S" or arrow down key
            self.bike.direction = 2
        elif key == 27:
            self.stop_game()
            print("Should kill the game")
        elif key == 114 and self.bike.dead:
            self.restart_game()

    def key_up(self, key):
        pass

    def handle_cpu_players(self):
        if random.randint(0, 100) > 95:
            self.opponent.direction = random.randint(0, 3)

    def victory(self):
        self.misc.draw_text("Inconsolate", 80, "You've won!", (255, 0, 0), self.surface, 50, 50)

    def player_dead(self):
        self.misc.draw_text("Inconsolate", 80, "You're dead, press R to retry.", (255, 0, 0), self.surface, 50, 50)

    def restart_game(self):
        self.misc.stop_music()
        self.__init__(self.surface)
        self.load()

    def stop_game(self):
        self.misc.stop_music()
        self.bike = None
        self.sprite_group.empty()
