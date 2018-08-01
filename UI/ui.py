import pygame
from sys import exit
#from KinectTools import PyKinectRuntime
#from KinectTools import PyKinectV2
import ctypes


class ui(object):
    def __init__(self,n):
        self.SCREEN_WIDTH=(int)(1080 / n)
        self.SCREEN_HEIGHT=(int)(1920 / n)
        print(self.SCREEN_WIDTH)
        self.n = n
        pygame.init()
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        pygame.display.set_caption('v0.1')


    def load_set_images(self):
        #self.background = pygame.image.load()
        self.zhidao_image = pygame.image.load('images/1.jpg')
        zwidth = (int)(self.zhidao_image.get_width()*1.43/self.n)
        print(zwidth)
        zheight = (int)(self.zhidao_image.get_height()*1.43/self.n)
        print(zheight)
        self.zhidao_image = pygame.transform.scale(self.zhidao_image,(zwidth,zheight))
        self.screen.blit(self.zhidao_image,[16/375*self.SCREEN_WIDTH,189/667*self.SCREEN_HEIGHT])


        self.meiyan_image = pygame.image.load('images/2.jpg')
        mwidth = (int)(self.meiyan_image.get_width()*1.43/self.n)
        mheight = (int)(self.meiyan_image.get_height()*1.43/self.n)
        self.meiyan_image = pygame.transform.scale(self.meiyan_image,(mwidth,mheight))
        self.screen.blit(self.meiyan_image,[16/375*self.SCREEN_WIDTH,456/667*self.SCREEN_HEIGHT])

        self.jiance_image = pygame.image.load('images/3.jpg')
        width = (int)(self.jiance_image.get_width()*1.44/self.n)
        height = (int)(self.jiance_image.get_height()*1.44/self.n)
        self.jiance_image = pygame.transform.scale(self.jiance_image,(width,height))
        self.screen.blit(self.jiance_image,[192/375 * self.SCREEN_WIDTH,189/667*self.SCREEN_HEIGHT])

        self.baogao_image = pygame.image.load('images/4.jpg')
        width = (int)(self.baogao_image.get_width()*1.44/self.n)
        height = (int)(self.baogao_image.get_height()*1.44/self.n)
        self.zhidao_image = pygame.transform.scale(self.baogao_image,(width,height))
        self.screen.blit(self.zhidao_image,[16,189])

        self.logo_image = pygame.image.load('images/logo.png')

    def set_kinect(self):
        #self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
        pass
    def run(self):
        self.load_set_images()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()





