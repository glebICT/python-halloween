import turtle

def draw_cobweb():
    turtle.speed(0.1)  # Fastest drawing speed
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.color("white")

    # Draw the concentric circles
    for radius in range(20, 200, 20):
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.circle(radius)

    # Draw the spokes
    for angle in range(0, 360, 15):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.forward(200)

    turtle.hideturtle()

def draw_spider(x, y):
    turtle.penup()
    turtle.goto(x, y)  # Position the spider
    turtle.pendown()
    turtle.color("#ff0000")  # Spider color

    # Draw a bigger spider body
    turtle.begin_fill()
    turtle.circle(15)  # Bigger spider body
    turtle.end_fill()

    # Draw bigger spider legs
    for angle in range(0, 360, 45):  # 8 legs
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.forward(30)  # Longer legs

    turtle.hideturtle()

# Setup the window size
turtle.setup(width=1920, height=1080)

# Draw the cobweb and spider
draw_cobweb()
draw_spider(0, -10)  # Position the spider in the center

turtle.done()
