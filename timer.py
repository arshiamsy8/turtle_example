#IMPORTING_LIBRARIES_________________________________________star((
import datetime as dt
from time import *
from turtle import *
#IMPORTING_LIBRARIES___________________________________________end))


#FUNCTIONS___________________________________________________start((
def timerr(s , P_O_N , SH_O_N) :
    global ERROR_p_o_n
    global ERROR_second
    global ERROR_shape

    #check if the entered value in (P_O_N) is 'n' or 'y'
    if P_O_N != 'y' and P_O_N != 'n' :
        print(ERROR_p_o_n)
        return

    #check if the entered value in (SH_O_N) is 'n' or 'y'
    if SH_O_N != 'y' and SH_O_N != 'n' :
        print(ERROR_shape)
        return

    #check if the (P_O_N) is "str", make it a lowercase
    try :
        P_O_N = P_O_N.lower()
    #if (P_O_N) isn't "str" print an error
    except :
        print(ERROR_p_o_n)
        return

    #check if the (SH_O_N) is "str", make it a lowercase
    try :
        SH_O_N = SH_O_N.lower()
    #if (P_O_N) isn't "str" print an error
    except :
        print(ERROR_shape)
        return

    #make sure that (s) is an "intiger"
    try :
        s = int(s)
    #if (s) isn't an "intiger"
    except :
        print(ERROR_second)
        return

    #chek if the entered value in (s) is more than 1
    if s < 1 :
        print(ERROR_second)

    #if (SH_O_N) was 'y', draw a timer
    if SH_O_N == 'y' :
        speed(0)
        delay(0)

    #draw a second hand without a hour hand without the second hand
        clock()
        
    #draw a second hand for the timer wich is able to move
        player1 = Turtle()
        player1.shape("triangle")
        player1.shapesize(0.01 , 15 , 10)
        player1.left(90)

    #run the timer!
    for i in range(s) :
    #if the user wanted to print the seconds, print them
        if P_O_N == 'y' :
            print(i+1)
    #if the user wanted to run the shape clock, run it
        if SH_O_N == 'y' :
            player1.right(6)
    #when each 1 second pass, stop for 1 second
        sleep(1)

    #if the (SH_O_N) was 'y', wait 2 second before closing the drawing window
    if SH_O_N == 'y' :
        sleep(2)

def clock() :
    
    penup()
    goto(0 , -250)
    pendown()

    circle(250)

    penup()
    goto(0 , -10)
    pendown()

    penup()
    goto(0 , 0)
    pendown()

    for i in range(60) :
        left(i*6)

        penup()
        forward(250)
        pendown()

        backward(7)
        
        right(i*6)

        penup()
        goto(0 , 0)
        pendown()

    dot(30)
#FUNCTIONS_____________________________________________________end))


#MAIN________________________________________________________start((

#make a error massage for each error
#an error for when the (P_O_N) wasn't a "string" or wasn't 'n' or 'y'
ERROR_p_o_n = "\nError : please enter 'y' or 'n' in (P_O_N)\n"
#an error for when the (s) wasn't an "intiger" and it's more than 1
ERROR_second = "\nError : please enter a ((number)) bigger than '1' in (second)\n"
#an error for when the (SH_O_N) wasn't 'n' or 'y'
ERROR_shape = "\n Error : please enter 'y' or 'n' in (SH_O_N)\n"

s = input("how many seconds? ")
P_O_N = input("do you wanna print the seconds? ")
SH_O_N = input("do you wanna run the (shape_timer)? ")

timerr(s, P_O_N, SH_O_N)
#MAIN__________________________________________________________end))