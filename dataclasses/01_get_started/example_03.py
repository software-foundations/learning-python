class RegularCard:
	def __init__(self, rank: str, suit: str):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		return(f"{self.__class__.__name__} \
			(rank={self.rank}, suit={self.suit!r})")

	def __eq__(self, other):
		if other.__class__ is not self.__class__:
			return NotImplemented
		return (self.rank, self.suit) == (other.rank, other.suit)


queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts)
print(queen_of_hearts.rank)
print(queen_of_hearts == RegularCard('Q', 'Hearts'))
