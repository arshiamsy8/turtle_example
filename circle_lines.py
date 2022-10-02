from turtle import *

speed(0)

def lines(side_size) :
    right(90)
    penup()
    forward(side_size/2)
    pendown()
    left(90)

    forward(side_size/2)
    left(180)
    forward(side_size)
    right(175)

    for j in range(2) :
        forward(side_size)
        left(360/3)

bgcolor("black")

for i in range(25) :
    color("yellow")
    lines(200)

done()