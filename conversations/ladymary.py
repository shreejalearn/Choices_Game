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


splash_page = pygame.image.load('images_fonts/lady_mar.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You notice elegant yet mysterious Lady Mary lingering...', False, 'white')
text_splash1 = font1.render('You decide to talk to her.', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: How's the ship ride been for you so far?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("Lady Mary: Smooth sailing for me...", False, "white")
                text_splash1 = font1.render("my sister, not so much...", False, "white")
            if counter==4:
                text_splash = font1.render("You: You have a sister?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==5:
                text_splash = font1.render("Lady Mary: Why of course! Lady Margaret...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==6:
                text_splash = font1.render("You: Oh, what happened to her?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==7:
                text_splash = font1.render("Lady Mary: She's just been pretty sick lately, ", False, "white")
                text_splash1 = font1.render("this food is really taking a toll on her.", False, "white")
            if counter==8:
                text_splash = font1.render("You: What's wrong with the food? Tastes fine to me.", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==9:
                text_splash = font1.render("Lady Mary: The food is subpar at most. We're used to lavish dining with clams and ", False, "white")
                text_splash1 = font1.render("desert and at least 5 entrees to pick from. We had a personal chef back at home.", False, "white")
            if counter==10:
                text_splash = font1.render("You: You must've been rich...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==11:
                text_splash = font1.render("Lady Mary: Yes, well the food here hasn't been good for her... ", False, "white")
                text_splash1 = font1.render("there's something wrong with the chef here!", False, "white")
            if counter==12:
                text_splash = font1.render("You: *hmm could the chef or Lady Margaret", False, "white")
                text_splash1 = font1.render("be the sick person?", False, "white")
            if counter==13:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)