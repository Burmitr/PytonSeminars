# 3.1 Вводим с клавиатуры десятичное число. Необходимо перевести его в двоичную систему счисления.

# num = int(input('Введите число: '))
#
# def to_binary(num):
#     ans = ''
#     while num > 0:
#         help = num % 2
#         ans = str(help) + ans
#         num //=2
#     return ans
#
# print(to_binary(num))

# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.

# def count_letters(txt: str):
#     txt = txt.strip() # убираем пробелы в тексте
#     count_vowels = 0 # счетчик гласных
#     count_consonants = 0 # счетчик согласных
#
#     for i in 'a', 'o', 'i', 'u', 'e':
#         count_vowels += txt.count(i) # txt.count(i) ищет количество вхождений
#
#     count_consonants = len(txt) - count_vowels
#
#     print('vowels= ', count_vowels)
#     print('consonants', count_consonants)
#
# s = input('Введите текст: ')
# count_letters(s)


# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом

# string = input('Введите слово: ')
# string = string.lower() # делаем строку малого регистра
# newString = ''
#
# for i in range(len(string)-1, -1, -1):
#     newString += string[i]
#
# if string == newString:
#     print('Это палиндром!')
# else:
#    print('Это не палиндром!')


# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами

#a = ''
# b = ''
#
# text = input('Введите текст: ')
# dlina = len(text)
#
# a = text[0:dlina//2]
# b = text[(dlina//2):dlina]
#
# print(b+a)


# TODO дорешать
# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре




# 3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать - безопасный он или нет. Безопасным считается, если он от 8 символов, есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы




# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего




# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
