from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


ace_of_spades = PlayingCard('A', '♠')

print(ace_of_spades)

"""
The cards now look much nicer, but the deck is still as verbose as ever
"""