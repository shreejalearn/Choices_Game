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
            text_splash = font1.render("As you are travelling, you come accross a lifeboat telling you to steer away from the North. ", False, "white")
            text_splash1 = font1.render("However, a lighthouse on the other hand suggests that the North is a safer direction.", False, "white")
            splash_page = pygame.image.load('images_fonts/lighthouse.png')
            scaled_splash = pygame.transform.scale(splash_page, (1700, 853))
            counter+=1
            sync()
        if counter==101:
            text_splash = font1.render("What do you do? ", False, "white")
            text_splash1 = font1.render("[left arrow --> go north, right arrow --> right avoid north]", False, "white")
            
            eventvar="e3_1"
            sync()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("You come across a huge boulder right in front of your ship", False, "white")
                    text_splash1 = font1.render("You must do something, or will crash.", False, "white")
                    counter+=1
                    sync()
                if counter==2:
                    text_splash = font1.render("Which way do you want to direct your ship?", False, "white")
                    text_splash1 = font1.render("[left arrow --> left of boulder, right arrow --> right of boulder]", False, "white")
                    splash_page = pygame.image.load('images_fonts/ocean.jpg')
                    scaled_splash = pygame.transform.scale(splash_page, (1700, 853))

                    eventvar="e1"
                    sync()
                
                if counter==4:
                    text_splash = font1.render("Now, you are faced with another challenge...", False, "white")
                    text_splash1 = font1.render("Oh no! The waters are rough. Your boat feels like it's going to capsize", False, "white")
                    counter+=1
                    sync()
                if counter==5:
                    text_splash = font1.render("Do you speed up your ship, or slow it down to combat this danger?", False, "white")
                    text_splash1 = font1.render("[left arrow --> slow down, right arrow --> speed up]", False, "white")
                    eventvar="e2"
                    sync()
                if counter==7:
                    
                    sync()
                if counter==9:
                    text_splash = font1.render("DANGER! DANGER! There's a fire aboard! What should you do?", False, "white")
                    text_splash1 = font1.render("[left arrow --> break the windows and jump, right arrow --> grab a fire extinguisher]", False, "white")
                    splash_page = pygame.image.load('images_fonts/fire.jpg')
                    scaled_splash = pygame.transform.scale(splash_page, (1700, 853))
                    eventvar="e3"
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
                    file=open("main_files/infofile.txt", "w")
                    health+=happy/2
                    info=str(float(stuff[0])+float(health))+"," +str(float(stuff[1])+float(money))
                    file.write(info)
                    file.close()
                    file=open("main_files/hourtracker.txt","w")
                    file.write("14")
                    file.close()

                    os.system("python day2/day2_part3.py")
                    pygame.quit()


        if event.type == pygame.KEYDOWN:
            if eventvar=="e1":
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You navigate to the right, and see clear waters ahead of you.", False, "white")
                    text_splash1 = font1.render("You get +10 happiness.", False, "white")
                    happy+=10
                    counter=4
                    eventvar="na"
                    sync()
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You run into pirates and get attacked by them, losing all your money!", False, "white")
                    text_splash1 = font1.render("You now have 0 dollars and lose 10 happiness!", False, "white")
                    happy-=10
                    money=0
                    counter=4
                    eventvar="na"
                    sync()

            if eventvar=="e2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("A ship is strong, but the sea is stronger.", False, "white")
                    text_splash1 = font1.render("Good thinking, captain! You gain 5 happiness, and 10 dollars", False, "white")
                    money+=10
                    happy+=5
                    counter=9
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You speed up your boat, trying to push through.", False, "white")
                    text_splash1 = font1.render("Unfortunately, your ship gets damaged and you lose 10 dollars, along with 5 health", False, "white")
                    eventvar="na"
                    money-=10
                    health-=5
                    counter=9
                    sync()
            if eventvar=="e3":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You break the windows and jump into the water.", False, "white")
                    text_splash1 = font1.render("However, it was a false alarm and you caught a fever. You lose 10 health!", False, "white")
                    eventvar="na"
                    health-=10
                    counter=100
                    sync()
                if event.key==pygame.K_RIGHT:
                    eventvar="na"
                    text_splash = font1.render("You grab the extinguisher but realize it was a false alarm!", False, "white")
                    text_splash1 = font1.render("Thank goodness... and at least your heroics were appreciated!", False, "white")
                    counter=100
                    sync()
            if eventvar=="e3_1":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You go north, and run into heavy waves and cause your ship to sink.", False, "white")
                    text_splash1 = font1.render("...", False, "white")
                    os.system("python main_files/death.py 1")
                    pygame.quit()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You avoid the north. Whew! Good call", False, "white")
                    text_splash1 = font1.render("(you avoided death) and gain 5 health!", False, "white")
                    eventvar="na"
                    health+=5
                    counter=11
                    sync()
                             
            
                
            

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        

        
        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()
    