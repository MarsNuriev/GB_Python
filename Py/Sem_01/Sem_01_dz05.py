# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
while True:
    try:
        p_ax = int(input('введите коордиату x точки A: '))
        p_ay = int(input('введите коордиату y точки A: '))
        p_bx = int(input('введите коордиату x точки B: '))
        p_by = int(input('введите коордиату y точки B: '))
        break
    except ValueError:
        print('введите число!')    
dlina = round(((p_ax-p_bx)**2 + (p_ay-p_by)**2)**(0.5),2)
print(f'A ({p_ax}, {p_ay}); B ({p_bx}, {p_by}) -> {dlina}')
