import turtle
import time
from random import randint, random
from time import sleep
import random
x = random.randint(-100,100)
y = random.randint(-100,100)


# field (screen setup)
mscreen = turtle.Screen()
mscreen.bgcolor('dark green')
mscreen.title('Fossball simlitor')
mscreen.setup(1000,700)
mscreen.tracer(0)
#borders
l = turtle.Turtle()
l.hideturtle()
l.speed(10)
l.color("white")
l.pensize(2)
l.goto(0,0)
l.setheading(90)
l.forward(200)
l.left(90)
l.forward(430)
l.left(90)
l.forward(470)
l.left(90)
l.forward(830)
l.left(90)
l.forward(470)
l.left(90)
l.forward(400)
l.left(90)
l.forward(470)
l.penup()
l.hideturtle()
#borders ends

#Goal border
l.setpos(70,-35)
l.right(90)
l.forward(400)
l.penup()
l.forward(100)
l.pendown()
l.right(90)
l.forward(135)
l.right(90)
l.forward(100)
l.right(90)
l.forward(265)
l.right(90)
l.forward(100)
l.penup()
l.setpos(-90,-35)
l.pendown()
l.right(180)
l.penup()
l.forward(390)
l.penup()
l.forward(100)
l.pendown()
l.left(90)
l.forward(135)
l.left(90)
l.forward(100)
l.left(90)
l.forward(265)
l.left(90)
l.forward(100)
l.penup() 

      
    

       
# start circle
cir = turtle.Turtle()
cir.hideturtle()
cir.speed(100)

cir.right(90)
cir.penup()
cir.forward(90)
cir.pendown()
cir.left(90)
cir.pensize(2)
cir.color('white')
cir.circle(50)
cir.penup() 


#ball
ball = turtle.Turtle()
ball.hideturtle()
ball.penup()
ball.speed(50)
ball.showturtle()
ball.shape('circle')
ball.color('white')
ball.shapesize(.8)
ball.goto(0,0)
ball.speed(2)

ball.dy= 4.5
ball.dx= 3
ball.penup() 

   
 
#Goal team 1 > right 
goalN1 = turtle.Turtle()
goalN1.shape('square')
goalN1.color('white')
goalN1.shapesize(stretch_wid=10,stretch_len=.1)
goalN1.penup()
goalN1.goto(400,-35)
goalN1.penup()
#Goal team 2 > right 
goalN2 = turtle.Turtle()
goalN2.shape('square')
goalN2.color('white')
goalN2.shapesize(stretch_wid=10,stretch_len=.1)
goalN2.penup()
goalN2.goto(-430,-35)
goalN2.penup() 


 
#goalKeeper Team 1
goalKeeperT1 = turtle.Turtle()
goalKeeperT1.penup()
goalKeeperT1.shape('square')
goalKeeperT1.color('white')
goalKeeperT1.shapesize(stretch_wid=2,stretch_len=1)
goalKeeperT1.goto(350,-15)
goalKeeperT1.pu()
line = turtle.Turtle()
line.penup()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.goto(350,-15)
line.penup()


#goalKeeper Team 2
goalKeeperT2 = turtle.Turtle()
goalKeeperT2.penup()
goalKeeperT2.shape('square')
goalKeeperT2.color('white')
goalKeeperT2.shapesize(stretch_wid=2,stretch_len=1)
goalKeeperT2.goto(385,-15)
goalKeeperT2.pu()
line = turtle.Turtle()
line.penup()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.goto(-385,-15)
goalKeeperT2.goto(-385,-15)
goalKeeperT2.penup()
#defender Team 1
defenderT1D1 = turtle.Turtle()
defenderT1D1.penup()
defenderT1D1.shape('square')
defenderT1D1.color('white')
defenderT1D1.shapesize(stretch_wid=2,stretch_len=1)
defenderT1D1.goto(250,0)
defenderT1D2 = turtle.Turtle()
defenderT1D2.penup()
defenderT1D2.shape('square')
defenderT1D2.color('white')
defenderT1D2.shapesize(stretch_wid=2,stretch_len=1)
defenderT1D2.goto(250,-150)
defenderT1D3 = turtle.Turtle()
defenderT1D3.penup()
defenderT1D3.shape('square')
defenderT1D3.color('white')
defenderT1D3.shapesize(stretch_wid=2,stretch_len=1)
defenderT1D3.goto(250,150)
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(250,-15)

#defender Team 2
defenderT2D1 = turtle.Turtle()
defenderT2D1.penup()
defenderT2D1.shape('square')
defenderT2D1.color('white')
defenderT2D1.shapesize(stretch_wid=2,stretch_len=1)
defenderT2D1.goto(-285,0)
defenderT2D2 = turtle.Turtle()
defenderT2D2.penup()
defenderT2D2.shape('square')
defenderT2D2.color('white')
defenderT2D2.shapesize(stretch_wid=2,stretch_len=1)
defenderT2D2.goto(-285,-150)
defenderT2D3 = turtle.Turtle()
defenderT2D3.penup()
defenderT2D3.shape('square')
defenderT2D3.color('white')
defenderT2D3.shapesize(stretch_wid=2,stretch_len=1)
defenderT2D3.goto(-285,150)
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(-285,-15)
#attackersT1 Team 1
attackersT1 = turtle.Turtle()
attackersT1.shape('square')
attackersT1.color('white')
attackersT1.shapesize(stretch_wid=30,stretch_len=.1)
attackersT1.penup()
attackersT1.goto(-190,-15)
attackersT1.penup()
#attackersT2 Team 2
attackersT2 = turtle.Turtle()
attackersT2.shape('square')
attackersT2.color('white')
attackersT2.shapesize(stretch_wid=30,stretch_len=.1)
attackersT2.penup()
attackersT2.goto(150,-15)
attackersT2.penup()
#medFieldT1 Team 1
medFieldT1 = turtle.Turtle()
medFieldT1.shape('square')
medFieldT1.color('white')
medFieldT1.shapesize(stretch_wid=30,stretch_len=.1)
medFieldT1.penup()
medFieldT1.goto(60,-15)
medFieldT1.penup()
#medFieldT2 Team 2
medFieldT2 = turtle.Turtle()
medFieldT2.shape('square')
medFieldT2.color('white')
medFieldT2.shapesize(stretch_wid=30,stretch_len=.1)
medFieldT2.penup()
medFieldT2.goto(-70,-15)
medFieldT2.penup()











   
while True:
    
    i = 0
 

    mscreen.update()
    ball.sety(ball.ycor()+ ball.dy)
    ball.setx(ball.xcor()+ball.dx)

    
#check walls    
    if ball.xcor() > 385:
        ball.dx *= -1
    if ball.xcor() < -415:
        ball.dx *= -1
        #check flors
    if ball.ycor() > 190:
        ball.dy *= -1
    if ball.ycor() < -260:

        ball.dy *= -1
    
    


        #check collicion


    if (ball.xcor() > 380 and ball.xcor() < 390)and (ball.ycor() < goalN1.ycor() + 100
    and ball.ycor() > goalN1.ycor() -100):
        
        ball.dx *= -1
       
           
        print("done")
    if (ball.xcor() < -410 and ball.xcor() > -420)and (ball.ycor() < goalN2.ycor() + 100
    and ball.ycor() > goalN2.ycor() -100):
       
        ball.dx *= -1
       
           
        print("done1")


    if (ball.xcor() > 330 and ball.xcor() < 340)and (ball.ycor() < goalKeeperT1.ycor() + 300
    and ball.ycor() > goalKeeperT1.ycor() + 220):
        
        ball.dx *= -1
       
           
        print("done2")





    def up():
            c  = goalKeeperT1.ycor()
            y  = defenderT1D1.ycor()
            x  = defenderT1D2.ycor()
            z  = defenderT1D3.ycor()
            y += 20
            c += 20
            x += 20
            z += 20
            goalKeeperT1.sety(c)
            defenderT1D1.sety(y)
            defenderT1D2.sety(x)
            defenderT1D3.sety(z)
            print("e")
    def down():
        
            c  = goalKeeperT1.ycor()
            y  = defenderT1D1.ycor()
            x  = defenderT1D2.ycor()
            z  = defenderT1D3.ycor()
            y -= 20
            c -= 20
            x -= 20
            z -= 20
            goalKeeperT1.sety(c)
            defenderT1D1.sety(y)
            defenderT1D2.sety(x)
            defenderT1D3.sety(z)
            print("e")
    def down2():
        
            c  = goalKeeperT2.ycor()
            y  = defenderT2D1.ycor()
            x  = defenderT2D2.ycor()
            z  = defenderT2D3.ycor()
            y -= 5
            c -= 5
            x -= 5
            z -= 5
            goalKeeperT2.sety(c)
            defenderT2D1.sety(y)
            defenderT2D2.sety(x)
            defenderT2D3.sety(z)
            print("e")
    mscreen.onkey(up, "Up")
    mscreen.onkey(down, "Down")
    mscreen.onkey(down2, "w")
    mscreen.listen()


















 

