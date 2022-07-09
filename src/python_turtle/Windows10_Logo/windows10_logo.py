# Import turtle package
import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")
window.title("Windows 10 Logo")

t.speed(1)
t.penup()
t.goto(-50, 60)
t.pendown()
t.color("blue")
t.begin_fill()
t.goto(100, 100)
t.goto(100, -100)

# Draw wondows
t.goto(-50, -60)
t.goto(-50, 60)
t.end_fill()
t.color("black")
t.goto(15, 100)

# cut 2 eequal parts
t.color("black")
t.width(10)
t.goto(15, -100)
t.penup()
t.goto(100, 0)
t.pendown()
t.goto(-100, 0)

t.hideturtle()
turtle.done()
