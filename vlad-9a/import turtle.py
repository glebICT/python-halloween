import turtle


screen = turtle.Screen()
screen.bgcolor("black")

bob = turtle.Turtle()
bob.color ("black")
bob.goto(-200, 50)
bob.color("orange")
for _ in range (180):
    bob.forward(2)
    bob.left(2)

bob.color ("black")
bob.goto( 200, 50)
bob.color("orange")
for _ in range (180):
    bob.forward(2)
    bob.left(2)



turtle.done()