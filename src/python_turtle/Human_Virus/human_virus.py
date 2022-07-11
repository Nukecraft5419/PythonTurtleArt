import turtle

# get the instance of turtle
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("black")  # background color
window.title("Human Virus")  # title of the window

t.pencolor("cyan")  # Pencolor set to black
t.speed(0)
t.penup()
t.goto(0, 200)  # position of the turtle
t.pendown()

# Intialization of variables
forDis = 0
dR = 0

while(True):
    t.forward(forDis)
    t.right(dR)
    forDis += 3  # forDis increased by 3 on every iteration
    dR += 1  # right angle distance increased by 1 on every iteration
    # If the distance for right angle becomes 210 the loop breaks
    if dR == 210:
        break
        # Hide the turtle on completion of loop
    t.hideturtle()

t.hideturtle()
turtle.done()
