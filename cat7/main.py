import pygame


pygame.init()

screen_width = 1550
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 50)

x,y = 1300,610
x1,y1 = 5, 0
x2,y2 = 450, 0
speed1 = 2
h = 15
speed2 = 3
flagL = False
flagF = False

apple = pygame.image.load('img/яблоко-PhotoRoom.png-PhotoRoom.png.')
apple = pygame.transform.scale(apple, (100, 100))


forest = pygame.image.load('img/лесок.jpg')
forest = pygame.transform.scale(forest, (1550, 800))

banana = pygame.image.load('img/банан-PhotoRoom.png-PhotoRoom.png')
banana = pygame.transform.scale(banana, (150, 150))

danana = pygame.image.load('img/00000001-PhotoRoom.png-PhotoRoom.png')
danana = pygame.transform.scale(danana, (100, 100))

knife = pygame.image.load('img/нож.png')
knife = pygame.transform.scale(knife, (100, 100))

x_bullet, y_bullet = 0, 0
x1_bullet, y1_bullet = 1000, 1000


pew = pygame.mixer.Sound("img/pew_pew-dknight556-1379997159.mp3")

bonk = pygame.mixer.Sound("img/bonk_7zPAD7C.mp3")

kljhuhgkuhgkvhgvygv = pygame.mixer.Sound("img/марё-23360 (mp3cut.net) (1).mp3")


pygame.mixer.music.load("img/veselaya-i-rasslablennaya-fonovaya-muzyika-42250.mp3")
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and y<630-h:             #кнопка вниз
        y += speed1
    if keys[pygame.K_UP] and y>0:             #кнопка вверх
        y -= speed1
    if keys[pygame.K_LEFT] and x>0:             #кнопка влево
        x -= speed1
    if keys[pygame.K_RIGHT] and x<1300-h:             #кнопка вправо
        x += speed1

    if keys[pygame.K_s] and y1<630-h:             #кнопка вниз
        y1 += speed2
    if keys[pygame.K_w] and y1>0:             #кнопка вверх
        y1 -= speed2
    if keys[pygame.K_a] and x1>0:             #кнопка влево
        x1 -= speed2
    if keys[pygame.K_d] and x1<1300-h:             #кнопка вправо
        x1 += speed2

    screen.blit(forest, (0, 0))
    screen.blit(banana, (x, y))
    text = font.render("banana cat ", True, (255,255,0))
    screen.blit(text, (670, 150))
    text2 = font2.render("VS", True, (255,255,255))
    screen.blit(text2, (670,250 ))
    textadsf = font.render("apple cat", True, (230,0,0))
    screen.blit(textadsf, (670, 350))
    screen.blit(apple, (x1, y1))

    if keys[pygame.K_l ]:
        flagL = True
        pew.play()

    if x1_bullet < 10:
        flagL = False

    if flagL == True:
        x1_bullet -= 1
        screen.blit(danana, (x1_bullet, y1_bullet))
    else:
        x1_bullet, y1_bullet = x, y

    # --------------------------------------------нож
    if keys[pygame.K_f ]:
        flagF = True

        bonk.play()

    else:
        flagF = False

    if flagF == True:
        # x_bullet += 1
        screen.blit(knife, (x_bullet, y_bullet))
        x_bullet = x1
        y_bullet = y1
    else:
        x_bullet = x1
        y_bullet = y1
    # --------------------------------------------

    pygame.display.update()