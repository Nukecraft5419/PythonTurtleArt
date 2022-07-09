# Import turtle package
import turtle

# get the instance of turtle
t = turtle.Turtle()

t.speed(0)

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")
window.title("Infinity Circle")

for i in range(15):
    for colors in ("red", "magenta", "blue", "cyan", "green", "yellow"):
        t.color(colors)
        t.pensize(3)
        t.left(4)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
t.hideturtle()
turtle.done()
