def save_fractal(screen):
    """
    Save turtle drawing as an image file.
    """

    canvas = screen.getcanvas()
    canvas.postscript(file="sierpinski_output.eps")

    print("Fractal image saved as sierpinski_output.eps")