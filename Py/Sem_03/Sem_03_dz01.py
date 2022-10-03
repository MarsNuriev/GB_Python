# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
arr = []
arr_sum = 0
n = random.randint(2, 20)
for arr_index in range(n):
    arr.append(random.randint(0, 100))

for arr_index1 in range(0,len(arr)):
    if arr_index1 % 2 != 0:
        arr_sum = arr_sum + arr[arr_index1]


print(f'количество элементов в списке = {n}')
print(f'исходный список: {arr}')
print(f'сумма нечетных элементов на нечетных поициях: {arr_sum}')
