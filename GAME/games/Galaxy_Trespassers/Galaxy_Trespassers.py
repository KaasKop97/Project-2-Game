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
        self.bg, self.bg_rect = self.misc.load_background(os.path.join(os.getcwd(), "games", "Galaxy_Trespassers", "data", "bg1.png"))

        self.Player = Player()
        self.enemy1 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying.png"))
        self.enemy2 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying2.png"))
        self.enemy3 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying3.png"))
        self.enemy4 = Enemy(os.path.join("games", "Galaxy_Trespassers", "data",
                                         "enemy_ship_flying4.png"))
        self.bullet = None
        self.explosion = None
        self.Player.score = 0
        self.wall = Wall()
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.Player, self.wall, self.enemy1, self.enemy2, self.enemy3, self.enemy4)
        self.enemies = [self.enemy1, self.enemy2, self.enemy3, self.enemy4]

    def load(self):
        self.surface.blit(self.bg, (0, 0))
        self.misc.play_music(os.path.abspath("games/Galaxy_Trespassers/data/Galaxy_trespassers_theme.wav"), -1)
        return True

    def update(self):
        # This method gets called every frame so be careful with this one.
        self.surface.blit(self.bg, (0, 0))
        if self.sprite_group.has(self.bullet):
            if self.bullet.rect.bottom < 18:
                self.sprite_group.remove(self.bullet)
                self.bullet = None
            elif self.bullet.hit and pygame.time.get_ticks() >= self.bullet.spawn_time + 1000:
                self.sprite_group.remove(self.bullet)
                self.bullet = None
        self.collision()
        self.sprite_group.update()
        self.sprite_group.draw(self.surface)
        self.misc.draw_text("Verdana", 30, "Score: " + str(self.Player.killed), (255, 255, 255), self.surface, 100, 100)

    def mousebutton_down(self, surface, event):
        pass

    def mousebutton_up(self, surface, event):
        pass

    def key_up(self, key):
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.speedx = 0
            self.Player.image = self.Player.image_stationary
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.speedx = 0
            self.Player.image = self.Player.image_stationary

    def key_down(self, key):
        if not self.Player.dead:
            if key == 97 or key == 276:
                # "A" or arrow left key
                self.Player.image = self.Player.image_flying
                self.Player.speedx = -self.Player.added_speed
            elif key == 100 or key == 275:
                # "D" or arrow right key
                self.Player.image = self.Player.image_flying
                self.Player.speedx = self.Player.added_speed
            elif key == 32:
                if not self.sprite_group.has(self.bullet):
                    self.misc.play_sound(
                        os.path.join("games", "Galaxy_Trespassers", "data", "pew.wav"))
                    self.bullet = Bullet(self.Player.rect.centerx, self.Player.rect.centery)
                    self.sprite_group.add(self.bullet)

    def stop_game(self):
        self.sprite_group.empty()
        self.misc.stop_music()
        self.Player = None
        for x in range(len(self.enemies)):
            self.enemies[x] = None
            pygame.event.pump()
        self.wall = None
        self.bullet = None
        self.explosion = None

    def stop_moving(self):
        for x in range(len(self.enemies)):
            self.enemies[x].speedy = 0
            pygame.event.pump()
        self.Player.dead = True
        self.Player.speedx = 0

    def died(self):
        self.explosion = Explosion(self.Player.rect.center)
        self.sprite_group.add(self.explosion)
        self.misc.draw_text("verdana", 63, "YOU DIED!", (255, 0, 0), self.surface, 300, 100)
        self.misc.draw_text("verdana", 63, "Your score: " + str(self.Player.killed), (255, 255, 255), self.surface, 300,
                            200)

    def invaded(self):
        self.misc.draw_text("verdana", 63, "INVADED", (255, 0, 0), self.surface, 300, 100)
        self.misc.draw_text("verdana", 63, "Your score: " + str(self.Player.killed), (255, 255, 255), self.surface, 300,
                            200)

    def collision(self):
        for x in range(len(self.enemies)):
            # Player collision with the enemy
            if self.enemies[x].rect.colliderect(self.Player.rect):
                self.stop_moving()
                self.died()

            if self.enemies[x].rect.colliderect(self.wall.rect):
                self.stop_moving()
                self.invaded()

            # Bullet collision with the enemy
            if self.bullet and self.enemies[x].rect.colliderect(self.bullet.rect):
                self.bullet.explode(self.enemies[x].rect.center)
                self.bullet.hit = True
                self.Player.killed += 100
                self.enemies[x].reset_position()
            pygame.event.pump()
