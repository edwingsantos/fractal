"""
Main program file for the Sierpinski Triangle Generator.
Handles user input and overall program flow.
"""

import turtle
from fractal import draw_sierpinski
from file_handler import save_image


def get_user_input():
    """
    Ask the user for recursion depth, triangle color,
    and background color.
    """

    print("Welcome to the Sierpinski Triangle Generator!")
    print("This program creates a Sierpinski Triangle fractal using recursion.\n")

    # Get recursion depth
    depth = int(input("Enter recursion depth (1-5): "))
    while depth < 1 or depth > 5:
        depth = int(input("Please enter a number between 1 and 5: "))

    # Get triangle color
    triangle_color = input("Enter triangle color (e.g., red, blue, green): ")

    # Extra Credit: Background color
    background_color = input("Enter background color: ")

    return depth, triangle_color, background_color


def setup_screen(background_color):
    """
    Set up the turtle screen and background color.
    """

    screen = turtle.Screen()
    screen.bgcolor(background_color)
    screen.title("Sierpinski Triangle Fractal")

    return screen


def main():
    """
    Main function controlling the program.
    """

    depth, triangle_color, background_color = get_user_input()

    screen = setup_screen(background_color)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    print("\nGenerating Sierpinski Triangle...\n")

    # Starting coordinates of the large triangle
    points = [(-200, -100), (0, 200), (200, -100)]

    draw_sierpinski(pen, points, depth, triangle_color)

    print("Fractal generated successfully!")

    # Extra Credit: Save image option
    save_option = input("Would you like to save the image? (yes/no): ").lower()
    if save_option == "yes":
        save_image(screen)

    input("\nPress Enter to exit the program.")
    turtle.bye()


if __name__ == "__main__":
    main()