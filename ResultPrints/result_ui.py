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
        self.up = data["up"]
        self.down = data["down"]
        self.surface = surface
        self.big_font = pygame.font.SysFont("SimHei",25)
        self.little_font = pygame.font.SysFont("SimHei",17)
        self.title_font = pygame.font.SysFont("SimHei",42)
        self.dig_font = pygame.font.Font("dig.TTF",41)
    def render(self):
        self._background_surface = pygame.image.load("images/result_background.png")

        self.surface.bilt(self._background_surface,(770,40))

        self.circle = pygame.image.load("images/circle1.png")

        self.surface.bilt(self.circle, (382+740, 311))

        self.surface.bilt(self.circle, (382+740, 525))

        self.surface.bilt(self.dig_font.render("72", True, (253, 255, 116)), (400 + 740, 327))

        self.surface.bilt(self.dig_font.render("80", True, (253, 255, 116)), (404 + 740, 542))

        self.surface.blit(self.title_font.render("体能评估报告", True, (0,199,140)),
                                (740 + 63, 74))

        self.surface.blit(self.little_font.render("个人信息", True, (0,199,140)),
                                (740 + 61, 143))



        self.surface.blit(self.little_font.render("姓名", True, (0,199,140)),
                                (63 + 740, 186))


        self.surface.bilt(self.little_font.render(self.name, True ,(94,183,153)) , (109 + 740 , 187))


        self.surface.blit(self.little_font.render("年龄", True, (0,199,140)),
                                (63 + 740, 213))

        self.surface.bilt(self.little_font.render(self.year, True, (94, 183, 153)), (109 + 740, 214))

        self.surface.blit(self.little_font.render("评估时间", True, (0,199,140)),
                                (63 + 740, 241))

        self.surface.bilt(self.little_font.render(self.time, True, (94, 183, 153)), (142 + 740, 242))

        self.surface.blit(self.big_font.render("身高围度测量", True, (0,199,140)),
                                (61 + 740, 301))

        self.surface.blit(self.little_font.render("体重", True, (0,199,140)),
                                 (253 + 740, 344))

        self.surface.bilt(self.little_font.render(self.weight, True, (94, 183, 153)), (300 + 740, 345))

        self.surface.blit(self.little_font.render("身高", True, (0,199,140)),
                                 (63 + 740, 345))

        self.surface.bilt(self.little_font.render(self.height, True, (94, 183, 153)), (110 + 740, 344))

        self.surface.blit(self.little_font.render("胸围", True, (0,199,140)),
                                 (63 + 740, 371))

        self.surface.bilt(self.little_font.render(self.bust, True, (94, 183, 153)), (110 + 740, 371))

        self.surface.blit(self.little_font.render("腰围", True, (0,199,140)),
                                 (253 + 740, 371))

        self.surface.bilt(self.little_font.render(self.waist, True, (94, 183, 153)), (300 + 740, 371))

        self.surface.blit(self.little_font.render("臀围", True, (0,199,140)),
                                 (63 + 740, 399))

        self.surface.bilt(self.little_font.render(self.hip, True, (94, 183, 153)), (109 + 740, 399))

        self.surface.blit(self.big_font.render("运动能力评估", True, (0,199,140)),
                                 (61 + 740,513))

        self.surface.blit(self.little_font.render("侧平举个数", True, (0,199,140)),
                                 (63 + 740 ,556))

        self.surface.bilt(self.little_font.render(self.up, True, (94, 183, 153)), (109 + 740, 556))


        self.surface.blit(self.little_font.render("蹲起个数", True, (0,199,140)),
                                 (253 + 740, 556))

        self.surface.bilt(self.little_font.render(self.down, True, (94, 183, 153)), (253 + 740, 556))

        self.surface.blit(self.big_font.render("肌肉问题分析", True, (0,199,140)),
                                 (61+740, 672))













