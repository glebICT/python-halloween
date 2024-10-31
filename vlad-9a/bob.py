import turtle


screen = turtle.Screen()
screen.bgcolor("black")

bob = turtle.Turtle()
bob.color ("black")
bob.goto(-300, 50)
bob.color("orange")
for _ in range (180):
    bob.forward(3)
    bob.left(2)

bob.color ("black")
bob.goto( 300, 50)
bob.color("orange")
for _ in range (180):
    bob.forward(3)
    bob.left(2)
bob.right(90)
for _ in range (180):
    bob.forward(5)
    bob.right(1)

turtle.done()