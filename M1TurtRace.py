from turtle import *
import random
speed(9)
penup()
goto(-140,140)
for step in range(11):
    write(step)
    right(90)
    forward(30)
    pendown()
    forward(250)
    penup()
    backward(280)
    left(90)
    forward(30)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

adb = Turtle()
adb.color('blue')
adb.shape('turtle')
adb.penup()
adb.goto(-160,50)
adb.pendown()

adc = Turtle()
adc.color('magenta')
adc.shape('turtle')
adc.penup()
adc.goto(-160,0)
adc.pendown()

add = Turtle()
add.color('yellow')
add.shape('turtle')
add.penup()
add.goto(-160,-50)
add.pendown()

for turn in range(100):
    ada.forward(random.randint(1,5))
    adb.forward(random.randint(1,5))
    adc.forward(random.randint(1,5))
    add.forward(random.randint(1,5))
