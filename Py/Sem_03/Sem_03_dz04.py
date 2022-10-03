# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
while True:
    try:
        value = int(input('Введите целое положительное число: '))
        value_fix = value
        if value > 0:
            break
    except ValueError:
        print('------')
arr = []
while value // 2 >= 1:
    arr.append(value - (value//2)*2)
    value = value // 2
if value % 2 != 0:
    arr.append(1)
else:
    arr.append(0)
arr.reverse()
print(f"{value_fix} -> {''.join(map(str,arr))}")