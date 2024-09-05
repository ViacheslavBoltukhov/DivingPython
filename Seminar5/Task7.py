'''
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''


def prime(count_prime: int) -> int:
    for num in range(2, count_prime + 1):
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                break
        else:
            yield num


print(*prime(int(input())))
