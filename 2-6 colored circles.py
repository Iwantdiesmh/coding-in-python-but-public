import turtle
h = turtle.Turtle()
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'red']

for i in range(36):
    i = -1
    s = 12
    h.penup()
    h.forward(200)
    for i in range(6):
        i += 1
        s -= 2
        h.color(colors[i])
        h.pendown()
        h.circle(s)
        h.penup()
        h.back(20)
    h.goto(0,0)
    h.right(10)
h.hideturtle()
