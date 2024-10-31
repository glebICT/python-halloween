import time
import turtle

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
pum = turtle.Turtle()
 
# "Flatten" the lower part of the pumpkin
pum.penup()
pum.setposition(-200, -100)
pum.pensize(60)
pum.pendown()
pum.forward(600)
pum.pensize(2)

def carve_pumpkin(colour):
    pum.color(colour)

    # Make eyes
    def make_eye(start, orientation):
        pum.setheading(0)
        pum.penup()
        pum.setposition(*start)
        pum.pendown()
        pum.begin_fill()
        pum.forward(orientation * 40)
        pum.setheading(orientation * 135)
        pum.forward(orientation * 70)
        pum.end_fill()

    make_eye((-50, 20), 1)
    make_eye((50, 20), -1)

    # Make mouth
    pum.penup()
    pum.setposition(-50, -30)
    pum.setheading(45)
    pum.pendown()
    pum.pensize(1)
    pum.begin_fill()
    for _ in range(5):
        pum.forward(15)
        pum.right(90)
        pum.forward(15)
        pum.left(90)
    pum.setheading(260)
    pum.forward(20)
    pum.setheading(180)
    pum.forward(99)
    pum.end_fill()

    # Make nose
    pum.penup()
    pum.setposition(0, 0)
    pum.setheading(90)
    pum.shape("triangle")
    pum.stamp()

carve_pumpkin("black")

# Write text on animation
text = turtle.Turtle()
text.hideturtle()
text.color("orange")
text.penup()
text.sety(175)
text.write("Happy Halloween", font=("Trattatello", 60, "bold"), align="center")
 
window.tracer(0)
start = time.time()
count = 0
colours = "yellow", "black"
while True:
    if time.time() - start > 1:
        carve_pumpkin(colours[count % 2])
        window.update()
        count += 1
        start = time.time() # Reset timer

turtle.done()