def all_bull(balls: list):
    print(f'\n____ВСЕ ОЦЕНКИ____')
    for i in range(len(balls)):
        print(f'{i+1}: {balls[i]}')


def retake(balls: list):
    print(f'\n____ПЕРЕСДАЧА ЭКЗАМЕНА____')
    num = int(input('Введите номер в списке: '))
    ball = int(input('Введите новую оценку: '))
    balls[num-1] = ball
    print('Оценка изменена')


def stipend(balls: list):
    print(f'\n____СТИПЕНДИЯ____')
    if (sum(balls)/len(balls)>=10.7):
        print('Вам назначена стипендия')
    else:
        print ('Стипендия вам не назначена')

def insertion_sort(balls: list, type_sort='1'):
    """Сортировка вставками"""
    for i in range(1, len(balls), 1):
        item = balls[i]  # сохраняем i-ый элемент списка
        j = i - 1  # временная переменная
        while j >= 0 and balls[j] > item:
            balls[j + 1] = balls[j]
            j = j - 1  # j-=1
        balls[j + 1] = item
    if type_sort=='2':
        balls.reverse()


def sort_func(balls: list):
    type_sort = input('Сделать сортировку 1 - по возрастанию или 2 - по убыванию?')
    insertion_sort(balls, type_sort)
    all_bull(balls)


def academic_record():
    balls = [4, 7, 2, 3, 10, 12, 9, 8, 9, 10]
    button = '1'
    while('1' <= button <= '4'):
        print(f'\n___________МЕНЮ__________\n'
              f'1. Все оценки\n'
              f'2. Пересдача экзамена\n'
              f'3. Стипендия\n'
              f'4. Отсортированные оценки\n')
        button = input('Введите пункт меню: ')

        match button:
            case '1':
                all_bull(balls)
            case '2':
                retake(balls)
            case '3':
                stipend(balls)
            case '4':
                sort_func(balls)


academic_record()



