import pygame
from sys import exit

# pygame.init()
# screen = pygame.display.set_mode((300, 200), 0, 32)
# upImageFilename = 'game_again.png'
# downImageFilename = 'game_again_down.png'


class Button(object):
    def __init__(self, upimage, downimage, position,screen):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position
        self.screen = screen

    def isOver(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()

        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            self.screen.blit(self.imageDown, (x - w / 2, y - h / 2))
        else:
            self.screen.blit(self.imageUp, (x - w / 2, y - h / 2))




