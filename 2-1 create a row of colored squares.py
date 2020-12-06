import turtle

shelly = turtle.Turtle()
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
shelly.pendown()
i = -1

for n in range(6):
    i += 1
    shelly.color(colors[i])
    for n in range(4):
        shelly.forward(20)
        shelly.left(90)
    shelly.penup()
    shelly.forward(30)
    shelly.pendown()
