import turtle
screen = turtle.Screen()
screen.screensize(1000,1000)
screen.bgcolor("tan")

t = turtle.Turtle()
#blue circle
t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.circle(35)

#black circle
t.penup()
t.goto(0,15)
t.pendown()
t.pencolor("black")
t.circle(35)

#yellow circle
t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor("yellow")
t.circle(35)

#green cricle
t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor("green")
t.circle(35)

#red circle
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor("red")
t.circle(35)
t.penup()

#text1
t.goto(0,100)
t.pencolor("purple")
t.write("Winter Olympics" , font=("Arial",30,"bold italic"),align='center')

#text2
t.goto(0,-100)
t.write("2026" , font=("Arial",30,"bold italic"),align='center')

turtle.done()