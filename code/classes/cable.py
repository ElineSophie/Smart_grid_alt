class Cable(object):
    def __init__(self, house, battery):
        self.house = house
        self.battery = battery

    def distance(self):
        """
        Calculates the distance between house and battery
        according to the Manhatten Distance.
        """
        
