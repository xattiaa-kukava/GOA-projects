from turtle import *


#i want a house
speed(30)
width(5)

color("grey")
begin_fill()
forward(300)
left(90)

forward(300)
left(90)

forward(50)
left(90)

forward(200)
right(90)

forward(500)
right(90)

forward(200)
left(90)

forward(50)
left(90)

forward(300)
left(90)

forward(300)
end_fill()
#doors
color("purple")
begin_fill()
forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(180)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
end_fill()
penup()
goto(300, 300)
pendown()

#rooftop
color("brown")
begin_fill()
forward(25)
left(120)
forward(100)
left(120)

forward(100)
left(120)
forward(75)
end_fill()

penup()
goto(-300, 300)
pendown()

color("brown")
begin_fill()
forward(75)
left(120)
forward(100)
left(120)

forward(100)
left(120)

forward(25)
end_fill()
penup()
goto(-200, 100)
pendown()

color("maroon")
begin_fill()

left(30)
forward(240)
right(60)
forward(240)
right(150)
forward(410)
end_fill()




exitonclick()
