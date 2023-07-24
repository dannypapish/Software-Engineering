import math


class Polygons:

    def __init__(self, num_sides, side_length):
        """
        A class that represents a regular polygon.

        attributes:
            - num_sides: the number of sides of the polygon
            - side_length: the length of each side of the polygon
            - radius: the radius of the circumscribed circle of the polygon
            - area: the area of the polygon
        """

        # TODO 7: Create an attribute called num_sides and set it to the num_sides given in the constructor
        self.num_sides = num_sides

        # TODO 8: Create an attribute called side_length and set it to the side_length given in the constructor
        self.side_length = side_length

        # TODO 9: Create an attribute called radius and set it equal to the result of the following formula:
        # - side_length / (2 * sin(pi / num_sides))
        # - use the math library to get the value of pi and the sin() function
        self.radius = side_length / (2 * math.sin(math.pi / num_sides))

        # TODO 10: Create an attribute called area and set it equal to the result of the polygon_area() method
        self.area = self.polygon_area()

    def polygon_area(self):
        """
        Method that calculates the area of the polygon from the number of sides and side length.
        returns:
            - the area of the polygon
        """
        return self.num_sides * self.side_length ** 2 / (4 * math.tan(math.pi / self.num_sides))
