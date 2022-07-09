import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")  # set the Back Ground color
window.title("Cute Heart")

# set the pen size
t.pensize(4)
t.speed(10)

# Defining a method to draw curve


def drawcurve():
    for i in range(200):
        # Defining step by step curve motion
        t.right(1)
        t. forward(1)


# Set the fill color to pink and border color to Red
t.color("red", "pink")
# Start filling the color
t.begin_fill()
t.left(140)

# Draw the left line
t.forward(111.65)
# Draw the left curve
drawcurve()
t.left(120)
drawcurve()
# Draw the right line
t.forward(111.65)
# end_fill() : This method fills the polygon with the current fill color by closing it between the current position and the initial position.
t.end_fill()
t.penup()
t.goto(77, -40)
t.pendown()

t.hideturtle()
turtle.done()
