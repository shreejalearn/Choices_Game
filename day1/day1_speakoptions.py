import pygame
import sys, os

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Menu")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

menu_font = pygame.font.Font(None, 48)
item_font = pygame.font.Font(None, 24)

menu_items = [
    ("Captain", "conversations/captain.py"),
    ("Crewmates", "conversations/crewmates.py"),
]

file=open("main_files/hourtracker.txt","w")
file.write("11")
file.close()
selected_item = None
global y
def draw_menu():
    global y
    game_display.fill(WHITE)
    menu_text = menu_font.render("Who Do You Want To Talk To?", True, BLACK)
    menu_text_rect = menu_text.get_rect(center=(WINDOW_WIDTH/2, 50))
    game_display.blit(menu_text, menu_text_rect)

    y = 150
    for item_text, item_file in menu_items:
        item_rect = pygame.Rect(50, y, WINDOW_WIDTH-100, 50)
        pygame.draw.rect(game_display, DARK_GRAY if selected_item == item_file else GRAY, item_rect)
        item_text = item_font.render(item_text, True, BLACK)
        item_text_rect = item_text.get_rect(center=item_rect.center)
        game_display.blit(item_text, item_text_rect)
        y += 70

    pygame.display.update()

menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print(position)
            if position[0]>50 and position[0]<350:
                if position[1]>150 and position[1]<200:
                    os.system("python conversations/captain.py 1")
                    os.system("python day1/day1_part1.py 1")
                    pygame.quit() 
                elif position[1]>215 and position[1]<275:
                    os.system("python conversations/crewmates.py 1")
                    os.system("python day1/day1_part1.py 1")
                    pygame.quit()
    draw_menu()

pygame.quit()
sys.exit()