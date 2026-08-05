import turtle
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.speed(1)
postition = [
    (100,100),
    (-100,100),
    (-100,-100),
    (100,-100)
]
def triangle():
    my_turtle.color("red")
    for i in range(3):
        my_turtle.forward(50)
        my_turtle.left(120)

def square():
    my_turtle.color("yellow")
    for i in range(4):
        my_turtle.forward(50)
        my_turtle.left(90)

def pentagon():
    my_turtle.color("pink")
    for i in range(5):
        my_turtle.forward(50)
        my_turtle.left(72)

def hexagon():
    my_turtle.color("blue")
    for i in range(6):
        my_turtle.forward(50)
        my_turtle.left(60)
shapes = [
    triangle,square,pentagon,hexagon
]

def final_output():
    for i in range(4):
        my_turtle.penup()
        my_turtle.goto(postition[i])
        my_turtle.pendown()
        shapes[i]()

final_output()
turtle.done()