import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("white")  # background color
window.title("Google Chrome Logo")  # title of the window

radius = 120

# heading position -150 is opposite of 150 degree angle
t.setheading(-150)
t.penup()

# -Red shape of the Chrome Logo
t.color("red")
t.begin_fill()
t.forward(radius)
t.pendown()

# set the angle to 90
t.right(90)
t.circle(-radius, 120)

# forward distance is equal to 180
t.forward(radius*3**.5)
t.left(120)

# draw the circle angle 120 and radius of 240
t.circle(2*radius, 120)
t.left(60)
t.forward(radius*3**.5)
t.end_fill()

# |-------------[ ● Green ● ]-------------|

t.left(180)
t.color("green")
t.begin_fill()
t.forward(radius*3**.5)
t.left(120)
t.circle(2*radius, 120)
t.left(60)
t.forward(radius*3**.5)
t.left(180)
t.circle(-radius, 120)
t.end_fill()

# |-------------[ ● Yellow ● ]-------------|

t.left(180)
t.circle(radius, 120)
t.color("yellow")
t.begin_fill()
t.circle(radius, 120)
t.right(180)
t.forward(radius*3**.5)
t.right(60)
t.circle(-2*radius, 120)
t.right(120)
t.forward(radius*3**.5)
t.end_fill()

# |-------------[ ● Blue Circle ● ]-------------|

t.penup()
t.left(98)
t.forward(radius/20)
t.setheading(60)
t.color("blue")
t.pendown()
t.begin_fill()
t.circle(t.distance(0, 0))
t.end_fill()

t.hideturtle()
turtle.done()
