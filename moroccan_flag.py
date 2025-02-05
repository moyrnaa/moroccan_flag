# since 1915

import turtle as t 

screen = t.Screen()
screen.title("Moroccan flag")
screen.setup(width=600, height=400)
screen.bgcolor("red") # also t.
 
t.hideturtle()
t.penup()
t.goto(-105,45)
t.pendown()

t.pensize(8)
t.speed(0)
t.pencolor("green")

for i in range(5):
    t.forward(200)
    t.right(144)


t.done()
