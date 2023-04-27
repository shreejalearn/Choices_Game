####FIX URGENT


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

global scaled_splash, text_splash, text_splash1, counter
splash_page = pygame.image.load('images_fonts/standinimage.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


global money, happy
health=0
happy=0
hunger=0
money=0

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You are casually hanging out on the ship when you hear the alarm blare', False, 'white')
text_splash1 = font1.render('You dash to the captain room and look outside from behind the wheel', False, 'white')
counter=1

global eventvar

eventvar="na"

def sync():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
def masterloop():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy, health
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if counter==100:
            text_splash = font1.render("While exploring, you hear rumors about the captain's secret diary being here.", False, "white")
            text_splash1 = font1.render("Where do you look? [left arrow --> under the table, right arrow --> behind the sofa]", False, "white")
            splash_page = pygame.image.load('images_fonts/captain.jpg')
            scaled_splash = pygame.transform.scale(splash_page, (600, 450))

            counter+=1
            sync()
        if counter==101:
            eventvar="e3_1"
            sync()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("You hear of a case of food poisoning going around the ship.", False, "white")
                    text_splash1 = font1.render("This could be incredibly detrimental to one's health.", False, "white")
                    splash_page = pygame.image.load('images_fonts/food.jpg')
                    scaled_splash = pygame.transform.scale(splash_page, (600, 450))

                    counter+=1
                    sync()
                if counter==2:
                    text_splash = font1.render("Do you go for a drink to take your mind off these worries, or do you eat crackers?", False, "white")
                    text_splash1 = font1.render("[left arrow --> alcohol, right arrow --> crackers]", False, "white")
                    eventvar="e1"
                    sync()
                
                if counter==4:
                    text_splash = font1.render("Now, you are faced with another challenge...", False, "white")
                    text_splash1 = font1.render("Lightning strikes and part of the boat was destroyed!", False, "white")
                    splash_page = pygame.image.load('images_fonts/lightning-storm.jpg')
                    scaled_splash = pygame.transform.scale(splash_page, (600, 450))
                    counter+=1
                    sync()
                if counter==5:
                    text_splash = font1.render("What do you do, take a detour to the nearest port city, or try to fix it yourself?", False, "white")
                    text_splash1 = font1.render("[left arrow --> detour, right arrow --> fix it yourself]", False, "white")
                    eventvar="e2"
                    sync()
                if counter==7:
                    
                    sync()
                if counter==9:
                    text_splash = font1.render("Anyways, you are approached by a fortune teller who agrees to give you a reading for 10$", False, "white")
                    text_splash1 = font1.render("[left arrow --> take the risk, right arrow --> NO WAY!]", False, "white")
                    splash_page = pygame.image.load('images_fonts/town.png')
                    scaled_splash = pygame.transform.scale(splash_page, (1920, 1080))
                    eventvar="e3"
                    sync()
                if counter==11:
                    text_splash = font1.render("You decide to go back to what you were doing before", False, "white")
                    text_splash1 = font1.render("Events over for today.", False, "white")
                    counter+=2
                    sync()
                if counter==13:
                    fi=open("main_files/infofile.txt")
                    stuff=""
                    for line in fi:
                        stuff+=line
                    stuff=stuff.split(",")
                    file=open("main_files/infofile.txt", "w")
                    health+=happy/2
                    info=str(float(stuff[0])+float(health))+"," +str(float(stuff[1])+float(money)) 
                    file.write(info)
                    file.close()
                    file=open("main_files/hourtracker.txt","w")
                    file.write("17")
                    file.close()
                    os.system("python day3/day3_part1.py")
                    pygame.quit()


        if event.type == pygame.KEYDOWN:
            if eventvar=="e1":
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You decide to keep it simple and eat some crackers.", False, "white")
                    text_splash1 = font1.render("You get +7 health.", False, "white")
                    health+=7
                    counter=4
                    eventvar="na"
                    sync()
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You drink alcohol to take your mind off your worries...", False, "white")
                    text_splash1 = font1.render("Uh oh... you might have to run to the restroom! You lose 7 health", False, "white")
                    health-=7
                    counter=4
                    eventvar="na"
                    sync()

            if eventvar=="e2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You go to the port city and buy yourself some supplies, and now it's good as new!", False, "white")
                    text_splash1 = font1.render("Although you lose 10 coins, you gain 10 health!", False, "white")
                    money-=10
                    health+=10
                    counter=9
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You decide to fix the boat yourself, not bad! You definitely saved money", False, "white")
                    text_splash1 = font1.render("You gain 10 coins, but also are anxious about breaking down the ship. You lose 10 happiness!", False, "white")
                    eventvar="na"
                    money+=10
                    happy-=10
                    counter=100
                    sync()
            if eventvar=="e3":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("Of course! You find out that somebody on the ship is sick with the virus (although you already knew that)", False, "white")
                    text_splash1 = font1.render("Despite that, she gives you a mask and ppe, you gain 5 health but lose 10 money.", False, "white")
                    eventvar="na"
                    health+=5
                    money-=10
                    counter=100
                    sync()
                if event.key==pygame.K_RIGHT:
                    
                    text_splash = font1.render("there's no way you're wasting money...", False, "white")
                    text_splash1 = font1.render("it's not worth it.", False, "white")
                    
                    eventvar="na"
                    counter=100
                    sync()
            if eventvar=="e3_1":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You search under the table! Darn it, it's not here.", False, "white")
                    text_splash1 = font1.render("however, you DID find 5 coins lying on the ground!", False, "white")
                    eventvar="na"
                    money+=5
                    counter=11
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You search by the sofa, here it is!", False, "white")
                    text_splash1 = font1.render("You find out the captain isn't the one with the illness. What a relief!", False, "white")
                    eventvar="na"
                    health+=5
                    counter=11
                    sync()
                             
            
                
            

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        

        
        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()
    