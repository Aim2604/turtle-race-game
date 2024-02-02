import random
import turtle 

s = turtle.Screen()
s.bgcolor("light blue")
s.setup(1.0,1.0)
s.title("Turtle Race Game")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200,200)
t.pendown()

for i in range(1,11):
  t.write(i,font=('Arial',10))
  t.setheading(-90)
  t.forward(250)
  if i==10:
    t.write(" FINISH",font=('Arial',14))
  t.back(250)
  t.penup()
  t.setheading(0)
  t.forward(50)
  t.pendown()

finishLineX=250

def createTurtlePlayer(color,startx,starty):
  player=turtle.Turtle()
  player.color(color)
  player.shape("turtle")
  player.penup()
  player.goto(startx,starty)
  player.pendown()
  return player

p1=createTurtlePlayer('red',-210,150)
p2=createTurtlePlayer('blue',-210,100)
p3=createTurtlePlayer('orange',-210,50)
p4=createTurtlePlayer('green',-210,0)

while True:
  p1.forward(random.randint(5,10))
  if p1.pos()[0]>=finishLineX:
    p1.write(' I won the race!!',font=('Arial',10))
    break
  p2.forward(random.randint(5,10))
  if p2.pos()[0]>=finishLineX:
    p2.write(' I won the race!!',font=('Arial',10))
    break
  p3.forward(random.randint(5,10))
  if p3.pos()[0]>=finishLineX:
    p3.write('I won the race!!',font=('Arial',10))
  p4.forward(random.randint(5,10))
  if p4.pos()[0]>=finishLineX:
    p4.write('I wont the race!!',font=('Arial',10))