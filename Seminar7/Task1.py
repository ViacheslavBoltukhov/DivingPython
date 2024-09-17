'''
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
'''
from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def addition_num(name, inlines):
    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(inlines):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    lines = int(input('Введите количество строк: '))
    file_name = input('Введите имя файла: ')

    addition_num(file_name, lines)