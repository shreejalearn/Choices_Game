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


splash_page = pygame.image.load('images_fonts/rooms/captainquarters.png')
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
                splash_page = pygame.image.load('images_fonts/rooms/captainquarters.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))


def clickedbookshelf():
    global screenn,scaled_splash,bookshelfchecked
    bookshelfchecked=True
    screenn="bookshelf"
    print(screenn)
    splash_page = pygame.image.load('day2/bookshelf.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))


def clickedbed():
    global screenn,scaled_splash,bookshelfchecked,key1,listenunlock1
    screenn="bed"
    print(screenn)
    if bookshelfchecked==False:
        splash_page = pygame.image.load('day2/bedsheets.png')
        scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    else:
        splash_page = pygame.image.load('day2/bedunder.png')
        scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
        key1=True
        listenunlock1=True


    


def clickedwheel():
    global screenn,scaled_splash
    screenn="wheel"
    print(screenn)
    splash_page = pygame.image.load('day2/wheelpuzzle.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))


def clickedrug():
    global screenn,scaled_splash
    screenn="rug"
    print(screenn)
    splash_page = pygame.image.load('day2/trapdoorlock.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))

def clickeddrawer():
    global screenn,scaled_splash
    screenn="drawer"
    print(screenn)
    splash_page = pygame.image.load('day2/lockeddrawer.png')
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))

def smthwheelpuzzle():
    global wheelpuzzlestr, scaled_splash, splash_page,key2,listenunlock2
    position=pygame.mouse.get_pos()
    if position[0]>641 and position[0]<768:
        if position[1]>203 and position[1]<297:
            wheelpuzzlestr+="n"
    if position[0]>998 and position[0]<1105:
        if position[1]>489 and position[1]<590:
            wheelpuzzlestr+="e"
    if position[0]>678 and position[0]<798:
        if position[1]>778 and position[1]<851:
            wheelpuzzlestr+="s"
    if position[0]>308 and position[0]<425:
        if position[1]>492 and position[1]<582:
            wheelpuzzlestr+="w"
    if position[0]>561 and position[0]<883:
        if position[1]>463 and position[1]<614:
            wheelpuzzlestr=""
    if position[0]>1099 and position[0]<1448:
        if position[1]>138 and position[1]<274:
            if wheelpuzzlestr=="wsne":
                print("got here")
                splash_page = pygame.image.load('day2/wheelsolve.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))
                key2=True
                listenunlock2=True
            else:
                wheelpuzzlestr=""

while True:

    back = Button(0, 0, 200, 50, (225,225,225))
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="captain":

            position=pygame.mouse.get_pos()
            if position[0]>71 and position[0]<607:
                if position[1]> 68 and position[1]<255:
                    clickedbookshelf()
            if position[0]>82 and position[0]<538:
                if position[1]>600 and position[1]<802:
                    clickedbed()
            if position[0]>1195 and position[0]<1382:
                if position[1]>312 and position[1]<573:
                    clickedwheel()
            if position[0]>548 and position[0]<1032:
                if position[1]>285 and position[1]<557:
                    clickedrug()
            if position[0]>1041 and position[0]<1261:
                if position[1]>98 and position[1]<255:
                    clickeddrawer()
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="drawer":
            if listenunlock111==True:
                splash_page = pygame.image.load('day2/openeddrawer.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))

            elif listenunlock11==True:
                splash_page = pygame.image.load('day2/unlockeddrawer.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))
                listenunlock111=True

            elif listenunlock1==True:
                splash_page = pygame.image.load('day2/lockeddrawer.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                listenunlock11=True
                screen.blit(scaled_splash,(0,0))
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="wheel":
            smthwheelpuzzle()
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="rug":
            if listenesc==True:
                os.system("python day2/day2_part2.py")
                pygame.quit()

            elif listenunlock222==True:
                splash_page = pygame.image.load('day2/trapdooropen.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))
                listenesc=True


            elif listenunlock22==True:
                splash_page = pygame.image.load('day2/trapdoorunlock.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))
                listenunlock222=True

            elif listenunlock2==True:
                splash_page = pygame.image.load('day2/trapdoorlock.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                listenunlock22=True
                screen.blit(scaled_splash,(0,0))


        
            
        
        
        
    screen.blit(scaled_splash,(0,0))
    back.handle_event(event)
    back.draw(screen)
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))