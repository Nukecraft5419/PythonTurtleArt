import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")  # background color
window.title("Instagram Logo")  # title of the window

t.pencolor("blue")
t.width(23)
t.penup()
t.goto(160, -100)
t.pendown()
t.left(90)

for i in range(4):
    t.forward(250)
    t.circle(34, 90)
t.penup()
t.goto(85, 30)
t.pendown()
t.circle(80, 360)
t.penup()
t.goto(110, 130)
t.pendown()
t.circle(7, 360)

t.hideturtle()
turtle.done()
