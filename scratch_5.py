from turtle import Turtle, Screen
import turtle
def inside(point, poly):
    x, y = point

    x1 = min(p[0] for p in poly)
    y1 = min(p[1] for p in poly)
    x2 = max(p[0] for p in poly)
    y2 = max(p[1] for p in poly)

    return x1 < x < x2 and y1 < y < y2


def notsafe(turtle):
    position = turtle.position()
    return inside(position, circle) and not inside(position, redcross)

wn = Screen()
wn.bgcolor('lightgreen')
WIDTH = wn.window_width()

layout = Turtle(visible=False)
layout.speed('fastest')
layout.penup()
# turtle.shape("square")

x=15
def north(x):
    turtle.seth(90)
    turtle.forward(x)

def hitnorth():
    north(x)

def south(x):
    turtle.seth(270)
    turtle.forward(x)

def hitsouth():
    south(x)

def east(x):
    turtle.seth(0)
    turtle.forward(x)

def hiteast():
    east(x)

def west(x):
    turtle.seth(180)
    turtle.forward(x)

def hitwest():
    west(x)



def drawarena(turtle):
    turtle.up()
    # turtle.home()
    turtle.color("gray")
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.setx(0)
    turtle.sety(-300)
    turtle.down()
    turtle.circle(350, 360)
    turtle.end_fill()
    turtle.end_poly()

    return turtle.get_poly()

# drawarena(turtle)
circle = drawarena(layout)
def drawredcross (north, south, east, west):
    turtle.penup()
    north(175)
    turtle.down()
    turtle.color("red")
    turtle.begin_fill()
    turtle.begin_poly()
    east(60)
    west(120)
    north(120)
    west(120)
    north(120)
    east(120)
    north(120)
    east(120)
    south(120)
    east(120)
    south(120)
    west(120)
    south(120)
    turtle.end_fill()
    turtle.end_poly()

    return turtle.get_poly()



redcross = drawredcross(north, south, east, west)

wn.penup()
wn.goto(0,300)

notsafe(turtle)

wn.onkey(hitnorth, "Up")
wn.onkey(hitsouth, "Down")
wn.onkey(hiteast, "Right")
wn.onkey(hitwest, "Left")
wn.listen()



wn.exitonclick()
wn.mainloop()

