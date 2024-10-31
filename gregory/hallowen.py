import turtle
import time


window = turtle.Screen()
window.bgcolor("black")


circle1 = turtle.Turtle()
circle1.hideturtle()
circle1.goto(-40, 0)
circle1.color("dark orange")
circle1.dot(250)

circle2 = turtle.Turtle()
circle2.hideturtle()
circle2.goto(40, 0)
circle2.color("dark orange")
circle2.dot(250)


pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(250)


carver = turtle.Turtle()


carver.penup()
carver.setposition(-200, -100)
carver.pensize(50)
carver.pendown()
carver.forward(600)
carver.pensize(2)

def carver_pumpkin(color):
    carver.color(color)

  
    def make_eye(start, orientation):
        carver.setheading(0)
        carver.penup()
        carver.setposition(*start)
        carver.pendown()
        carver.begin_fill()
        carver.forward(orientation * 40)
        carver.setheading(orientation * 135)
        carver.forward(orientation * 70)
        carver.end_fill()

    make_eye((-50, 20), 1)
    make_eye((50, 20), -1)


    carver.penup()
    carver.setposition(-50, -30)
    carver.setheading(45)
    carver.pendown()
    carver.pensize(1)
    carver.begin_fill()
    for _ in range(5):
        carver.forward(15)
        carver.right(90)
        carver.forward(15)
        carver.left(90)
    carver.setheading(260)
    carver.forward(20)
    carver.setheading(180)
    carver.forward(99)
    carver.end_fill()

   
    carver.penup()
    carver.setposition(0, 0)
    carver.setheading(90)
    carver.shape("triangle")
    carver.stamp()


carver_pumpkin("black")


text = turtle.Turtle()
text.hideturtle()
text.color("orange")
text.penup()
text.sety(175)
text.write("Witching you a Happy Halloween!", font=("Trattatello", 40, "bold"), align="center")


window.tracer(0)
start = time.time()
count = 0
colors = ["yellow", "black"]

while True:
    if time.time() - start > 1:
        carver_pumpkin(colors[count % 2])
        window.update()
        count += 1
        start = time.time()  

turtle.done()