import pygame
import os
import time
import random

global surv1
global health, happiness, hunger,money
global variable

global width, height

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')
global lived,splash_page,scaled_splash

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 20)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('main_files/keychoice.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))




def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

lived=False

def die():
    os.system("python main_files/death.py 1")
    pygame.quit()

def live():
    global width, height,lived,splash_page,scaled_splash

    splash_page = pygame.image.load('main_files/keyyay.png')
    scaled_splash = pygame.transform.scale(splash_page, (800, 800))
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    screen.blit(scaled_splash,(0,0))
    lived=True
    

def had():
    r=random.randint(1,10)
    if r<=3:
        die()
    else:
        live()

while True:
    if lived==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                print(position)
                if position[0]>=825 and position[0]<=1383:
                    if position[1]>=269 and position[1]<=359:
                        had()

                if position[0]>=825 and position[0]<=1383:
                    if position[1]>=390 and position[1]<=483:
                        pygame.quit()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.quit()


            

    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    screen.blit(scaled_splash,(0,0))