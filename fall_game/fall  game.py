import pygame
from random import randint

pygame.init()
win = pygame.display.set_mode((1036,512))

pygame.display.set_caption("fall game")
walkRigh = [pygame.image.load('right-1.png'),
pygame.image.load('right-2.png'), pygame.image.load('right-3.png')]
walkLeft = [pygame.image.load('left-1.png'),
pygame.image.load('left-2.png'), pygame.image.load('left-3.png')]
playerStand = pygame.image.load('idle.png')
bg = pygame.image.load('bg.jpg')
crate = pygame.image.load('crate.png')
GameOver = pygame.image.load('game-over.png')
money = pygame.image.load('money.png')

BackSound = 'back-sound.mp3'
crack = 'crack.mp3'
GameOverSound = 'game-over-sound.mp3'
MoneySound = 'money-sound.mp3'

pygame.mixer.init()
pygame.mixer.music.load(BackSound)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

white = [255, 255, 255]

x = 50
y = 400

aga = 0
noll = 0
CrateNumber = 0
MoneyNumber = 0

y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
y7 = 0
y8 = 0
y9 = 0
y10 = 0
y11 = 0
y12 = 0
y13 = 0
y14 = 0
y15 = 0
y16 = 0

x1 = 0
x2 = 64
x3 = 128
x4 = 192
x5 = 256
x6 = 320
x7 = 384
x8 = 448
x9 = 512
x10 = 576
x11 = 640
x12 = 704
x13 = 768
x14 = 832
x15 = 896
x16 = 960

width = 64
height = 64
speed = 10
isJump = False
jumpCount = 10

run = True
left = False
right = False
animCount = 0

crate1 = False
crate2 = False
crate3 = False
crate4 = False
crate5 = False
crate6 = False
crate7 = False
crate8 = False
crate9 = False
crate10 = False
crate11 = False
crate12 = False
crate13 = False
crate14 = False
crate15 = False
crate16 = False

def fail():
    global run
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load(crack)
    pygame.mixer.music.play(1)
    pygame.time.wait(500)
    pygame.mixer.init()
    pygame.mixer.music.load(GameOverSound)
    pygame.mixer.music.play(1)
    win.fill(white)
    win.blit(GameOver, (310, 60))
    f1 = pygame.font.SysFont(None, 40)
    text = f1.render("You score - ", 1, (180, 0, 0))
    win.blit(text, (400, 380))
    f2 = pygame.font.SysFont(None, 40)
    text2 = f2.render(str(time), 1, (180, 0, 0))
    win.blit(text2, (570, 380))
    pygame.display.update()
    print("game over!")
    pygame.time.wait(3500)
    run = False

def drawWindow():
    global animCount


    if animCount + 1 >= 10:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRigh[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x,y))
    pygame.display.update()



while run:
    clock.tick(30)
    win.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1024 - width:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):

        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 3
            else:
                y -= (jumpCount ** 2) / 3
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if noll == 10:
        CrateNumber = randint(1, 16)
        noll = 0
    noll += 1
    if CrateNumber == 1:
        crate1 = True
    if CrateNumber == 2:
        crate2 = True
    if CrateNumber == 3:
        crate3 = True
    if CrateNumber == 4:
        crate4 = True
    if CrateNumber == 5:
        crate5 = True
    if CrateNumber == 6:
        crate6 = True
    if CrateNumber == 7:
        crate7 = True
    if CrateNumber == 8:
        crate8 = True
    if CrateNumber == 9:
        crate9 = True
    if CrateNumber == 10:
        crate10 = True
    if CrateNumber == 11:
        crate11 = True
    if CrateNumber == 12:
        crate12 = True
    if CrateNumber == 13:
        crate13 = True
    if CrateNumber == 14:
        crate14 = True
    if CrateNumber == 15:
        crate15 = True
    if CrateNumber == 16:
        crate16 = True

    if crate1 == True:
        win.blit(crate, (x1,y1))
        y1 += 15
    if crate2 == True:
        win.blit(crate, (x2,y2))
        y2 += 15
    if crate3 == True:
        win.blit(crate, (x3,y3))
        y3 += 15
    if crate4 == True:
        win.blit(crate, (x4,y4))
        y4 += 15
    if crate5 == True:
        win.blit(crate, (x5,y5))
        y5 += 10
    if crate6 == True:
        win.blit(crate, (x6,y6))
        y6 += 15
    if crate7 == True:
        win.blit(crate, (x7,y7))
        y7 += 15
    if crate8 == True:
        win.blit(crate, (x8,y8))
        y8 += 15
    if crate9 == True:
        win.blit(crate, (x9,y9))
        y9 += 15
    if crate10 == True:
        win.blit(crate, (x10,y10))
        y10 += 15
    if crate11 == True:
        win.blit(crate, (x11,y11))
        y11 += 15
    if crate12 == True:
        win.blit(crate, (x12,y12))
        y12 += 15
    if crate13 == True:
        win.blit(crate, (x13,y13))
        y13 += 15
    if crate14 == True:
        win.blit(crate, (x14,y14))
        y14 += 15
    if crate15 == True:
        win.blit(crate, (x15,y15))
        y15 += 15
    if crate16 == True:
        win.blit(crate, (x16,y16))
        y16 += 15

    if y1 >= 512:
        crate1 = False
        у1 = 0
    if y2 >= 512:
        crate2 = False
        y2 = 0
    if y3 >= 512:
        crate3 = False
        y3 = 0
    if y4 >= 512:
        crate4 = False
        y4 = 0
    if y5 >= 512:
        crate5 = False
        y5 = 0
    if y6 >= 512:
        crate6 = False
        y6 = 0
    if y7 >= 512:
        crate7 = False
        y7 = 0
    if y8 >= 512:
        crate8 = False
        y8 = 0
    if y9 >= 512:
        crate9 = False
        y9 = 0
    if y10 >= 512:
        crate10 = False
        y10 = 0
    if y11 >= 512:
        crate11 = False
        y11 = 0
    if y12 >= 512:
        crate12 = False
        y12 = 0
    if y13 >= 512:
        crate13 = False
        y13 = 0
    if y14 >= 512:
        crate14 = False
        y14 = 0
    if y15 >= 512:
        crate15 = False
        y15 = 0
    if y16 >= 512:
        crate16 = False
        y16 = 0

    if y == 400 and x > 430 and x < 541:
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(GameOverSound)
        pygame.mixer.music.play(1)
        win.fill(white)
        win.blit(GameOver, (310, 60))
        f1 = pygame.font.SysFont(None, 40)
        text = f1.render("You score - ", 1, (180, 0, 0))
        win.blit(text, (400, 380))
        f2 = pygame.font.SysFont(None, 40)
        text2 = f2.render(str(time), 1, (180, 0, 0))
        win.blit(text2, (570, 380))
        pygame.display.update()
        print ("game over!")
        pygame.time.wait(3500)
        run = False

    if x >= x1 and x <= (x1 + 50):
        if y >= y1 and y <= (y1 + 50):
            fail()
    if (x + 50) >= x1 and (x + 50) <= (x1 + 50):
        if (y + 50) >= y1 and (y + 50) <= (y1 + 50):
            fail()
    if (x + 50) >= x1 and (x + 50) <= (x1 + 50):
        if y >= y1 and y <= (y1 + 50):
            fail()
    if x >= x1 and x <= (x1 + 50):
        if (y + 50) >= y1 and (y + 50) <= (y1 + 50):
            fail()

    if x >= x2 and x <= (x2 + 50):
        if y >= y2 and y <= (y2 + 50):
            fail()
    if (x + 50) >= x2 and (x + 50) <= (x2 + 50):
        if (y + 50) >= y2 and (y + 50) <= (y2 + 50):
            fail()
    if (x + 50) >= x2 and (x + 50) <= (x2 + 50):
        if y >= y2 and y <= (y2 + 50):
            fail()
    if x >= x2 and x <= (x2 + 50):
        if (y + 50) >= y2 and (y + 50) <= (y2 + 50):
            fail()

    if x >= x3 and x <= (x3 + 50):
        if y >= y3 and y <= (y3 + 50):
            fail()
    if (x + 50) >= x3 and (x + 50) <= (x3 + 50):
        if (y + 50) >= y3 and (y + 50) <= (y3 + 50):
            fail()
    if (x + 50) >= x3 and (x + 50) <= (x3 + 50):
        if y >= y3 and y <= (y3 + 50):
            fail()
    if x >= x3 and x <= (x3 + 50):
        if (y + 50) >= y3 and (y + 50) <= (y3 + 50):
            fail()

    if x >= x4 and x <= (x4 + 50):
        if y >= y4 and y <= (y4 + 50):
            fail()
    if (x + 50) >= x4 and (x + 50) <= (x4 + 50):
        if (y + 50) >= y4 and (y + 50) <= (y4 + 50):
            fail()
    if (x + 50) >= x4 and (x + 50) <= (x4 + 50):
        if y >= y4 and y <= (y4 + 50):
            fail()
    if x >= x4 and x <= (x4 + 50):
        if (y + 50) >= y4 and (y + 50) <= (y4 + 50):
            fail()

    if x >= x5 and x <= (x5 + 50):
        if y >= y5 and y <= (y5 + 50):
            fail()
    if (x + 50) >= x5 and (x + 50) <= (x5 + 50):
        if (y + 50) >= y5 and (y + 50) <= (y5 + 50):
            fail()
    if (x + 50) >= x5 and (x + 50) <= (x5 + 50):
        if y >= y5 and y <= (y5 + 50):
            fail()
    if x >= x5 and x <= (x5 + 50):
        if (y + 50) >= y5 and (y + 50) <= (y5 + 50):
            fail()

    if x >= x6 and x <= (x6 + 50):
        if y >= y6 and y <= (y6 + 50):
            fail()
    if (x + 50) >= x6 and (x + 50) <= (x6 + 50):
        if (y + 50) >= y6 and (y + 50) <= (y6 + 50):
            fail()
    if (x + 50) >= x6 and (x + 50) <= (x6 + 50):
        if y >= y6 and y <= (y6 + 50):
            fail()
    if x >= x6 and x <= (x6 + 50):
        if (y + 50) >= y6 and (y + 50) <= (y6 + 50):
            fail()

    if x >= x7 and x <= (x7 + 50):
        if y >= y7 and y <= (y7 + 50):
            fail()
    if (x + 50) >= x7 and (x + 50) <= (x7 + 50):
        if (y + 50) >= y7 and (y + 50) <= (y7 + 50):
            fail()
    if (x + 50) >= x7 and (x + 50) <= (x7 + 50):
        if y >= y7 and y <= (y7 + 50):
            fail()
    if x >= x7 and x <= (x7 + 50):
        if (y + 50) >= y7 and (y + 50) <= (y7 + 50):
            fail()

    if x >= x8 and x <= (x8 + 50):
        if y >= y8 and y <= (y8 + 50):
            fail()
    if (x + 50) >= x8 and (x + 50) <= (x8 + 50):
        if (y + 50) >= y8 and (y + 50) <= (y8 + 50):
            fail()
    if (x + 50) >= x8 and (x + 50) <= (x8 + 50):
        if y >= y8 and y <= (y8 + 50):
            fail()
    if x >= x8 and x <= (x8 + 50):
        if (y + 50) >= y8 and (y + 50) <= (y8 + 50):
            fail()

    if x >= x9 and x <= (x9 + 50):
        if y >= y9 and y <= (y9 + 50):
            fail()
    if (x + 50) >= x9 and (x + 50) <= (x9 + 50):
        if (y + 50) >= y9 and (y + 50) <= (y9 + 50):
            fail()
    if (x + 50) >= x9 and (x + 50) <= (x9 + 50):
        if y >= y9 and y <= (y9 + 50):
            fail()
    if x >= x9 and x <= (x9 + 50):
        if (y + 50) >= y9 and (y + 50) <= (y9 + 50):
            fail()

    if x >= x10 and x <= (x10 + 50):
        if y >= y10 and y <= (y10 + 50):
            fail()
    if (x + 50) >= x10 and (x + 50) <= (x10 + 50):
        if (y + 50) >= y10 and (y + 50) <= (y10 + 50):
            fail()
    if (x + 50) >= x10 and (x + 50) <= (x10 + 50):
        if y >= y10 and y <= (y10 + 50):
            fail()
    if x >= x10 and x <= (x10 + 50):
        if (y + 50) >= y10 and (y + 50) <= (y10 + 50):
            fail()

    if x >= x11 and x <= (x11 + 50):
        if y >= y11 and y <= (y11 + 50):
            fail()
    if (x + 50) >= x11 and (x + 50) <= (x11 + 50):
        if (y + 50) >= y11 and (y + 50) <= (y11 + 50):
            fail()
    if (x + 50) >= x11 and (x + 50) <= (x11 + 50):
        if y >= y11 and y <= (y11 + 50):
            fail()
    if x >= x11 and x <= (x11 + 50):
        if (y + 50) >= y11 and (y + 50) <= (y11 + 50):
            fail()

    if x >= x12 and x <= (x12 + 50):
        if y >= y12 and y <= (y12 + 50):
            fail()
    if (x + 50) >= x12 and (x + 50) <= (x12 + 50):
        if (y + 50) >= y12 and (y + 50) <= (y12 + 50):
            fail()
    if (x + 50) >= x12 and (x + 50) <= (x12 + 50):
        if y >= y12 and y <= (y12 + 50):
            fail()
    if x >= x12 and x <= (x12 + 50):
        if (y + 50) >= y12 and (y + 50) <= (y12 + 50):
            fail()

    if x >= x13 and x <= (x13 + 50):
        if y >= y13 and y <= (y13 + 50):
            fail()
    if (x + 50) >= x13 and (x + 50) <= (x13 + 50):
        if (y + 50) >= y13 and (y + 50) <= (y13 + 50):
            fail()
    if (x + 50) >= x13 and (x + 50) <= (x13 + 50):
        if y >= y13 and y <= (y13 + 50):
            fail()
    if x >= x13 and x <= (x13 + 50):
        if (y + 50) >= y13 and (y + 50) <= (y13 + 50):
            fail()

    if x >= x14 and x <= (x14 + 50):
        if y >= y14 and y <= (y14 + 50):
            fail()
    if (x + 50) >= x14 and (x + 50) <= (x14 + 50):
        if (y + 50) >= y14 and (y + 50) <= (y14 + 50):
            fail()
    if (x + 50) >= x14 and (x + 50) <= (x14 + 50):
        if y >= y14 and y <= (y14 + 50):
            fail()
    if x >= x14 and x <= (x14 + 50):
        if (y + 50) >= y14 and (y + 50) <= (y14 + 50):
            fail()

    if x >= x15 and x <= (x15 + 50):
        if y >= y15 and y <= (y15 + 50):
            fail()
    if (x + 50) >= x15 and (x + 50) <= (x15 + 50):
        if (y + 50) >= y15 and (y + 50) <= (y15 + 50):
            fail()
    if (x + 50) >= x15 and (x + 50) <= (x15 + 50):
        if y >= y15 and y <= (y15 + 50):
            fail()
    if x >= x15 and x <= (x15 + 50):
        if (y + 50) >= y15 and (y + 50) <= (y15 + 50):
            fail()

    if x >= x16 and x <= (x16 + 50):
        if y >= y16 and y <= (y16 + 50):
            fail()
    if (x + 50) >= x16 and (x + 50) <= (x16 + 50):
        if (y + 50) >= y16 and (y + 50) <= (y16 + 50):
            fail()
    if (x + 50) >= x16 and (x + 50) <= (x16 + 50):
        if y >= y16 and y <= (y16 + 50):
            fail()
    if x >= x16 and x <= (x16 + 50):
        if (y + 50) >= y16 and (y + 50) <= (y16 + 50):
            fail()

    time = (pygame.time.get_ticks()//1000)

    drawWindow()
pygame.quit()