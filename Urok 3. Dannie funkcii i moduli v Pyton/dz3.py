# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
#
# def hexadecimal(decimal):
#     answer = ''
#     while decimal > 0:
#         temp = decimal % 16
#         answer = conversion_table[temp] + answer
#         decimal //= 16
#     return answer
import sys

# num = int(input('Введите число: '))
#
# conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
#                     5: '5', 6: '6', 7: '7',
#                     8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
#                     13: 'D', 14: 'E', 15: 'F'}
#
# print (hexadecimal(num))



# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

#def isfloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False
#
# text = input('Введите данные: ')
# if isfloat(text):
#     print('Введено дробное число!')
# else:
#     print('Это не число!')



# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней
# буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.
#
# text = input('Введите текст: ')
# text = text.lower()
#
# index_min = text.find('о')
# index_max = text.find('о', index_min+1)
#
# if index_max <= 0:
#     print('В данном тексте только одна буква "О"!')
#     sys.exit()
#
# first_part = text[:index_min]
# second_part = text[index_max:index_min-1:-1]
# last_part = text[index_max+1:len(text)]
#
# print(first_part+second_part+last_part)