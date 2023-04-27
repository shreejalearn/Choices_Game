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
splash_page2 = pygame.image.load('images_fonts/lightning-storm.jpg')
splash_page3 = pygame.image.load('images_fonts/dock.png')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))
scaled_splash2 = pygame.transform.scale(splash_page2, (1700, 1000))
scaled_splash3 = pygame.transform.scale(splash_page3, (1700, 1100))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You wake up and know the whole truth.', False, 'white')
text_splash1 = font1.render('The person who had the disease all along is the chef.', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You contemplate the turn of events.", False, "white")
                text_splash1 = font1.render("You have been manipulated, decieved.", False, "white")
            if counter==3:
                text_splash = font1.render("There is only one thing left do to.", False, "black")
                text_splash1 = font1.render("You decide to fight...", False, "black")
            if counter==4:
                text_splash = font1.render("But where?", False, "black")
                text_splash1 = font1.render("The creepy hallway, that might be fitting...", False, "black")
            if counter==5:
                text_splash = font1.render("You only have the resources that are on you right now.", False, "white")
                text_splash1 = font1.render("You can't waste any time, each passing second is precious.", False, "white")
            if counter==6:
                text_splash = font1.render("With a new resolve, you decide to leave your room.", False, "white")
                text_splash1 = font1.render("Best of luck!", False, "white")
            if counter==7:
                os.system("python day5/fight.py 1")
                pygame.quit()

        
    screen.blit(text , (0,0))
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