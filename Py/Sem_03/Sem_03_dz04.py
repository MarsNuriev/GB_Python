# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

value = int(input('Введите целое число: '))
value_fix = value
arr = []
while value // 2 >= 1:
    arr.append(value - (value//2)*2)
    value = value // 2
if value % 2 != 0:
    arr.append(1)
else:
    arr.append(0)
# arr_reversed = arr.reverse()
arr.reverse()
print(f"{value_fix} -> {''.join(map(str,arr))}")