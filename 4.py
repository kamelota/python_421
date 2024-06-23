def repeat(repeats=2):
    """Декоратор - повторение выполнения кода repeats раз"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeats):
                print(f'{i+1}: ', end='')
                val = func(*args, **kwargs)
            return val
        return wrapper
    return decorator


@repeat(repeats=3)
def testing_function_1():
    print('Три раза')


testing_function_1()


@repeat()
def testing_function_2(name):
    print(f'Hello {name}!')


testing_function_2('Ирина')

# РЕЗУЛЬТАТ
# 1: Три раза
# 2: Три раза
# 3: Три раза
# 1: Hello Ирина!
# 2: Hello Ирина!
