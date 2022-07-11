import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")  # background color
window.title("Facebook Logo")  # title of the window

t.speed(10)
t.color("#0270d6")

# setup the coordinates
t.penup()
t.goto(0, 150)
t.pendown()

# Draw the rectangle
t.begin_fill()
t.forward(150)
t.circle(-50, 90)
t.forward(300)
t.circle(-50, 90)
t.forward(300)
t.circle(-50, 90)
t.forward(300)
t.circle(-50, 90)
t.forward(150)
t.end_fill()

# drawing the letter F
t.color("white")
t.penup()
t.goto(140, 80)
t.pendown()

t.begin_fill()
t.right(180)
t.forward(50)
t.circle(80, 90)
t.forward(50)
t.right(90)
t.forward(80)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.right(90)
t.forward(160)
t.left(90)
t.forward(55)
t.left(90)
t.forward(160)
t.right(90)
t.forward(70)
t.left(80)
t.forward(45)
t.left(100)
t.forward(80)
t.right(90)
t.forward(40)
t.circle(-40, 90)
t.forward(40)
t.left(90)
t.forward(45)
t.end_fill()

t.hideturtle()
turtle.done()
