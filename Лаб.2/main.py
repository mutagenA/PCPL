import argparse

import numpy as np

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


def main():
    parser = argparse.ArgumentParser(description="Площади геометрических фигур")
    parser.add_argument("variant", type=int, metavar="N",
                        help="номер по списку группы")
    args = parser.parse_args()
    n = args.variant
    if n < 1:
        parser.error("номер варианта должен быть положительным")

    figures = (
        Rectangle(n, n, "синий"),
        Circle(n, "зелёный"),
        Square(n, "красный"),
    )
    print("Вариант {}".format(n))
    for figure in figures:
        print(repr(figure))

    total_area = np.sum([figure.area() for figure in figures])
    print("Суммарная площадь (NumPy): {:.2f}".format(total_area))


if __name__ == "__main__":
    main()
