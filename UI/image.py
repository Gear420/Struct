import pygame
import random
from pygame.locals import *
from utils.utils import choose

class image(pygame.sprite.Sprite):
    def __init__(self,image):
        super(image, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def update(self,press):
        pass