'''Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.'''
n = int(input())
print(hex(n)[2:])
n16 = ''
while n:
    x = n % 16
    if x > 9:
        n16 = chr(x + 87) + n16
    else:
        n16 = str(x) + n16
    n //= 16
print(n16)