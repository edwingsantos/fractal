def draw_triangle(pen, points, color):
    """
    Draw one filled triangle.
    """
    pen.fillcolor(color)

    pen.penup()
    pen.goto(points[0])
    pen.pendown()

    pen.begin_fill()
    pen.goto(points[1])
    pen.goto(points[2])
    pen.goto(points[0])
    pen.end_fill()


def midpoint(p1, p2):
    """
    Return midpoint between two points.
    """
    return ((p1[0] + p2[0]) / 2,
            (p1[1] + p2[1]) / 2)


def draw_sierpinski(pen, points, depth, color):
    """
    Recursive function.

    Base Case:
        depth == 0 → draw triangle

    Recursive Case:
        Split triangle into 3 smaller ones
    """

    if depth == 0:
        draw_triangle(pen, points, color)
    else:
        m1 = midpoint(points[0], points[1])
        m2 = midpoint(points[1], points[2])
        m3 = midpoint(points[0], points[2])

        draw_sierpinski(pen, [points[0], m1, m3], depth - 1, color)
        draw_sierpinski(pen, [points[1], m1, m2], depth - 1, color)
        draw_sierpinski(pen, [points[2], m2, m3], depth - 1, color)