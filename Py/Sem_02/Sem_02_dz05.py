# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10

# -> [0, 1,2, 3, 4, 5, 6, 7, 8, 9]

# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
n = int(input('ввведите n: '))
arr = []
for i in range(0,n):
    arr.append(i)
print(arr)
for i in range(0,len(arr)):
    a = random.randint(0,len(arr)-1)
    arr[i],arr[a] = arr[a],arr[i]
print(arr)