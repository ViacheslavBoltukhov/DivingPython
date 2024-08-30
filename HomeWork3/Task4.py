'''Напишите программу, которая генерирует случайный пароль заданной длины,
состоящий из букв, цифр и специальных символов.'''
from random import choices
from string import ascii_letters, digits, punctuation
alph = ascii_letters + digits + punctuation
len_pass = int(input('Enter len password: '))
print(''.join(choices(alph, k=len_pass)))
