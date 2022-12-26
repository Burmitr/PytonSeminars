# nums = []
# n = 10
# for i in range(n):
#     if i % 2 == 0:
#         nums.append(i**3)
#
# print(nums)
#
# n = 10
# nums = [x**3 for x in range(n) if x % 2 == 0]
# print(nums)


# Задача написать программу игры "Камень - ножницы - бумага"

# from random import randint
# list1 = {1: "Камень", 2:"Ножницы", 3:"Бумага"}
#
# while True:
#     player = int(input('1 - Камень, 2 - Ножницы, 3 - Бумага. Выберите вариант хода: '))
#     if player == 0:
#         break
#     else:
#         comp_choice = randint(1, 3)
#         print(comp_choice)
#         if player == comp_choice:
#             print('Draw!')
#         elif player == 1 and comp_choice == 2 or player == 3 and comp_choice == 1 or player == 2 and comp_choice == 3:
#             print ('You win!!!')
#         else:
#             print('Вы проиграли!((((' )


