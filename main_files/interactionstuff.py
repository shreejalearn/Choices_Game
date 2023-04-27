import pygame, os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/Neucha-Regular.ttf', 90)

screen = pygame.display.set_mode()
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Ariel',35)
text = smallfont.render('S T A R T' , True , color)

room = pygame.image.load('images_fonts/rooms/room.png')

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if 70 <= pygame.mouse.get_pos()[0] <= 270 and 50 <= pygame.mouse.get_pos()[1] <= 670 :
                os.system("main_files/screen2.py 1")
                pygame.quit()
        
    position=pygame.mouse.get_pos()
    screen.blit(room, (0,0))
    room = pygame.transform.smoothscale(room, (width, height)) 
    
    pygame.display.update()
    clock.tick(60)