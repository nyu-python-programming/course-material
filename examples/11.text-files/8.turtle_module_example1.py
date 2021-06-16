import turtle
import random

turtle.color('red', 'yellow') # set the stroke to red and the fill to yellow

turtle.begin_fill() # turns on the fill

# draw four lines at right angles
for i in range(4):
    turtle.forward(200) # move the turtle forward 200 pixels (i.e dots on the screen)
    turtle.left(90) # rotate the turtle to the left by 90 degrees

turtle.end_fill() # draw the fill

# turn off the stroke drawing temporarily
turtle.penup()

# move the turtle backwards by 600 pixels
turtle.backward(300)

turtle.fillcolor('blue')
turtle.begin_fill() # start filling again
turtle.pendown() # start drawing the stroke again

# draw four lines at right angles
for i in range(4):
    turtle.forward(200) # move the turtle forward 200 pixels (i.e dots on the screen)
    turtle.right(90) # rotate the turtle to the left by 90 degrees

turtle.end_fill() # draw the fill

for i in range(100):
    turtle.color('green')
    rand_movement = random.randint(0, 500) - 250
    rand_rotate = random.randint(0, 180)
    turtle.forward(rand_movement)
    turtle.left(rand_rotate)


turtle.done() # tell the turtle module we're done moving the turtle
