'''Напишите функцию, которая принимает строку текста.
✔ Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки'''

def func(s: str) -> str:
    lst = sorted(s.split())
    max_len = len(max(lst, key=len))
    return '\n'.join(f'{i} {word:>{max_len}}' for i, word in enumerate(lst, 1))

print(func(input('Input text: ')))