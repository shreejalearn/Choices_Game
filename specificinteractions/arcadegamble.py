import pygame
import random

# initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode()
pygame.display.set_caption("Sink or Swim")

# set up fonts
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
# set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set up game variables
bet = 0

infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    money=float(line[1])

balance=money

img = pygame.image.load('images_fonts/rooms/arcade.jpg')

# define functions
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x,y))

def draw_screen():
    screen.fill(WHITE)
    draw_text("Balance: $" + str(balance), font, BLACK, 500, 200)
    draw_text("Bet: $" + str(bet), font, BLACK, 500, 300)

def roll_dice():
    dice = []
    for i in range(3):
        dice.append(random.randint(1, 6))
    return dice

def check_win(dice):
    if len(set(dice)) == 1:
        return "win_big"
    elif len(set(dice)) == 2:
        return "win_small"
    else:
        return "lose"

# set up game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                bet = int(str(bet) + event.unicode)
            elif event.key == pygame.K_RETURN:
                if bet > balance:
                    bet = balance
                if bet > 0:
                    balance -= bet
                    dice = roll_dice()
                    result = check_win(dice)
                    if result == "win_big":
                        balance += bet * 10
                    elif result == "win_small":
                        balance += bet * 3
                    draw_screen()
                    draw_text(str(dice[0]), font, BLACK, 800 // 2 - 50, 600 // 2)
                    draw_text(str(dice[1]), font, BLACK, 800 // 2, 600 // 2)
                    draw_text(str(dice[2]), font, BLACK, 800 // 2 + 50, 600 // 2)
                    draw_text(result, font, BLACK, 800 // 2, 600 // 2 + 50)
                bet = 0
            elif event.key == pygame.K_BACKSPACE:
                bet = int(bet / 10)
            elif event.key==pygame.K_e:
                stuff=line
                print(stuff)
                stuff[1]=balance
                infofile=open("main_files/infofile.txt","w")
                for thing in stuff:
                    t=str(thing)+","
                    infofile.write(t)
                infofile.close()
                pygame.quit()
        if balance==0:
            stuff=line
            print(stuff)
            stuff[1]=balance
            infofile=open("main_files/infofile.txt","w")
            for thing in stuff:
                t=str(thing)+","
                infofile.write(t)
            infofile.close()
            pygame.quit()



    # draw the screen
    draw_screen()
    draw_text("Enter your bet:", font, BLACK, 500, 500)
    draw_text("$" + str(bet), font, BLACK, 500, 600)
    draw_text("Press 'e' to exit", font, BLACK, 500,700)
    # screen.blit(img, (0,0))

    # update the display
    pygame.display.update()

# quit pygame
pygame.quit()