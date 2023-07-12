from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np


COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#9edae5', '#dbdb8d', '#c5b0d5', '#c49c94', '#f7b6d2']


def plot_fractions_as_pie_chart(fractions, graph_shape='circle'):
    """Plot a list of fractions as a pie chart.
       If the sum of the fractions is less than 1, the difference is added to the list
       and the pie chart is plotted.

       If the sum of the fractions is greater than 1, the function raises a ValueError.

    """

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

        case 'square':
            # todo: implement a square chart
            # Create a bar chart.
            fig, ax = plt.subplots()
            y_pos = np.arange(len(fractions))

            ax.barh(y_pos, fractions, color=colors[:len(fractions)])
            ax.set_yticks(y_pos)
            ax.set_yticklabels(labels)
            ax.set_xlabel('Fraction')
            ax.set_title('Bar Chart of Fractions')
        case _:
            raise ValueError(f'Invalid graph shape: {graph_shape}')

    # Show the plot.
    plt.show()


if __name__ == '__main__':
    fractions_list = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 10) ]
    plot_fractions_as_pie_chart(fractions_list, graph_shape='circle')
