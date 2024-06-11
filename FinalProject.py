import pgzrun
from pgzhelper import *

WIDTH = 500
HEIGHT = 500

star = Actor('star', (250, 375))
star_hit = Rect((0, 0), (32, 32))
star_hit.center = star.center

heart = Actor('heart', (375, 375))

bubble = Actor('bubble', (0, 0))
bubble.bottom = heart.top
bubble.left = heart.left
bubble_hit = Rect((0, 0), (32, 32))
bubble_hit.center = bubble.center

window = Actor('window', (150, 150))

inv = Actor('inv', (100, 100))

flower = Actor('flower', (100, 100))
flower_hit = Rect((0, 0), (5, 5))
flower_hit.center = flower.center

Flower = Actor('big flower', (100, 250))
Flower_hit = Rect((0, 0), (32, 32))
Flower_hit.center = Flower.center

circle = Actor('circle', (155, 160))
circle_hit = Rect((0, 0), (5, 5))
circle_hit.center = circle.center

x = Actor('x', (100, 100))
x_hit = Rect((0, 0), (32, 32))
x_hit.center = x.center

giving = Actor('give window', (150, 150))

flower_name = Actor('flower name', (150, 150))

y = Actor('y', (145, 160))
y_hit = Rect((0, 0), (5, 10))
y_hit.center = y.center

n = Actor('n', (155, 160))
n_hit = Rect((0, 0), (5, 10))
n_hit.center = n.center

north = Actor('travel north', (250, 250))
north.scale = 5.21
north_hit = Rect((0, 0), (41, 83))
north_hit.center = north.center

east = Actor('travel east', (250, 250))
east.scale = 5.21

south = Actor('travel south', (250, 250))
south.scale = 5.21

west = Actor('travel west', (250, 250))
west.scale = 5.21

background1 = Actor('background 1', (250, 250))
background1.scale = 5.21

background = 1
click = 0
speech = 0
show_flower = 1
inventory = 0
pause = 0
flower_inv = 0
ask = 0
ask_flower = 0
flower_given = 0
heart_hello = 1
heart_hello2 = 0
north_click = 0
south.click = 0


def draw():
    global background, inventory
    screen.clear()
    screen.fill((255, 255, 255))

    if background == 1:
        screen.clear()
        background1.draw()
        heart.draw()
        if star.top > WIDTH:
            background = 2
            star.top = 0
        if star.distance_to(heart) < 40:
            if speech == 0 or ask == 0:
                bubble.draw()
        if speech == 1:
            window.draw()
        if ask == 1 and heart_hello == 0:
            giving.draw()
            y.draw()
            n.draw()
            if ask_flower == 1:
                flower_name.draw()

    if background == 2:
        screen.blit("test background 2", (0, 0))
        if show_flower == 1:
            Flower.draw()
        if star.bottom < 0:
            background = 1
            star.bottom = WIDTH

    if inventory == 1:
        inv.draw()
        if flower_inv:
            flower.draw()

    north.draw()
    east.draw()
    south.draw()
    west.draw()
    star.draw()


def update():
    global click, pause, show_flower, flower_inv, ask_flower
    star_hit.center = star.center
    if click != 1:
        if (keyboard.w or keyboard.up): #and star.top > 275:
            star.y -= 2
        if keyboard.s or keyboard.down:
            star.y += 2
        if keyboard.a or keyboard.left:
            star.x -= 2
        if keyboard.d or keyboard.right:
            star.x += 2
        if Flower_hit.colliderect(star_hit) and background == 2:
            show_flower = 0
            flower_inv = 1
            ask_flower = 1
    if click == 1:
        pause = pause + 1


def on_mouse_down(pos):
    global click, speech, ask_flower, ask, flower_given, flower_inv, pause, heart_hello, heart_hello2
    if bubble_hit.collidepoint(pos[0], pos[1]) and background == 1 and star.distance_to(heart) < 40:
        click = 1
        speech = 1
        pause = 0
        print("Did you find a flower for me?")
    if bubble_hit.collidepoint(pos[0], pos[1]) and background == 1 and star.distance_to(heart) < 40 and ask_flower == 1:
        click = 1
        ask = 1
        pause = 0
    if bubble_hit.collidepoint(pos[0], pos[1]) and background == 1 and star.distance_to(heart) < 40 and heart_hello == 1:
        click = 1
        speech = 1
        pause = 0
        heart_hello = 0
        heart_hello2 = 1
        print("Oh hello there!")
    if background == 1 and heart_hello2 == 1 and pause > 0:
        click = 1
        speech = 1
        pause = 0
        heart_hello2 = 0
        print("Could you help me find a flower?")
    if y_hit.collidepoint(pos[0], pos[1]) and background == 1 and ask == 1:
        flower_given = 1
        ask = 0
        speech = 0
        click = 0
        flower_inv = 0
    if n_hit.collidepoint(pos[0], pos[1]) and background == 1 and ask == 1:
        speech = 0
        ask = 0
        click = 0
    if click == 1 and pause > 0 and heart_hello2 == 0 and heart_hello == 0:
        click = 0
        speech = 0


def on_key_down(key):
    global inventory, click, pause
    if key == key.I and inventory == 0:
        inventory = 1
        click = 1
        pause = 0
    if key == key.I and inventory == 1 and pause > 1:
        inventory = 0
        click = 0


pgzrun.go()
