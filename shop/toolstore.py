import pygame

pygame.init()

width = 400
height = 300
screen = pygame.display.set_mode((400,300))
money=0

file=open("main_files/hourtracker.txt")
for line in file:
    line=line.strip()
    hour=int(line)
hour+=1

file=open("main_files/hourtracker.txt","w")
file.write(str(hour))
file.close()

infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    money=float(line[1])

pygame.display.set_caption("Sink or Swim Shop")

font = pygame.font.SysFont('Arial',15)
items = [("Dagger(5damage)", 10,5), ("Bow(3damage)", 5,3), ("Sword(10damage)", 15,10), ("Helmet(+2protection)",5,2),("Chestplate(+7protection)",15,7),("Boots(+1protection)",3,1)]

inventory = []

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            x = position[0]
            y = position[1]

            for i in range(len(items)):
                item = items[i]
                text = font.render(f"{item[0]} - {item[1]} dollars", True, (0,0,0))
                rect = text.get_rect()
                rect.x = 10
                rect.y = 10 + i * 30
                if rect.collidepoint(position):
                    if money >= item[1]:
                        inventory.append(item[0]+"-"+str(item[2]))
                        money -= item[1]
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                stuff=line
                stuff[1]=money
                infofile=open("main_files/infofile.txt","w")
                for thing in stuff:
                    t=str(thing)+","
                    infofile.write(t)
                infofile.close()
                invent=open("main_files/inventory.txt")
                stuff=[]
                for line in invent:
                    line=line.strip()
                    line=line.split()
                    for thing in line:
                        stuff.append(thing)
                for thing in inventory:
                    stuff.append(thing)
                i=open("main_files/inventory.txt","w")
                for thing in stuff:
                    a=thing+","
                    i.write(a)
                i.close()

                pygame.quit()

    screen.fill((255,255,255))

    inventory_text = font.render(f"Inventory: {' '.join(inventory)}", True, (0,0,0))
    screen.blit(inventory_text, (10, height - 60))

    money_text = font.render(f"Money: {money}", True, (0,0,0))
    screen.blit(money_text, (10, height - 90))

    instru = font.render("Press e to exit", True, (0,0,0))
    screen.blit(instru, (10, height - 30))

    for i in range(len(items)):
        item = items[i]
        text = font.render(f"{item[0]} - {item[1]} dollars", True, (0,0,0))
        rect = text.get_rect()
        rect.x = 10
        rect.y = 10 + i * 30
        screen.blit(text, rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()