# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
while True:
    try:
        k = int(input('Введите k: '))
        break
    except ValueError:
        print('введите целое число: ')

def urav(value):
    my_list = []
    my_list1 = []
    for i in range(value+1):
        my_list.append(randint(0, 100))
    # print(my_list)
    for koef in range(value+1)[::-1]:
        if my_list[koef]!=0:
            my_list1.append(f'{my_list[koef]}x^{koef}')
    my_list1 = ' + '.join(map(str,my_list1))
    my_list1 = my_list1.replace('x^0','')
    my_list1 = my_list1.replace('x^1','x')
    my_list1 = f'{my_list1} = 0'
    return my_list1
# print(urav(k))
f = open('uravnenie.txt','w')
f.write(urav(k))
f.close