# X and Y offsets of the rectangle
x = 100
y = 160

# How many frames should our animation be
frames = 60

# Everything in this loop will run once per frame
for frame in range(frames):
    
    # If we're less than halfway through the animation,
    # increase the X and Y offsets. Otherwise, decrease them.
    if frame < frames / 2:
        x += 10
        y += 15
    else:
        x -= 10
        y -= 15
    # Try changing the values above and see what happens
    
    # Make a new page (each page will be a frame in the gif)
    newPage(900, 900)
    
    # Draw the rectangle
    rect(x, y, 200, 200)

# Everything which is indented is part of the loop
# We want to run this next line at the end, not as part of the loop,
# So we're not indenting it.
saveImage('animation.gif')