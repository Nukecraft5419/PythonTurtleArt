import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("#caf0f8")
window.title("Penguin")

t.speed(1)

# Setting the headposition  of turtle at angle 270 degree
t.setheading(270)
t.begin_fill()

# draws the penguin body
t.circle(50, 180)
t.forward(80)
t.circle(50, 180)
t.forward(80)
t.end_fill()

# Belly of penguin
t.fillcolor("white")
t.goto(10, 0)
t.begin_fill()
t.circle(40)
t.end_fill()

# Eyes of penguin
t.setheading(0)
t.goto(30, 80)
t.begin_fill()
t.circle(20)
t.end_fill()
t.goto(70, 80)
t.begin_fill()
t.circle(20)
t.end_fill()

# Eye  dot of penguins eye
t.shape("circle")
t.fillcolor("black")
t.penup()
t.goto(30, 100)
t.stamp()
t.goto(70, 100)
t.stamp()

# Nose of penguin
t.shape("triangle")
t.fillcolor("orange")

t.goto(50, 70)
t.setheading(270)
t.stamp()

# Hands of penguin
t.fillcolor("black")
t.pencolor("white")
t.setheading(180)
t.goto(0, 50)
t.stamp()
t.setheading(0)
t.goto(100, 50)
t.stamp()


# legs of penguin
t.shape("square")
t.fillcolor("orange")
t.goto(35, -50)
t.stamp()
t.goto(65, -50)
t.stamp()

t.hideturtle()
turtle.done()
