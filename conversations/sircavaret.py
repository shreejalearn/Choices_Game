            
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


splash_page = pygame.image.load('images_fonts/sir.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You see Sir Cavaret sitting down.', False, 'white')
text_splash1 = font1.render('You incite conversation...', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: Good day!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("Sir Cavaret: More like terrible day! I've", False, "white")
                text_splash1 = font1.render("had a headache since last night...", False, "white")
            if counter==4:
                text_splash = font1.render("You: oh I'm so sorry...", False, "white")
                text_splash1 = font1.render("I hope you feel better", False, "white")
            if counter==5:
                text_splash = font1.render("Sir Cavaret: yeah, yeah, everyone says that.", False, "white")
                text_splash1 = font1.render("Y'know what would make my life better?", False, "white")
            if counter==6:
                text_splash = font1.render("You: Uh... rest?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==7:
                text_splash = font1.render("Sir Cavaret: No, good food.", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==8:
                text_splash = font1.render("You: You too! The food tastes fine to me,", False, "white")
                text_splash1 = font1.render("but I guess I'm the only one", False, "white")
            if counter==9:
                text_splash = font1.render("Sir Cavaret: Huh, naive little poor people", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==10:
                text_splash = font1.render("You: EXCUSE ME!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==11:
                text_splash = font1.render("Sir Cavaret: Please leave... I need my rest", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==12:
                text_splash = font1.render("You: *storm out*", False, "white")
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