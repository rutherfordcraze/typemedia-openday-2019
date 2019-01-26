# Make a UI with some variables
# More info about these: http://www.drawbot.com/content/variables.html
Variable([
    dict(name="w", ui="Slider"),
    dict(name="h", ui="Slider")
    ], globals())

# X and Y offset of the rectangle
offset = 100

# Make a new artboard / page with dimensions 700x700 (default 1000x1000)
newPage(700,700)

# Draw a rectangle with width and height controlled by the sliders
rect(offset, offset, w * 5, h * 5)
# (slider values are between 0 and 100 by default, so we're
# multiplying them by 5 here.)