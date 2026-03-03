import turtle
import fractal
import save_image


def safe_color(screen, color_name, default="black"):
    """
    Try to apply a color.
    If invalid, return default color.
    """
    try:
        screen.bgcolor(color_name)
        return color_name
    except turtle.TurtleGraphicsError:
        print("Invalid color. Using", default)
        return default


def main():

    print("Welcome to the Sierpinski Triangle Generator!")
    print("This program creates a Sierpinski Triangle using recursion.\n")

    depth = int(input("Enter recursion depth (1-5): "))
    while depth < 1 or depth > 5:
        depth = int(input("Please enter a number between 1 and 5: "))

    triangle_color = input("Enter triangle color: ")
    background_color = input("Enter background color: ")

    # Create screen
    screen = turtle.Screen()

    # Validate background color
    try:
        screen.bgcolor(background_color)
    except turtle.TurtleGraphicsError:
        print("Invalid background color. Using white.")
        screen.bgcolor("white")

    screen.title("Sierpinski Triangle")

    # Create turtle
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    # Validate triangle color
    try:
        pen.color(triangle_color)
    except turtle.TurtleGraphicsError:
        print("Invalid triangle color. Using black.")
        triangle_color = "black"
        pen.color("black")

    print("\nGenerating Sierpinski Triangle...\n")

    points = [(-200, -150), (0, 200), (200, -150)]

    fractal.draw_sierpinski(pen, points, depth, triangle_color)

    print("Fractal generated successfully!")

    # Save actual IMAGE file
    save_image.save_fractal(screen)

    input("\nPress Enter to exit the program.")
    turtle.bye()


if __name__ == "__main__":
    main()