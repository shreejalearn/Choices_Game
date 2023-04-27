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


splash_page = pygame.image.load('images_fonts/br.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You notice the plumber in the corner and walk over to him.', False, 'white')
text_splash1 = font1.render('He seems interesting...', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: What's the coolest room on this ship?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("Plumber: Dunno... I've been everywhere fixing things up but", False, "white")
                text_splash1 = font1.render("what I can say is the bathroom is the most important.", False, "white")
            if counter==4:
                text_splash = font1.render("You: Huh... why? What about the ", False, "white")
                text_splash1 = font1.render("nurse's room and the other rooms?", False, "white")
            if counter==5:
                text_splash = font1.render("Plumber: You can live without the nurse's room but ya can't live without a", False, "white")
                text_splash1 = font1.render("bathroom... especially with the food quality on this ship.", False, "white")
            if counter==6:
                text_splash = font1.render("You: What's wrong with the food?", False, "white")
                text_splash1 = font1.render("Tastes fine to me.", False, "white")
            if counter==7:
                text_splash = font1.render("Plumber: I've been on ships with this chef before... something", False, "white")
                text_splash1 = font1.render("just tastes different...it doesn't seem his style.", False, "white")
            if counter==8:
                text_splash = font1.render("You: What do you mean different?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==9:
                text_splash = font1.render("Plumber: You sure have a lot", False, "white")
                text_splash1 = font1.render("of questions, don't you?", False, "white")
            if counter==10:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)