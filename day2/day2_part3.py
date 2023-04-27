import pygame
import os
import time

global surv1
global health, happiness, hunger,money
global variable


pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 20)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('images_fonts/rooms/commons.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))

player1=pygame.image.load('images_fonts/person1.png')
player2=pygame.image.load('images_fonts/person2.png')
player3=pygame.image.load('images_fonts/person3.png')



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

variable="commons"
health = 100
wealth = 100

clock_game = 0
global min, hour, count, var,thing
booleee=False
file =open("main_files/infofile.txt")

list=[]
for line in file:
    line=line.strip()
    list=line.split(",")

health=list[0]
money=list[1]
min=0
pmam="AM"
thing=False
count=1


file=open("main_files/hourtracker.txt")
for line in file:
    print(line)
    line=line.strip()
    hour=int(line)
    if hour=="5":
        pmam="PM"
        count=2
        thing=True
        count+=1
        morning=False


b=False
for line in file:
    if line!="75,100":
        b=True

if thing==True:
    hour=5
    pmam="PM"
    count=1
    

def hourplusone():
    global hour
    file=open("main_files/hourtracker.txt")
    for line in file:
        hour=int(line)
    hour+=1

    file=open("main_files/hourtracker.txt","w")
    file.write(str(hour))
    file.close()


var=0

morning=True
try:
    something=int(hour)
except:
    hour=11

def mornclockfunc():
    global health,money,thing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    global min, hour, count, var,pmam
    if hour==20:
        os.system("python day3/day3.py 1")
        pygame.quit()


    time.sleep(0.05)
    min+=1
    if min<10:
        mindisp="0"+str(min)
    else:
        mindisp=str(min)
    clock_game = f"{hour}:{mindisp} "
    

    
    if min==60:
        min=0
        hour+=1
        
        clock_game = f"{hour}:{mindisp} "
        
    text_splash=font1.render(clock_game, False, 'white')
    
    
    screen.blit(text_splash, (10,10))

    pygame.draw.rect(screen, "white", pygame.Rect(width-250, height-250, 250, 250))

    healthdisp=font1.render("health: "+str(health)+"/100",False,"black")
    screen.blit(healthdisp,(width-200,height-150))
    moneydisp=font1.render("money: $"+str(money),False,"black")
    screen.blit(moneydisp,(width-200,height-50))
    list=[]
    file=open("main_files/infofile.txt")
    for line in file:
        line=line.strip()
        list=line.split(",")

    health=list[0]
    money=list[1]

    file=open("main_files/hourtracker.txt","w")
    file.write(str(hour))
    file.close()

    

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and variable=="commons" or event.key==pygame.K_DOWN and variable=="hallway" or event.key==pygame.K_UP and variable=="rooms":
                variable="stores"
                splash_page = pygame.image.load('images_fonts/rooms/stores.png')
            elif event.key == pygame.K_RIGHT and variable=="commons" or event.key==pygame.K_DOWN and variable=="outsideup" or event.key==pygame.K_UP and variable=="outsidedown":       
                variable="captain"
                splash_page = pygame.image.load('images_fonts/rooms/captainquarters.png')
            elif event.key == pygame.K_UP and variable=="commons" or event.key==pygame.K_LEFT and variable=="outsideup" or event.key==pygame.K_RIGHT and variable=="hallway":
                variable="arcade"
                splash_page = pygame.image.load('images_fonts/rooms/arcade.png')
            elif event.key == pygame.K_DOWN and variable=="commons" or event.key ==pygame.K_LEFT and variable=="outsidedown" or event.key==pygame.K_RIGHT and variable=="rooms":
                variable="medbay"
                splash_page = pygame.image.load('images_fonts/rooms/medbay.png')
            elif event.key == pygame.K_LEFT and variable=="arcade" or event.key == pygame.K_UP and variable=="stores":
                variable="hallway"
                splash_page = pygame.image.load('images_fonts/hallway.png')
            elif event.key == pygame.K_DOWN and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="medbay":
                variable="outsidedown"
                splash_page = pygame.image.load('images_fonts/outsidedown.png')
            elif event.key == pygame.K_UP and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="arcade":
                variable="outsideup"
                splash_page = pygame.image.load('images_fonts/outsideup.png')
            elif event.key == pygame.K_DOWN and variable =="stores" or event.key ==pygame.K_LEFT and variable=="medbay":
                variable="rooms"
                splash_page = pygame.image.load('images_fonts/rooms/rooms.png')
            elif event.key==pygame.K_DOWN and variable=="arcade" or event.key==pygame.K_RIGHT and variable=="stores" or event.key==pygame.K_UP and variable=="medbay" or event.key==pygame.K_LEFT and variable=="captain":
                variable="commons"
                splash_page = pygame.image.load('images_fonts/rooms/commons.png')
            position=pygame.mouse.get_pos()
            scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            screen.blit(scaled_splash,(0,0))
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print(position)
            if variable=="arcade" and position[0]>56 and position[0]<1466 and position[1]>74 and position[1]<287:
                hourplusone()
                os.system("python specificinteractions/arcademenu.py 1")
            if variable=="stores" and position[0]>71 and position[0]<556 and position[1]>64 and position[1]<292:
                hourplusone()
                os.system("python shop/foodstore.py 1")
            if variable=="stores" and position[0]>70 and position[0]<556 and position[1]>576 and position[1]<808:
                hourplusone()
                os.system("python shop/toolstore.py 1")
            if variable=="medbay" and position[0]>76 and position[0]<536 and position[1]>593 and position[1]<806:
                hourplusone()
                os.system("python shop/healthstore.py 1")
         

    if float(health)<=0:
        os.system("python main_files/death.py 1")
        pygame.quit()
        

                
                
    if morning==True:
        mornclockfunc()
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    screen.blit(scaled_splash,(0,0))