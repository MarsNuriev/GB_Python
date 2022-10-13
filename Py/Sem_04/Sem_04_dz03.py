# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
my_list = []
n = random.randint(10, 20)
for arr_index in range(n):
    my_list.append(random.randint(0, 10))

def uniq(some_list):
    uniq_list = []
    for i in some_list:
        if some_list.count(i) == 1:
            uniq_list.append(i)
    return print (f'исходный список: {my_list} --> список неповторяющихся элементов: {uniq_list}')

uniq(my_list)
