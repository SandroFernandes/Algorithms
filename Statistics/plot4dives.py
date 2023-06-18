import plotly.graph_objects as go
import numpy as np

dice_rolls = list(range(1, 7))

dice1_rolls = []
dice2_rolls = []
dice3_rolls = []
dice4_rolls = []

for dice1 in dice_rolls:
    for dice2 in dice_rolls:
        for dice3 in dice_rolls:
            for dice4 in dice_rolls:
                dice1_rolls.append(dice1)
                dice2_rolls.append(dice2)
                dice3_rolls.append(dice3)
                dice4_rolls.append(dice4)

# Create a 3D plot of the dice roll combinations
text = [f'({dice1}, {dice2}, {dice3}, {dice4})' for dice1, dice2, dice3, dice4 in zip(dice1_rolls, dice2_rolls, dice3_rolls, dice4_rolls)]
dice4_colors = np.array(dice4_rolls) / max(dice4_rolls)  # Normalize to [0, 1] for the color scale

trace = go.Scatter3d(x=dice1_rolls, y=dice2_rolls, z=dice3_rolls, text=text, mode='text',
                     marker=dict(size=0, color=dice4_colors, colorscale='Rainbow', showscale=True))

layout = go.Layout(scene=dict(xaxis=dict(range=[0, 7], visible=False),
                              yaxis=dict(range=[0, 7], visible=False),
                              zaxis=dict(range=[0, 7], visible=False)))

fig = go.Figure(data=[trace], layout=layout)

fig.show()
