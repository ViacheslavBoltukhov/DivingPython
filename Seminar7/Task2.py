from random import randint, choices
from string import ascii_lowercase

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def generate_name(filename, name_count):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(name_count):
            name = ''.join(choices(ascii_lowercase, k=randint(MIN_LEN, MAX_LEN)))
            if len(set(name) - set(CONSONANTS)) != 0:
                f.write(f'{name.capitalize()}\n')


generate_name(input(), int(input()))
