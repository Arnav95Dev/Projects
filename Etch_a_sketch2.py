import turtle
colors = ["red","blue",
          'pink',"yellow","green","orange"]
sides = int(input("Enter the number of sides of polygon: "))
screen = turtle.Screen()
screen.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.speed(1)
my_turtle.pensize(4)
def move_forward():
    my_turtle.forward(150)
def turn_left():
    my_turtle.left(360/sides)
for i in range(sides):
    move_forward()
    turn_left()
    my_turtle.pencolor(colors[i])
turtle.done()