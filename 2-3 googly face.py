import turtle

h = turtle.Turtle()
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
turtle.bgcolor('gray')

h.penup()
h.goto(0,-100)
h.pendown()
h.begin_fill()
h.color('green')
h.circle(150)
h.end_fill()


h.penup()
h.goto(-30,100)
h.pendown()
h.begin_fill()
h.color('white')
h.circle(30)
h.end_fill()
h.begin_fill()
h.color('black')
h.circle(20)
h.end_fill()

h.penup()
h.goto(30,100)
h.pendown()
h.begin_fill()
h.color('white')
h.circle(30)
h.end_fill()
h.begin_fill()
h.color('black')
h.circle(20)
h.end_fill()

h.penup()
h.goto(0,0)
h.pendown()
