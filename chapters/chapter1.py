# Example 1.1 Pythonic Card deck.
# This example details the uses and importance
# of dunder/special/magic methods in a pythonic way

import collections



Card = collections.namedtuple('Card', ['rank', 'suit'])
""" Notes on namedtuple from collections

Great tool for simple classes that dont need custom methods.


collections.namedtuple() > https://docs.python.org/3/library/collections.html#collections.namedtuple
Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.
"""

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # this is a interesting way to make a list on definition with .split()
    suits = 'spades diamonds clubs hearts'.split() 

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]