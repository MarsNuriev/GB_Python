# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
arr = []
arr_div = []
n = random.randint(1, 10)
for arr_index in range(n):
    arr.append(round(random.uniform(0, 10), 2))


for arr_index1 in range(0,len(arr)):
    arr_div.append(round(arr[arr_index1] % 1, 2))

razn_max_min = int(round((max(arr_div) - min(arr_div))*100,0))


print(f'количество элементов в списке = {n}')
print(f'исходный список: {arr} -> разница между макс и мин остатком равна: {razn_max_min}')

