'''
Степан использует калькулятор для расчёта суммы и разности чисел, но на
работе ему требуются не только обычные арифметические действия. Он ничего
не хочет делать вручную, поэтому решил немного расширить функционал
калькулятора.
Напишите программу, запрашивающую у пользователя число и действие,
которое нужно сделать с числом: вывести сумму его цифр, максимальную или
минимальную цифру. Каждое действие оформите в виде отдельной функции, а
основную программу зациклите.
Запрошенные числа должны передаваться в функции суммы, максимума и
минимума при помощи аргументов.
'''


def sum_digits(num: int) -> int:
    summa = 0
    while num:
        summa += num % 10
        num //= 10
    return summa


def min_digit(num: int) -> int:
    min_d = 10
    while num:
        min_d = min(min_d, num % 10)
        num //= 10
    return min_d


def max_digit(num):
    max_d = -1
    while num:
        max_d = max(max_d, num % 10)
        num //= 10
    return max_d


num_in = int(input())
oper = int(input('Input number operation:\n'
                 '1 - Summa digits of numbers\n'
                 '2 - Minimum digit\n'
                 '3 - Maximum digit\n'))

if oper == 1:
    print(sum_digits(num_in))
elif oper == 2:
    print(min_digit(num_in))
elif oper == 3:
    print(max_digit(num_in))
else:
    print('Error operation')
