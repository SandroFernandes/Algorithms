from fractions import Fraction
from math import comb


total_cards = 52
total_clubs = 13

# how many ways to shuffle a deck of cards
print(f'How many ways to shuffle a deck of cards ? {total_cards * (total_cards - 1) * (total_cards - 2) * (total_cards - 3) * (total_cards - 4) * (total_cards - 5) * (total_cards - 6) * (total_cards - 7) * (total_cards - 8) * (total_cards - 9) * (total_cards - 10) * (total_cards - 11) * (total_cards - 12) * (total_cards - 13)}')
# how many ways to shuffle 2 decks of cards
print(f'How many ways to shuffle 2 decks of cards ? {total_cards * (total_cards - 1) * (total_cards - 2) * (total_cards - 3) * (total_cards - 4) * (total_cards - 5) * (total_cards - 6) * (total_cards - 7) * (total_cards - 8) * (total_cards - 9) * (total_cards - 10) * (total_cards - 11) * (total_cards - 12) * (total_cards - 13) * total_cards * (total_cards - 1) * (total_cards - 2) * (total_cards - 3) * (total_cards - 4) * (total_cards - 5) * (total_cards - 6) * (total_cards - 7) * (total_cards - 8) * (total_cards - 9) * (total_cards - 10) * (total_cards - 11) * (total_cards - 12) * (total_cards - 13)}')

# rules of poker
# https://en.wikipedia.org/wiki/Poker_probability
# https://en.wikipedia.org/wiki/Poker_probability_(Texas_hold_%27em)
# https://en.wikipedia.org/wiki/Poker_probability_(Omaha)


# how many ways to make a royal flush
print(f'How many ways to make a royal flush ? {4 * 4 * 4 * 4 * 4}')

# how many ways to make a straight flush
print(f'How many ways to make a straight flush ? {4 * 4 * 4 * 4 * 4 * (total_cards - 5)}')

# how many ways to make a 4 of a kind
print(f'How many ways to make a 4 of a kind ? {4 * 13 * 12 * 11 * 10}')

# how many ways to make a full house
print(f'How many ways to make a full house ? {4 * 13 * 12 * 4 * 13}')

# how many ways to make a flush
print(f'How many ways to make a flush ? {4 * 4 * 4 * 4 * 4 * (total_cards - 5)}')

# how many ways to make a straight
print(f'How many ways to make a straight ? {4 * 4 * 4 * 4 * 4 * (total_cards - 5)}')

# how many ways to make a 3 of a kind
print(f'How many ways to make a 3 of a kind ? {4 * 13 * 12 * 11 * 4 * 4}')

# how many ways to make a 2 pair
print(f'How many ways to make a 2 pair ? {4 * 13 * 12 * 11 * 4 * 4}')

# how many ways to make a 1 pair
print(f'How many ways to make a 1 pair ? {4 * 13 * 12 * 11 * 4 * 4 * 4}')

# how many ways to make a high card
print(f'How many ways to make a high card ? {4 * 4 * 4 * 4 * 4 * (total_cards - 5)}')






prob_club = Fraction(total_clubs / total_cards)
prob_2_clubs = prob_club * prob_club
print(f'Whats the probability of getting 2 clubs of a deck of cards with replacement ? {prob_2_clubs}')


prob_2_clubs = comb(total_clubs, 2) / comb(total_cards, 2)
prob_2_clubs = Fraction(prob_2_clubs).limit_denominator()
print(f'Whats the probability of getting 2 clubs of a deck of cards without replacement ? {prob_2_clubs}')



