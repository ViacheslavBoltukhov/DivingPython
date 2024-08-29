'''Программа принимает два целых числа и находит их наибольший общий
делитель (НОД)'''
print(__import__('math').gcd(int(input()), int(input())))
# a, b = int(input()), int(input())
# while a:
#     a, b = b % a, a
# print(b)