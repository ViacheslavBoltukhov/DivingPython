'''
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''


def unicode_symbol(start: int, stop: int) -> dict[int, str]:
    return {key: chr(key) for key in range(start, stop + 1)}


start_in, stop_in = map(int, input().split())
print(unicode_symbol(start_in, stop_in))
