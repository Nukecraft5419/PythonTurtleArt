import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("pink")  # background color
window.title("Spiral Shapes")  # title of the window

# set speed of the turtle
t.speed(20)
pattern = 0

for i in range(100):
    for color in ["blue", "green"]:
        t.color(color)
        t.forward(pattern)
        t.right(90)
        t.right(1)
        pattern += 1

t.hideturtle()
turtle.done()
