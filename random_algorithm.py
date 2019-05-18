"""
Pseudocode:
Randomly loop through the batteries and connect
house out of random selection. Stop when the
battery has no capacity left.
"""
from loader import Data
import random

data = Data(1)

house_id = []
for key in data.houses:
    # print(data.houses[key])
    houseid = data.houses[key].get_id()
    house_id.append(houseid)

battery_id = []
for key in data.batteries:
    # Print
    batteryid = data.batteries[key].get_id()
    battery_id.append(batteryid)

random.shuffle(battery_id)
random.shuffle(house_id)
print(battery_id)
