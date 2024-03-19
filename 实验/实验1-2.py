import turtle
turtle.circle(200,360)
angle = -45
for n in range (0,4):
    angle = angle+90
    turtle.seth(angle)
    turtle.forward(200*1.414)