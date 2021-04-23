from dataclasses import dataclass


"""
TypeError: '>' not supported between instances of 'PlayingCard' and 'PlayingCard'

This is, however, (seemingly) easy to rectify: order=True
"""

@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')

print(ace_of_spades > queen_of_hearts)

"""
The @dataclass decorator has two forms. So far you have seen the simple form where @dataclass is specified without any parentheses and parameters. However, you can also give parameters to the @dataclass() decorator in parentheses. The following parameters are supported:

init: Add .__init__() method? (Default is True.)
repr: Add .__repr__() method? (Default is True.)
eq: Add .__eq__() method? (Default is True.)
order: Add ordering methods? (Default is False.)
unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
frozen: If True, assigning to fields raise an exception. (Default is False.)
"""

"""
How are the two cards compared though? You have not specified how the ordering should be done, and for some reason Python seems to believe that a Queen is higher than an Ace…

It turns out that data classes compare objects as if they were tuples of their fields. In other words, a Queen is higher than an Ace because 'Q' comes after 'A' in the alphabet:
"""

print(('A', '♠') > ('Q', '♡'))
