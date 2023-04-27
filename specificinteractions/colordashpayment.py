import pygame,sys,os
pygame.init()

required_amount = 10
infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    print(line)
    current_balance=float(line[1])

screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 30)

text1 = font.render("Please pay $10 to proceed to color dash", True, (255, 255, 255))
text2 = font.render("Your current balance is ${}".format(current_balance), True, (255, 255, 255))

screen.blit(text1, (50, 50))
screen.blit(text2, (50, 100))

button_text = font.render("Next", True, (255, 255, 255))
button_rect = pygame.Rect(50, 150, 100, 50)
pygame.draw.rect(screen, (0, 0, 0), button_rect)
screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

if current_balance >= required_amount:
    pygame.draw.rect(screen, (0, 255, 0), button_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print(position)
            if position[0]>50 and position[0]<150 and position[1]>150 and position[1]<200:
                if current_balance >= required_amount:
                    current_balance-=10
                    line[1]=current_balance
                    infofile=open("main_files/infofile.txt","w")
                    for thing in line:
                        t=str(thing)+","
                        infofile.write(t)
                    infofile.close()
                    os.system("python specificinteractions/colordash.py 1")
                    pygame.quit()
                else:
                    pygame.quit()
    pygame.display.update()

                    