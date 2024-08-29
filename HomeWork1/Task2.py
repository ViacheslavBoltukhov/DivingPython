a, b, c = float(input()), float(input()), float(input())
if a < b + c and b < a + c and c < a + b:
    print('Треугольник существует')
    if a == b and b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')