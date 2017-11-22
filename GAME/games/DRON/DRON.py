import pygame
from games.DRON.MotorBike import MotorBike


class Dron:
    def __init__(self):
        self.game_name = "DRON"
        self.game_author = "Mitchel van Hamburg"
        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)
        self.area = pygame.display.get_surface()
        self.bike1 = MotorBike()

        self.sprites = pygame.sprite.RenderPlain(self.bike1)

    def update(self, surface):
        if self.bike1.dead:
            self.player_dead()
        self.bike1.move()
        self.bike1.draw(surface)

    def load(self):
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
            self.bike1.direction = "left"
        elif key == 119 or key == 273:
            # "W" or arrow up key
            self.bike1.direction = "up"
        elif key == 100 or key == 275:
            # "D" or arrow right key
            self.bike1.direction = "right"
        elif key == 115 or key == 274:
            # "S" or arrow down key
            self.bike1.direction = "down"
        elif key == 27:
            self.stop_game()
            print("Should kill the game")

    def player_dead(self):
        print("Display a message saying that the user is dead and is able to try again or something")

    def stop_game(self):
        self.bike1 = None
        self.font = None
        self.sprites = None
        print("Stopping game")
