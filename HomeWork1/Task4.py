'''Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы'''
n = int(input())
for i in range(1, n + 1):
    num = ''.join(str(j) for j in range(n, n - i, -1))
    print(num + '.' * (n - i) * 2 + num[::-1])