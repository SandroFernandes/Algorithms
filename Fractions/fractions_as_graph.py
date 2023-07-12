from math import lcm
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import plotly.graph_objects as go

COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#9edae5', '#dbdb8d', '#c5b0d5', '#c49c94', '#f7b6d2']


def plot_fractions_as_pie_chart(fractions, graph_shape='circle', complete=True):
    """Plot a list of fractions as a pie chart.
       If the sum of the fractions is less than 1, the difference is added to the list
       and the pie chart is plotted.


    """
    if complete:
        # the sum of the fractions is less than 1
        if sum(fractions) < 1:
            # calculate the difference
            difference = 1 - sum(fractions)
            # add the difference to the list
            fractions.append(difference)

    # Convert fractions to labels.
    labels = [str(f) for f in fractions]

    # Create a list of colors.
    colors = COLORS[:len(fractions)]

    match graph_shape:

        case 'circle':

            # Plot the pie chart.
            fig, ax = plt.subplots()
            ax.pie(fractions, labels=labels, colors=colors, autopct='%1.1f%%')
            # Add a title.
            ax.set_title('Pie Chart of Fractions')
            # Show the plot.
            plt.show()

        case 'line':

            # Convert fractions to decimal
            decimal_fractions = [fraction.numerator / fraction.denominator for fraction in fractions]

            # Create a figure and a single subplot (axis)
            fig, ax = plt.subplots()

            # Draw the number line using a horizontal line
            # Arguments are: y, x min, y max
            ax.hlines(0, 0, 1)

            # Highlight the fractions by coloring the points in red
            x = 0
            labels_pos = []
            for decimal, fraction in zip(decimal_fractions, fractions):
                x += decimal
                labels_pos.append(x)
                ax.plot(x, 0, '|', color='red', markersize=15)

            # Add labels to the points
            ax.set_xlim(-0.1, 1.1)
            ax.set_ylim(-1, 1)
            ax.set_yticks([])
            ax.set_xticks(labels_pos)
            ax.set_xticklabels(labels)
            ax.set_title("Fractions  on the number line")

            # Show the plot.
            plt.show()

        case 'square':

            # Create a new figure with defined size
            fig, ax = plt.subplots(figsize=(6, 6))

            # Draw the colored rectangles representing the fractions
            start = 0
            labels_pos = []
            for fraction, label, color in zip(fractions, labels, colors):
                rectangle = Rectangle((start, 0), fraction, 1, edgecolor='black', facecolor=color, label=label)
                ax.add_patch(rectangle)
                start += fraction
                labels_pos.append(start.numerator / start.denominator)

            # Set limits
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal')  # Ensure the plot remains a square

            # Hide  y ticks
            ax.set_yticks([])
            # Set x ticks and labels
            ax.set_xticks(labels_pos)
            ax.set_xticklabels(labels)

        case 'grid':

            # Find the least common multiple of the denominators
            denominator = lcm(*[fraction.denominator for fraction in fractions])
            # Create a new figure with defined size
            fig, ax = plt.subplots(figsize=(6, 6))

            for i, fraction in enumerate(fractions):
                # convert the fractions to have the same denominator and equivalent numerator
                numerator = fraction.numerator * (denominator // fraction.denominator)
                for j in range(denominator):
                    rect = plt.Rectangle((j / denominator, i / len(fractions)), 1 / denominator, 1 / len(fractions),
                                         # fill=(i * denominator + j < numerator),
                                         edgecolor='black',
                                         facecolor=COLORS[i] if j < numerator else 'white')
                    ax.add_patch(rect)

                    # Add fraction label in the center of each strip
                    ax.text(-0.12, (i + 0.5) / len(fractions), str(fraction), ha='center', va='center', fontsize=12)

            # Hide ticks
            ax.set_xticks([])
            ax.set_yticks([])
            # Add title
            ax.set_title(f"Compare fractions using a grid")

            # Show the plot.
            plt.show()

        case 'tiles':

            # Create the figure and axes
            fig, axs = plt.subplots(len(fractions), 1, figsize=(8, 2 * len(fractions)))

            # For each fraction, create a bar and fill in the appropriate amount
            for i, (fraction, ax) in enumerate(zip(fractions, axs)):
                ax.broken_barh([(0, fraction.numerator / fraction.denominator),
                                (fraction.numerator / fraction.denominator,
                                 1 - fraction.numerator / fraction.denominator)],
                               (0, 1), facecolors=(colors[i], 'white'))

                # Configure the axes
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.set_title(f'{fraction.numerator}/{fraction.denominator}', fontsize=16)
                ax.get_yaxis().set_visible(False)
                ax.set_xticks([0, 1])
                ax.grid(True)

            # Show the plot.
            plt.tight_layout()
            plt.show()

        case 'cubes':
            # Define the fraction to visualize
            fraction = fractions[0]

            # Create the figure and 3D axes
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Create the fraction cubes
            x, y, z = np.indices((fraction.denominator, fraction.denominator, fraction.denominator))
            cube = (x < fraction.numerator) & (y < fraction.numerator) & (z < fraction.numerator)
            ax.voxels(cube, edgecolor='k')

            # Show the plot.
            plt.show()

        case 'cubes-i':

            max_denominator = lcm(*[fraction.denominator for fraction in fractions])

            fig = go.Figure()

            for i, fraction in enumerate(fractions):
                # Convert the fractions to have the same denominator and equivalent numerator
                fraction_size = fraction.numerator * (max_denominator // fraction.denominator)

                # For each fraction, create a cube of points with fraction size
                x = [0, 0, fraction_size, fraction_size, 0, 0, fraction_size, fraction_size]
                y = [0, fraction_size, 0, fraction_size, 0, fraction_size, 0, fraction_size]
                z = [0, 0, 0, 0, fraction_size, fraction_size, fraction_size, fraction_size]

                # Offset each fraction along the x-axis
                x = [val + i * max_denominator for val in x]

                # Create a mesh3d object for the fraction
                fig.add_trace(go.Mesh3d(
                    x=x, y=y, z=z,
                    color=colors[i % len(colors)],
                    opacity=0.50,

                    # i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                    # j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                    # k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                    showscale=False
                ))

                # Set layout properties
            fig.update_layout(
                scene=dict(
                    xaxis=dict(range=[0, max_denominator * len(fractions)]),
                    yaxis=dict(range=[0, max_denominator]),
                    zaxis=dict(range=[0, max_denominator])
                )
            )

            fig.show()

        case _:
            raise ValueError(f'Invalid graph shape: {graph_shape}')


if __name__ == '__main__':
    fractions_list = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 10)]
    plot_fractions_as_pie_chart(fractions_list, graph_shape='circle')
    plot_fractions_as_pie_chart(fractions_list, graph_shape='line')
    plot_fractions_as_pie_chart(fractions_list, graph_shape='square')
    fractions_list.append(Fraction(1, 1))
    plot_fractions_as_pie_chart(fractions_list, graph_shape='grid')
    plot_fractions_as_pie_chart(fractions_list, graph_shape='tiles')
    plot_fractions_as_pie_chart(fractions_list, graph_shape='cubes')
    plot_fractions_as_pie_chart([Fraction(1, 3), Fraction(1, 3), Fraction(1, 10)], graph_shape='cubes-i')
