from turtle import *
speed(0)

from random import *
speed(0)
bgcolor("black")
color("blue")
colors = ["red" , "blue" , "yellow" , "white" , "green" , "purple" , "pink" , "orange" , "brown" , "gold"]

for j in range(4) :

    x = randint(-500 , 500)
    y = randint(-300 , 300)

    penup()
    goto(x , y)
    pendown()

    for i in range(40) :
        a = randint(0, len(colors)-1)
        color(colors[a])
        forward(30)
        right(30)
        forward(20)
        left(50)
        forward(43)
        goto(x , y)
        right(20)
        left(9)

done()