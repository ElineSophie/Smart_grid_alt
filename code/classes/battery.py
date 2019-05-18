class Battery(object):

    def __init__(self, id, x_pos, y_pos, capacity):
        """
        Initializes an Item
        """
        self.id = id
        self.x_battery = int(x_pos)
        self.y_battery = int(y_pos)
        self.capacity = float(capacity)
        self.capacity_available = 0

    def __str__(self):
        return f"House {self.id} \nCoordinates (x,y): {self._x_house},{self._y_house}\nMaximum Output: {self.max_output}"
