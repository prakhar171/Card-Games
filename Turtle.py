#Turtle in Python
from turtle import *

pen1=Pen()
pen2=Pen()

#Setting Background Color
pen1.screen.bgcolor("#B51108")

pen1.color("#FFFFFF")
pen2.color("#532222")

pen2.up()
pen2.goto(-50,0)
pen2.down()
pen1.begin_fill()
pen1.circle(100)
pen1.end_fill()
pen2.write("KP",font=('Candara',75))

