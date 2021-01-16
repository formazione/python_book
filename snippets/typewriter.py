import sys, time
from random import randrange


def texttime(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        # if c == " ":
        if randrange(1, 5) == 3:
            time.sleep(0.1)



text = """
# pong!
import pygame
from random import choice

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Coordinates p1, p2 and ball
x1 = 490
y1 = 490
x2 = 0
y2 = 250
xb = 500
yb = 300

dbo = 'left'
dbv = 'down'

scorep1 = 0
scorep2 = 0

vel_bal = 2

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))

pygame.init()

def ball():
    "Draw the ball"
    global xb, yb
    pygame.draw.ellipse(screen, GREEN, (xb, yb, 10, 10))

def sprite1(x,y):
    "Draw Player 1"
    pygame.draw.rect(screen, RED, (x, y, 50, 10))

def sprite2(x,y):
    "Draw Player 2"
    pygame.draw.rect(screen, GREEN, (x, y, 10, 50))

def move_ball(x,y):
    "The ball moves"
    global xb, yb, dbo, dbv
    if dbo == "left":
        xb -= vel_bal
        if xb < 10:
            dbo = "right"
    if dbv == 'down':
        yb += vel_bal
    if dbv == 'up':
        yb -= vel_bal
        if yb < 10:
            dbv = 'down'
    if dbo == "right":
        xb += vel_bal
        if xb > 480:
            dbo = "left"
    
def collision():
    global x1, y1 # the player 1 x and y (on the right)
    global x2, y2 # the player 2 x and y (on the left)
    global xb, yb # the ball x and y
    global x, y
    global dbo, dbv, vel_bal
    global scorep1, scorep2
    if dbo == "left":
        if yb > 480:
            if xb >= x and  xb < x + 50:
                print("Collision detected")
                dbv = "up"
                vel_bal = choice([1,2,3])
                print(dbv)
                print(yb)
            else:
                pygame.draw.ellipse(screen, BLACK, (xb, yb, 10, 10))
                pygame.display.update()
                xb, yb = 500, 300
                # scorep1 += 10
                pygame.display.set_caption("My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))



def move1():
    global y2
    if y2 <= 450:
        if keys[pygame.K_z]:
            y2 += 20
    if y2 > 0:
        if keys[pygame.K_a]:
            y2 -= 20

def move2():
    global y1
    if y1 <= 450:
        if keys[pygame.K_m]:
            y1 += 20
    if y1 > 0:
        if keys[pygame.K_k]:
            y1 -= 20
pygame.mouse.set_visible(False)
loop = 1
while loop:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    x, y = pygame.mouse.get_pos()
    move1()
    move2()
    move_ball(xb, yb)
    ball()
    sprite1(x,y1)
    collision()
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(120)



pygame.quit()
"""

texttime(text)
