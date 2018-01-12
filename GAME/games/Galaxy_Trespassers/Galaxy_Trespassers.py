import  pygame, sys, time, random, os, math
from handlers import config_handler
from games.Galaxy_Trespassers import player, enemy

from games.Galaxy_Trespassers.bullet import Player
from games.Galaxy_Trespassers.enemies import enemy00
from games.Galaxy_Trespassers.enemies import enemy01
from games.Galaxy_Trespassers.enemies import enemy02
from games.Galaxy_Trespassers.enemies import enemy03
from games.Galaxy_Trespassers.bullet import Bullet
from games.Galaxy_Trespassers.explosion import Explosion
from games.Galaxy_Trespassers.wall import Wall

from helpers import misc_helper, log_helper
from handlers import config_handler
class GalaxyTrespassers:
    def __init__(self, surface):
        self.game_name = "Galaxy_Trespassers"
        self.author = "Chérie Cederboom"
        self.gamedisplay = surface
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))
        self.Player = player.Player(self.game_width / 2, self.game_height - 20, 70, 56,
                                    os.path.join("games", "Galaxy_Trespassers", "data", "aircraft (flying) zone trespassers.png"))
        self.enemy1 = enemy.Enemy00(random.randrange(0, self.game_width), -500, 75, 63,
                                   os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying 3.png"), 50)
        self.enemy2 = enemy.Enemy01(random.randrange(0, self.game_width), -300, 75, 63,
                                   os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying 5.png"), 150)
        self.enemy3 = enemy.Enemy02(random.randrange(0, self.game_width), -700, 75, 63,
                                   os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying.png"), 200)
        self.enemy4 = enemy.Enemy03(random.randrange(0, self.game_width), -100, 75, 63,
                                   os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying 2.png"), 500)
        self.bullet = bullet.Bullet()
        self.wall = wall.Wall()
        self.explosion = explosion.Explosion()
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.Player, self.enemy1, self.enemy2, self.enemy3,
                              self.enemy4, self.wall, self.bullet, self.explosion)

    def load(self, surface):
        self.misc.set_background(surface, os.path.abspath("games/Galaxy_Trespassers/data/bg1.png"))
        self.misc.play_music(os.path.abspath("games/Galaxy_Trespassers/data/Galaxy trespassers.wav"))
        return True

    def update(self):
        # This method gets called every frame so be careful with this one.
        self.sprite_group.update()
        self.sprite_group.draw(self.gamedisplay)

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

    def invaded(self):
        gamedisplay.blit(background, background_rect)
        draw_text(gamedisplay, 'INVADED', 63, game_width / 2, game_height / 4.4)
        draw_text(gamedisplay, 'your score:', 22, game_width / 2, game_height / 2.3)
        draw_text(gamedisplay, str(player_score) + 'pts', 42, game_width / 2, game_height / 1.9)
        pygame.display.flip()
        time.sleep(4)

    def key_up(self, key):
        # If you need to do an action on key inputs use this access key codes, check DRON.py for examples
        # For example: key A = keycode 97 so to check this do 'if key == 97'
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.speedx = 0
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.speedx = 0

    def key_down(self, key):
        if key == 97 or key == 276:
            # "A" or arrow left key
            self.Player.speedx =+ self.Player.added_speed
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.Player.speedx =+ self.Player.added_speed

    def stop_game(self):
        pass
