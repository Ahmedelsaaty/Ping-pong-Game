import turtle
from typing import SupportsComplex
wind = turtle.Screen()
wind.title("ping pong by wzara")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)      #stop auto update

#block1
block1= turtle.Turtle()  #initialize turtle object(shape)
block1.speed(0) #set animation speed
block1.shape("square")
block1.color("blue")
block1.shapesize(stretch_wid=5,stretch_len=1) #block hight & width
block1.penup() #delete any line from turtle
block1.goto(-350,0)  


#block2
block2= turtle.Turtle()
block2.speed(0)
block2.shape("square")
block2.color("Red")
block2.shapesize(stretch_wid=5,stretch_len=1)
block2.penup()
block2.goto(350,0)


#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup() 
ball.goto(0,0)

ball.dx = .2
ball.dy = .2


#Score Sheet
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player1 : 0          Player2 : 0 " , align="center", font=("Courier",20,"normal"))





#Functions

def block1_up():
    y=block1.ycor()  #get Y Coordinate of block1
    y +=20           #icrease it with +20px for every step
    block1.sety(y)   #set y value is the newest value after adding +20px

def block1_down():
    y=block1.ycor()
    y -=20
    block1.sety(y)


def block2_up():
    y=block2.ycor()
    y +=20
    block2.sety(y)

def block2_down():
    y=block2.ycor()
    y -=20
    block2.sety(y)


#keyboard Bindings
wind.listen() #tell the window to expect the next step from keyboard
wind.onkeypress(block1_up,"w")
wind.onkeypress(block1_down,"s")

wind.listen()
wind.onkeypress(block2_up,"Up")
wind.onkeypress(block2_down,"Down") 









#main Game Loop
while True:
    wind.update()  #update screen every time  the  screen  run

    #ball movement
    ball.setx(ball.xcor() + ball.dx)  #all start from 0,0 and every time will increase .15 at X axis
    ball.sety(ball.ycor() + ball.dy)  #all start from 0,0 and every time will increase .15 at Y axis


    #Border Check , top border 300px , bottom border -300px, Ball is 20px already

    if ball.ycor() >290:     #if ball at top border
        ball.sety(290)       #set y coordinate +290 
        ball.dy *=-1         #reverse direction , making .15 -----> -.15


    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *=-1


    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *=-1
        score1 += 1
        score.clear()
        score.write("Player1 : {}          Player2 : {} " .format(score1,score2) , align="center", font=("Courier",20,"normal"))



    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        score.write("Player1 : {}          Player2 : {} " .format(score1,score2) , align="center", font=("Courier",20,"normal"))




    #Ball & blocks Collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < block2.ycor() + 40 and ball.ycor() > block2.ycor() -40) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < block1.ycor() + 40 and ball.ycor() > block1.ycor() -40) :
        ball.setx(-340)
        ball.dx *= -1






