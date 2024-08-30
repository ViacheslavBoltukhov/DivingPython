'''Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов'''
elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(list(set(elements)))
# dubl = []
# for item in elements:
#     if item not in dubl:
#         dubl.append(item)
# print(dubl)