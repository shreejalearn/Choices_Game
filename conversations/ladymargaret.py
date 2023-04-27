import pygame
import os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 26)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('images_fonts/continue.png')


splash_page = pygame.image.load('images_fonts/lady_marg.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You catch sight of Lady Margaret.', False, 'white')
text_splash1 = font1.render('How interesting...', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: Hello there! I head you're not feeling too well...", False, "white")
                text_splash1 = font1.render("How are you holdilng up so far?", False, "white")
            if counter==3:
                text_splash = font1.render("Lady Margaret: Decent.", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==4:
                text_splash = font1.render("You: Is it the food?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==5:
                text_splash = font1.render("Lady Margaret: Not sure.", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==6:
                text_splash = font1.render("You: oh uh", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==7:
                text_splash = font1.render("Lady Margaret: Look I know what you are trying to do... find the sick one. I know myself and I've lost", False, "white")
                text_splash1 = font1.render("people close to me because of the sickness... I know this is just food poisoning and motion sickness.", False, "white")
            if counter==8:
                text_splash = font1.render("You: Yeah, I wasn't doubting that just...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==9:
                text_splash = font1.render("Lady Margaret: Look, I know. I don't blame you for", False, "white")
                text_splash1 = font1.render("thinking I'm the one with the disease.", False, "white")
            if counter==10:
                text_splash = font1.render("You: I don't think that you are...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==11:
                text_splash = font1.render("Lady Margaret: Save it. Have you had a chance to talk ", False, "white")
                text_splash1 = font1.render("with the nurse yet?", False, "white")
            if counter==12:
                text_splash = font1.render("You: no...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==13:
                text_splash = font1.render("Lady Margaret: Talk to her, she might give you a better idea of who's the ", False, "white")
                text_splash1 = font1.render("sick one, she has all of our health logs.", False, "white")
            if counter==14:
                text_splash = font1.render("You: Yeah, I will.", False, "white")
                text_splash1 = font1.render("Feel better!", False, "white")
            if counter==15:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)