# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# List comprehension

num = float(input('введите число: '))
num_str = str(num)
num_str = num_str.replace('.', '0')
if num_str[0] == '-':
    sum = int(num_str[1])*-1*2
else:
    sum = 0
num_str = num_str.replace('-', '0')
arr = [i for i in num_str]  # list comprehension
# for _ in num_str:
#     arr.append(_)
print(arr)

for _ in arr:
    arr_int = int(_)
    sum += arr_int
print(f"{num} -> {sum}")
