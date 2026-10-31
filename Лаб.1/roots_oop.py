import sys
import math

class BiquadraticRoots:

    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.num_roots = 0
        self.roots_list = []

    def get_coef(self, index, prompt):
        coef_str = None
        if len(sys.argv) > index:
            coef_str = sys.argv[index]
        while True:
            try:
                return float(coef_str)
            except (ValueError, TypeError):
                print(prompt)
                coef_str = input()

    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        D = b*b - 4*a*c
        if D < 0.0:
            return
        sqD = math.sqrt(D)
        y_list = [(-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a)]
        for y in y_list:
            if y >= 0.0:
                x = math.sqrt(y)
                for root in (x, -x):
                    if root not in self.roots_list:
                        self.roots_list.append(root)
        self.num_roots = len(self.roots_list)

    def print_roots(self):
        if self.num_roots == 0:
            print('Нет действительных корней')
        else:
            print('Количество корней: {}'.format(self.num_roots))
            for root in self.roots_list:
                print(root)

def main():
    r = BiquadraticRoots()
    r.get_coefs()
    if r.coef_A == 0.0:
        print('Коэффициент A не может быть равен 0')
        return
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()
