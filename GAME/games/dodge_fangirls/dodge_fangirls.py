import pygame
import os
from handlers import config_handler
from games.dodge_fangirls import player, enemy
import random


class DodgeFangirls:
    def __init__(self, surface):
        self.game_name = "Dodge the Fangirls"
        self.author = "Charone"
        self.gamedisplay = surface
        self.conf = config_handler.ConfigHandler()
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
                                   os.path.join("games", "dodge_fangirls", "data", "OBSTACLE4.png"), 1)
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.Player, self.enemy1, self.enemy2, self.enemy3, self.enemy4)

    def load(self, surface):
        # This is the first thing that's called, load stuff here. Must return a boolean!!
        return True

    def update(self):
        # This method gets called every frame so be careful with this one.
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
            self.Player.changeX = -5
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.changeX = 5

    def stop_game(self):
        pass
