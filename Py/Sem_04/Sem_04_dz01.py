# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

while True:
    try:
        d = float(input('Введите точность d: '))
        break
    except ValueError:
        print('введите число 10^{-1} ≤ d ≤10^{-10}: ')

def okrugl(value):
    value_round = len(str(d))-2
    value = round(value,value_round)

    return print(value)

okrugl(3.3476374638)