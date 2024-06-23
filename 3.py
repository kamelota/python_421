def math_function_resolver(func: "функция с 1 аргументом x", *arg: tuple, res_to_str=False) -> list or None:
    """вычисляет округлённые значения для различных математических функций.
    Функция func принимает один обязательный позиционно-ключевой аргумент
    — число x, для которого необходимо вычислить значение математической функции"""
    try:
        return [round(func(i)) if res_to_str is False else str(round(func(i))) for i in arg]
    except TypeError:
        return None


# РЕЗУЛЬТАТ
# math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']
