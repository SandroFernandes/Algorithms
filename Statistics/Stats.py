from math import comb
from fractions import Fraction
from itertools import product


def roll_dices(number_of_dices, show_steps=False):
    odd = 0
    even = 0
    possibilities = [range(1, 7) for _ in range(number_of_dices)]
    total_outcomes = 6**number_of_dices
    for outcome in product(*possibilities):
        product_of_outcome = 1
        for number in outcome:
            product_of_outcome *= number
        if product_of_outcome % 2 == 1:
            odd += 1
        else:
            even += 1
    print('Probability of odd:', Fraction(odd, total_outcomes))
    print('Probability of even:', Fraction(even, total_outcomes))


print('Whats the probability of getting 2 clubs of a deck of cards with replacement ?')
total_cards = 52
total_clubs = 13

prob_club = Fraction(total_clubs / total_cards)
prob_2_clubs = prob_club * prob_club

print("Probability of getting 2 clubs with replacement:", prob_2_clubs)

print('Whats the probability of getting 2 clubs of a deck of cards without replacement ?')

total_cards = 52
total_clubs = 13

# Calculate the probability
prob_2_clubs = comb(total_clubs, 2) / comb(total_cards, 2)
prob_2_clubs = Fraction(prob_2_clubs).limit_denominator()

print("Probability of getting 2 clubs without replacement:", prob_2_clubs)
roll_dices(2)

print('What’s the probability that the product of 2 rolls of a d6 is odd? 3 rolls?')
roll_dices(3)
print('What’s the probability that the product of 2 rolls of a d6 is odd? 4 rolls?')
roll_dices(4)
print('What’s the probability that the product of 2 rolls of a d6 is odd? 5 rolls?')
roll_dices(5)
