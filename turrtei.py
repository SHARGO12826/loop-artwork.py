import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
    for x in range(360):
        t.pencolor(colors[x %len(colors)])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(59)
    t.right(59)
    for x in range(200,10,-1):
        t.pencolor(colors[x % len(colors)])
        t.width(x / 100 + 1)
        t.forward(x)
        t.right(59)
