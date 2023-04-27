import pygame,sys,os
pygame.init()
global current_balance
required_amount = 10
infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    print(line)
    current_balance=float(line[1])
    print(line)
try:
    current_balance=float(current_balance)
except:
    current_balance=0

screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 30)

text1 = font.render("Wanna buy a random key for $10?", True, (255, 255, 255))
text2 = font.render("Your current balance is ${}".format(current_balance), True, (255, 255, 255))

screen.blit(text1, (50, 50))
screen.blit(text2, (50, 100))

button_text = font.render("Yes", True, (255, 255, 255))
button_rect = pygame.Rect(50, 150, 100, 50)
pygame.draw.rect(screen, (0, 0, 0), button_rect)
screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

te = font.render("No", True, (255, 255, 255))
v = pygame.Rect(50, 250, 100, 50)
pygame.draw.rect(screen, (0, 0, 0), v)
screen.blit(te, (v.x + 10, v.y + 10))

if current_balance >= required_amount:
    pygame.draw.rect(screen, (0, 255, 0), button_rect)

file=open("main_files/hourtracker.txt","w")
file.write("9")
file.close()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print(position)
            if position[0]>50 and position[0]<150 and position[1]>150 and position[1]<200 and current_balance>=10:
                if current_balance >= required_amount:
                    current_balance-=10
                    line[1]=current_balance
                    infofile=open("main_files/infofile.txt","w")
                    for thing in line:
                        t=str(thing)+","
                        infofile.write(t)
                    infofile.close()
                    file=open("main_files/key.txt","w")
                    file.write("yes")
                    file.close()
                    os.system("python day3/day3_part1.py 1")
                    pygame.quit()
                else:
                    pygame.quit()
            elif position[0]>50 and position[0]<150 and position[1]>250 and position[1]<300:
                os.system("python day3/day3_part1.py 1")
                pygame.quit()

    pygame.display.update()

                    