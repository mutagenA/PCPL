from .color import FigureColor
from .figure import Figure


class Rectangle(Figure):
    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return (
            "{}: ширина {}, высота {}, цвет {}, площадь {:.2f}"
            .format(self.get_name(), self.width, self.height,
                    self.color.color, self.area())
        )
