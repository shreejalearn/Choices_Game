import pygame
import os
import time

global surv1
global health, happiness, hunger,money



pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 20)
global scaled_splash

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('day4/randomhint.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)


scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
health = 100
wealth = 100

clock_game = 0
global bookshelfchecked,key1,listenunlock1,listenunlock11,listenunlock111,key2,listenunlock2,listenunlock22,listenunlock222,listenesc
bookshelfchecked=False
key1=False
key2=False
booleee=False

listenesc=False

global screenn
screenn="captain"
var=0
listenunlock1=False
listenunlock11=False
listenunlock111=False

listenunlock2=False
listenunlock22=False
listenunlock222=False


while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
                
                position=pygame.mouse.get_pos()
                print(position)
                if position[0]>130 and position[0]<347:
                    if position[1]>714 and position[1]<749:
                        os.system("python day4/day4_part2.py")
                        pygame.quit()
            
        
        
    screen.blit(scaled_splash,(0,0))
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))