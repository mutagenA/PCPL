def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            result = {key: item[key] for key in args if item.get(key) is not None}
            if result:
                yield result

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стол', 'price': None, 'color': 'brown'},
        {'title': None, 'price': None, 'color': 'white'},
    ]
    print("field(goods, 'title'):")
    print(*field(goods, 'title'), sep=', ')
    print("field(goods, 'title', 'price'):")
    for item in field(goods, 'title', 'price'):
        print(item)