import pygame
import os


# DO NOT USE YET
class MiscHelper:
    def load_image(self, image):
        image = pygame.image.load(os.path.join(image))
        return image