# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# num = int(input('Введите число: '))
# if (num >= 1) and (num <=7):
#     print('Число обозначает день недели!')
# else:
#     print('Число не является днем недели.')
num = int(input('Введите число: '))
if (num < 1) or (num > 7):
    print ('Ой, это не день недели!')
elif num > 5:
    print('Всё верно, это выходной день!')
else:
    print('Увы, но это рабочий день!)')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# x = int(input('Введите число x: '))
# y = int(input('Введите число y: '))
# z = int(input('Введите число z: '))

# a = x * y * z
# b = x + y + z

# if a > 0:
#     a = 0
# elif a < 1:
#     a = 1
# if b > 0:
#     b = 1
# elif b < 1:
#     b = 1

# if a == b:
#     print('Истина')
# elif a != b:
#     print('Ложь')




# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координату Х: '))
# y = int(input('Введите координату Y: '))

# if x == 0 or y == 0:
#     print('Ошибка! Х/Y не может быть равен 0!')

# if x > 0 and y > 0:
#     print('--> 1')
# if x > 0 and y < 0:
#     print('--> 2')
# if x < 0 and y < 0:
#     print('--> 3')
# if x < 0 and y > 0:
#     print('--> 4')




# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
 
# num_quater = int(input('Введите номер четверти: '))
# if num_quater < 1 or num_quater > 4:
#     print('Число вне доступного диапазона! Укажите от 1 до 4 включительно.')
# elif num_quater == 1:
#     print('x > 0 and y > 0')
# elif num_quater == 2:
#     print('x > 0 and y < 0')
# elif num_quater == 3:
#     print('x < 0 and y < 0')
# elif num_quater == 4:
#     print('x < 0 and y > 0')



# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from math import sqrt

# print('Введите координаты точки А:')
# xA = float(input('X: '))
# yA = float(input('Y: '))
# print('Введите координаты точки В:')
# xB = float(input('X: '))
# yB = float(input('Y: '))

# print('Расстояние между точками A и B: ',round(sqrt((xA - xB)**2 + (yA - yB)**2), 2))