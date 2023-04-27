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


splash_page = pygame.image.load('images_fonts/mechani.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You catch sight of the mechanic', False, 'white')
text_splash1 = font1.render('He seems interesting!', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: Oh, hello there!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("Mechanic: Hey there!", False, "white")
                text_splash1 = font1.render("How've things been going?", False, "white")
            if counter==4:
                text_splash = font1.render("You: not bad, I guess", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==5:
                text_splash = font1.render("Mechanic: let me guess, it's the food?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==6:
                text_splash = font1.render("You: Huh? ", False, "white")
                text_splash1 = font1.render("What do you mean?", False, "white")
            if counter==7:
                text_splash = font1.render("Mechanic: Well all the rich people were complaining", False, "white")
                text_splash1 = font1.render("about the food so I just assumed you didn't like it either...", False, "white")
            if counter==8:
                text_splash = font1.render("You: OMG, finally... another person who doesn't think", False, "white")
                text_splash1 = font1.render("the food is all that bad!", False, "white")
            if counter==9:
                text_splash = font1.render("Mechanic: I don't know what's up with everyone... I think the", False, "white")
                text_splash1 = font1.render("people complaining about the food are genuinely losing it... or maybe I am", False, "white")
            if counter==10:
                text_splash = font1.render("You: Who knows at this point?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==11:
                text_splash = font1.render("Mechanic: I've just been really tired to be honest with you...", False, "white")
                text_splash1 = font1.render("I can't wait for this ship ride to be done with...", False, "white")
            if counter==12:
                text_splash = font1.render("Mechanic: Anyways, just a tip, stay away from the nurse, she's been in a ", False, "white")
                text_splash1 = font1.render("bad mood lately, maybe she's the sick one... not that crankiness is a symptom but who knows?", False, "white")
            if counter==13:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)