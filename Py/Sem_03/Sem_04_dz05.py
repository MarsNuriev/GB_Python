# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
while True:
    try:
        value = int(input('введите число value >= 1: '))
        if value >= 1:
            break
    except ValueError:
        print('------------')

arr = []

def fibo(x):
    sum_x = 0
    if x == 1 or x == 2:
        sum_x = 1
    elif x == 0:
        sum_x = 0
    else:
        sum_x = fibo(x-1) + fibo(x-2)
    return sum_x

def nega_fibo(y):
    sum_y = 0
    if y == -1:
        sum_y = 1
    elif y == -2:
        sum_y = -1
    elif y == 0:
        sum_y = 0    
    else:
        sum_y = ((-1)**(y+1))*fibo(abs(y))
    return int(sum_y)

for arr_index in range(-value, value+1, 1):
    if arr_index < 0:
        arr.append(nega_fibo(arr_index))
    else:
        arr.append(fibo(arr_index))

print(f'при value = {value} -> {arr}')