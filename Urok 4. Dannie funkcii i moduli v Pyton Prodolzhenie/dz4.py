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

line_a = int(input('Задайте количество строк: '))
column_b = int(input('Задайте количество столбцов: '))




# _________________________________


# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.