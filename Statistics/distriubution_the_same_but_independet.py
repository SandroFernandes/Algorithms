# In the given example, we have two dice: a red die and a blue die.
# Each die has a certain number of pips or dots on its faces, ranging from 1 to 6.
# When we roll the dice, the number of pips that appear on each die is considered a random variable.
# Let's denote the number of pips on the blue die as B and the number of pips on the red die as R.
# The statement "the number of pips on the blue die, B, and the number of pips on the red die, R,
# are two random variables that have the same distribution" means that both B and R follow the same probability distribution.
# In this case, since both dice are standard six-sided dice, the probability of obtaining each number (1 to 6) is equal for both B and R.
# However, it's important to note that the actual values of B and R are not equal.
# They represent independent random variables, meaning that the outcome of one die
# does not provide any information or influence the outcome of the other die.
# For example, if we roll the blue die, and it shows a 4, that information does
# not tell us anything about the value of the red die.
# The red die could show any number from 1 to 6 with equal probability, regardless of what the blue die shows.
# Therefore, we say that B and R are independent random variables because knowing the outcome of one die (B or R)
# does not provide any information about the outcome of the other die.
# Refer to page 4 of trading-interview.pdf

import random
import matplotlib.pyplot as plt
import numpy as np


def roll_die():
    return random.randint(1, 6)


def simulate_rolls(num_rolls):
    blue_rolls = [roll_die() for _ in range(num_rolls)]
    red_rolls = [roll_die() for _ in range(num_rolls)]
    return blue_rolls, red_rolls


def plot_distribution(rolls, label, offset_to_right):
    counts = [0] * 6

    for roll in rolls:
        counts[roll - 1] += 1

    x = np.arange(1, 7) + offset_to_right
    plt.bar(x, counts, alpha=0.5, label=label, width=0.4)


# Set the number of rolls you want to simulate
dice_rolls = 10000

# Simulate rolls
blue, red = simulate_rolls(dice_rolls)

# Set the offset for the bars
offset = 0.2

# Plot the distribution of blue and red die rolls
plot_distribution(blue, 'Blue Die', -offset)
plot_distribution(red, 'Red Die', offset)

plt.xlabel('Pips')
plt.ylabel('Frequency')
plt.title('Distribution of Rolled Dice')
plt.legend()

plt.xticks(np.arange(1, 7))
plt.show()
