class House(object):

    def __init__(self, id, x_pos, y_pos, output):
        """
        Initializes an Item
        """
        self.id = id
        self.x_house = x_pos
        self.y_house = y_pos
        self.max_output = output

    # Accessor methods (getters)
    def get_id(self):
        """
        Returns id of house.
        """
        return self.id

    def get_coord(self):
        """
        Returns coordinates of house.
        :return: int, int
        """
        return self.x_house, self.y_house

    def get_x(self):
        return self.x_house

    def get_y(self):
        return self.y_house

    def get_max(self):
        """
        Returns maximum output of house.
        :return:
        """
        return self.max_output

    def __str__(self):
        return f"House {self.id} \nCoordinates (x,y): {self.x_house},{self.y_house}\nMaximum Output: {self.max_output}"
