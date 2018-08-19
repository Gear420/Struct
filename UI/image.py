import pygame
import random
from pygame.locals import *


class image(pygame.sprite.Sprite):
    def __init__(self,image):
        super(image, self).__init__()
        self.image = pygame.image.load(image)
