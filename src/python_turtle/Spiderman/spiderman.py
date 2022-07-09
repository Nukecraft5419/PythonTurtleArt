# Import turtle package
import turtle

# Set the turtle object
t = turtle.Turtle()

window = turtle.Screen()
window.setup(width=700, height=700)
window.bgcolor("red")
window.title("SpiderMan Logo")

# draw the head
t.goto(0, 0)
t.begin_fill()
t.circle(20)
t.end_fill()

# draw the body
t.penup()
t.setheading(270)
t.left(60)
t.pendown()
t.begin_fill()
t.forward(20)
t.right(80)
t.forward(70)
t.right(147)
t.forward(70)
t.right(80)
t.forward(20)
t.penup()
t.end_fill()

# right upper first upper leg
t.pendown()
t.goto(10, 35)
t.pendown()
t.begin_fill()
t.left(20)
t.forward(25)
t.right(60)
t.forward(50)
t.left(120)
t.forward(80)
t.right(175)
t.forward(95)
t.right(127)
t.forward(63)
t.left(60)
t.forward(18)
t.end_fill()

# right upper second leg

t.pendown()
t.goto(13, 25)
t.pendown()
t.begin_fill()
t.left(90)
t.left(90)
t.forward(20)
t.right(60)
t.forward(80)
t.left(125)
t.forward(130)
t.right(175)
t.forward(145)
t.right(128)
t.forward(95)
t.left(60)
t.forward(20)
t.end_fill()
t.penup()

# left first upper leg of the spider
t.pendown()
t.goto(-10, 35)
t.pendown()
t.begin_fill()
t.right(80)
t.forward(25)
t.left(60)
t.forward(50)
t.right(120)
t.forward(80)
t.left(175)
t.forward(95)
t.left(127)
t.forward(63)
t.right(60)
t.forward(18)
t.end_fill()

# left second upper leg of the spider
t.pendown()
t.goto(-13, 25)
t.pendown()
t.begin_fill()
t.right(90)
t.right(90)
t.forward(20)
t.left(60)
t.forward(80)
t.right(125)
t.forward(130)
t.left(175)
t.forward(145)
t.left(128)
t.forward(95)
t.right(60)
t.forward(20)
t.end_fill()
t.penup

# right first lower leg of spider
t.pendown()
t.goto(15, 12)
t.left(60)
t.begin_fill()
t.forward(20)
t.right(40)
t.forward(95)
t.right(100)
t.forward(135)
t.right(175)
t.forward(120)
t.left(90)
t.forward(80)
t.left(40)
t.forward(20)
t.end_fill()

# right second lower leg of the spider
t.pendown()
t.goto(11, 8)
t.left(150)
t.begin_fill()
t.forward(25)
t.right(10)
t.forward(65)
t.right(95)
t.forward(70)
t.right(175)
t.forward(60)
t.left(85)
t.forward(65)
t.left(15)
t.forward(15)
t.end_fill()

# left lower first leg of the spider
t.pendown()
t.goto(-15, 14)
t.right(3)
t.begin_fill()
t.forward(20)
t.left(40)
t.forward(95)
t.left(100)
t.forward(135)
t.left(175)
t.forward(120)
t.right(90)
t.forward(80)
t.right(40)
t.forward(20)
t.end_fill()
t.penup()

# left lower second leg of the spider
t.pendown()
t.goto(-11, 8)
t.right(90)
t.right(60)
t.begin_fill()
t.forward(25)
t.left(10)
t.forward(65)
t.left(95)
t.forward(70)
t.left(175)
t.forward(60)
t.right(85)
t.forward(65)
t.right(15)
t.forward(15)
t.end_fill()

t.hideturtle()
turtle.done()
