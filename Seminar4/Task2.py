'''Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''

def sotr_unicode(st: str) -> list[int]:
    st = sorted(set(st))
    return [ord(symb) for symb in st]

letters = input()
print(sotr_unicode(letters))