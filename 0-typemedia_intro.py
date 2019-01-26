# Print a string
print("Hello, TypeMedia")

# Make a variable called 'message' with the value 'Hello, TypeMedia'
message = "Hello, TypeMedia "
print(message * 3)


# Drawing shapes

# Make a variable for the bottom-left margins
# You can select the number, hold 'cmd' and drag to change it
offset = 100

# Draw an oval
# Syntax: oval(<x position>, <y position>, <width>, <height>)
oval(offset, offset, 400, 400)

# Change the fill colour to a random colour
# random() will give you a random number between 0 and 1
fill(random(), random(), random())

# Draw a rectangle
rect(offset + 100, offset + 100, 374, 500)

fill(random(), random(), random())

# Draw another oval
oval(offset, offset, 200, 200)

# Export the drawing (in the same folder as the script is saved)
saveImage("shapes.png")