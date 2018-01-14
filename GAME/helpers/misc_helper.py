import pygame
import os

from handlers import config_handler


class MiscHelper:
    def __init__(self):
        self.config = config_handler.ConfigHandler()
        self.game_width = int(self.config.get_value("game", "width"))
        self.game_height = int(self.config.get_value("game", "height"))
        self.font = pygame.font.init()

    @staticmethod
    def load_image(image):
        image = pygame.image.load(os.path.join(image))
        image_rect = image.get_rect()
        return image, image_rect

    def set_background(self, surface, image):
        bg_img = pygame.image.load(image)
        bg_img = pygame.transform.scale(bg_img, (self.game_width, self.game_height))
        image_rect = bg_img.get_rect()

        surface.blit(bg_img, image_rect)

    def is_out_of_bounds(self, rectangle):
        if not type(rectangle) is pygame.Rect:
            raise TypeError("Error, given argument is not of type 'pygame.Rect'")

        if rectangle[0] >= self.game_width - rectangle.width or rectangle[0] <= 0 or rectangle[1] >= self.game_height or \
                rectangle[1] <= 0:
            return True
        else:
            return False

    def draw_text(self, font, size, text, colour, surface, x, y, sysfont=True):
        if sysfont:
            self.font = pygame.font.SysFont(font, size)
        else:
            self.font = pygame.font.Font(font, size)
        text = self.font.render(text, 1, (colour))
        surface.blit(text, (x, y))

    def game_over(self, score, surface, additional_text="", additional_text_font="", additional_text_size=0,
                  additional_text_colour=(0, 0, 0)):
        self.set_background(surface, os.path.join("menu", "game_over.jpg"))
        self.draw_text("verdana", 20, "Your score: " + str(score), (255, 255, 255), surface, self.game_width // 2 - 150,
                       self.game_height - 100)
        if not additional_text == "" and not additional_text_font == "" and not additional_text_size == "":
            self.draw_text(str(additional_text_font), int(additional_text_size), str(additional_text),
                           additional_text_colour, surface, self.game_width // 2 - 150, self.game_height - 50)

    @staticmethod
    def play_music(soundfile, loop):
        pygame.mixer.init()
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play(loop)

    @staticmethod
    def stop_music():
        pygame.mixer.music.fadeout(500)

    @staticmethod
    def play_sound(soundfile):
        sound = pygame.mixer.Sound(soundfile)
        sound.play()
