'''Напишите программу, которая принимает список чисел через строку и
возвращает наибольшее число в этом списке.'''
print(max(map(int, input().split())))
# nums = input().split()
# max_num = int(nums[0])
# for item in nums[1:]:
#     max_num = max(max_num, int(item))
# print(max_num)