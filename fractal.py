"""
Contains recursive fractal drawing functions.
"""


def draw_triangle(pen, points, color):
    """
    Draw a filled triangle using three coordinate points.
    """

    pen.fillcolor(color)
    pen.up()
    pen.goto(points[0])
    pen.down()
    pen.begin_fill()

    pen.goto(points[1])
    pen.goto(points[2])
    pen.goto(points[0])

    pen.end_fill()


def midpoint(p1, p2):
    """
    Return the midpoint between two coordinate points.
    """

    return (
        (p1[0] + p2[0]) / 2,
        (p1[1] + p2[1]) / 2
    )


def draw_sierpinski(pen, points, depth, color):
    """
    Recursive function to draw the Sierpinski Triangle.

    Base Case:
        If depth == 0, draw one triangle.

    Recursive Case:
        Divide the triangle into 3 smaller triangles
        and call the function again with depth - 1.
    """

    # Base Case
    if depth == 0:
        draw_triangle(pen, points, color)

    else:
        # Find midpoints of triangle sides
        m1 = midpoint(points[0], points[1])
        m2 = midpoint(points[1], points[2])
        m3 = midpoint(points[0], points[2])

        # Recursively draw 3 smaller triangles
        draw_sierpinski(pen, [points[0], m1, m3], depth - 1, color)
        draw_sierpinski(pen, [points[1], m1, m2], depth - 1, color)
        draw_sierpinski(pen, [points[2], m2, m3], depth - 1, color)