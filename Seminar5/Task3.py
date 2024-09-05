'''
 Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''
dct = {key: ord(key) for key in set(input()) if key.isalpha()}
dct_iter = iter(dct.items())
for _ in range(5):
    print(next(dct_iter))