import pygame, sys, time, random, os, math
from handlers import config_handler
from helpers import misc_helper

from games.Galaxy_Trespassers.enemy import Enemy
from games.Galaxy_Trespassers.bullet import Bullet
from games.Galaxy_Trespassers.explosion import Explosion
from games.Galaxy_Trespassers.wall import Wall
from games.Galaxy_Trespassers.player import Player


# Classes to use: Enemy, Player, Bullet, Wall, Explosion


class GalaxyTrespassers:
    def __init__(self, surface):
        self.game_name = "Galaxy Trespassers"
        self.author = "Chérie Cederboom"
        self.surface = surface
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

        self.Player = Player()
        self.enemy1 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying.png"))
        self.enemy2 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying2.png"))
        self.enemy3 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying3.png"))
        self.enemy4 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying4.png"))
        # self.wall = wall.Wall()
        # self.explosion = explosion.Explosion()
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.Player, self.enemy1, self.enemy2, self.enemy3,
                              self.enemy4)  # , self.wall, self.bullet, self.explosion)

    def load(self):
        try:
            self.misc.set_background(self.surface, os.path.abspath("games/Galaxy_Trespassers/data/bg1.png"))
            self.misc.play_music(os.path.join("games", "Galaxy_Trespassers" "data", "Galaxy_trespassers_theme.wav"), -1)
        except pygame.error as e:
            print("ERROR in load()")
            return False
        return True

    def update(self):
        # This method gets called every frame so be careful with this one.
        self.misc.set_background(self.surface, os.path.abspath("games/Galaxy_Trespassers/data/bg1.png"))
        if self.sprite_group.has()
        self.sprite_group.update()
        self.sprite_group.draw(self.surface)

    def game_menu(self):
        gamedisplay.blit(background, background_rect)
        draw_text(gamedisplay, 'GALAXY TRESPASSERS', 63, game_width / 2, game_height / 6)
        draw_text(gamedisplay, 'PRESS TAB TO CONTINUE', 40, game_width / 2, game_height / 2.57)
        draw_text(gamedisplay, 'use WASD or arrow keys to move', 22, game_width / 2, game_height / 1.5)
        draw_text(gamedisplay, 'tap or hold space to fire', 22, game_width / 2, game_height / 1.4)
        draw_text(gamedisplay, 'press esc to quit game', 22, game_width / 2, game_height / 1.2)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_TAB:
                        waiting = False

    def died(self):
        gamedisplay.blit(background, background_rect)
        draw_text(gamedisplay, 'YOU HAVE DIED', 63, game_width / 2, game_height / 4.4)
        draw_text(gamedisplay, 'your score:', 22, game_width / 2, game_height / 2.3)
        draw_text(gamedisplay, str(player_score) + 'pts', 42, game_width / 2, game_height / 1.9)
        pygame.display.flip()
        time.sleep(4)

    def mousebutton_down(self, surface, event):
        # If you need to do an action on mouse button while it's in the down position then use this
        pass

    def mousebutton_up(self, surface, event):
        # If you need to do an action on mouse button while it's in the up position (after a down) then use this
        pass

    def invaded(self):
        self.misc.draw_text("verdana", 63, "INVADED", (255, 255, 255), self.surface, 100, 100)
        self.misc.draw_text("verdana", 63, "Your score: ", (255, 255, 255), self.surface, 100, 300)
        self.misc.draw_text("verdana", 63, "miljoenen", (255, 255, 255), self.surface, 100, 500)

    def collision(self):
        pass

    def key_up(self, key):
        # If you need to do an action on key inputs use this access key codes, check DRON.py for examples
        # For example: key A = keycode 97 so to check this do 'if key == 97'
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.speedx = 0
            self.Player.image = self.Player.image_stationary
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.speedx = 0
            self.Player.image = self.Player.image_stationary

    def key_down(self, key):
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.image = self.Player.image_flying
            self.Player.speedx = -self.Player.added_speed
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.image = self.Player.image_flying
            self.Player.speedx = self.Player.added_speed
        elif key == 32:
            self.sprite_group.add(Bullet(self.Player.rect.centerx, self.Player.rect.centery))
            self.Player.shoot()

    def stop_game(self):
        pass
