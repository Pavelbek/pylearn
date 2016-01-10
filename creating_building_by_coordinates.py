# Here we receive two coordinates and widths of walls for a building and using them we create instance of building

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {
            "north-west": [self.south + self.width_NS, self.west],
            "north-east": [self.south + self.width_NS, self.west + self.width_WE],
            "south-west": [self.south, self.west],
            "south-east": [self.south, self.west + self.width_WE]
        }

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.south, self.west, self.width_WE, self.width_NS, self.height)
		

if __name__ == "__main__":
    building = Building(1, 2, 2, 2)
    print building
    print 'Corners:', building.corners()
    print 'Area:', building.area()
    print 'Volume:', building.volume()
	
	
# Philipp's solution:



class Building(object):
    def __init__(self, south, west, width_we, width_ns, height=10):
        super(Building, self).__init__()
        self.south = south
        self.west = west
        self.width_we = width_we
        self.width_ns = width_ns
        self.height = height

    def __repr__(self):
        return 'Building({}, {}, {}, {}, {})'.format(
            self.south,
            self.west,
            self.width_we,
            self.width_ns,
            self.height,
        )

    def corners(self):
        return {
            'north-west': [self.south + self.width_ns, self.west],
            'north-east': [self.south + self.width_ns, self.west + self.width_we],
            'south-west': [self.south, self.west],
            'south-east': [self.south, self.west + self.width_we],
        }

    def area(self):
        return self.width_we * self.width_ns

    def volume(self):
        return self.area() * self.height


if __name__ == "__main__":
    building = Building(1, 2, 2, 2)
    print building
    print 'Corners:', building.corners()
    print 'Area:', building.area()
    print 'Volume:', building.volume()
	
	
