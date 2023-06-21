import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle 90 degrees to the right
t.right(90)

# Move the turtle forward by 100 units again
t.forward(100)

# Repeat the above two steps to complete the square
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# Close the turtle window when done
turtle.done()
