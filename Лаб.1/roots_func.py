import sys
import math


def parse_float(text):
    try:
        return float(text)
    except (ValueError, TypeError):
        return None

def get_coef(prompt, text=None):
    value = parse_float(text)
    match value:
        case None:
            print(prompt)
            return get_coef(prompt, input())
        case _:
            return value

def get_arg(index):
    return sys.argv[index] if len(sys.argv) > index else None

def get_y_roots(a, b, c):
    D = b*b - 4*a*c
    match D:
        case d if d < 0.0:
            return []
        case 0.0:
            return [-b / (2.0*a)]
        case d:
            sqD = math.sqrt(d)
            return [(-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a)]

def y_to_x(y):
    match y:
        case 0.0:
            return [0.0]
        case v if v > 0.0:
            r = math.sqrt(v)
            return [-r, r]
        case _:
            return []

def get_roots(a, b, c):
    xs = [x for y in get_y_roots(a, b, c) for x in y_to_x(y)]
    return sorted(set(xs))

def format_roots(roots):
    match roots:
        case []:
            return 'Нет действительных корней'
        case _:
            lines = ['Количество корней: {}'.format(len(roots))]
            lines += [str(x) for x in roots]
            return '\n'.join(lines)

def main():
    a = get_coef('Введите коэффициент А:', get_arg(1))
    b = get_coef('Введите коэффициент B:', get_arg(2))
    c = get_coef('Введите коэффициент C:', get_arg(3))
    match a:
        case 0.0:
            print('Коэффициент A не может быть равен 0')
        case _:
            print(format_roots(get_roots(a, b, c)))

if __name__ == "__main__":
    main()