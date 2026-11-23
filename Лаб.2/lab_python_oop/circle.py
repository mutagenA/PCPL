from math import pi

from .color import FigureColor
from .figure import Figure


class Circle(Figure):
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return "{}: радиус {}, цвет {}, площадь {:.2f}".format(
            self.get_name(), self.radius, self.color.color, self.area()
        )
