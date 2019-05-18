import csv
from house import House


class Data():
    """
    This class contains the necessary functions to load in
    the data that is needed for the smartgrid.
    """

    def __init__(self, number):
        """
        Create houses and batteries for the smartgrid
        """
        self.houses = self.load_houses(f"data/wijk{number}_huizen.csv")
        self.houses = self.load_batteries(f"data/wijk{number}_batteries.txt")

    def load_houses(self, filename):
        """
        Loads houses and returns a dictionary with number of houses
        as key and house as object
        """
        # Create house objects
        houses = {}
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            id = 1
            for rows in reader:
                x_house = int(rows[0])
                y_house = int(rows[1])
                max_output = float(rows[2])
                # Initialize a house object and put it in a dictionary with its
                # id as key.
                house = House(id, x_house, y_house, max_output)
                houses[id] = house
                id += 1

        return houses

    def load_batteries(self, filename):
        """
        Loads batteries and returns dictionary with id and batteries
        as object.
        """

        f = open(infile, "r")
        print(f.read())

data = Data(1)
data.load_houses()
