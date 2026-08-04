import turtle
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.speed(1)
position = [
    (100,100),
    (-100,100),
    (-100,-100),
    (100,-100)
            ]
colors = ["red","blue","green","yellow"]
def squares():
    for i in range(4):
        my_turtle.forward(50)
        my_turtle.left(90)

def work():
    for i in range(4):
        my_turtle.penup()
        my_turtle.goto(position[i])
        my_turtle.pendown()
        my_turtle.color(colors[i])
        squares()

work()

turtle.done()