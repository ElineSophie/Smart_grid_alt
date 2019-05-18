import numpy as np
import matplotlib.pyplot as plt
from loader import Data

data = Data(1)

grid_house = []
for key in data.houses:
    # print(data.houses[key])
    coord_houses = data.houses[key].get_coord()
    grid_house.append(coord_houses)

grid_batteries = []
for key in data.batteries:
    # Print
    coord_batteries = data.batteries[key].get_coord()
    grid_batteries.append(coord_batteries)

# Load images.
# house_marker = plt.imread('Huis.jpg')
# battery_marker = plt.imread('Batterij.jpg')

# Make the plot for
data = np.array(grid_house)
xs, ys = data.T
plt.scatter(xs, ys, marker='^')
data2 = np.array(grid_batteries)
xb, yb = data2.T
plt.scatter(xb, yb, marker='s')
plt.show()

#
# colors = {1: 'green', 2: 'red'}
#
# for house in house_list:
#     x = house.x_house
#     y = house.y_house
#     battery_number = house.connected_battery
#
#     plt.scatter(x, y, marker='^', color=colors[battery_number])
#
#     # voor de horizontale lijn
#     plt.plot((x, battery.x), (y, y), color=colors[battery_number])
#
#     # Voor de verticale lijn
#     plt.plot((battery.x, battery.x), (y, battery.y), color=colors[battery_number])
#
#
# for battery in battery_list:
#     x ...
#     y ...
#     battery_number = battery.battery_id
#
#     plt.scatter(x, y, marker='s', color=colors[battery_number])
#
# plt.show()
#
# for battery in battery_list:
#     for house in battery.connected_houses:
#         een manier om de xs en ys te verzamelen
#
#     battery_number = battery.battery_id
#     plt.scatter(xs, ys, marker='^', color=colors[battery_number])
#
#     plt.scatter(x, y, marker='s', color=colors[battery_number])
