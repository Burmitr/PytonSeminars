# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# sum = 0
#
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
#     else:
#         i += 1
#
# print(my_list)
# print(sum)
# _________________________________


# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
#
# from random import randint
#
# line_a = int(input('Задайте количество строк: '))
# column_b = int(input('Задайте количество столбцов: '))
# average = []
#
# mass_a_b = [[randint(1, 10) for j in range(column_b)] for i in range(line_a)]
# for row in mass_a_b: print(row)
#
#
# for i in range(len(mass_a_b)):
#     summ = 0
#     for j in range(len(mass_a_b[i])):
#         summ += mass_a_b[i][j]
#     # average.append(summ // len(mass_a_b[i]))
#     average.append(summ // len(mass_a_b[i]))
#
# print(f'Cреднее арифметическое строк массива: {average}')

# _________________________________


# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

# from random import randint
# def sel_sort(array):
#     for i in range(len(array) - 1):
#         min_index = i
#         temp = i + 1
#         while temp < len(array):
#             if array[temp] < array[min_index]:
#                 min_index = temp
#             temp += 1
#         array[i], array[min_index] = array[min_index], array[i]
#
# num = 30 # кол-во элементов массива
# my_list = []
#
# for i in range(num):
#     my_list.append(randint(1, 90))
#
# print(f'Исходный список: \n', my_list)
# sel_sort(my_list)
# print('Отсортированный список: \n', my_list)