# Игра морской бой
import random

game_field = [['+ ', '+ ', '+ '], ['+ ', '+ ', '+ '], ['+ ', '+ ', '+ ']]
field_size = 3

x_of_ship = random.randint(1, field_size)
y_of_ship = random.randint(1, field_size)

x_of_strike = 0
y_of_strike = 0

def print_game_field():
    print(" ", end=" ")
    for k in range(field_size):
        print(f'{k+1}', end='  ')
    print()
    for i in range(field_size):
        print(f'{i+1}', end=' ')
        for j in range(field_size):
            print(game_field[i][j], end=' ')
        print()

print_game_field()
# для примера оффтопа

while x_of_ship != x_of_strike and y_of_ship != y_of_strike:
    x_of_strike = int(input(f'Для выстрела введите номер строки от 1 до {field_size}: '))
    y_of_strike = int(input(f'а теперь выберите номер столбца от 1 до {field_size}: '))
    if x_of_ship != x_of_strike and y_of_ship != y_of_strike:
        game_field[x_of_strike - 1][y_of_strike - 1] = '0 '
        print_game_field()
        print("Мазила! ;-Р Пробуй ещё!")
        print()
    else:
        game_field[x_of_strike - 1][y_of_strike - 1] = 'Х '
        print_game_field()
        print('Завалил кабанчика! :)')
