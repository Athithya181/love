import turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-75,130)
t.pendown()
t.color('white')
t.write("I love my friends",font=("Verdana",15,"bold"))

t.penup()
t.goto(75,-230)
t.pendown()
t.color('white')
t.write("creat by Adhithya",font=("Verdana",5,"bold"))

for i in range(400):
	t.color("red")
	t.circle(i)
	t.left(5)
	
turyle.done()
