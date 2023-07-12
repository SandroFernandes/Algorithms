import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define all possible outcomes of a die roll
dice_rolls = list(range(1, 7))

# Initialize an empty dictionary to store the outcomes
outcomes = {}

# For each combination of dice rolls
for dice1 in dice_rolls:
    for dice2 in dice_rolls:
        
        # Calculate the sum of the dice
        roll_sum = dice1 + dice2

        # If this sum is already in the dictionary, increment its count
        # Otherwise, add it to the dictionary with a count of 1
        if roll_sum in outcomes:
            outcomes[roll_sum] += 1
        else:
            outcomes[roll_sum] = 1

# Create a bar graph of the outcomes
plt.bar(outcomes.keys(), outcomes.values())
plt.xlabel('Sum of Two Dice Rolls')
plt.ylabel('Frequency')
plt.title('Possible Outcomes of Rolling Two Dice')
plt.xticks(list(range(2, 13)))  # The possible sums range from 2 to 12
plt.grid(True)
plt.show()

# A heat map
# Creates a 6x6 matrix to store the outcomes
outcomes = np.zeros((6, 6))

# For each combination of dice rolls
for i, dice1 in enumerate(dice_rolls):
    for j, dice2 in enumerate(dice_rolls):
        # Store the sum of the dice in the matrix
        outcomes[i, j] = dice1 + dice2

# Create a heatmap of the outcomes
sns.heatmap(outcomes, annot=True, fmt=".0f", cmap='viridis',
            xticklabels=dice_rolls, yticklabels=dice_rolls)
plt.xlabel('Dice 2')
plt.ylabel('Dice 1')
plt.title('Sum of Outcomes from Rolling Two Dice')
plt.show()

# Initialize a 6x6 pandas DataFrame
outcomes = pd.DataFrame(index=dice_rolls, columns=dice_rolls)

# For each combination of dice rolls
for dice1 in dice_rolls:
    for dice2 in dice_rolls:
        # Store the sum of the dice in the DataFrame
        outcomes.loc[dice1, dice2] = dice1 + dice2

# Print the DataFrame
print(outcomes)
