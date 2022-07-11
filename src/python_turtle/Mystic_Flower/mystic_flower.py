import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")
window.title("Mystic Flower")

t.reset()
t.hideturtle()
t.speed(0)

c = 0
x = 0

colors = [

    # reddish colors
    (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.33)

    # orangey colors
    (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.05)

    # yellowy colors
    (1.00, 1.00, 0.00), (0.95, 1, 00, 0.00), (0.90, 1.00, 0.00)

    # greenish colors
    (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.22)

    # blueish colors
    (0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00)
]

while x < 1000:
    idx = int(c)
    color = colors[idx]
    t.color(color)
    t.forward(x)
    t.right(98)
    x = x + 1
    c = c + 0.1

t.hideturtle()
turtle.done()
