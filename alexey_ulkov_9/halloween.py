import turtle
import time

t = turtle.Pen()
turtle.Screen().bgcolor("black")
turtle.colormode(255)

t.up()
t.speed(0)

def circle(r, g, b, size):
    t.color(int(r), int(g), int(b))
    t.begin_fill()
    t.down()
    t.circle(int(size))
    t.end_fill()
    t.up()

t.sety(-150)
t.setx(65)
circle(210, 115, 5, 210)
t.setx(-65)
circle(210, 115, 5, 210)
t.setx(0)
circle(220, 120, 5, 208)

def triangle(r, g, b, size):
    t.color(int(r), int(g), int(b))
    t.down()
    t.begin_fill()
    t.circle(size, None, 3)
    t.end_fill()
    t.up()

t.setpos(-80, 70)
t.right(5)
triangle(0, 0, 0, 50)
t.setpos(85, 68)
t.left(15)
triangle(0, 0, 0, 45)

t.home()

t.right(190)

for n in range(10):
    xcord = (n - 5) * 20
    ycord = ((n - 5) ** 2) / 2 - 30
    t.setpos(xcord, ycord)
    t.left(2)
    triangle(0, 0, 0, 35)

t.home()
t.setpos(0, 20)
triangle(0, 0, 0, 30)

number = 0

while True:
    number = number + 1
    if number == 100:
        for a in range(100):
            number = number - 1
            turtle.bgcolor(number, number, number)
            time.sleep(0.02)
    else:
        turtle.bgcolor(number, number, number)
        time.sleep(0.01)

turtle.done()