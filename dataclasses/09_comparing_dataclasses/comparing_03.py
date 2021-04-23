from dataclasses import dataclass, field


"""
For PlayingCard to use this sort index for comparisons, we need to add a field .sort_index to the class. However, this field should be calculated from the other fields .rank and .suit automatically. This is exactly what the special method .__post_init__() is for. It allows for special processing after the regular .__init__() method is called:
"""

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

"""
Note that .sort_index is added as the first field of the class. That way, the comparison is first done using .sort_index and only if there are ties are the other fields used. Using field(), you must also specify that .sort_index should not be included as a parameter in the .__init__() method (because it is calculated from the .rank and .suit fields). To avoid confusing the user about this implementation detail, it is probably also a good idea to remove .sort_index from the repr of the class.
"""

queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')

print(ace_of_spades > queen_of_hearts)
