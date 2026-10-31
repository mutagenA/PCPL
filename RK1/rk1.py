from operator import itemgetter


class Composition:
    def __init__(self, id, title, duration, orch_id):
        self.id = id
        self.title = title
        self.duration = duration
        self.orch_id = orch_id


class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompOrch:
    def __init__(self, orch_id, comp_id):
        self.orch_id = orch_id
        self.comp_id = comp_id


orchestras = [
    Orchestra(1, 'Симфонический оркестр'),
    Orchestra(2, 'Камерный оркестр'),
    Orchestra(3, 'Струнный оркестр'),
    Orchestra(4, 'Духовой оркестр'),
]

compositions = [
    Composition(1, 'Адажио соль минор', 9, 3),
    Composition(2, 'Аве Мария', 6, 2),
    Composition(3, 'Болеро', 15, 1),
    Composition(4, 'Времена года', 42, 2),
    Composition(5, 'Шехеразада', 45, 1),
    Composition(6, 'Арлезианка', 17, 1),
]

comps_orchs = [
    CompOrch(1, 3), CompOrch(1, 5), CompOrch(1, 6),
    CompOrch(2, 2), CompOrch(2, 4), CompOrch(2, 1),
    CompOrch(3, 1), CompOrch(3, 2),
    CompOrch(4, 3), CompOrch(4, 6),
]


def get_one_to_many(comps, orchs):
    return [(c.title, c.duration, o.name)
            for o in orchs
            for c in comps
            if c.orch_id == o.id]


def get_many_to_many(comps, orchs, links):
    temp = [(o.name, l.comp_id)
            for o in orchs
            for l in links
            if o.id == l.orch_id]
    return [(c.title, c.duration, orch_name)
            for orch_name, comp_id in temp
            for c in comps
            if c.id == comp_id]


def task1(one_to_many):
    return [(title, orch)
            for title, _, orch in one_to_many
            if title.startswith('А')]


def task2(one_to_many, orchs):
    res = [(o.name, min(durs))
           for o in orchs
           if (durs := [d for _, d, name in one_to_many
                        if name == o.name])]
    return sorted(res, key=itemgetter(1))


def task3(many_to_many):
    return sorted(((title, orch) for title, _, orch in many_to_many),
                  key=itemgetter(0))


def main():
    one_to_many = get_one_to_many(compositions, orchestras)
    many_to_many = get_many_to_many(compositions, orchestras,
                                    comps_orchs)

    print('Задание В1')
    for title, orch in task1(one_to_many):
        print(f'  {title} — {orch}')

    print('\nЗадание В2')
    for orch, min_dur in task2(one_to_many, orchestras):
        print(f'  {orch}: {min_dur} мин')

    print('\nЗадание В3')
    for title, orch in task3(many_to_many):
        print(f'  {title} — {orch}')


if __name__ == '__main__':
    main()
