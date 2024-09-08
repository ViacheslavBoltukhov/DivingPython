'''
Напишите генераторную функцию substrings(s), которая принимает строку
s и возвращает генератор всех возможных подстрок этой строки.
На вход подается строка abc
На выходе будут выведены обозначения:
a
ab
abc
b
bc
c
'''

def substrings(s: str):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]

print(*substrings(input()), sep='\n')