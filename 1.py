from ref_1 import *


def pick_resistors(resistor: int) -> dict or None:
    """Функция подбирает ближайшие к переданному номиналы сопротивления из всех рядов сопротивлений"""
    try:
        if not isinstance(resistor, int) or not (100 <= resistor <= 999):
            raise ValueError

        def min_rez(t):
            """Ищет минимальное расхожение между значением сопротивления и номинальным значением"""
            return min(list(map(lambda i: abs(i - resistor), t)))

        def ty(t):
            """Возвращает список (ключ, (ближайшие номинальные значения сопротивления))"""
            return t[0], tuple(filter(lambda x: x == resistor - min_rez(t[1]) or x == resistor + min_rez(t[1]), t[1]))

        return dict(map(ty, resistance_ratings.items()))
    except ValueError:
        return None

# РЕЗУЛЬТАТЫ
# pick_resistors(112)
# {'E6': (100,), 'E12': (120,), 'E24': (110,), 'E48': (110,), 'E96': (113,)}
# pick_resistors(549)
# {'E6': (470,), 'E12': (560,), 'E24': (560,), 'E48': (536, 562), 'E96': (549,)}
# pick_resistors('549')
# pick_resistors(54)
# pick_resistors(1120)
