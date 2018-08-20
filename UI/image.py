import pygame
import random
from pygame.locals import *
from utils.utils import choose,click

class Image(pygame.sprite.Sprite):
    def __init__(self,image,choose_image,pos):
        super(Image, self).__init__()
        self.choose_image = choose_image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.pos = pos

    def update(self):
        if choose(self.image,self.pos):
            self.rect.move_ip(0,-100)



