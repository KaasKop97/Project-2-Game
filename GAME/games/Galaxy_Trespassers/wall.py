import pygame


#.......................................WALL.......................................#


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'WAll.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = gamedisplay.get_width() / 2
        self.rect.bottom = game_height