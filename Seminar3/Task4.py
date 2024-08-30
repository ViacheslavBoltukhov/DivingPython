'''Задание №4
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.'''

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
COUNT = 2
new_data = []
for item in data:
    if data.count(item) != COUNT:
        new_data.append(item)
print(new_data)


from collections import Counter
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
COUNT = 2
new_data = []
count_data = Counter(data)
for key, val in count_data.items():
    if val != COUNT:
        new_data.extend([key] * val)
print(new_data)