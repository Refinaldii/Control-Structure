import turtle

# Setup turtle window
t = turtle.Turtle()
turtle.bgcolor("lightblue")
t.speed(5)

# Function to draw rectangle
def draw_rectangle(length, width, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()

# Function to draw a circle (wheel)
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Drawing the tank body
t.penup()
t.goto(-100, -50)  # Start position for tank body
t.pendown()
draw_rectangle(200, 50, "green")

# Drawing tank wheels using loop
t.penup()
t.goto(-90, -50)
t.pendown()
for _ in range(4):  # Draw 4 wheels in a row
    draw_circle(15, "black")
    t.penup()
    t.forward(50)
    t.pendown()

# Drawing tank turret
t.penup()
t.goto(-50, 0)
t.pendown()
draw_rectangle(100, 30, "green")

# Drawing tank gun
t.penup()
t.goto(50, 10)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(60)  # Length of gun barrel
t.left(90)
t.forward(10)
t.left(90)
t.forward(60)
t.left(90)
t.forward(10)
t.left(90)
t.end_fill()

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()