max_n = 1
min_n = 100
count = 0
while True:
    count += 1
    n = (min_n + max_n) // 2
    print('Загаданное число равно, меньше или больше', n)
    ans = int(input('''Загаданное число: 
    1 - равно
    2 - меньше
    3 - больше
'''))
    if ans == 1:
        print('Я угадал! Ура! с', count, 'попытки')
        break
    elif ans == 2:
        max_n = n
    else:
        min_n = n