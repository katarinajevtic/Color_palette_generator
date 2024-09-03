import random
import matplotlib.pyplot as plt


def generate_random_color():
    """Generate a random RGB color."""
    return random.random(), random.random(), random.random()


def generate_color_palette(n):
    """Generate a palette of n colors."""
    palette = []
    for _ in range(n):
        color = generate_random_color()
        palette.append(color)
    return palette


def display_palette(palette):
    """Display the color palette using matplotlib."""
    fig, ax = plt.subplots(1, figsize=(8, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
    ax.imshow([palette], extent=[0, 10, 0, 1])
    plt.show()


if __name__ == "__main__":
    num_colors = int(input("Enter the number of colors in the palette: "))
    palette = generate_color_palette(num_colors)
    display_palette(palette)
