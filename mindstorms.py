import turtle

def draw_square(turtle):
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)

def draw_circle(turtle):
    turtle.circle(50)

def draw_triangle(turtle):
    for i in range(0,3):
        turtle.forward(100)
        turtle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("#293275")

    turtleOne = turtle.Turtle()
    turtleOne.shape("circle")
    turtleOne.color("#00afb4")
    turtleOne.speed(2)

    draw_square(turtleOne)

    turtleOne.shape("arrow")
    turtleOne.color("#ff7301")

    draw_circle(turtleOne)

    turtleOne.shape("turtle")
    turtleOne.color("yellow")
    turtleOne.left(180)

    draw_triangle(turtleOne)

    window.exitonclick()

def draw_circle_of_squares():
    window = turtle.Screen()
    window.bgcolor("#293275")

    turtleOne = turtle.Turtle()
    turtleOne.shape("circle")
    turtleOne.color("#00afb4")
    turtleOne.speed(0)

    for i in range(0,72):
        draw_square(turtleOne)
        turtleOne.right(5)

    window.exitonclick()

draw_circle_of_squares()
draw_art()