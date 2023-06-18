import collections
from random import shuffle


C, H, D, S = "CLUBS", "HEARTS", "DICE", "SPADE"
Card = collections.namedtuple("Card", "suit value")

deck = [Card(suit, value) for suit in (C, H, D, S) for value in 'A23456789TJQK']

print(deck)
shuffle(deck)

print(deck)

