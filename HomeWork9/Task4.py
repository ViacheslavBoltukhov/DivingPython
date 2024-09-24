'''
Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
результаты вызова функции и, при повторном вызове с теми же аргументами,
возвращает сохранённый результат.
Примените его к рекурсивной функции вычисления чисел Фибоначчи.
В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
если такие аргументы уже использовались, должен вернуть сохранённый результат
вместо запуска расчёта.
'''


def cache_decorator(func):
    cache = {}  # Словарь для хранения кэшированных результатов

    def wrapper(number):
        if number in cache:
            return cache[number]
        result = func(number)
        cache[number] = result  # Сохраняем результат в кэше
        return result

    return wrapper


@cache_decorator
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5))
