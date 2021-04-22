from dataclasses import make_dataclass


Position = make_dataclass('Position', ['name', 'lat', 'lon'])

position = Position('Oslo', 10.8, 59.9)

print(position)

print(position.lat)

print(f"{position.name} is at {position.lat}°N, {position.lon}°E")
