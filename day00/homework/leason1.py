from turtle import *


#we want to pait a house
shape("turtle")


#step 1: draw a square]
width(10)
color("blue")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
#end of square
#draw a door
left(90)
forward(70)
begin_fill()
color("red")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#end of door
#draw aroof
penup()
goto(200,200)
pendown()
color ("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof
#draw a Window
penup()
goto(0,150)
pendown()
color ("purple")
begin_fill()
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#end of window 1
#draw a window 2
penup()
goto(200,150)
pendown()
color ("purple")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of window 2
exitonclick()