import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
m=36
h=0
for i in range(460):
    c=colorsys.hsv_to_rgb(h, 1, 0.5)
    h+=1/m
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(360)
        t.left(150)