"""
Be aware though that if your data class contains mutable fields, 
those might still change. This is true for all nested data structures in Python
"""

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]

"""
Even though both ImmutableCard and ImmutableDeck are immutable, 
the list holding cards is not.

You can therefore still change the cards in the deck:
"""

queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
print(deck)

print(ImmutableDeck(cards=[ImmutableCard(rank='Q', suit='♡'), ImmutableCard(rank='A', suit='♠')]))

deck.cards[0] = ImmutableCard('7', '♢')
print(deck)
