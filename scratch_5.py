import turtle

turtle.shape("square")
x = []
turtle.speed(10)

def north(x):
    turtle.seth(90)
    turtle.forward(x)

def south(x):
    turtle.seth(270)
    turtle.forward(x)

def east(x):
    turtle.seth(0)
    turtle.forward(x)

def west(x):
    turtle.seth(180)
    turtle.forward(x)

turtle.begin_poly()

def arena():
    turtle.up()
    # turtle.home()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.setx(0)
    turtle.sety(-300)
    turtle.down()
    turtle.circle(350, 360)
    turtle.end_fill()
    # turtle.setx(30)
    # turtle.sety(30)



arena()

def redcross (north, south, east, west):
    turtle.penup()
    north(175)
    turtle.down()
    turtle.color("red")
    turtle.begin_fill()
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

redcross(north, south, east, west)

turtle.end_poly()
redcrosspic = turtle.get_poly()
turtle.register_shape("myfav", redcrosspic)
turtle.clear

# def size(redcross):




# north(x)
# east(x)
# west(x)
# south(x)
# redcross()
# turtle.exitonclick()