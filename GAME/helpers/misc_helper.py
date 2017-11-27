import pygame
import os

from handlers import config_handler


class MiscHelper:
    def __init__(self):
        self.config = config_handler.ConfigHandler()
        self.font = pygame.font.init()

    @staticmethod
    def load_image(image):
        image = pygame.image.load(os.path.join(image))
        image_rect = image.get_rect()
        return image, image_rect

    def set_background(self, surface, image):
        bg_img = pygame.image.load(image)
        bg_img = pygame.transform.scale(bg_img, (
            int(self.config.get_value("game", "width")), int(self.config.get_value("game", "height"))))
        image_rect = bg_img.get_rect()

        surface.blit(bg_img, image_rect)

    def is_out_of_bounds(self, rectangle):
        if not type(rectangle) is pygame.Rect:
            raise TypeError("Error, given argument is not of type 'pygame.Rect'")

        if rectangle[0] >= int(self.config.get_value("game", "width")) or rectangle[0] <= 0 or rectangle[1] >= int(
                self.config.get_value("game", "height")) or rectangle[1] <= 0:
            return True
        else:
            return False

    def draw_text(self, font, size, text, colour, surface, x, y):
        self.font = pygame.font.SysFont(font, size)
        text = self.font.render(text, 1, (colour))
        surface.blit(text, (x, y))

    @staticmethod
    def play_music(soundfile):
        pygame.mixer.init()
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play(1)

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()
