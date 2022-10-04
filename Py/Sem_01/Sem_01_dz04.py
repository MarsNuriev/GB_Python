#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
while True:
    try:
        max_x = int(input('введите максимальную x: '))
        max_y = int(input('введите максимальную y: '))
        quart = int(input('выберите четверть от 1 до 4: '))
        if quart in (1,4):
            break
    except ValueError:
        print('введите число!')    
if quart == 1:
    print(f'координаты x = от 0 до {max_x}, y = от 0 до {max_y}')
elif quart == 2:
    print(f'координаты x = от 0 до {max_x}, y = от 0 до {-max_y}')
elif quart == 3:
    print(f'координаты x = от 0 до {-max_x}, y = от 0 до {-max_y}')
elif quart == 4:
    print(f'координаты x = от 0 до {-max_x}, y = от 0 до {max_y}')
