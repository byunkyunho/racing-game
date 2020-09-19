import pygame as pg
import random
import time
import math

line = []
car_list = []
bonus_list = []
px = 274
score = 0
T_score = 0
heart = 3
count = 0
level = 0
a_car = True
a_bonus = False
running = True
gameover = False
play_sound = False
for a in range(7):
    line.append(a*150)

pg.init()

screen = pg.display.set_mode((600, 800))

pg.display.set_caption("Racing Game")

font = pg.font.SysFont("arial", 40)
bigfont = pg.font.SysFont("arial", 100)

oil = pg.image.load("image/연료통.png")
b_heart = pg.image.load("image/하트.png")
s_heart = pg.transform.scale(b_heart, (30, 30))
bonus = pg.transform.scale(oil, (100, 100))
Car1 = pg.image.load("image/RacingCar01.png")
Car2 = pg.image.load("image/RacingCar02.png")
Car3 = pg.image.load("image/RacingCar03.png")
Car4 = pg.image.load("image/RacingCar04.png")
Car5 = pg.image.load("image/RacingCar05.png")
Car6 = pg.image.load("image/RacingCar06.png")
Car7 = pg.image.load("image/RacingCar07.png")
Car8 = pg.image.load("image/RacingCar08.png")
Car9 = pg.image.load("image/RacingCar09.png")
Car10 = pg.image.load("image/RacingCar10.png")
Car11 = pg.image.load("image/RacingCar11.png")
Car12 = pg.image.load("image/RacingCar12.png")
Car13 = pg.image.load("image/RacingCar13.png")
Car14 = pg.image.load("image/RacingCar14.png")
Car15 = pg.image.load("image/RacingCar15.png")
Car16 = pg.image.load("image/RacingCar16.png")
Car17 = pg.image.load("image/RacingCar17.png")
Car18 = pg.image.load("image/RacingCar18.png")
Car19 = pg.image.load("image/RacingCar19.png")
Car20 = pg.image.load("image/RacingCar20.png")
Start_image = pg.image.load("image/Carracing_bg.jpg")
car = [Car2 , Car3 ,Car4, Car5, Car6, Car7, Car8, Car9, Car10, Car11, Car12, Car13, Car14, Car15, Car16, Car17, Car18, Car19, Car20]

crash = pg.mixer.Sound("sound/crash.wav")
engine = pg.mixer.Sound("sound/engine.wav")
race = pg.mixer.Sound("sound/race.wav")

pg.key.set_repeat(1, 1)

def sound(a, b):
    if play_sound == True:
        a.play(b)

def reset():
    global px, score, heart, count, a_car, a_bonus, gameover, car_list, bonus_list, running, level
    car_list = []
    bonus_list = []
    px = 274
    score = 0
    heart = 3
    count = 0
    level = 0
    a_car = False
    a_bonus = False
    running = True
    gameover = False

def d_level():
    global count, level
    if count % 1500 == 0:
        level += 1
        t_level = bigfont.render("level {}".format(level), True, (255, 255, 255))
        screen.blit(t_level, (155, 100))
        pg.display.update()
        time.sleep(2)

def u_bonus():
    global a_bonus
    if a_bonus == True:
        bonus_list.append([random.randint(200, 300), -50])
        a_bonus = False
    for h in bonus_list:
        h[1] += 8

def d_bonus():
    for h in bonus_list:
        screen.blit(bonus, h)

def check_car():
    global px, heart
    for c in car_list:
        d = math.sqrt(math.pow((c[1] + 23) - (px + 23), 2) + math.pow((c[2] + 67) - 667 , 2))
        if d <= 60:
            heart -= 1
            car_list.remove(c)
            sound(crash, 0)

def check_bonus():
    global px, heart
    for h in bonus_list:
        d = math.sqrt(math.pow((h[0] + 50) - (px + 23), 2) + math.pow((h[1] + 50) - 667 , 2))
        if d <= 50:
            heart += 1
            bonus_list.remove(h)

def u_car():
    global score, a_car
    if a_car == True:
        car_list.append([car[random.randint(0, 18)],random.randint(130, 415), -133, random.randint(1, 8)])
        a_car = False
    for c in car_list:
        c[2] += c[3]
        if c[2] >= 800:
            car_list.remove(c)
            score += 100
        

def u_line():
    for l in range(6):
        line[l] += 8
        if line[l] >= 800:
            line[l] = -100
            
def d_line():
    for l in line:
        pg.draw.rect(screen, (255,255, 0), (296, l, 8, 60))

def d_heart():
    global heart, gameover
    if heart == 3:
        screen.blit(s_heart, (480, 20))
    if heart >= 2:
        screen.blit(s_heart, (520, 20))
    if heart >= 1:
        screen.blit(s_heart, (560, 20))
    if heart == 0:
        gameover = True
        
def d_car():
    for c in car_list:
        screen.blit(c[0], (c[1], c[2]))

def d_score():
    global score, T_score
    bestscore = open("bestscore.text", "r")
    T_score = int(bestscore.read())
    if score >= T_score:
        writebestscore = open("bestscore.text", "w")
        writebestscore.write(str(score))
        bestscore.close()

    scoreT = font.render("score : {}".format(score), True, (255,255,255))
    scoreTT = font.render("Bestscore : {}".format(T_score), True, (255,255,255))
    screen.blit(scoreT, (20, 70))
    screen.blit(scoreTT, (20, 20))
    
def d_background():
    screen.fill((0, 0 ,0))
    pg.draw.rect(screen, (0, 255, 0), (0, 0, 130, 800))
    pg.draw.rect(screen, (0, 255, 0), (470, 0, 130, 800))

def d_mycar():
    screen.blit(Car1, ( px ,667))


def d_gameover():
    gameoverT = bigfont.render("Game Over", True, (255,255,255))    
    screen.blit(gameoverT, (50, 200))
    pg.display.update()

sound(race, -1)

while not gameover:
    while running:
        for event in pg.event.get():    
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                running = False

        screen.blit(Start_image, (0,0))

        pg.display.update()

    running = True
    
    sound(engine, 0)

    while running and not gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    if px >= 413:
                        pass
                    else:
                        px += 4
                if event.key == pg.K_LEFT:
                    if px <= 131:
                        pass
                    else:
                        px -= 4

        u_car()
        u_bonus()
        u_line()
        check_car()
        check_bonus()
        d_background()
        d_line()
        d_car()
        d_mycar()
        d_bonus()
        d_heart()
        d_score()
        d_level()

        pg.display.update()

        if count % (200 - level*50) == 0:
            a_car = True

        if count % 500 == 0:
            if heart < 3:
                a_bonus = True

        count += 1

        time.sleep(0.01)

    if running == False:
        pg.quit()
        break

    reset()

    d_gameover()

    time.sleep(3)
