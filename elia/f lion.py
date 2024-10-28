import turtle

def draw_head():
    turtle.speed(0)
    turtle.bgcolor("#8FE79B")
    turtle.color("#ffde0c")
    turtle.goto(100,-10)
    turtle.begin_fill()
    turtle.circle(100) 
    turtle.end_fill()

def draw_eyes():
    turtle.speed(0)
    turtle.color("white")
    turtle.penup()
    turtle.goto(150,80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25) 
    turtle.end_fill()

    turtle.speed(0)
    turtle.color("white")
    turtle.penup()
    turtle.goto(50,80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25) 
    turtle.end_fill()

    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(150,80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20) 
    turtle.end_fill()

    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(50,80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20) 
    turtle.end_fill()

def draw_nose():
    turtle.speed(0)
    turtle.fillcolor('black')
    turtle.penup()
    turtle.goto(90,70)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(20)
        turtle.right(120)
    turtle.end_fill()

def draw_mouth(): 
    turtle.speed(0)
    turtle.color('black')
    turtle.penup()
    turtle.goto(100,55)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(1):
        turtle.forward(50)
        turtle.right(180)
    turtle.end_fill()

    turtle.speed(0)
    turtle.fillcolor('black')
    turtle.penup()
    turtle.goto(100,55)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(1):
        turtle.forward(50)
        turtle.left(80)
    turtle.end_fill()

def draw_tooth(x,y, t):
    t.speed(0)
    t.fillcolor('white')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(20)
        t.right(120)
    t.end_fill()
    t.hideturtle()

 

def draw_ear(x,y):
    turtle.speed(0)
    turtle.color("#ffde0c")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(23) 
    turtle.end_fill()

def draw_hair():
    turtle.speed(0)
    turtle.color("#FFBF00")
    turtle.begin_fill()
    turtle.circle(100) 
    turtle.end_fill()

def draw_mandala(repeats, size):
    for i in range(repeats):
        draw_hair()
       
        turtle.right(360 / repeats)

def main():
    turtle.title("lion")
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    draw_mandala(8, 50)
    draw_head()
    draw_eyes()
    draw_nose()
    draw_mouth()
    bob = turtle.Turtle()
    draw_tooth(58,55, bob)
    draw_tooth(120,55, bob)
    draw_ear(155,175) 
    draw_ear(5,175) 

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()