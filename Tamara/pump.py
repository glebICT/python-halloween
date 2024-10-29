import turtle
turtle.speed(0)
turtle.bgcolor("black")

def draw_pumpkin():
    turtle.color("#FF4500")
    
    # Draw the pumpkin body
    turtle.begin_fill()
    turtle.circle(100) 
    turtle.end_fill()

    turtle.begin_fill()
    turtle.penup()
    turtle.backward(70)
    turtle.pendown()
    turtle.circle(100)
    turtle.end_fill() 

    turtle.begin_fill()
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()
    turtle.circle(100)
    turtle.end_fill() 
 
def eye(x,y, color): 
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(3):
        turtle.forward(50)
        turtle.right(-120)
    turtle.end_fill()
   





 # Draw the mouth  
def mouth1(x,y, color):    
     turtle.penup()
     turtle.goto(x,y)
     turtle.pendown()
     turtle.begin_fill()
     turtle.color(color)
     for _ in range(3):
        turtle.forward(35)
        turtle.right(-120)
     turtle.end_fill() 

def mouth2(x,y, color):    
     turtle.penup()
     turtle.goto(x,y)
     turtle.pendown()
     turtle.begin_fill()
     turtle.color(color)
     for _ in range(3):
        turtle.forward(35)
        turtle.right(120)
     turtle.end_fill() 


def draw_face():
    eye(-150,110, 'black')
    eye(-20, 110, 'black')
    mouth1(-155,50, "black")
    mouth2(-145,55, "black")
    mouth1(-135,50, "black")
    mouth2(-125,55, "black")
    mouth1(-115,50, "black")
    mouth2(-105,55, "black")
    mouth1(-95,50, "black")
    mouth2(-85,55, "black")
    mouth1(-75,50, "black")
    mouth2(-65,55, "black")
    mouth1(-55,50, "black")
    mouth2(-45,55, "black")
    mouth1(-35,50, "black")
    mouth2(-25,55, "black")
    mouth1(-15,50, "black")
   

 
def main():
    turtle.title("Scary Pumpkin")
    draw_pumpkin()
    draw_face()

    # draw_triangle()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
