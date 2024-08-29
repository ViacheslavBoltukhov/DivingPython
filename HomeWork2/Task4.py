'''Программа принимает две строки вида "a/b" - дробь с числителем и
знаменателем. Возвращает сумму и произведение дробей. Для проверки
используется модуль fractions'''
from fractions import Fraction
a1, b1 = map(int, input().split('/'))
a2, b2 = map(int, input().split('/'))
print(Fraction(a1, b1) + Fraction(a2, b2))
den = __import__('math').lcm(b1, b2)
num = a1 * den // b1 + a2 * den // b2
nod = __import__('math').gcd(num, den)
print(f'{num // nod}/{den // nod}')