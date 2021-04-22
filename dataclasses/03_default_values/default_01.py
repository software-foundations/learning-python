from dataclasses import dataclass


@dataclass
class Position:
	name: str
	lon: float = 0.0
	lat: float = 0.0


island = Position('Null Island')
print(island)

greenwich = Position('Greenwich', lat=51.8)
print(greenwich)

vancouver = Position('Vancouver', -123.1, 49.3)
print(vancouver)
