from house import House
from battery import Battery


class Cable(object):
    def __init__(self, house, battery):
        self.house = house
        self.battery = battery
        self.route = route

    def distance(self):
        """
        Calculates a route between battery and house
        according to the manhatten distance
        """
        coordinates_h = House.get_coord()
        coordinates_b = Battery.get_coord()
        length = abs(coordinates_h[0] - coordinates_b[0]) + abs(coordinates_h[1] - coordinates_b[1])

        return length
