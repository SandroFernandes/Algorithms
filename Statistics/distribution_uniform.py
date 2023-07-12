# Distribution of rolling a die 100000 times
import random
import matplotlib.pyplot as plt


def simulate_rolls(num_rolls):
    return [random.randint(1, 6) for _ in range(num_rolls)]


def plot_distribution(rolls):
    counts = [0] * 6
    for roll in rolls:
        counts[roll - 1] += 1

    x = [1, 2, 3, 4, 5, 6]
    plt.bar(x, counts)
    plt.xlabel('Dice Number')
    plt.ylabel('Frequency')
    plt.title('Dice Roll Distribution')
    plt.show()


# Set the number of rolls you want to simulate, bigger number will give more accurate results
dice_rolls = 1_000_000

# Simulate rolls
total_rolls = simulate_rolls(dice_rolls)

# Plot the distribution
plot_distribution(total_rolls)
