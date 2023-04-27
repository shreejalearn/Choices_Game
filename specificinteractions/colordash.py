import pygame
import random

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Color Dash")

infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    print(line)
    current_balance=float(line[1])

typed_color=""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

font = pygame.font.Font(None, 20)

COUNTDOWN_TIMER = 15

COLORS = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "yellow": YELLOW,
    "cyan": CYAN,
    "magenta": MAGENTA
}

current_color1 = random.choice(list(COLORS.keys()))
current_color2 = random.choice(list(COLORS.keys()))
score = 0
time_left = COUNTDOWN_TIMER * 60

def update_game():
    global current_color1,current_color2, score, time_left
    if current_color2 == typed_color.lower():
        score += 1
        current_color2 = random.choice(list(COLORS.keys()))
        current_color1 = random.choice(list(COLORS.keys()))
    else:
        score -=3
    

game_running = True
while game_running:
    time_left -= 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            

            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            else:
                if event.key == pygame.K_RETURN:
                    typed_color = typed_color.lower()
                    update_game()
                    typed_color = ""
                elif event.key == pygame.K_BACKSPACE:
                    typed_color = typed_color[:-1]
                elif event.unicode.isalpha():
                    typed_color += event.unicode

    background_color = COLORS[current_color2]
    game_display.fill(background_color)
    text = font.render(current_color1.capitalize(), True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-100))
    game_display.blit(text, text_rect)

    score_text = font.render("Score: {}".format(score), True, WHITE)
    score_text_rect = score_text.get_rect(topright=(WINDOW_WIDTH-10, 10))
    game_display.blit(score_text, score_text_rect)
    time_text = font.render("Time left: {}s".format(int(time_left/60)), True, WHITE)
    time_text_rect = time_text.get_rect(topleft=(10, 10))
    game_display.blit(time_text, time_text_rect)

    typed_text = font.render(typed_color, True, WHITE)
    typed_rect = typed_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-50))
    game_display.blit(typed_text, typed_rect)

    a = font.render("Type the color of the background.", True, WHITE)
    arect = a.get_rect(bottomleft=(10, WINDOW_HEIGHT-150))
    game_display.blit(a, arect)
    a = font.render("Press enter to submit.", True, WHITE)
    arect = a.get_rect(bottomleft=(10, WINDOW_HEIGHT-125))
    game_display.blit(a, arect)
    a = font.render("+1 point for every right answer.", True, WHITE)
    arect = a.get_rect(bottomleft=(10, WINDOW_HEIGHT-100))
    game_display.blit(a, arect)
    a = font.render("-3 points for every wrong answer.", True, WHITE)
    arect = a.get_rect(bottomleft=(10, WINDOW_HEIGHT-75))
    game_display.blit(a, arect)
    a = font.render("The points times 0.75 will be added to your balance.", True, WHITE)
    arect = a.get_rect(bottomleft=(10, WINDOW_HEIGHT-50))
    game_display.blit(a, arect)
    a = font.render("(but there will be a cap at 0$ being the lowest).", True, WHITE)
    arect = a.get_rect(bottomleft=(10, WINDOW_HEIGHT-25))
    game_display.blit(a, arect)

    pygame.display.update()

    if time_left <= 0:
        game_running = False
        if current_balance+score*0.75>0:
            infofile=open("main_files/infofile.txt","w")
            line[1]=current_balance+score*0.75
                
            for thing in line:
                t=str(thing)+","
                infofile.write(t)
            infofile.close()
        else:
            infofile=open("main_files/infofile.txt","w")
            line[1]=0
            for thing in line:
                t=str(thing)+","
                infofile.write(t)
            infofile.close()