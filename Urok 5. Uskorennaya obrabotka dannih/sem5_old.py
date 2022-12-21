# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5

# path = 'G:/Мой диск/GeekBrains/Факультеты/Разработчик - Программист/Знакомство с языком Python/Семинары/Урок 5. Ускоренная обработка данных lambda, filter, map, zip, enumerate, list comprehension/file.txt'
# f = open (path, 'r')

# output1 = f.read()

# nlist = output1.split(' ')
# print(nlist)

# for i in range(1, len(nlist)):
#     if int(nlist[i]) -1 != int(nlist[i-1]):
#         numb = int(nlist[i])-1

# print (numb)

# my_list = [int(nlist[i])-1 for i in range(1, len(nlist)) if int(nlist[i]) -1 != int(nlist[i-1])]
# print (my_list)



# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# count = 0
# new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] >= max(my_list[0:i])]
# new_list.insert(0, my_list[0])

# print(new_list)



# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'


# my_str = 'Мы неабв очень любим Питон иабв Джавабв'
# sub_str = 'абв'
# my_list = my_str.split()
# print(my_list)

# res_list = [item for item in my_list if sub_str not in item]

# print(res_list)