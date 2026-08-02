import turtle
movement = 5
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.speed(0)
my_turtle.forward(5)
while True:
    movement += 5
    my_turtle.forward(movement)
    my_turtle.left(59)

turtle.done()