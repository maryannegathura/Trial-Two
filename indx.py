import math
from turtle import *

def hearta(t):
    return 16 * math.sin(t) ** 3

def heartb(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

# Setup the turtle
speed(3)
bgcolor("black")
color("red")
pensize(2)
penup()

# Start drawing the heart shape
begin_fill()
for i in range(1000):
    t = i * 2 * math.pi / 1000  # Scale the loop variable to range from 0 to 2π
    x = hearta(t) * 20
    y = heartb(t) * 20
    goto(x, y)
    pendown()

end_fill()
penup()
goto(0, -200)  # Position the turtle away from the drawing
done()
