"""
One of the defining features of the namedtuple you saw earlier is that it is 
immutable. That is, the value of its fields may never change. For many types of 
data classes, this is a great idea! To make a data class immutable, 
set frozen=True when you create it. For example, the following is an immutable 
version of the Position class you saw earlier:
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


"""
In a frozen data class, you can not assign values to the fields after creation:
"""

pos = Position('Oslo', 10.8, 59.9)
print(pos.name)
pos.name = 'Stockholm'
# dataclasses.FrozenInstanceError: cannot assign to field 'name'