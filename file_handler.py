"""
Handles saving the turtle screen as an image file.
"""


def save_image(screen):
    """
    Save the current turtle canvas as a .eps image file.
    """

    filename = input("Enter file name (without extension): ")

    canvas = screen.getcanvas()
    canvas.postscript(file=filename + ".eps")

    print(f"Image saved as {filename}.eps")