import turtle
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.speed(0)
colors_for_squares = ["red","blue","pink","green"]
colors_for_triangles = ["yellow","orange","cyan","purple"]
position_for_squares = [
    (100,100),
    (-100,100),
    (-100,-100),
    (100,-100)
]
position_for_triangles = [
    (100,150),
    (-100,150),
    (-100,-50),
    (100,-50)
]
def squares():
    for i in range(4):
        my_turtle.forward(50)
        my_turtle.left(90)

def triangles():
    for i in range(3):
        my_turtle.forward(50)
        my_turtle.left(120)

def final_output():
    for i in range(4):
        my_turtle.penup()
        my_turtle.goto(position_for_squares[i])
        my_turtle.pendown()
        my_turtle.color(colors_for_squares[i])
        squares()
        my_turtle.penup()
        my_turtle.goto(position_for_triangles[i])
        my_turtle.pendown()
        my_turtle.color(colors_for_triangles[i])
        triangles()

final_output()
turtle.done()