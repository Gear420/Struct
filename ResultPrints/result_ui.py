#coding=utf-8

import pygame
import random

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
        self.up = data["up"]
        self.down = data["down"]
        self.surface = surface
        self.score1 = str(90)
        self.score2 = str(78)
        self.big_font = pygame.font.SysFont("SimHei",25)
        self.little_font = pygame.font.SysFont("SimHei",17)
        self.title_font = pygame.font.SysFont("SimHei",42)
        self.dig_font = pygame.font.Font("dig.TTF",41)
        self.big_dig_font =pygame.font.Font("dig.TTF",25)
    def render(self):
        self._background_surface = pygame.image.load("images/result_background.png")
        self._background_surface = pygame.transform.smoothscale(self._background_surface,(480,765))
        self.surface.blit(self._background_surface,(770,40))

        self.circle = pygame.image.load("images/circle1.png")
        self.circle = pygame.transform.smoothscale(self.circle,(76,76))
        self.surface.blit(self.circle, (382+740, 311))

        self.surface.blit(self.circle, (382+740, 525))

        self.surface.blit(self.dig_font.render(self.score1, True, (253, 255, 116)), (400 + 740, 300))

        self.surface.blit(self.dig_font.render(self.score2, True, (253, 255, 116)), (404 + 740, 522))

        self.surface.blit(self.title_font.render("体能评估报告", True, (0,199,140)),
                                (740 + 63, 74))

        self.surface.blit(self.little_font.render("个人信息", True, (0,199,140)),
                                (740 + 61, 143))



        self.surface.blit(self.little_font.render("姓名", True, (0,199,140)),
                                (63 + 740, 186))


        self.surface.blit(self.little_font.render(self.name, True ,(94,183,153)) , (109 + 740 , 187))


        self.surface.blit(self.little_font.render("年龄", True, (0,199,140)),
                                (63 + 740, 213))

        self.surface.blit(self.little_font.render(str(self.year), True, (94, 183, 153)), (109 + 740, 214))

        self.surface.blit(self.little_font.render("评估时间", True, (0,199,140)),
                                (63 + 740, 241))

        self.surface.blit(self.little_font.render(str(self.time), True, (94, 183, 153)), (142 + 740, 242))

        self.surface.blit(self.big_font.render("身高围度测量", True, (0,199,140)),
                                (61 + 740, 301))

        self.surface.blit(self.little_font.render("体重", True, (0,199,140)),
                                 (253 + 740, 344))

        self.surface.blit(self.little_font.render(str(self.weight), True, (94, 183, 153)), (300 + 740, 345))

        self.surface.blit(self.little_font.render("身高", True, (0,199,140)),
                                 (63 + 740, 345))

        self.surface.blit(self.little_font.render(str(self.height), True, (94, 183, 153)), (110 + 740, 344))

        self.surface.blit(self.little_font.render("胸围", True, (0,199,140)),
                                 (63 + 740, 371))

        self.surface.blit(self.little_font.render(str(self.bust), True, (94, 183, 153)), (110 + 740, 371))

        self.surface.blit(self.little_font.render("腰围", True, (0,199,140)),
                                 (253 + 740, 371))

        self.surface.blit(self.little_font.render(str(self.waist), True, (94, 183, 153)), (300 + 740, 371))

        self.surface.blit(self.little_font.render("臀围", True, (0,199,140)),
                                 (63 + 740, 399))

        self.surface.blit(self.little_font.render(str(self.hip), True, (94, 183, 153)), (109 + 740, 399))

        self.surface.blit(self.big_font.render("运动能力评估", True, (0,199,140)),
                                 (61 + 740,513))

        self.surface.blit(self.little_font.render("侧平举个数", True, (0,199,140)),
                                 (63 + 740 ,556))

        self.surface.blit(self.little_font.render(str(self.up), True, (94, 183, 153)), (150 + 740, 556))


        self.surface.blit(self.little_font.render("蹲起个数", True, (0,199,140)),
                                 (253 + 740, 556))

        self.surface.blit(self.little_font.render(str(self.down), True, (94, 183, 153)), (340 + 740, 556))

        self.surface.blit(self.big_font.render("肌肉问题分析", True, (0,199,140)),
                                 (61+740, 672))


        self.surface.blit(self.big_font.render("BMI=" ,True ,(0,199,140)),(64+740,433))

        self.surface.blit(self.big_dig_font.render("27.1%", True,(0,199,140)),(120+740,430))

        self.button_red = pygame.image.load("images/rect_red.png")
        self.button_green = pygame.image.load("images/rect_green.png")

        self.button_red = pygame.transform.smoothscale(self.button_red,(163,80))
        self.button_green = pygame.transform.smoothscale(self.button_green,(163,80))

        self.surface.blit(self.button_red,(76+740,840))
        self.surface.blit(self.button_green,(76+740,8840))
        self.surface.blit(self.big_font.render("重新评估" ,True,(0,199,140)) , (740 + 106 ,867))
        self.surface.blit(self.big_font.render("下载评估表"))







