# Задайте список из n чисел, заполненный по формуле (1 + 1/n) * n и выведите на экран их сумму.
# Для n = 6: [2 2,2,2.2,3] -> 13


# lambda, map
n = int(input('введите n: '))
arr = list(map(lambda x: (1+1/x)*x,[i for i in range(1,n)]))
arr = list(map(int, arr))
print(arr)

# for i in range(1, n):
#     arr.append(int((1+1/i)*i))
sum = 0
for j in arr:
    sum = sum + j
print(f'n = {n}: {arr} -> {sum}')