import pygame
import os, time

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


global money, happy, health
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

splash_page = pygame.image.load('images_fonts/captain.jpg')
scaled_splash = pygame.transform.scale(splash_page, (width*1.01, height*1.01))
screen.blit(scaled_splash,(0,0))
text_splash = font1.render('You are casually hanging out on the ship when you hear the alarm blare', False, 'white')
text_splash1 = font1.render('You dash to the captain room and look outside from behind the wheel', False, 'white')
screen.blit(text_splash, (60,70))
screen.blit(text_splash1, (60,140))

counter=1

global eventvar

eventvar="na"

def masterloop():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy, health
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if counter==100:
            eventvar="e3_1"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("There, you see dangerous waters.", False, "white")
                    text_splash1 = font1.render("On the left, there is a thunderstorm, and on the right, there is a whirlpool", False, "white")
                    screen.blit(text_splash, (60,70))
                    screen.blit(text_splash1, (60,140))
                    counter+=1

                if counter==2:
                    text_splash = font1.render("Which way do you want to direct your ship?", False, "white")
                    text_splash1 = font1.render("[left arrow --> thunderstorm, right arrow --> whirlpool]", False, "white")
                    eventvar="e1"
                    sync()
                
                if counter==4:
                    text_splash = font1.render("Now, you are faced with another challenge...", False, "white")
                    text_splash1 = font1.render("Towards your left, you see sharks, and towards your right, you see pirhanas.", False, "white")
                    counter+=1
                    sync()
                if counter==5:
                    text_splash = font1.render("Which way do you want to direct your ship?", False, "white")
                    text_splash1 = font1.render("[left arrow --> sharks, right arrow --> piranhas]", False, "white")
                    eventvar="e2"
                    sync()
                if counter==7:
                    
                    sync()
                if counter==9:
                    text_splash = font1.render("You see a town! Do you want to go past it, or explore?", False, "white")
                    text_splash1 = font1.render("[left arrow --> go past, right arrow --> explore]", False, "white")
                    eventvar="e3"
                    splash_page = pygame.image.load('images_fonts/town.png')
                    scaled_splash = pygame.transform.scale(splash_page, (1920, 1080))
                    sync()
                if counter==11:
                    text_splash = font1.render("Anyways, you leave the town.", False, "white")
                    text_splash1 = font1.render("The water looks boring...", False, "white")
                    counter+=1
                    sync()
                if counter==12:
                    text_splash = font1.render("You decide to go back to what you were doing before", False, "white")
                    text_splash1 = font1.render("Events over for today.", False, "white")
                    counter+=1
                    sync()
                if counter==13:
                    
                    fi=open("main_files/infofile.txt")
                    stuff=""
                    for line in fi:
                        stuff+=line
                    stuff=stuff.split(",")
                    health+=happy/2
                    file=open("main_files/infofile.txt", "w")
                    print(str(float(stuff[0])+float(health))+"," +str(float(stuff[1])+float(money)))
                    info=str(float(stuff[0])+float(health))+"," +str(float(stuff[1])+float(money))
                    file.write(info)
                    file.close()
                    file=open("main_files/hourtracker.txt","w")
                    file.write("17")
                    file.close()
                    os.system("python day1/day1_part1.py")
                    pygame.quit()


        if event.type == pygame.KEYDOWN:
            if eventvar=="e1":
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You navigate your ship towards the whirlpool...", False, "white")
                    text_splash1 = font1.render("And are able to circumnavigate the dangers.", False, "white")
                    counter=4
                    eventvar="na"
                    sync()
                if event.key==pygame.K_LEFT:
                    os.system("python main_files/death.py 1")
                    pygame.quit()

            if eventvar=="e2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You navigate your ship towards the sharks... \nAnd are surprised to see they did not attack you.", False, "white")
                    text_splash1 = font1.render("In addition, you discover a new species of shark! \nYou get 10 coins for your achievement", False, "white")
                    money+=10
                    counter=9
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You steer your ships towards the fishies, surprised when they eat some of your boat!", False, "white")
                    text_splash1 = font1.render("You have to spend 10 coins to fix it. ", False, "white")
                    eventvar="na"
                    money-=10
                    counter=9
                    sync()
            if eventvar=="e3":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You pass the town.", False, "white")
                    text_splash1 = font1.render("Maybe you missed something important...", False, "white")
                    eventvar="na"
                    counter=11
                    sync()
                if event.key==pygame.K_RIGHT:
                    eventvar="na"
                    text_splash = font1.render("You look around and see some resources! \nYou eat some food and get +10 on your hunger bar!", False, "white")
                    text_splash1 = font1.render("You see a cat and a dog. Do you (right) leave them or (left) take them?", False, "white")
                    counter=100
                    sync()
            if eventvar=="e3_1":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You take the cat and dog with you! Hopefully they aren't sick", False, "white")
                    text_splash1 = font1.render("You gain 10 happiness!", False, "white")
                    counter=11
                    happy+=10
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("Who knows, the cat and dog might be sick. You leave them", False, "white")
                    text_splash1 = font1.render("You lose 10 happiness!", False, "white")
                    eventvar="na"
                    happy-=10
                    counter=11
                    sync()
                             
            
                
            

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        

        
        

        pygame.display.update()
        clock.tick(60)

def sync():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 

def sync_spec():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
    time.sleep(3)


while True:
    masterloop()
    