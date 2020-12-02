import turtle
turtle.bgcolor('blue')
h = turtle.Turtle() #too lazy to type a long var for every line.

h.begin_fill()
h.color('gray')
for i in range(4):
    h.forward(100)
    h.left(90)
h.end_fill()
h.penup()
h.goto(-20,100)
h.pendown()

h.begin_fill()
h.color('red')
h.left(60)
h.forward(140)
h.right(120)
h.forward(140)
h.right(120)
h.forward(140)
h.end_fill()

h.penup()
h.goto(25,80)
h.pendown
h.begin_fill()
h.color('yellow')
for i in range(4):
    h.forward(20)
    h.left(90)
h.end_fill()
h.hideturtle()
