import sys
import math

def get_coef(index, prompt):
    coef_str = None
    if len(sys.argv) > index:
        coef_str = sys.argv[index]
    while True:
        try:
            return float(coef_str)
        except (ValueError, TypeError):
            print(prompt)
            coef_str = input()

def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D < 0.0:
        return result
    sqD = math.sqrt(D)
    y_list = [(-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a)]
    for y in y_list:
        if y >= 0.0:
            x = math.sqrt(y)
            for root in (x, -x):
                if root not in result:
                    result.append(root)
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    if a == 0.0:
        print('Коэффициент A не может быть равен 0')
        return
    roots = get_roots(a, b, c)
    if len(roots) == 0:
        print('Нет действительных корней')
    else:
        print('Количество корней: {}'.format(len(roots)))
        for root in roots:
            print(root)

if __name__ == "__main__":
    main()