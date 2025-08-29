# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import turtle

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
WIDTH = 800
HEIGHT = 600
BIG = 8

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# Setup the turtle environment
# =====> Add a comment to identify the data type of the argument
#        to the turtle.mode () subprogram
turtle.mode ("standard")
screen = turtle.Screen ()

# =====> Fix the NameError
screen.setup (WIDTH, HIGHT)
turtle.screensize (WIDTH, HEIGHT)

# Prepare the turtle
# =====> Fix the AttributeError
theTurtle = turtle.turtle ()                # Create a turtle
theTurtle.penup ()

# Draw grid lines
theTurtle.setpos (-200, 0)
theTurtle.setheading (0)

# =====> Fix the TypeError
theTurtle.pendown (200)
theTurtle.forward (400)
theTurtle.penup ()

# ====> Fix the logic error that causes the vertical axis to be
#       too far right
theTurtle.setpos (100, 200)
theTurtle.setheading (270)
theTurtle.pendown ()

# =====> Fix the logic error that causes the vertical axis
#        to be drawn too short
theTurtle.forward (100)
theTurtle.penup ()

# Draw a square
theTurtle.setpos (-200, -200)               # Lower left

# =====> Fix the logic error that makes the outside square
#        tilt left of the vertical axis
theTurtle.setheading (95)                   # Point north
theTurtle.pendown ()
for count in range (4):
    theTurtle.forward (400)                 # Side
    theTurtle.right (90)                    # Turn
theTurtle.penup ()

# Draw a circle
theTurtle.setpos (100, 0)                   # Right side of circle
theTurtle.setheading (90)                   # Point north

# ====> Add a line to set the size of the pen to the constant BIG


# =====> Add a line to set the colour of the pen to gold


theTurtle.pendown ()
theTurtle.circle (100)                      # Radius of 100
theTurtle.penup ()

# =====> Add a line to hide the turtle


print ("Be sure to close the turtle window.")
turtle.done ()
