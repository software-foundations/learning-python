"""
You can subclass data classes quite freely.

As an example, we will extend our Position example with a country field and 
use it to record capitals:
"""

from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

@dataclass
class Capital(Position):
    country: str


position = Capital('Oslo', 10.8, 59.9, 'Norway')

print(position)

"""
The country field of Capital is added after the
three original fields in Position.
"""