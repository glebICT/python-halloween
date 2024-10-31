import turtle


screen = turtle.Screen()
screen.bgcolor("black")

bob = turtle.Turtle()
bob.color ("black")
bob.goto(-200, 50)
bob.color("orange")
for _ in range (90):
    bob.forward(4)
    bob.left(4)

bob.color ("black")
bob.goto( 200, 50)
bob.color("orange")
for _ in range (90):
    bob.forward(4)
    bob.left(4)
bob.color("black")
bob.right(90)
bob.forward(200)
bob.color("orange")
bob.right(180)
for _ in range (90):
    bob.forward(7)
    bob.left(2)
bob.left(90)
bob.forward(400)


turtle.done()