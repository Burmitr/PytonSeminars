# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# first_list = input('Введите числа через пробел: ').split(' ')
# print (first_list)
# result_list = []

# for i in range(len(first_list)):
#     result_list.append(int(first_list[i]))

# print(min(result_list), max(result_list))



# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# *2) с помощью дополнительных библиотек Python

# a = int(input('Введите А: '))
# b = int(input('Введите B: '))
# c = int(input('Введите C: '))

# def solution(a, b, c):
#     desc = b**2 - (4*a*c)
#     if desc > 0:
#         desc = desc ** 0.5
#         answer1 = (-b - desc) / (2 *a)
#         answer2 = (-b + desc) / (2 *a)
#         return answer1, answer2
#     elif desc == 0:
#         desc = desc ** 0.5
#         answer = -b / (2 * a)
#         return answer
#     else:
#         print('Решения не существует')

# print (solution(a, b, c))




# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.
