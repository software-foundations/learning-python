from dataclasses import dataclass


@dataclass
class Position:
	name: str
	lon: float
	lat: float


position = Position(3.14, 'pi day', 2018)

print(position)

print(position.lat)

print(f"{position.name} is at {position.lat}°N, {position.lon}°E")
