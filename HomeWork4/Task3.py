'''
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
каждое число на число, которое получается из исходного записью его цифр в
обратном порядке, затем складывает их, снова переворачивает и выводит
ответ на экран.
Пример:
Введите первое число: 102
Введите второе число: 123
Первое число наоборот: 201
Второе число наоборот: 321
Сумма: 522
Сумма наоборот: 225
'''


def revers_number(num: int) -> int:
    res = 0
    while num:
        res = res * 10 + num % 10
        num //= 10
    return res


n = int(input('Enter the first number: '))
m = int(input('Enter the second number: '))
n_revers = revers_number(n)
m_revers = revers_number(m)
print('First number revers:', n_revers)
print('Second number revers:', m_revers)
summa = n_revers + m_revers
print('Summa:', summa)
print('Summa revers: ', revers_number(summa))