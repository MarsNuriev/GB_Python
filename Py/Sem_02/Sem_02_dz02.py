# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1-1*1,2-1*2,3-1*2*3,4-1*2*3*4итд.

# -4 -> 1,2,6,24]

# -6 -> 1,2, 6, 24, 120, 720]

n = int(input('введите N: '))
nn = int((n**2)**0.5)
i =1
comp = 1
while i <= nn:
    comp = comp*i
    i +=1
print(f'N = {n} -> {comp}')