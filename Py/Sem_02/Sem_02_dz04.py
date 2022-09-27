# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4,-3,-2, -1, 0,1,2, 3, 4, 5]
# ->15

pos1 = int(input('position one: '))
pos2 = int(input('position two: '))
n = int(input('N: '))
arr =[]
for i in range(-n,n):
    arr.append(i)
comp = arr[pos1-1]*arr[pos2-1]
print(f'{arr} -> {comp}')