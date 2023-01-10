# 1)
# Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за
# основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

# class Soup():
#     def __init__(self, main_ingredient):
#         self.main_ingredient = main_ingredient
#         self.soup_check = False
#
#     def show_my_soup(self):
#         if self.soup_check:
#             print(f'У вас получилcя отличный суп с {self.main_ingredient}')
#         else:
#             print('Это не суп, а простой кипяток!')
#
#     def check_on(self):
#         self.soup_check = True
#
# c = Soup('Кот')
# c.check_on()
# c.show_my_soup()

# 2)Нужно написать программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки

class Student_name:
    def __init__(self, name):
        self.name = name

    def students(self):

        self.name = input()

class Group:
    pass

class Grade:
    pass