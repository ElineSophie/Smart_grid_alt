# Import structure to path
import os
import sys
from sys import argv
# from house import House
from loader import Data
import visualisation

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


def main():
    # Check for correct usage command line argument
    if len(argv) != 2:
        print("Usage: python district.py 1, 2 or 3")
        exit(1)

    if argv[1] != "1" and argv[1] != "2" and argv[1] != "3":
        print("Choose: 1, 2 or 3 for the districts")
        exit(1)


if __name__ == "__main__":
    main()

    district = sys.argv[1]
    data = Data(district)
    print(data)
    # print(House.get_id())
    for key in data.houses:
        print(data.houses[key].get_coord())

    # visualisation()
