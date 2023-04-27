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


splash_page = pygame.image.load('images_fonts/captain.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You talk to the captain of the ship. ', False, 'white')
text_splash1 = font1.render('Your conversation goes along the lines of this:', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: How long did it take you to ", False, "white")
                text_splash1 = font1.render("build Promise and learn to operate it?", False, "white")
            if counter==3:
                text_splash = font1.render("Captain: It was a struggle working my way up as I was born", False, "white")
                text_splash1 = font1.render("poor and suffered poverty - the ocean is an escape for me. ", False, "white")
            if counter==4:
                text_splash = font1.render("You:", False, "white")
                text_splash1 = font1.render("Wow...", False, "white")
            if counter==5:
                text_splash = font1.render("Captain: That's the thing with 'em rich people... I don't trust 'em...", False, "white")
                text_splash1 = font1.render("they never appreciate what they have and go their whole lives without fighting for survival.", False, "white")
            if counter==6:
                text_splash = font1.render("You: Who are the ", False, "white")
                text_splash1 = font1.render("rich people on the ship?", False, "white")
            if counter==7:
                text_splash = font1.render("Captain: *gets distracted", False, "white")
                text_splash1 = font1.render("The question is left unanswered.", False, "white")
            if counter==8:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)