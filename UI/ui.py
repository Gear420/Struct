import pygame
from sys import exit
from KinectTools import PyKinectRuntime
from KinectTools import PyKinectV2
import ctypes


class ui(object):
    def __init__(self):
        self.SCREEN_WIDTH=(int)(1080 / 3)
        self.SCREEN_HEIGHT=(int)(1920 / 3)
        self.pygame.init()
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        pygame.display.set_caption('v0.1')

    def load_images(self):
        background = pygame.image.load()
        zhidao_image = pygame.image.load('images/1.jpg')
        meiyan_image = pygame.image.load('images/2.jpg')
        jiance_image = pygame.image.load('images/3.jpg')
        baogao_image = pygame.image.load('images/4.jpg')
        logo_image = pygame.image.load('images/logo.jpg')
    def set_imgaes(self):
        pass

    def setkinect(self):
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)

    def run(self):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()





