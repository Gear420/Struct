
import os
import pygame

class Image(object):
    def __init__(self, image, position, screen):
        self.image = pygame.image.load(image).convert_alpha()
        self.position = position
        self.screen = screen
        #print(self.screen.get_width())
        #print(self.screen.get_height())
        self.image = pygame.transform.smoothscale(self.image,[self.screen.get_width(),self.screen.get_height()])

    def isOver(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.image.get_size()

        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        return in_x and in_y

    def render(self,position):
        w, h = self.image.get_size()
        x, y = self.position


        self.screen.blit(self.image,position)
    def rect(self):
        pass

