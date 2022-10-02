from turtle import *
from random import *

speed(0)

bgcolor('black')

def lines(l_color) :

    pensize(3)
    color('white')

    left(90)
    forward(100)
    right(90)

    fillcolor(l_color)
    begin_fill()
    circle(50)
    end_fill()

penup()
goto(300 , -50)
pendown()

for i in range(20) :
    lines('blue')
    left(360/20)

penup()
goto(225 , -50)
pendown()

for j in range(15) :
    lines('red')
    left(360/15)

penup()
goto(150 , -50)
pendown()

for t in range(10) :
    lines('green')
    left(360/10)

penup()
goto(75 , -50)
pendown()

for f in range(5) :
    lines('yellow')
    left(360/5)

done()