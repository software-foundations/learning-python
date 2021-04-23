from dataclasses import dataclass, field, fields


@dataclass
class Position:
	name: str
	lon: float = field(default=0.0, metadata={'unit': 'degrees'})
	lat: float = field(default=0.0, metadata={'unit': 'degrees'})

print(fields(Position), end='\n\n')

position = Position('My City', 3.4, 6.8)

print(position, end='\n\n')

print(fields(position), end='\n\n')

lat_unit = fields(Position)[2].metadata['unit']

print(lat_unit)
"""
The metadata parameter is not used by the data classes themselves but is available for you (or third party packages) to attach information to fields. In the Position example, you could for instance specify that latitude and longitude should be given in degrees

The metadata (and other information about a field) can be retrieved using the fields() function (note the plural s):
"""