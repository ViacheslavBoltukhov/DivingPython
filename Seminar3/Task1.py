data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
print(list(set(data)))
data_new = []
for item in data:
    if item not in data_new:
        data_new.append(item)
print(data_new)