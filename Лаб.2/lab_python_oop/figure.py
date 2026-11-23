from abc import ABC, abstractmethod


class Figure(ABC):
    name = "Геометрическая фигура"

    @classmethod
    def get_name(cls):
        return cls.name

    @abstractmethod
    def area(self):
        """Вычислить площадь фигуры."""
