from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:	
	rank: str
	suit: str

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck() -> List[PlayingCard]:
	return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:  # Will NOT work
	# ValueError: mutable default <class 'list'> for field cards is not allowed: use default_factory
	cards: List[PlayingCard] = make_french_deck()


"""
Don’t do this! This introduces one of the most common anti-patterns in Python: using mutable default arguments. The problem is that all instances of Deck will use the same list object as the default value of the .cards property. This means that if, say, one card is removed from one Deck, then it disappears from all other instances of Deck as well. Actually, data classes try to prevent you from doing this, and the code above will raise a ValueError.

Instead, data classes use something called a default_factory to handle mutable default values. To use default_factory (and many other cool features of data classes), you need to use the field() specifier
"""