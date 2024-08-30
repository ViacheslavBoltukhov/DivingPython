'''Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔Строки нумеруются начиная с единицы.
✔Слова выводятся отсортированными согласно кодировки Unicode.
✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.'''

whod = input("Введите текст: ")
arr_w = sorted(whod.split())
max_len = 0
for word in arr_w:
    cur_len = len(word)
    if cur_len > max_len:
        max_len = cur_len

for i, word in enumerate(arr_w, 1):
    print(f'{i}. {word:>{max_len}}')