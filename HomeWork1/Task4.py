n = int(input())
for i in range(1, n + 1):
    num = ''.join(str(j) for j in range(n, n - i, -1))
    print(num + '.' * (n - i) * 2 + num[::-1])