from turtle import*

#we want to paint house

#step 1:
penup()
goto(-450, -70)
pendown()

speed(0)
width(7)
color('green')
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
begin_fill()

#drawing a door

begin_fill()
forward(70)
color('black')
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(-250, 130)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#and

#add window

width(3)
penup()
goto(-250, 100)
pendown()

begin_fill()
color('blue')
left(30)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(-450, 60)
pendown()

begin_fill()
color('blue')
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

