from fractions import Fraction
import seaborn as sns
import pandas as pd
from collections import Counter


def roll_dices(number_of_dices):
    odd = even = 0
    total_outcomes = 6 ** number_of_dices

    for outcome in product(range(1, 7), repeat=number_of_dices):
        product_of_outcome = 1
        for number in outcome:
            product_of_outcome *= number
        if product_of_outcome % 2:
            odd += 1
        else:
            even += 1

    return odd, even, total_outcomes


def show_probability():
    for rolls in range(2, 6):
        result = roll_dices(rolls)

        # express the result as a fraction
        odd_probability = Fraction(result[0], result[2])
        even_probability = Fraction(result[1], result[2])
        print(f'What’s the probability that the product of {rolls} rolls of a d6 is odd? 2 rolls? {odd_probability}')
        print(f'What’s the probability that the product of {rolls} rolls of a d6 is even? 2 rolls? {even_probability}')


import matplotlib.pyplot as plt
import numpy as np
from itertools import product


def plot_dice_product_distribution(n):

    # Create a 6x6 matrix with the product of two dice outcomes

    products = np.outer(range(1, 7), range(1, 7))

    # Create a heatmap
    sns.heatmap(products, annot=True, fmt="d", cmap='viridis', xticklabels=range(1, 7), yticklabels=range(1, 7))

    # Set the title and labels
    plt.title('Product of outcomes for two dice')
    plt.xlabel('Die 1')
    plt.ylabel('Die 2')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    # show_probability()
    plot_dice_product_distribution(2)
