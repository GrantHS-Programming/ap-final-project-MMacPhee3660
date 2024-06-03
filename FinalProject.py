import pgzrun

WIDTH = 300
HEIGHT = 300

star = Actor('star', (150, 150))
star_hit = Rect((0, 0), (32, 32))
star_hit.center = star.center

heart = Actor('heart', (250, 250))

bubble = Actor('bubble', (255, 230))
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

y = Actor('y', (150, 150))
y_hit = Rect((0,0), (5,10))

n = Actor('n', (150, 150))

background = 1
click = 0
speech = 0
show_flower = 1
inventory = 0
pause = 0
flower_inv = 0
ask = 0
ask_flower = 0


def draw():
    global background, inventory, pause
    screen.clear()
    screen.fill((255, 255, 255))
    if background == 1:
        screen.blit("test background 1", (150, 150))
        heart.draw()
        if star.top > WIDTH:
            background = 2
            star.top = 0
        if star.distance_to(heart) < 40:
            if speech != 1:
                bubble.draw()
        if speech == 1:
            window.draw()
            x.draw()
        if ask == 1:
            giving.draw()
            y.draw()
            n.draw()
            if ask_flower == 1:
                flower_name.draw()


    if background == 2:
        screen.blit("test background 2", (150, 150))
        if show_flower == 1:
            Flower.draw()
        if star.bottom < 0:
            background = 1
            star.bottom = WIDTH

    if inventory == 1:
        inv.draw()
        if flower_inv:
            flower.draw()

    star.draw()


def update():
    global click, pause, show_flower, flower_inv, ask, ask_flower
    star_hit.center = star.center
    if click != 1:
        if keyboard.w or keyboard.up:
            star.y -= 1
        if keyboard.s or keyboard.down:
            star.y += 1
        if keyboard.a or keyboard.left:
            star.x -= 1
        if keyboard.d or keyboard.right:
            star.x += 1
        if Flower_hit.colliderect(star_hit) and background == 2:
            show_flower = 0
            flower_inv = 1
            ask = 1
            ask_flower = 1
    if click == 1:
        pause = pause + 1


def on_mouse_down(pos):
    global click, speech
    if bubble_hit.collidepoint(pos[0], pos[1]) and background == 1:
        click = 1
        speech = 1
    if x_hit.collidepoint(pos[0], pos[1]) and background == 1:
        click = 0
        speech = 0


def on_mouse_up():
    global click


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
