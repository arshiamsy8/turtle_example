from turtle import *
speed(0)

bgcolor("black") 
colors = ["blue" , "green" , "red"]

for i in range(100) :

    color(colors[i % 3])
    forward((i+1)*5)
    right((360/3)-1)

done()