import turtle
import time
from random import randint, random
from time import sleep
import random
x = random.randint(3,5)
y = random.randint(1,2)


# field (screen setup)
mscreen = turtle.Screen()
mscreen.bgcolor('dark green')
mscreen.title('Fossball simulation')
mscreen.setup(1000,1000)
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
ball.showturtle()
ball.shape('circle')
ball.color('white')
ball.shapesize(.8)
ball.penup()
ball.goto(0,0)
ball.speed(0)
ball.dy= y
ball.dx= x


#Goal team 1 > right
goalN1 = turtle.Turtle()
goalN1.shape('square')
goalN1.color('white')
goalN1.shapesize(stretch_wid=10,stretch_len=.1)
goalN1.penup()
goalN1.goto(400,0)
goalN1.penup()

#Goal team 2 > left
goalN2 = turtle.Turtle()
goalN2.shape('square')
goalN2.color('white')
goalN2.shapesize(stretch_wid=10,stretch_len=.01)
goalN2.penup()
goalN2.goto(-430,0)
goalN2.penup()


#goalKeeper Team 1
line = turtle.Turtle()
line.penup()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.goto(350,-15)
line.penup()
goalKeeperT1 = turtle.Turtle()
goalKeeperT1.penup()
goalKeeperT1.shape('square')
goalKeeperT1.color('red')
goalKeeperT1.shapesize(stretch_wid=2,stretch_len=1)
goalKeeperT1.goto(350,-35)
goalKeeperT1.pu()


#goalKeeper Team 2
line = turtle.Turtle()
line.penup()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.goto(-385,-15)
goalKeeperT2 = turtle.Turtle()
goalKeeperT2.penup()
goalKeeperT2.shape('square')
goalKeeperT2.color('purple')
goalKeeperT2.shapesize(stretch_wid=2,stretch_len=1)
goalKeeperT2.goto(-385,-35)
goalKeeperT2.pu()


#defender Team 1
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(250,-15)
defenderT1D1 = turtle.Turtle()
defenderT1D1.penup()
defenderT1D1.shape('square')
defenderT1D1.color('red')
defenderT1D1.shapesize(stretch_wid=2,stretch_len=1)
defenderT1D1.goto(250,50)
defenderT1D2 = turtle.Turtle()
defenderT1D2.penup()
defenderT1D2.shape('square')
defenderT1D2.color('red')
defenderT1D2.shapesize(stretch_wid=2,stretch_len=1)
defenderT1D2.goto(250,-150)


#defender Team 2
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(-285,-15)
defenderT2D1 = turtle.Turtle()
defenderT2D1.penup()
defenderT2D1.shape('square')
defenderT2D1.color('purple')
defenderT2D1.shapesize(stretch_wid=2,stretch_len=1)
defenderT2D1.goto(-285,50)
defenderT2D2 = turtle.Turtle()
defenderT2D2.penup()
defenderT2D2.shape('square')
defenderT2D2.color('purple')
defenderT2D2.shapesize(stretch_wid=2,stretch_len=1)
defenderT2D2.goto(-285,-150)


#attackersT1 Team 1
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(-190,-15)
attackersT1A1 = turtle.Turtle()
attackersT1A1.penup()
attackersT1A1.shape('square')
attackersT1A1.color('red')
attackersT1A1.shapesize(stretch_wid=2,stretch_len=1)
attackersT1A1.goto(-190,-50)
attackersT1A2 = turtle.Turtle()
attackersT1A2.penup()
attackersT1A2.shape('square')
attackersT1A2.color('red')
attackersT1A2.shapesize(stretch_wid=2,stretch_len=1)
attackersT1A2.goto(-190,-150)
attackersT1A3 = turtle.Turtle()
attackersT1A3.penup()
attackersT1A3.shape('square')
attackersT1A3.color('red')
attackersT1A3.shapesize(stretch_wid=2,stretch_len=1)
attackersT1A3.goto(-190,50)


#attackersT2 Team 2
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(150,-15)
attackersT2A1 = turtle.Turtle()
attackersT2A1.penup()
attackersT2A1.shape('square')
attackersT2A1.color('purple')
attackersT2A1.shapesize(stretch_wid=2,stretch_len=1)
attackersT2A1.goto(150,-50)
attackersT2A2 = turtle.Turtle()
attackersT2A2.penup()
attackersT2A2.shape('square')
attackersT2A2.color('purple')
attackersT2A2.shapesize(stretch_wid=2,stretch_len=1)
attackersT2A2.goto(150,-150)
attackersT2A3 = turtle.Turtle()
attackersT2A3.penup()
attackersT2A3.shape('square')
attackersT2A3.color('purple')
attackersT2A3.shapesize(stretch_wid=2,stretch_len=1)
attackersT2A3.goto(150,50)



#medFieldT1 Team 1
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(60,-15)
medFieldT1D1 = turtle.Turtle()
medFieldT1D1.penup()
medFieldT1D1.shape('square')
medFieldT1D1.color('red')
medFieldT1D1.shapesize(stretch_wid=2,stretch_len=1)
medFieldT1D1.goto(60,100)
medFieldT1D2 = turtle.Turtle()
medFieldT1D2.penup()
medFieldT1D2.shape('square')
medFieldT1D2.color('red')
medFieldT1D2.shapesize(stretch_wid=2,stretch_len=1)
medFieldT1D2.goto(60,0)
medFieldT1D3 = turtle.Turtle()
medFieldT1D3.penup()
medFieldT1D3.shape('square')
medFieldT1D3.color('red')
medFieldT1D3.shapesize(stretch_wid=2,stretch_len=1)
medFieldT1D3.goto(60,-100)
medFieldT1D4 = turtle.Turtle()
medFieldT1D4.penup()
medFieldT1D4.shape('square')
medFieldT1D4.color('red')
medFieldT1D4.shapesize(stretch_wid=2,stretch_len=1)
medFieldT1D4.goto(60,-200)

#medFieldT2 Team 2
line = turtle.Turtle()
line.shape('square')
line.color('white')
line.shapesize(stretch_wid=30,stretch_len=.1)
line.penup()
line.goto(-70,-15)
medFieldT2D1 = turtle.Turtle()
medFieldT2D1.penup()
medFieldT2D1.shape('square')
medFieldT2D1.color('purple')
medFieldT2D1.shapesize(stretch_wid=2,stretch_len=1)
medFieldT2D1.goto(-70,100)
medFieldT2D2 = turtle.Turtle()
medFieldT2D2.penup()
medFieldT2D2.shape('square')
medFieldT2D2.color('purple')
medFieldT2D2.shapesize(stretch_wid=2,stretch_len=1)
medFieldT2D2.goto(-70,0)
medFieldT2D3 = turtle.Turtle()
medFieldT2D3.penup()
medFieldT2D3.shape('square')
medFieldT2D3.color('purple')
medFieldT2D3.shapesize(stretch_wid=2,stretch_len=1)
medFieldT2D3.goto(-70,-100)
medFieldT2D4 = turtle.Turtle()
medFieldT2D4.penup()
medFieldT2D4.shape('square')
medFieldT2D4.color('purple')
medFieldT2D4.shapesize(stretch_wid=2,stretch_len=1)
medFieldT2D4.goto(-70,-200)


#Goal scors
score_T1 = 0
score_T2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 300)
score.write("Red Player: 0  Blue Player: 0", align="center", font=("Courier", 24, "normal"))


while True:
   mscreen.update()
   ball.sety(ball.ycor()+ ball.dy)
   ball.setx(ball.xcor()+ball.dx)

   #check walls
   if ball.xcor() > 385:
      ball.dx *= -1
      ball.setx(385)
   if ball.xcor() < -415:
      ball.dx *= -1
      ball.setx(-415)
   #check flors
   if ball.ycor() > 190:
      ball.dy *= -1
      ball.sety(190)
   if ball.ycor() < -260:
      ball.dy *= -1
      ball.sety(-260)
   if defenderT1D1.xcor() < -415:
      defenderT1D1.dx *= -1
      defenderT1D1.setx(-415)
      print('die')

   #check collicion  for the team 1 Goal check
   if (ball.xcor() > 380 and ball.xcor() < 390)and (ball.ycor() < goalN1.ycor() + 90
   and ball.ycor() > goalN1.ycor() -90):
      time.sleep(1)
      ball.home()
      mscreen.update()
      score.clear()
      score_T1 += 1
      score.write("Red Player: {}  Blue Player: {}".format(score_T1, score_T2), align="center", font=("Courier", 24, "normal"))
     

   #check collicion  for the team 2 Goal check
   if (ball.xcor() < -410 and ball.xcor() > -420)and (ball.ycor() < goalN2.ycor() + 100
   and ball.ycor() > goalN2.ycor() -100):
      time.sleep(1)
      ball.home()
      mscreen.update()
      score.clear()
      score_T2 += 1
      score.write("Red Player: {}  Blue Player: {}".format(score_T1, score_T2), align="center", font=("Courier", 24, "normal"))
     

   #IF socre is 5 of any team wins and clear
   if (score_T1 >= 5 or score_T2 >= 5):
      score.clear()
      score_T1= 0
      score_T2= 0  
      score.write("Red Player: {}  Blue Player: {}".format(score_T1, score_T2), align="center", font=("Courier", 24, "normal"))
      mscreen.update()
      ball.home()
      

      
   #if ball hit player kick ball for all player in team 1
   if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < goalKeeperT1.ycor() + 30
   and ball.ycor() > goalKeeperT1.ycor() -30):
      ball.setx(340)
      ball.dx *= -1


      #defenderT1D1.goto(250,50)
   if (ball.xcor() > 240 and ball.xcor() < 250)and (ball.ycor() < defenderT1D1.ycor() + 30
   and ball.ycor() > defenderT1D1.ycor() -30):
      ball.setx(240)
      ball.dx *= -1
   if (ball.xcor() > 240 and ball.xcor() < 250)and (ball.ycor() < defenderT1D2.ycor() + 30
   and ball.ycor() > defenderT1D2.ycor() -30):
      ball.setx(240)
      ball.dx *= -1

      #medFieldT1D1.goto(60,100)
   if (ball.xcor() > 50 and ball.xcor() < 60)and (ball.ycor() < medFieldT1D1.ycor() + 30
   and ball.ycor() > medFieldT1D1.ycor() -30):
      ball.setx(50)
      ball.dx *= -1
   if (ball.xcor() > 50 and ball.xcor() < 60)and (ball.ycor() < medFieldT1D2.ycor() + 30
   and ball.ycor() > medFieldT1D2.ycor() -30):
      ball.setx(50)
      ball.dx *= -1
   if (ball.xcor() > 50 and ball.xcor() < 60)and (ball.ycor() < medFieldT1D3.ycor() + 30
   and ball.ycor() > medFieldT1D3.ycor() -30):
      ball.setx(50)
      ball.dx *= -1
   if (ball.xcor() > 50 and ball.xcor() < 60)and (ball.ycor() < medFieldT1D4.ycor() + 40
   and ball.ycor() > medFieldT1D4.ycor() -40):
      ball.setx(50)
      ball.dx *= -1

     # attackersT1A1.goto(-190,-50)
   if (ball.xcor() > -190 and ball.xcor() < -180)and (ball.ycor() < attackersT1A1.ycor() + 30
   and ball.ycor() > attackersT1A1.ycor() -30):
      ball.setx(-190)
      ball.dx *= -1
      print("done")
   if (ball.xcor() > -190 and ball.xcor() < -180)and (ball.ycor() < attackersT1A2.ycor() + 30
   and ball.ycor() > attackersT1A2.ycor() -30):
      ball.setx(-190)
      ball.dx *= -1
   if (ball.xcor() > -190 and ball.xcor() < -180)and (ball.ycor() < attackersT1A3.ycor() + 30
   and ball.ycor() > attackersT1A3.ycor() -30):
      ball.setx(-190)
      ball.dx *= -1
      
   #if ball hit player kick ball for all player in team 2
   if (ball.xcor() < -375 and ball.xcor() > -385)and (ball.ycor() < goalKeeperT2.ycor() + 50
   and ball.ycor() > goalKeeperT2.ycor() -50):
      ball.setx(-375)
      ball.dx *= -1

   #defenderT2D1.goto(-285,50)
   if (ball.xcor() < -275 and ball.xcor() > -285)and (ball.ycor() < defenderT2D1.ycor() + 30
   and ball.ycor() > defenderT2D1.ycor() -30):
      ball.setx(-275)
      ball.dx *= -1
   if (ball.xcor() > -275 and ball.xcor() < -285)and (ball.ycor() < defenderT2D2.ycor() + 30
   and ball.ycor() > defenderT2D2.ycor() -30):
      ball.setx(-275)
      ball.dx *= -1

     #medFieldT2D1.goto(-70,100)
   if (ball.xcor() < -60 and ball.xcor() > -70)and (ball.ycor() < medFieldT1D1.ycor() + 30
   and ball.ycor() > medFieldT1D1.ycor() -30):
      ball.setx(-60)
      ball.dx *= -1
   if (ball.xcor() < -60 and ball.xcor() > -70)and (ball.ycor() < medFieldT2D2.ycor() + 30
   and ball.ycor() > medFieldT2D2.ycor() -30):
      ball.setx(-60)
      ball.dx *= -1
   if (ball.xcor() < -60 and ball.xcor() > -70)and (ball.ycor() < medFieldT2D3.ycor() + 30
   and ball.ycor() > medFieldT2D3.ycor() -30):
      ball.setx(-60)
      ball.dx *= -1
   if (ball.xcor() < -60 and ball.xcor() > -70)and (ball.ycor() < medFieldT2D4.ycor() + 40
   and ball.ycor() > medFieldT2D4.ycor() -40):
      ball.setx(-60)
      ball.dx *= -1

     # attackersT2A1.goto(150,-50)
   if (ball.xcor() < 150 and ball.xcor() > 140)and (ball.ycor() < attackersT2A1.ycor() + 30
   and ball.ycor() > attackersT2A1.ycor() -30):
      ball.setx(150)
      ball.dx *= -1
      print("done")
   if (ball.xcor() < 150 and ball.xcor() > 140)and (ball.ycor() < attackersT2A2.ycor() + 30
   and ball.ycor() > attackersT2A2.ycor() -30):
      ball.setx(150)
      ball.dx *= -1
   if (ball.xcor() < 150 and ball.xcor() > 140)and (ball.ycor() < attackersT2A3.ycor() + 30
   and ball.ycor() > attackersT2A3.ycor() -30):
      ball.setx(150)
      ball.dx *= -1










   def up():
      a = goalKeeperT1.ycor()
      b = defenderT1D1.ycor()
      c = defenderT1D2.ycor()
      d = medFieldT1D1.ycor()
      e = medFieldT1D2.ycor()
      f = medFieldT1D3.ycor()
      g = medFieldT1D4.ycor()
      h = attackersT1A1.ycor()
      i = attackersT1A2.ycor()
      j = attackersT1A3.ycor()
      a += 40
      b += 40
      c += 40
      d += 10
      e += 10
      f += 10
      g += 10
      h += 30
      i += 30
      j += 30
      goalKeeperT1.sety(a)
      defenderT1D1.sety(b)
      defenderT1D2.sety(c)
      medFieldT1D1.sety(d)
      medFieldT1D2.sety(e)
      medFieldT1D3.sety(f)
      medFieldT1D4.sety(g)
      attackersT1A1.sety(h)
      attackersT1A2.sety(i)
      attackersT1A3.sety(j)
      
   def down():
      a = goalKeeperT1.ycor()
      b = defenderT1D1.ycor()
      c = defenderT1D2.ycor()
      d = medFieldT1D1.ycor()
      e = medFieldT1D2.ycor()
      f = medFieldT1D3.ycor()
      g = medFieldT1D4.ycor()
      h = attackersT1A1.ycor()
      i = attackersT1A2.ycor()
      j = attackersT1A3.ycor()
      a -= 40
      b -= 40
      c -= 40
      d -= 10
      e -= 10
      f -= 10
      g -= 10
      h -= 30
      i -= 30
      j -= 30
      goalKeeperT1.sety(a)
      defenderT1D1.sety(b)
      defenderT1D2.sety(c)
      medFieldT1D1.sety(d)
      medFieldT1D2.sety(e)
      medFieldT1D3.sety(f)
      medFieldT1D4.sety(g)
      attackersT1A1.sety(h)
      attackersT1A2.sety(i)
      attackersT1A3.sety(j)
   def upT2():
      a = goalKeeperT2.ycor()
      b = defenderT2D1.ycor()
      c = defenderT2D2.ycor()
      d = medFieldT2D1.ycor()
      e = medFieldT2D2.ycor()
      f = medFieldT2D3.ycor()
      g = medFieldT2D4.ycor()
      h = attackersT2A1.ycor()
      i = attackersT2A2.ycor()
      j = attackersT2A3.ycor()
      a += 40
      b += 40
      c += 40
      d += 10
      e += 10
      f += 10
      g += 10
      h += 30
      i += 30
      j += 30
      goalKeeperT2.sety(a)
      defenderT2D1.sety(b)
      defenderT2D2.sety(c)
      medFieldT2D1.sety(d)
      medFieldT2D2.sety(e)
      medFieldT2D3.sety(f)
      medFieldT2D4.sety(g)
      attackersT2A1.sety(h)
      attackersT2A2.sety(i)
      attackersT2A3.sety(j)
      
   def downT2():
      a = goalKeeperT2.ycor()
      b = defenderT2D1.ycor()
      c = defenderT2D2.ycor()
      d = medFieldT2D1.ycor()
      e = medFieldT2D2.ycor()
      f = medFieldT2D3.ycor()
      g = medFieldT2D4.ycor()
      h = attackersT2A1.ycor()
      i = attackersT2A2.ycor()
      j = attackersT2A3.ycor()
      a -= 40
      b -= 40
      c -= 40
      d -= 10
      e -= 10
      f -= 10
      g -= 10
      h -= 30
      i -= 30
      j -= 30
      goalKeeperT2.sety(a)
      defenderT2D1.sety(b)
      defenderT2D2.sety(c)
      medFieldT2D1.sety(d)
      medFieldT2D2.sety(e)
      medFieldT2D3.sety(f)
      medFieldT2D4.sety(g)
      attackersT2A1.sety(h)
      attackersT2A2.sety(i)
      attackersT2A3.sety(j)
   



   mscreen.onkeypress(up, "Up")
   mscreen.onkeypress(down, "Down")
   mscreen.onkeypress(upT2, "q")
   mscreen.onkeypress(downT2, "a")
   mscreen.listen()





















