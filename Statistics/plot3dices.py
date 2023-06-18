import plotly.graph_objects as go

dice_rolls = list(range(1, 7))

dice1_rolls = []
dice2_rolls = []
dice3_rolls = []

for dice1 in dice_rolls:
    for dice2 in dice_rolls:
        for dice3 in dice_rolls:
            dice1_rolls.append(dice1)
            dice2_rolls.append(dice2)
            dice3_rolls.append(dice3)

# Create a color map
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

# Create a 3D plot of the dice roll combinations
text = [f'({dice1}, {dice2}, {dice3})' for dice1, dice2, dice3 in zip(dice1_rolls, dice2_rolls, dice3_rolls)]
color = [colors[(dice1 + dice2 + dice3) % len(colors) - 1] for dice1, dice2, dice3 in zip(dice1_rolls, dice2_rolls, dice3_rolls)]

trace = go.Scatter3d(x=dice1_rolls, y=dice2_rolls, z=dice3_rolls, text=text, mode='text', textfont=dict(color=color, size=10))
layout = go.Layout(scene=dict(xaxis=dict(range=[0, 7], visible=False), yaxis=dict(range=[0, 7], visible=False), zaxis=dict(range=[0, 7], visible=False)))

fig = go.Figure(data=[trace], layout=layout)

fig.show()
