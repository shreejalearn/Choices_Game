import pygame, os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/Neucha-Regular.ttf', 100)
font2=pygame.font.Font('images_fonts/Neucha-Regular.ttf', 30)

screen = pygame.display.set_mode()
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Ariel',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('images_fonts/howtoplayback.png')
continueb = pygame.image.load('images_fonts/continue.png')
virus_image = pygame.image.load('images_fonts/virus.png')
lightning2 = pygame.image.load('images_fonts/lightning.png')


scaled_splash = pygame.transform.scale(splash_page, (width/2, height/2))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('How to Play', False, 'white')
text_splash_name = font2.render("'Sick or Swim' is a gripping and intense choose your own adventure game that will put your survival skills to the test.", False, 'white')
text_splash_name2 = font2.render("You play as a survivor in a world ravaged by a deadly disease. Are you ready to make tough decisions in order to stay alive?", False, 'white')
text_splash_name3 = font2.render("Each choice you make will have consequences that affect your chances of survival. Can you make it to safety in time?", False, 'white')
text_splash_name4 = font2.render("Try to find the person with the disease on the boat, to protect yourself and every one else!", False, 'white')
text_splash_name5 = font2.render("Get ready...every decision could mean the difference between life and death in 'Sick or Swim.'", False, 'white')


play_button = pygame.image.load('images_fonts/play_button.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if width/2-500 <= pygame.mouse.get_pos()[0] <= width/2-360 and height/2+200 <= pygame.mouse.get_pos()[1] <= height/2+400:
                os.system("python main_files/screen2.py 1")
                pygame.quit()
        
    screen.blit(text , (width/2+50,height/2))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (200,70))
    screen.blit(continueb, (width/2-500,height/2+200))
    continueb = pygame.transform.smoothscale(continueb, (140, 200)) 
    screen.blit(text_splash_name, (165,270))
    screen.blit(text_splash_name2, (120,320))
    screen.blit(text_splash_name3, (120,370))
    screen.blit(text_splash_name4, (250,420))
    screen.blit(text_splash_name5, (250,470))
    screen.blit(virus_image, (290,420))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
    screen.blit(lightning2, (900,-20))
         
    pygame.display.update()
    clock.tick(60)