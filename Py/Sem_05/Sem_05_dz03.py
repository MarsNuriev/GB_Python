#Создайте программу для игры в ""Крестики-нолики"".
# Инициализация карты
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# # Инициализация победных линий
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 
# # Сделать ход в ячейку
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# # Получить текущий результат игры
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# # Основная программа
# game_over = False
# player1 = True
# player2 = input('введите имя игрока 2')
 
# while game_over == False:
 
#     # 1. Показываем карту
#     print_maps()
 
#     # 2. Спросим у играющего куда делать ход
#     if player1 == True:
#         symbol = "X"
#         step = int(input(f"{player1}, ваш ход X "))
#     else:
#         symbol = "O"
#         step = int(input(f"{player2}, ваш ход О: "))
 
#     step_maps(step,symbol) # делаем ход в указанную ячейку
#     win = get_result() # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
 
# # Игра окончена. Покажем карту. Объявим победителя.        
# print_maps()
# print("Победил", win)


board = list(range(1,10))

def draw_board(value):
   print("-" * 13)
   for i in range(3):
      print("|", value[0+i*3], "|", value[1+i*3], "|", value[2+i*3], "|")
      print("-" * 13)

def player_input(symbol_x_y):
   valid = False
   while not valid:
      try:
         player_number = int(input(f"Выберите клетку для {symbol_x_y}: "))
      except ValueError:
         print("Некорректный ввод. Введите число: ")
      
      if 1 <= player_number <= 9:
         if(str(board[player_number-1]) not in "XO"):
            board[player_number-1] = symbol_x_y
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(value):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for _ in win_coord:
       if value[_[0]] == value[_[1]] == value[_[2]]:
          return value[_[0]]
   return False

def main(value):
    count = 0
    win = False
    while not win:
        draw_board(value)
        if count % 2 == 0:
           player_input("X")
        else:
           player_input("O")
        count += 1
        if count > 4:
           tmp = check_win(value)
           if tmp:
              draw_board(value)
              print(tmp, "выиграл!")
              win = True
              break
        if count == 9:
            draw_board(value)
            print("Ничья!")
            break
    #draw_board(value)

main(board)