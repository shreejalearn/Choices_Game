            
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


splash_page = pygame.image.load('images_fonts/nurse.jpg')
scaled_splash = pygame.transform.scale(splash_page, (571, 301))

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('Time to talk to the nurse!', False, 'white')
text_splash1 = font1.render('You wearily approach her...', False, 'white')
counter=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter+=1
            if counter==2:
                text_splash = font1.render("You: hi there!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==3:
                text_splash = font1.render("Nurse: Why hello, how are you feeling?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==4:
                text_splash = font1.render("You: Oh, good. Good!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==5:
                text_splash = font1.render("Nurse: Huh, that's a first! Most people only come to ", False, "white")
                text_splash1 = font1.render("me when they're feeling sick. How may I help you?", False, "white")
            if counter==6:
                text_splash = font1.render("You: Well... to be honest I was trying to figure out who the", False, "white")
                text_splash1 = font1.render("person with the disease is, so...", False, "white")
            if counter==7:
                text_splash = font1.render("You: Oh, but you don't have our health logs?", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==8:
                text_splash = font1.render("Nurse: *scoffs*", False, "white")
                text_splash1 = font1.render("As if anyone writes the truth in it!", False, "white")
            if counter==9:
                text_splash = font1.render("You: Well, you're the expert, what", False, "white")
                text_splash1 = font1.render("are the symptoms of the disease?", False, "white")
            if counter==10:
                text_splash = font1.render("Nurse: Well, I would say mainly coughing and inability to focus", False, "white")
                text_splash1 = font1.render("are the most obvious ones. Are you sure you're feeling well?", False, "white")
            if counter==11:
                text_splash = font1.render("You: Yeah! Of course!", False, "white")
                text_splash1 = font1.render("What about throwing up?", False, "white")
            if counter==12:
                text_splash = font1.render("Nurse: Eh, hard to tell... it could just be plain", False, "white")
                text_splash1 = font1.render("food poisoning or potion sickness.", False, "white")
            if counter==13:
                text_splash = font1.render("You: Yeah, you're right.", False, "white")
                text_splash1 = font1.render("Thank you!", False, "white")  
            if counter==14:
                text_splash = font1.render("Nurse: Any time!", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==15:
                text_splash = font1.render("You: *you wonder who showed those symptoms...*", False, "white")
                text_splash1 = font1.render("", False, "white")
            if counter==16:
                pygame.quit()

        
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))

    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)