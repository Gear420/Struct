import pygame,sys
import time
import random



pygame.init()
screencaption=pygame.display.set_caption('hello world')
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(10):
    zhijing=random.randint(0,100)
    width=random.randint(0,255)
    height=random.randint(0,100)
    top=random.randint(0,400)
    left=random.randint(0,500)
    pygame.draw.circle(screen,[0,0,0],[top,left],zhijing,1)
    pygame.draw.rect(screen,[255,0,0],[left,top,width,height],3)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()