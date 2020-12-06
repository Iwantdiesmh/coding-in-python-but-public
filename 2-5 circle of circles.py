import turtle
h = turtle.Turtle()
for i in range(36):
    h.penup()
    h.forward(200)
    for i in range(6):
        h.pendown()
        h.circle(5)
        h.penup()
        h.back(20)
    h.goto(0,0)
    h.right(10)
h.hideturtle()
