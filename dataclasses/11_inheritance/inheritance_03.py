"""
Another thing to be aware of is how fields are ordered in a subclass.

Starting with the base class, fields are ordered in the order in which they are
first defined. If a field is redefined in a subclass, its order does not change.

For example, if you define Position and Capital as follows:
"""

from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str = 'Unknown'
    lat: float = 40.0


"""
Then the order of the fields in Capital will still be name, lon, lat, country.
However, the default value of lat will be 40.0.
"""

print(Capital('Madrid', country='Spain'))
