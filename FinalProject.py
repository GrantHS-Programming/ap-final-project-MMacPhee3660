import pgzrun

WIDTH = 300
HEIGHT = 300

star = Actor('star', (150, 150))

heart = Actor('heart', (250, 250))

bubble = Actor('bubble', (255, 230))
bubble_hit = Rect((0, 0), (32, 32))
bubble_hit.center = bubble.center

window = Actor('window', (150, 150))


x = Actor('x', (100, 100))
x_hit = Rect((0, 0), (32,32))
x_hit.center = x.center

background = 1
click = 0


def draw():
    global background
    screen.fill((255, 255, 255))

    if background == 1:
        screen.blit("test background 1", (150, 150))
        heart.draw()
        if star.top > WIDTH:
            background = 2
            star.top = 0
        if star.distance_to(heart) < 40:
            if click != 1:
                bubble.draw()
        if click == 1:
            window.draw()
            x.draw()

    if background == 2:
        screen.blit("test background 2", (150, 150))
        if star.bottom < 0:
            background = 1
            star.bottom = WIDTH
    star.draw()



def update():
    if click != 1:
        if keyboard.w or keyboard.up:
            star.y -= 1
        if keyboard.s or keyboard.down:
            star.y += 1
        if keyboard.a or keyboard.left:
            star.x -= 1
        if keyboard.d or keyboard.right:
            star.x += 1


def on_mouse_down(pos):
    global click
    if bubble_hit.collidepoint(pos[0], pos[1]) and background == 1:
        click = 1
    if x_hit.collidepoint(pos[0], pos[1]) and background == 1:
        click = 0


def on_mouse_up():
    global click









pgzrun.go()
