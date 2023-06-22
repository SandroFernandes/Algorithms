import random
import matplotlib.pyplot as plt


def simulate_rolls(num_rolls):
    return [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]


def plot_distribution(rolls):
    counts = [0] * 11
    for roll in rolls:
        counts[roll - 2] += 1

    x = list(range(2, 13))
    plt.bar(x, counts)
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Frequency')
    plt.title('Distribution of Sum of Two Dice Rolls')
    plt.show()


# Set the number of rolls you want to simulate
dice_rolls = 100

# Simulate rolls
total_rolls = simulate_rolls(dice_rolls)

# Plot the distribution
plot_distribution(total_rolls)
