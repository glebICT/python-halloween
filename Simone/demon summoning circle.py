import turtle

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_mandala_star(radius, star_size):
    for _ in range(9):  # Number of stars in the mandala
        draw_star(star_size)
        turtle.penup()
        turtle.forward(radius)  # Move outwards to position for the next star
        turtle.pendown()
        draw_star(star_size)
        turtle.penup()
        turtle.backward(radius)  # Move back to the center
        turtle.right(40)  # Rotate to the next position (360/9 = 40 degrees)
        turtle.pendown()

def main():
    turtle.bgcolor("black")  # Set background color to black
    turtle.speed(3)  # Set the speed of the turtle
    turtle.color("red")  # Change star color for better visibility against black
    
    turtle.penup()
    turtle.goto(0, 0)  # Start at the center
    turtle.pendown()
    
    draw_mandala_star(100, 30)  # Draw the mandala of stars

    turtle.hideturtle()  # Hide the turtle
    turtle.done()  # Finish the drawing

if __name__ == "__main__":
    main()