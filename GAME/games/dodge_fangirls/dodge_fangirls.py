import pygame
import os
from handlers import config_handler
from games.dodge_fangirls import player
from games.dodge_fangirls import enemy
import random
from helpers import misc_helper


class DodgeFangirls:
    def __init__(self, surface):
        self.game_name = "Dodge the Fangirls"
        self.author = "Charone Monteiro Tavares"
        self.gamedisplay = surface
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))
        self.Player = player.Player(self.game_width * 0.45, self.game_height * 0.9, 43, 55,
                                    os.path.join("games", "dodge_fangirls", "data", "cbCHARACTER.png"))
        self.enemy4 = enemy.Enemys(random.randrange(0, self.game_width), -500, 196, 57,
                                   os.path.join("games", "dodge_fangirls", "data", "OBSTACLE4.png"), 4)
        self.enemy3 = enemy.Enemys(random.randrange(0, self.game_width), -300, 140, 57,
                                   os.path.join("games", "dodge_fangirls", "data", "OBSTACLE3.png"), 3)
        self.enemy2 = enemy.Enemys(random.randrange(0, self.game_width), -700, 92, 57,
                                   os.path.join("games", "dodge_fangirls", "data", "OBSTACLE2.png"), 2)
        self.enemy1 = enemy.Enemys(random.randrange(0, self.game_width), -100, 45, 57,
                                   os.path.join("games", "dodge_fangirls", "data", "RiCHARACTER.png"), 1)

        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.Player, self.enemy1, self.enemy2, self.enemy3, self.enemy4)
        self.enemies = [self.enemy1, self.enemy2, self.enemy3, self.enemy4]
        self.score = self.Player.score

    def load(self):
        # This is the first thing that's called, load stuff here. Must return a boolean!!
        self.misc.set_background(self.gamedisplay,
                                 os.path.join("games", "dodge_fangirls", "data", "achtergrondfoto.png"))
        self.misc.play_music(os.path.join("games", "dodge_fangirls", "data", "loyal.mp3"), -1)

        return True

    def update(self):
        # This method gets called every frame so be careful with this one.
        self.misc.set_background(self.gamedisplay,
                                 os.path.join("games", "dodge_fangirls", "data", "achtergrondfoto.png"))

        for x in range(len(self.enemies)):
            if self.enemies[x].dodged:
                self.score = self.score + self.enemies[x].score
                self.enemies[x].dodged = False
            pygame.event.pump()

        self.misc.draw_text("verdana", 30, "Score: " + str(self.score), (255, 255, 255), self.gamedisplay, 10, 0)

        for x in range(len(self.enemies)):
            if self.Player.rect.colliderect(self.enemies[x].rect):
                self.die()

        if self.misc.is_out_of_bounds(self.Player.rect):
            self.die()

        self.sprite_group.update()
        self.sprite_group.draw(self.gamedisplay)

    def mousebutton_down(self, surface, event):
        # If you need to do an action on mouse button while it's in the down position then use this
        pass

    def mousebutton_up(self, surface, event):
        # If you need to do an action on mouse button while it's in the up position (after a down) then use this
        pass

    def key_up(self, key):
        # If you need to do an action on key inputs use this access key codes, check DRON.py for examples
        # For example: key A = keycode 97 so to check this do 'if key == 97'
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.changeX = 0
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.changeX = 0

    def key_down(self, key):
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.changeX = -15
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.changeX = 15

    def stop_game(self):
        self.sprite_group.empty()
        for x in range(len(self.enemies)):
            self.enemies[x] = None
            pygame.event.pump()
        self.Player = None
        self.misc.stop_music()

    def die(self):
        # self.misc.draw_text("verdana", 50, "CRASHED", (255, 0, 0), self.gamedisplay, self.game_width // 2.5,
        #                     self.game_height // 2)
        # self.misc.draw_text("freesanbold.ttf", 30, "Press ESC to play another game", (255, 0, 0), self.gamedisplay,
        #                     250, 0)
        self.misc.game_over(str(self.score), self.gamedisplay, "You bumped into an ex", "verdana", 20, (255, 255, 255))

        self.sprite_group.empty()

        self.misc.stop_music()
