# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# Ввод имен:
import random
while True:
    try:
        play_mode = int(input('Выберите режим игры: 1 - игрок против игрока, 2 - игрок против бота: '))
        if 1 <= play_mode <= 2:
            break
    except ValueError:
        print('Введите число 1 - игрок против игрока или 2 - игрок против бота: ')
if play_mode == 1:
    player1 = input('Введите имя игрока №1: ')
    player2 = input('Введите имя игрока №2: ')
else:
    player1 = input('Введите имя игрока №1: ')
    player2 = 'bot'
sum_konfet = 201
count = 0
print(f'Конфет на столе: {sum_konfet}')

# Розыгрыш права первого хода:
#--------------------------------------
first_move = random.randint(1, 2)
if first_move == 1:
    print(f'Начинает игрок: {player1}')
else:
    print(f'Начинает игрок: {player2}')
    player1, player2 = player2, player1
#--------------------------------------
if play_mode == 1:
#Игрок против игрока:
    while sum_konfet > 0:
        while sum_konfet >= 28:
            try:
                if count % 2 == 0:
                    player_number = int(input(f'{player1}, введите число от 1 до 28: '))
                else:
                    player_number = int(input(f'{player2}, введите число от 1 до 28: '))
                if 1 <= player_number <= 28:
                    break
            except ValueError:
                print('вы ввели не число, введите число в диапазоне от 1 до 28:')

        while 0 < sum_konfet < 28:
            try:
                if count % 2 == 0:
                    player_number = int(input(f'{player1}, введите число от 1 до {sum_konfet}: '))
                else:
                    player_number = int(input(f'{player2}, введите число от 1 до {sum_konfet}: '))
                if 1 <= player_number <= sum_konfet:
                    break
            except ValueError:
                print(f'вы ввели не число, введите число в диапазоне от 1 до {sum_konfet}:')

        sum_konfet -= player_number
        count += 1
        print(f'Конфет осталось: {sum_konfet}')
    else:
        if (count-1) % 2 == 0:
            print(f'Победитель {player1}')
        else:
            print(f'Победитель {player2}')
else:
    # Игрок против бота:
    while sum_konfet > 0:
        while sum_konfet >= 28:
            try:
                if first_move == 1:
                    if count % 2 == 0:
                        player_number = int(input(f'{player1}, введите число от 1 до 28: '))
                    else:
                        if sum_konfet > 56:
                            player_number = 28
                            print(f'{player1} ввел число {player_number}')
                        elif sum_konfet == 56:
                            player_number = 27 
                            print(f'{player1} ввел число {player_number}')
                        elif sum_konfet <= 28:
                            player_number = sum_konfet
                            print(f'{player1} ввел число {player_number}')
                        elif 29 < sum_konfet < 56:
                            player_number = sum_konfet - 29 
                            print(f'{player1} ввел число {player_number}')
                        else:
                            player_number = random.randint(1,28)
                            print(f'{player1} ввел число {player_number}') 
                if first_move == 2:
                    if count % 2 != 0:
                        player_number = int(input(f'{player2}, введите число от 1 до 28: '))
                    else:
                        if sum_konfet > 56:
                            player_number = 28
                            print(f'{player1} ввел число {player_number}')
                        elif sum_konfet == 56:
                            player_number = 27 
                            print(f'{player1} ввел число {player_number}')
                        elif sum_konfet <= 28:
                            player_number = sum_konfet
                            print(f'{player1} ввел число {player_number}')
                        elif 29 < sum_konfet < 56:
                            player_number = sum_konfet - 29 
                            print(f'{player1} ввел число {player_number}')
                        else:
                            player_number = random.randint(1,28)
                            print(f'{player1} ввел число {player_number}')                      
                if 1 <= player_number <= 28:
                    break
            except ValueError:
                print('вы ввели не число, введите число в диапазоне от 1 до 28:')

        while 0 < sum_konfet < 28:
            try:
                if first_move == 1:
                    if count % 2 == 0:
                        player_number = int(input(f'{player1}, введите число от 1 до {sum_konfet}: '))
                    else:
                        player_number = sum_konfet
                        print(f'{player1} ввел число {player_number}')
                if first_move == 2:
                    if count % 2 != 0:
                        player_number = int(input(f'{player2}, введите число от 1 до {sum_konfet}: '))
                    else:
                        player_number = sum_konfet
                if 1 <= player_number <= sum_konfet:
                    break
            except ValueError:
                print(f'вы ввели не число, введите число в диапазоне от 1 до {sum_konfet}:')

        sum_konfet -= player_number
        count += 1
        print(f'Конфет осталось: {sum_konfet}')
    else:
        if (count-1) % 2 == 0:
            print(f'Победитель {player1}')
        else:
            print(f'Победитель {player2}')

