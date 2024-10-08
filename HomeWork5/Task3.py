'''
Напишите генераторную функцию fibonacci(n), которая принимает на вход
одно целое число n и возвращает последовательность первых n чисел
Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
число является суммой двух предыдущих, начиная с 0 и 1.
'''

def fibonacci(n: int):
    fib = [0, 1]
    if n < 2:
        return fib[:n]
    else:
        for i in range(n - 2):
            fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(int(input())))