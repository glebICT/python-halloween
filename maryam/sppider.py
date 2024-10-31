import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_right_leg(x,y):
    p = turtle.Turtle()
    p.goto(x,y)
    p.forward(45)  # Length of the leg
    p.right(70)    # Adjust angle for the next leg
    p.forward(50) # Return to the starting point
    p.penup()
    p.backward(50)
    p.left(70)
    p.backward(45)
    p.right(90)
    p.forward(40)
    p.pendown()

def draw_left_leg(x,y):
    p = turtle.Turtle()
    p.setheading(180)
    p.goto(x,y)
    p.forward(45)  # Length of the leg
    p.left(70)    # Adjust angle for the next leg
    p.forward(50) # Return to the starting point
    p.penup()
    p.backward(50)
    p.right(70)
    p.backward(45)
    p.left(90)
    p.forward(40)
    p.pendown()
      
def draw_spider():
    # Draw body and head
    draw_circle('black', 50, 0, -50)  # Main body
   
    
    # Draw eyes
    draw_circle('pink', 10, -10, 10)    # Left eye
    draw_circle('light blue', 10, 10, 10)     # Right eye
    
    # Draw legs
    legs = 8
     
    turtle.left(30)
    for y in range(0,4):
        draw_right_leg(100, y*10)
        draw_left_leg(-100,-y*10)
        # turtle.penup() 

       
        

# Set up the screen
turtle.speed(3)
turtle.bgcolor('pink')

# Draw the spider
draw_spider()

# Finish
turtle.hideturtle()
turtle.done()