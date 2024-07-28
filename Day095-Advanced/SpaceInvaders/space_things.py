import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Screen Setup
win = turtle.Screen()
win.title("Space Invaders")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off the screen updates

# Ship Setup
ship = turtle.Turtle()
ship.speed(0)
ship.shape("triangle")
ship.color("white")
ship.penup()
ship.goto(0, -200)  # Starting position
ship.direction = "stop"

# Aliens Setup
aliens = []
for i in range(6):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("square")
    enemy.color("green")
    enemy.penup()
    x = -220 + i * 40
    y = 210
    enemy.goto(x, y)
    aliens.append(enemy)

# Functionality
def move_left():
    x = ship.xcor()
    x -= 3
    ship.setx(x)

def move_right():
    x = ship.xcor()
    x += 3
    ship.setx(x)

def move_up():
    y = ship.ycor()
    y += 3
    ship.sety(y)

def move_down():
    y = ship.ycor()
    y -= 3
    ship.sety(y)

def move_towards_ship(alien):
    x = alien.xcor()
    y = alien.ycor()
    if x < 0:
        direction = 270
    elif x > 290:
        direction = 90
    else:
        direction = random.choice([-180, 0, 180])
    alien.setheading(direction)
    alien.forward(2)

def check_collision(ship, alien):
    if (ship.distance(alien) < 20):
        return True
    return False

# Keyboard Bindings
win.listen()
win.onkeypress(move_left, "a")
win.onkeypress(move_right, "d")
win.onkeypress(move_up, "w")
win.onkeypress(move_down, "s")

# Main Gameplay
while True:
    for alien in aliens:
        move_towards_ship(alien)
        (collision,) = check_collision(ship, alien)
        if collision:
            time.sleep(1)
            ship.hideturtle()
            alien.hideturtle()
            break
    win.update()
    time.sleep(delay)
