import pygame
import os
import time

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 100)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial', 45)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('images_fonts/continue.png')


splash_page = pygame.image.load('images_fonts/ship_sink.jpeg')
splash_water = pygame.image.load('images_fonts/water_drop.png')
lightning = pygame.image.load('images_fonts/lightning.png')
lightning2 = pygame.image.load('images_fonts/lightning2.png')

scaled_splash = pygame.transform.scale(splash_page, (1500, 1500))
scaled_water = pygame.transform.scale(splash_water, (800, 495))
splash_water1 = pygame.transform.flip(scaled_water, True, False)


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('Sick Or Swim', False, 'white')
text_splash_name = font.render('By: Shreeja And Anna', False, 'white')

pygame.mixer.music.load('guitar.mp3')
pygame.mixer.music.play(-1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if width/2-500 <= pygame.mouse.get_pos()[0] <= width/2-360 and height/2+200 <= pygame.mouse.get_pos()[1] <= height/2+400:
                os.system("python main_files/howtoplay.py")
                pygame.quit()

       
    screen.blit(text, (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    blit_alpha(screen, scaled_water,(0,0),150)
    blit_alpha(screen, splash_water1,(0,450),150)
    screen.blit(text_splash, (320,80))
    screen.blit(text_splash_name, (330,570))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))
    scaled_water = pygame.transform.smoothscale(scaled_water, (width, height))
    screen.blit(continueb, (330, 650))
    continueb = pygame.transform.smoothscale(continueb, (200, 200))
    screen.blit(lightning, (900,-20))
    screen.blit(lightning2, (20,0))

         
    pygame.display.update()
    clock.tick(60)