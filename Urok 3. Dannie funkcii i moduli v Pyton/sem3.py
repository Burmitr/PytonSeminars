# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time

for i in range(10):
    a = time.time()
    print((int(a * 1000000) % 100))


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"

# mylist = ['65h34q', 'sdg634d', '147jnbv']
# n = 7

# for i in mylist:
#     if i.find(n) >= 0:
#         print (i)



# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# mylist = ["qwe", "asd", "qwe", "zxc", "qwe", "ertqwe"]
# item = 'qwe'
# count = 0

# for i in range(0, len(mylist)):
#     if mylist[i] == item:
#         count += 1
#         if count == 2:
#             print (i)
#             break
# if count < 2:
#     print ('None')