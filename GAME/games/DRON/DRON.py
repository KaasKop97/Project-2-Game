import pygame
import random
import os
import math

from games.DRON.MotorBike import MotorBike
from helpers import misc_helper, log_helper
from handlers import config_handler


class Dron:
    def __init__(self, surface):
        self.game_name = "DRON"
        self.game_author = "Mitchel van Hamburg"

        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

        self.surface = surface
        self.misc = misc_helper.MiscHelper()
        self.log = log_helper.LogHelper()

        self.bike = MotorBike((20, self.game_height // 2), 1, (255, 0, 0), self.surface)
        self.opponent = MotorBike((self.game_width - 50, self.game_height // 2), 3, (0, 255, 0), self.surface)

        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.bike, self.opponent)

    def update(self):
        if self.bike.dead:
            self.player_dead()
        elif self.opponent.dead:
            self.victory()

        if not self.bike.dead or self.opponent.dead:
            self.handle_cpu_players()
        self.handle_line_thing()
        self.sprite_group.update()
        self.sprite_group.draw(self.surface)

    def load(self):
        try:
            #self.misc.set_background(surface, os.path.abspath("games/DRON/data/floor.png"))
            self.misc.play_music(os.path.abspath("games/DRON/data/music.ogg"), 0)
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
        elif key == 114 or self.bike.dead or self.opponent.dead:
            self.restart_game()

    def key_up(self, key):
        pass

    # http://zulko.github.io/easyAI/get_started.html
    def handle_cpu_players(self):
        possible_moves = [0, 1, 2, 3]
        # Find direction to player
        dx, dy = self.bike.rect.x - self.opponent.rect.x, self.bike.rect.y - self.opponent.rect.y
        dist = math.hypot(dx, dy)
        try:
            dx, dy = dx / dist, dy / dist
        except ZeroDivisionError:
            print("Woopsie")

        if dx <= 0 and dy <= 0:
            possible_moves = [0, 1, 3]
            print("Left top")
        elif dx >= 0 and dy <= 0:
            possible_moves = [0, 1, 2]
            print("right top")
        elif dx <= 0 and dy >= 0:
            possible_moves = [1, 2, 3]
            print("Left bottom")
        elif dx >= 0 and dy >= 0:
            possible_moves = [0, 1, 2]
            print("right bottom")
        else:
            print("Idk where the fuck he is...")

        if random.randrange(0, 1000) > 900:

            self.opponent.direction = random.choice(possible_moves)



    def handle_line_thing(self):
        player_line = self.bike.line
        cpu_line = self.opponent.line

        # Checking if the player hit a line
        for x in range(len(self.bike.line)):
            player_rect = pygame.Rect(player_line[x])
            if player_rect.collidepoint(self.bike.hitbox[0], self.bike.hitbox[1]):
                self.player_dead()
            elif player_rect.collidepoint(self.opponent.hitbox[0], self.opponent.hitbox[1]):
                self.player_dead()

        for x in range(len(self.opponent.line)):
            cpu_rect = pygame.Rect(cpu_line[x])
            if cpu_rect.collidepoint(self.bike.hitbox[0], self.bike.hitbox[1]):
                self.victory()
            elif cpu_rect.collidepoint(self.opponent.hitbox[0], self.opponent.hitbox[1]):
                self.victory()

    def victory(self):
        self.bike.direction = 4
        self.opponent.direction = 4
        self.misc.draw_text("Inconsolate", 80, "You've won! Press R to retry", (0, 255, 0), self.surface, 50, 50)

    def player_dead(self):
        self.bike.direction = 4
        self.opponent.direction = 4
        self.misc.draw_text("Inconsolate", 80, "You're dead! Press R to retry.", (255, 0, 0), self.surface, 50, 50)

    def restart_game(self):
        self.misc.stop_music()
        self.__init__(self.surface)
        self.load()

    def stop_game(self):
        self.misc.stop_music()
        self.bike = None
        self.opponent = None
        self.sprite_group.empty()
