import turtle
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.color("red")
my_turtle.speed(1)
while True:
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.forward(2)
    
turtle.done()