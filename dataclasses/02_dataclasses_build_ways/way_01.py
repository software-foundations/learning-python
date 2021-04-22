from dataclasses import dataclass


@dataclass
class Position:
	name: str
	lon: float
	lat: float


position = Position('Oslo', 10.8, 59.9)

print(position)

print(position.lat)

print(f"{position.name} is at {position.lat}°N, {position.lon}°E")
