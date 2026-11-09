try:
    from .gen_random import gen_random
except ImportError:
    from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            key = item
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print('Unique(data):', list(Unique(data)))

    data = gen_random(10, 1, 3)
    print('Unique(gen_random(10, 1, 3)):', list(Unique(data)))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Unique(data):', list(Unique(data)))
    print('Unique(data, ignore_case=True):',
          list(Unique(data, ignore_case=True)))