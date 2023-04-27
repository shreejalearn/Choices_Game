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


splash_page = pygame.image.load('images_fonts/kitchen.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You see the chef in the kitchen.', False, 'white')
text_splash1 = font1.render('You decide to speak with him.', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("Chef: Howdy fella!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("You: How's the cooking going?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==4:
                text_splash = font1.render("Chef: which one? Breakfast or the evil plan", False, "white")
                text_splash1 = font1.render("I'm cooking up in my head? *evil laugh*", False, "white")
            if counter==5:
                text_splash = font1.render("You: oh um...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==6:
                text_splash = font1.render("Chef: I'm just messing with ya!", False, "white")
                text_splash1 = font1.render("So far so good, nothing burned yet.", False, "white")
            if counter==7:
                text_splash = font1.render("You: That's good", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==8:
                text_splash = font1.render("Chef: Oh, look at that...", False, "white")
                text_splash1 = font1.render("*gets distracted and starts coughing*", False, "white")
            if counter==9:
                text_splash = font1.render("You: are you okay?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==10:
                text_splash = font1.render("Chef: yeah, yeah... must be all the smoke from cooking. Anyway, something's just been feeling off lately though.", False, "white")
                text_splash1 = font1.render("I feel like all this pressure is getting to me, my flavors don't seem as cohesive *gets genuinely sad*", False, "white")
            if counter==11:
                text_splash = font1.render("You: no, no, no, your food", False, "white")
                text_splash1 = font1.render("is still as delicious as ever!", False, "white")
            if counter==12:
                text_splash = font1.render("Chef: Thanks mate!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==13:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)