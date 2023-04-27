import pygame
import os
import time

global surv1
global health, happiness, hunger,money



pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 20)
global scaled_splash

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('day4/kitchenn.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)


scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
health = 100
wealth = 100

clock_game = 0
global bookshelfchecked,key1,listenunlock1,listenunlock11,listenunlock111,key2,listenunlock2,listenunlock22,listenunlock222,listenesc
bookshelfchecked=False
key1=False
key2=False
booleee=False

listenesc=False

global screenn
screenn="captain"
var=0
listenunlock1=False
listenunlock11=False
listenunlock111=False

listenunlock2=False
listenunlock22=False
listenunlock222=False

global wheelpuzzlestr

wheelpuzzlestr=""

class Button:
    
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = font.render('Back', True, (0,0,0))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text, (self.rect.centerx - self.text.get_width() // 2, self.rect.centery - self.text.get_height() // 2))

    def handle_event(self, event):
        global screenn,scaled_splash
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = (225,0,0)
                screenn="captain"
                print(screenn)
                splash_page = pygame.image.load('day4/kitchenn.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))
global counter,puzzlestr,pineapplecut,keyy,microcount,clockkey,clockcount
clockcount=0
microcount=0
keyy=False
clockkey=False
pineapplecut=False
puzzlestr=""

def clickedOven():
    global screenn,scaled_splash,counter
    screenn="oven"
    print(screenn)
    splash_page = pygame.image.load('day4/cake1.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    counter=0

def clickedPuzzle(number):
    global puzzlestr,pineapplecut
    if number!="reset":
        puzzlestr+=(str(number))
    else:
        puzzlestr=""
    if puzzlestr=="7291":
        pineapplecut=True


def clickedFridge():
    global screenn,scaled_splash,pineapplecut,keyy
    screenn="fridge"
    print(screenn)
    if pineapplecut==False:
        splash_page = pygame.image.load('day4/fridgeclose.png')
        scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    else:
        splash_page = pygame.image.load('day4/fridgeopen.png')
        scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
        keyy=True
    

def clickedMicrowave():
    global screenn,scaled_splash
    screenn="microwave"
    print(screenn)
    splash_page = pygame.image.load('day4/microlock.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))

def clickedClock():
    global screenn,scaled_splash
    screenn="clock"
    print(screenn)
    splash_page = pygame.image.load('day4/clocklock.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))


while True:

    back = Button(0, 0, 200, 50, (225,225,225))
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="captain":

            if position[0]>465 and position[0]<563:
                if position[1]> 69 and position[1]<170:
                    clickedClock()
            if position[0]>37 and position[0]<419:
                if position[1]>50 and position[1]<570:
                    if not(position[0]>359 and position[0]<390) or not (position[1]>170 and position[1]<197):
                        clickedFridge()
            if position[0]>1220 and position[0]<1446:
                if position[1]>297 and position[1]<415:
                    clickedMicrowave()
            if position[0]>855 and position[0]<1189:
                if position[1]>385 and position[1]<550:
                    clickedOven()
            if position[0]>1027 and position[0]<1054:
                if position[1]>266 and position[1]<290:
                    clickedPuzzle(7)
            if position[0]>1450 and position[0]<1468:
                if position[1]>373 and position[1]<408:
                    clickedPuzzle(1)
            if position[0]>773 and position[0]<814:
                if position[1]>534 and position[1]<566:
                    clickedPuzzle(2)
            if position[0]>359 and position[0]<390:
                if position[1]>170 and position[1]<197:
                    clickedPuzzle(9)
            if position[0]>1222 and position[0]<1362:
                if position[1]>772 and position[1]<802:
                    clickedPuzzle("reset")
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="oven":
            counter+=1
            if counter==1:
                splash_page = pygame.image.load('day4/cake1.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            if counter==2:
                splash_page = pygame.image.load('day4/cake2.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            if counter==3:
                splash_page = pygame.image.load('day4/cake3.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            if counter==4:
                splash_page = pygame.image.load('day4/cake4.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            if counter==5:
                splash_page = pygame.image.load('day4/cake5.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            if counter==6:
                splash_page = pygame.image.load('day4/cakeeaten.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="microwave":
            if keyy==True:
                microcount+=1
                if microcount==1:
                    splash_page = pygame.image.load('day4/microlock.png')
                    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                if microcount==2:
                    splash_page = pygame.image.load('day4/microunlock.png')
                    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                if microcount==3:
                    splash_page = pygame.image.load('day4/microopen.png')
                    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                    clockkey=True
        
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="clock":
            if clockkey==True:
                clockcount+=1
                if clockcount==1:
                    splash_page = pygame.image.load('day4/clocklock.png')
                    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                if clockcount==2:
                    splash_page = pygame.image.load('day4/clockunlock.png')
                    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                if clockcount==3:
                    splash_page = pygame.image.load('day4/clockopen.png')
                    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                    clockcount-=1
                    position=pygame.mouse.get_pos()
                    if position[0]>623 and position[0]<930:
                        if position[1]>542 and position[1]<630:
                            os.system("python day4/day4_part2.py 1")
                            pygame.quit()
                    if position[0]>624 and position[0]<932:
                        if position[1]>643 and position[1]<735:
                            os.system("python day4/day4_randomhint.py 1")
                            pygame.quit()
                
                    


            
        
        
        
    screen.blit(scaled_splash,(0,0))
    back.handle_event(event)
    back.draw(screen)
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))