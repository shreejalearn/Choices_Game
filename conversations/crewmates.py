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


splash_page = pygame.image.load('images_fonts/kitchen_sink.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You approach the crewmates of the ship.', False, 'white')
text_splash1 = font1.render('You incite conversation with them, noting their jovial smiles.', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("Crewmate 1: Roses are red", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("Crewmate 2: Flowers are pink", False, "white")
                text_splash1 = font1.render(" ", False, "white")
            if counter==4:
                text_splash = font1.render("Crewmate 3: You wash your hands in the...", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==5:
                text_splash = font1.render("You: ...kitchen sink", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==6:
                text_splash = font1.render("Crewmates: Ay, he knows how to take a good joke... ", False, "white")
                text_splash1 = font1.render("I like him already!", False, "white")
            if counter==7:
                text_splash = font1.render("You: *let out a dry chuckle... you can't help but feel despite it being a silly joke,", False, "white")
                text_splash1 = font1.render("a deeper meaning...kitchen sink...hmm...who has worked with the kitchen sink?", False, "white")
            if counter==8:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)