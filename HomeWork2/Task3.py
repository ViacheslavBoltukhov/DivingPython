'''Программа принимает целое число и возвращает его римское представление в
виде строки.'''
dct_to_rum = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}
num = int(input('Введите число в десятмчной СС: '))
num_rum = ''
while num:
    for key in dct_to_rum.keys():
        if num >= key:
            num_rum += dct_to_rum[key]
            num -= key
            break
print(num_rum)