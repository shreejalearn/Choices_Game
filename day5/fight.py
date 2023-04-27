
import pygame,random,os
pygame.init()
attackstuff=["Dagger(5damage)-5","Bow(3damage)-3", "Sword(10damage)-10"]
armorstuff=["Helmet(+2protection)-2","Chestplate(+7protection)-7","Boots(+1protection)-1"]
foodstuff=["Apple(+2hunger)-2", "Bread(+5hunger)-5", "Steak(+10hunger)-10"]
healthstuff=["smallhealthpotion(+5health)-5", "mediumhealthpotion(+10health)-10", "largehealthpotion(+20health)-20"]
infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    health=float(line[0])
    money=float(line[1])
items=[]
inventory=open("main_files/inventory.txt")
extrastrength=0
moreproct=0
varrr=False
print(inventory)
for line in inventory:
    print(line)
    line=line.split(",")
    print(line)
    varrr=True
if varrr==False:
    line=[]

for thing in line:

    thingg=thing
    print(thing)
    if thing in attackstuff:
        thing=thing.split("-")
        extrastrength+=float(thing[1])
    elif thing in armorstuff:
        thing=thing.split("-")
        moreproct+=float(thing[1])
    else:
        items.append(thingg)
    if thing=="":
        print("nada")

opponenthealth=88
opponentdext=78
dext=35+(((health+money)/2)/4)
opponentstrength=75
opponentstrength-=moreproct
opponentdext-=moreproct/3
strength=50+extrastrength
health_bar_width = 200
health_bar_height = 30
screen_width = 1000
screen_height = 750
health_bar_x = 10
health_bar_y = screen_height -50
opp_health_bar_x=health_bar_y
opp_health_bar_y=screen_height-50
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Final Battle")
image1 = pygame.image.load("day5/image1.png")
image2 = pygame.image.load("day5/image2.png")
image1 = pygame.transform.scale(image1, (200, 200))
image2 = pygame.transform.scale(image2, (200, 200))

image_width = image1.get_width()
image_height = image1.get_height()
font = pygame.font.Font(None, 36)
textt = font.render("Attack", True, (255, 255, 255))
text_width = textt.get_width()
text_height = textt.get_height()
image1_x = 10
image1_y = (screen_height - image_height) // 2
image2_x = screen_width - image_width - 400
image2_y = (screen_height - image_height) // 2
button_x = (screen_width - text_width) // 2
button_y = (screen_height - text_height) // 2
def attack():
    global dext,opponentdext,health,opponenthealth,strength,opponentstrength
    diff=(dext-opponentdext)/2
    probability=50+diff
    r=random.randint(0,100)
    if r<=probability:
        damage=random.randint(0,strength)
        opponenthealth-=damage
        return (f"You hit your opponent causing {damage} damage.")
    else:
        return (f"You miss your opponent.")
    
def oppattack():
    global dext,opponentdext,health,opponenthealth,strength,opponentstrength
    diff=(opponentdext-dext)/2
    probability=50+diff
    r=random.randint(0,100)
    if r<=probability:
        damage=random.randint(0,opponentstrength)
        health-=damage
        return (f"Your opponent hits you causing {damage} damage.")
    else:
        return (f"Your opponent misses you.")
def draw_opponent_health_bar():
    global opponenthealth
    health_percentage = opponenthealth / 100
    health_bar_current_width = health_bar_width * health_percentage
    
    pygame.draw.rect(screen, (0,0,0), (opp_health_bar_x, opp_health_bar_y, health_bar_width, health_bar_height))
    
    if opponenthealth > 0:
        pygame.draw.rect(screen, (225,0,0), (opp_health_bar_x, opp_health_bar_y, health_bar_current_width, health_bar_height))
    
    pygame.draw.rect(screen, (0,0,0), (opp_health_bar_x, opp_health_bar_y, health_bar_width, health_bar_height), 2)
def draw_health_bar():
    global health
    health_percentage = health / 100
    health_bar_current_width = health_bar_width * health_percentage
    
    
    
    if opponenthealth > 0:
        pygame.draw.rect(screen, (0,225,0), (health_bar_x, health_bar_y, health_bar_current_width, health_bar_height))
    
    pygame.draw.rect(screen, (0,0,0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 2)
    
event1text=font.render("", True,(0,0,0))
event2text=font.render("", True,(0,0,0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            if position[0]>button_x and position[0]<(button_x+text_width+20) and position[1]>button_y and position[1]<(button_y+text_height+20):
                x=attack()
                y=oppattack()
                event1text=font.render(x, True,(0,0,0))
                event2text=font.render(y, True,(0,0,0))
            for i in range(len(items)-1):
                print(i)
                item = items[i]
                text = font.render(item, True, (0,0,0))
                rect = text.get_rect()
                rect.x = 10
                rect.y = 10 + i * 30
                if rect.collidepoint(position):
                    print(item)
                    g=items.index(item)
                    x=items[g]
                    items.remove(items[g])
                    x=x.split("-")
                    health+=int(x[1])



    screen.fill((255, 255, 255))

    screen.blit(image1, (image1_x+200, image1_y))
    screen.blit(image2, (image2_x+200, image2_y))
    draw_health_bar()
    draw_opponent_health_bar()
    
    health_text = font.render("Health: " + str(health), True, (255,255,255))
    screen.blit(health_text, (10, screen_height-50))
    opp_health_text = font.render("Health: " + str(opponenthealth), True, (255,255,255))
    screen.blit(opp_health_text, (screen_width-300, screen_height-50))
    dext_text = font.render("Dexterity: " + str(dext), True, (0,0,0))
    screen.blit(dext_text, (10, screen_height-75))
    opp_dext_text = font.render("Dexterity: " + str(opponentdext), True, (0,0,0))
    screen.blit(opp_dext_text, (screen_width-300, screen_height-75))
    strength_text = font.render("Strength: " + str(strength), True, (0,0,0))
    screen.blit(strength_text, (10, screen_height-100))
    opp_strength_text = font.render("Strength: " + str(opponentstrength), True, (0,0,0))
    screen.blit(opp_strength_text, (screen_width-300, screen_height-100))
    
    screen.blit(event1text,((screen_width-700),10))
    
    screen.blit(event2text,((screen_width-700),40))
    pygame.draw.rect(screen, (0, 0, 255), (button_x , button_y , text_width + 20, text_height + 20))
    screen.blit(textt, (button_x, button_y))
    for i in range(len(items)):
        item = items[i]
        text = font.render(item, True, (0,0,0))
        rect = text.get_rect()
        rect.x = 10
        rect.y = 10 + i * 30
        screen.blit(text, rect)
    if health<=0:
        os.system("python main_files/death.py")
        pygame.quit()
    if opponenthealth<=0:
        #work on this
        os.system("python main_files/win.py")
        pygame.quit()
    pygame.display.update()
pygame.quit()