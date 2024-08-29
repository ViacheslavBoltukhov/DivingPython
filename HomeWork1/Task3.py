n = int(input('Введите количество чисел: '))
count = 0
for i in range(n):
    x = int(input('Введите число: '))
    if x > 1:
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                break
        else:
            count += 1
print(count)