import turtle                               # allows us to use turtle library
wn = turtle.Screen()                        # allows us to create a graphics window
wn.bgcolor("blue")                          # sets gtaphics windows background color to blue
import math                                 # allows us to use math functions
quinn = turtle.Turtle()                     # sets up turtle quinn
quinn.setpos(0,0)
quinn.pensize(3)
quinn.up()


# drawing first circle middle
quinn.forward(70)
quinn.down()
quinn.left(90)

# calculation of cicumference of a circle
a = (math.pi*140.00/360)

#itineration for first circle
for i in range (1,361,1):
    quinn.left(a)
    quinn.forward (1)

# drawing second circle bottom
quinn.up()
quinn.home()
quinn.right(90)
quinn.forward(70)
quinn.left(90)
quinn.down()

b = (math.pi*200.00/360)

for i in range (1,361,1):
    quinn.right(b)
    quinn.forward(1)

# drawing third circle head top

quinn.up ()
quinn.goto(0,70)
quinn.right(90)
quinn.down()

c =(math.pi*80/360)

for i in range (1,361,1):
    quinn.left(c)
    quinn.forward(1)

wn.exitonclick()