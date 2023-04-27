import pygame
import os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 30)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('images_fonts/continue.png')


splash_page = pygame.image.load('images_fonts/fam.jpg')
splash_page2 = pygame.image.load('images_fonts/sickness.jpg')
splash_page3 = pygame.image.load('images_fonts/dock.png')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))
scaled_splash2 = pygame.transform.scale(splash_page2, (1800, 1351.5))
scaled_splash3 = pygame.transform.scale(splash_page3, (1700, 1100))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You are but a lowly human in the small town of Ethopia.', False, 'white')
text_splash1 = font1.render('Fortunately, you are lucky enough to have a good job, a wonderful wife, and a son.', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You have everything a person could ever want in life", False, "white")
                text_splash1 = font1.render("However, one day, everything changes...", False, "white")
            if counter==3:
                text_splash = font1.render("A disease called the Fisherman's Pox washes through the town", False, "black")
                text_splash1 = font1.render("One day, when you come home...", False, "black")
            if counter==4:
                text_splash = font1.render("You find your wife sick", False, "black")
                text_splash1 = font1.render("Fast forward a few weeks...", False, "black")
            if counter==5:
                text_splash = font1.render("You are all alone.", False, "white")
                text_splash1 = font1.render("There is only one thing left to do...", False, "white")
            if counter==6:
                text_splash = font1.render("You embark on a ship called 'Promise'", False, "white")
                text_splash1 = font1.render("Thus, your adventure begins...", False, "white")
            if counter==7:
                os.system("python day1/day1.py 1")
                pygame.quit()

        
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    if counter == 1 or counter==2:
        screen.blit(scaled_splash,(0,0))
    if counter==3 or counter==4:
        screen.blit(scaled_splash2,(0,0))
    if counter==5 or counter==6:
        screen.blit(scaled_splash3, (0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)