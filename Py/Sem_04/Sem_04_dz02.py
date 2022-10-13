# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
while True:
    try:
        n = int(input('Введите N: '))
        break
    except ValueError:
        print('введите целое число: ')


def mnozh(value):
    value_print = value
    my_list = []
    mn = 2
    while value >= mn:
        if value % mn == 0:
            my_list.append(mn)
            value = value / mn
            mn = 2
        else:
            mn += 1
    return print (f'n = {value_print} -> {my_list}')

mnozh(n)
