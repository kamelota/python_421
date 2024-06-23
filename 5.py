from copy import deepcopy


def logger(func):
    """Генератор, который в стандартном потоке вывода ведёт журнал вызовов декорируемой функции.
    В журнал вносятся: имя функции, переданные аргументы (включая аргументы по умолчанию) и
    возвращаемое функцией значение.
    Если возникает исключение в журнал вносятся: имя и текст исключения.
    """
    def wrapper(*args, **kwargs):
        try:
            # имя функции
            name_func = func.__name__

            # список позиционных аргументов
            arg_func = list(args)
            # если количество переданных аргументов меньше количества объеявленных аргументов
            if len(args) != func.__code__.co_argcount:
                # добавляем значения по умолчанию
                arg_func.extend(list(func.__defaults__))

            # словарь ключевых аргументов, объявленных в функции
            kwargs_func = deepcopy(func.__kwdefaults__)
            # Словарь ключевых аргументов, обновленный значениями переданными из функции
            kwargs_func.update(kwargs)
            # форматирование ключевых аргументов в список в виде ключ = значение
            kwargs_func_update = (k+'='+str(v) for k, v in kwargs_func.items())

            # объединенный список всех аргументов
            arg_func.extend(kwargs_func_update)

            print(f'{name_func}(', end='')
            print(*arg_func, sep=', ', end='')
            print(')', end='')

            # возвращаемое значение функции
            result = func(*args, **kwargs)

            print(f' -> {result}')

            return result

        except Exception as exception:
            print(f' .. {type(exception).__name__}: {exception}')

    return wrapper

# РЕЗУЛЬТАТЫ
# >>> def div_round(num1, num2=2, *, digits=0, h):
#         return round(num1 / num2, digits)+h
#
# >>> div_round = logger(div_round)
# >>> div_round(1, 3, digits=2, h=6)
#     div_round(1, 3, digits=2, h=6) -> 6.33
#     6.33
# >>> div_round(7, 2, h=8)
#     div_round(7, 2, digits=0, h=8) -> 12.0
#     12.0
# >>> div_round(6, h=8)
#     div_round(6, 2, digits=0, h=8) -> 11.0
#     11.0
# >>> div_round(5, 0, h=7)
#     div_round(5, 0, digits=0, h=7) .. ZeroDivisionError: division by zero
# >>> div_round(5, 2)
#     div_round(5, 2, digits=0) .. TypeError: div_round() missing 1 required keyword-only argument: 'h'
