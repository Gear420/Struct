import pygame
from sys import exit
#from KinectTools import PyKinectRuntime
#from KinectTools import PyKinectV2
import ctypes
#from Stamina.stamina import stamina
from faceRecognition.Login import login
from faceRecognition.Signup import signup
from image import Image
from button import Button
from utils.utils import scale
from utils.utils import choose,click





class ui(object):
    def __init__(self,n):
        self.SCREEN_WIDTH= 2160 /n
        self.SCREEN_HEIGHT= 3840 / n
        self.n = n
        self.start_flag = 0


        pygame.init()
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),pygame.HWSURFACE | pygame.DOUBLEBUF ,32)
        self.display_surface = pygame.Surface((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('v0.1')

        #self.start = Image("images/poster.png", (0, 0), self.screen)
        #self.stat = self.start.image
        #self.position = self.start.image.get_rect()

    #
    # def load_face_images(self):
    #     self.login =
    #     self.signup =


    #
    # def start(self,position):
    #     # start = Image("images/poster.png",(0,0),self.screen)
    #     self.start.render(position)


    def load_set_images(self):
        #self.background = pygame.Surface((1080,1920))
        #self.background.fill((255,255,255))


        self.zhidao_image = pygame.image.load('images/1.jpeg')
        self.zhidao_image = pygame.transform.smoothscale(self.zhidao_image,(int(168 * 5.76 / self.n),int(259 * 5.76 / self.n)))
        self.zh = (16*self.SCREEN_WIDTH)/375
        self.zz = (189*self.SCREEN_HEIGHT)/667


        self.display_surface.blit(self.zhidao_image,(self.zh,self.zz))






        self.meiyan_image = pygame.image.load('images/2.jpeg')
        self.meiyan_image = pygame.transform.smoothscale(self.meiyan_image, (int(168 * 5.76 / self.n), int(120 * 5.76 /self.n)))
        self.mh = (16 * self.SCREEN_WIDTH) / 375
        self.mz = (456 * self.SCREEN_HEIGHT) / 667
        self.display_surface.blit(self.meiyan_image, (self.mh, self.mz))




        self.pinggu_image = pygame.image.load('images/3.jpeg')
        self.pinggu_image = pygame.transform.smoothscale(self.pinggu_image, (int(168 * 5.76 /self.n), int(164 * 5.76 / self.n)))
        self.ph = (192 * self.SCREEN_WIDTH) / 375
        self.pz = (189 * self.SCREEN_HEIGHT) / 667
        self.display_surface.blit(self.pinggu_image, (self.ph, self.pz))

        self.baogao_image = pygame.image.load('images/4.jpeg')
        self.baogao_image = pygame.transform.smoothscale(self.baogao_image, (int(168 * 5.76 /self.n), int(215 * 5.76 / self.n)))
        self.bh = (192 * self.SCREEN_WIDTH) / 375
        self.bz = (361 * self.SCREEN_HEIGHT) / 667
        self.display_surface.blit(self.baogao_image, (self.bh, self.bz))
        # self.bh = (192 * self.SCREEN_WIDTH / 375)
        # self.bz = (361 * self.SCREEN_HEIGHT / 667)
        # self.baogao_image = Image("images/4.jpeg",None,(self.bh,self.bz))
        # #self.baogao_image.update()
        # self.display_surface.blit(self.baogao_image.image,(self.bh,self.bz))

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
        self.logo_image = pygame.image.load('images/logo2.png')
        self.logo_image = pygame.transform.smoothscale(self.logo_image,
                                                         (int(82 * 5.76 / self.n), int(74 * 5.76 / self.n)))
        self.lh = (150 * self.SCREEN_WIDTH) / 375
        self.lz = (44 * self.SCREEN_HEIGHT) / 667
        self.screen.blit(self.logo_image, (self.lh, self.lz))

        # width = (int)(41 * 2 * 2 / self.n)
        # height = (int)(37 * 2 * 2 / self.n)
        # self.logo_image = pygame.transform.scale(self.logo_image,(width,height))
        # self.screen.blit(self.logo_image,[172/375* self.SCREEN_WIDTH,44/667 * self.SCREEN_HEIGHT])



        # self.menu = pygame.image.load("images/menu.png").convert_alpha()
        # mwidth = (int)(self.menu.get_width()*1.43/self.n)
        # mheight = (int)(self.menu.get_height()*1.43/self.n)
        # self.menu = pygame.transform.scale(self.menu,(mwidth,mheight))
        # self.display_surface.blit(self.menu,[0,0])
    def change_mode(self):
        if click(self.pinggu_image,(self.ph,self.pz)):
            print("into2")
            return 2

    def run(self):

        #self.screen.blit(self.display_surface,[0,0])
        # self.start.render((0,0))
        # h = 0
        while True:

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if self.start_flag == 0:
                print("set_images...")
                self.load_set_images()
                self.screen.blit(self.display_surface,(0,0))
                if self.change_mode() == 2:
                    print("kinect work!")
                    self.start_flag = 1

            # press = pygame.mouse.get_pressed()
            # if press ==  (1,0,0):
            #     self.start_flag = 1
            # if self.start_flag == 1:
            #     self.position = self.position.move(0, -30)
            #
            # self.screen.blit(self.stat, self.position)




            if self.start_flag == 1:
                pass
                # c = stamina(self.screen,self.n)
                # c.run()

            #
            # for event in pygame.event.get():
            #     if event.type == pygame.eventMOUSEBUTTONDOWN;

                #c = stamina(self.screen,self.n)
                #c.run()
            # else:
            #     pass

            pygame.display.update()

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         exit()
            self._clock.tick(60)






