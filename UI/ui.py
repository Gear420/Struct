import pygame
from sys import exit
#from KinectTools import PyKinectRuntime
#from KinectTools import PyKinectV2
import ctypes
#from Stamina.stamina import stamina
from faceRecognition.Login import login
from faceRecognition.Signup import signup

class ui(object):
    def __init__(self,n):
        self.SCREEN_WIDTH=(int)(1080 / n)
        self.SCREEN_HEIGHT=(int)(1920 / n)
        self.n = n



        pygame.init()
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.display_surface = pygame.Surface((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('v0.1')


    def face_reg(self):
        pass

    def load_face_images(self):
        self.login = pygame.Surface(100,100)
        self.signup = 1



    def load_set_images(self):
        #self.background = pygame.Surface((1080,1920))
        #self.background.fill((255,255,255))


        # self.zhidao_image = pygame.image.load('images/1.jpg')
        # zwidth = (int)(self.zhidao_image.get_width()*1.43/self.n)
        # zheight = (int)(self.zhidao_image.get_height()*1.43/self.n)
        # self.zhidao_image = pygame.transform.scale(self.zhidao_image,(zwidth,zheight))
        # self.screen.blit(self.zhidao_image,[16/375*self.SCREEN_WIDTH,189/667*self.SCREEN_HEIGHT])
        #
        #
        # self.meiyan_image = pygame.image.load('images/2.jpg')
        # mwidth = (int)(self.meiyan_image.get_width()*1.43/self.n)
        # mheight = (int)(self.meiyan_image.get_height()*1.43/self.n)
        # self.meiyan_image = pygame.transform.scale(self.meiyan_image,(mwidth,mheight))
        # self.screen.blit(self.meiyan_image,[16/375*self.SCREEN_WIDTH,456/667*self.SCREEN_HEIGHT])
        #
        # self.jiance_image = pygame.image.load('images/3.jpg')
        # width = (int)(self.jiance_image.get_width()*1.44/self.n)
        # height = (int)(self.jiance_image.get_height()*1.44/self.n)
        # self.jiance_image = pygame.transform.scale(self.jiance_image,(width,height))
        # self.screen.blit(self.jiance_image,[192/375 * self.SCREEN_WIDTH,189/667*self.SCREEN_HEIGHT])
        #
        # self.baogao_image = pygame.image.load('images/4.jpg')
        # width = (int)(self.baogao_image.get_width()*1.44/self.n)
        # height = (int)(self.baogao_image.get_height()*1.44/self.n)
        # self.baogao_image = pygame.transform.scale(self.baogao_image,(width,height))
        # self.screen.blit(self.baogao_image,[192/375 * self.SCREEN_WIDTH,361/667 *self.SCREEN_HEIGHT])
        #
        # self.logo_image = pygame.image.load('images/logo.png')
        # width = (int)(41 * 2 * 2 / self.n)
        # height = (int)(37 * 2 * 2 / self.n)
        # self.logo_image = pygame.transform.scale(self.logo_image,(width,height))
        # self.screen.blit(self.logo_image,[172/375* self.SCREEN_WIDTH,44/667 * self.SCREEN_HEIGHT])



        self.menu = pygame.image.load('images/menu.png').convert_alpha()
        mwidth = (int)(self.menu.get_width()*1.43/self.n)
        mheight = (int)(self.menu.get_height()*1.43/self.n)
        self.menu = pygame.transform.scale(self.menu,(mwidth,mheight))
        self.display_surface.blit(self.menu,[0,0])
    def change_mode(self,pos):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                eventarray = pygame.mouse.get_pos()
                return 2


    def run(self):
        self.load_set_images()
        self.screen.blit(self.display_surface,[0,0])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()




            if self.change_mode(pygame.mouse.get_pos()) == 2:
                print("233")
                #c = stamina(self.screen,self.n)
                #c.run()
            else:
                pass

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()





