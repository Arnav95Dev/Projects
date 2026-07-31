import turtle
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.speed(1)
my_turtle.shape("circle")
def move_forward():
    my_turtle.forward(100)
def turn_left():
    my_turtle.left(120)
move_forward()
turn_left()
move_forward()
turn_left()
move_forward()
turtle.done()