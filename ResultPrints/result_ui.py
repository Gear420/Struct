import pygame


class result(object):
    def __init__(self,data,surface):
        self.name = data["name"]
        self.year = data["year"]
        self.time = data["time"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.bust = data["bust"]
        self.waist = data["waist"]
        self.hip = data["hip"]
        self.surface = surface
        self.up = data["up"]
        self.down = data["down"]
    def render(self):
        _background_surface = pygame.image.load("images/background_")






