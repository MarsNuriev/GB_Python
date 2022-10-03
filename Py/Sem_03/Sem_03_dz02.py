# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
arr = []
arr_multy = []
n = random.randint(1, 10)
for arr_index in range(n):
    arr.append(random.randint(0, 10))

for arr_index1 in range(0,len(arr)):
    if arr_index1 <= (len(arr)-1)/2:
        arr_multy.append(arr[arr_index1]*arr[((len(arr)-1)-arr_index1)])


print(f'количество элементов в списке = {n}')
print(f'исходный список: {arr}')
print(f'произведение пар чисел: {arr_multy}')