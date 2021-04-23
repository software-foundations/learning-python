"""
Things get a little more complicated if
any fields in the base class have default values:
"""

from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str  # Does NOT work

"""
This code will immediately crash with a TypeError complaining that
“non-default argument ‘country’ follows default argument.”

The problem is that our new country field has no default value, while the 
lon and lat fields have default values.

The data class will try to write an .__init__() method with the
following signature:

def __init__(name: str, lon: float = 0.0, lat: float = 0.0, country: str):
    ...
"""

"""
However, this is not valid Python. If a parameter has a default value,
all following parameters must also have a default value.

In other words, if a field in a base class has a default value, then
all new fields added in a subclass must have default values as well.
"""