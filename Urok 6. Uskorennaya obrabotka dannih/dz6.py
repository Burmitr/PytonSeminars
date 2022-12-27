# 1) Сделать Предыдущее ДЗ с использование функций
# Я сделал 5-е дз на основе функций


# 2*) Сделать поле чудес . Компьютер загадывает слово. А мы его угадываем. Делаем с помощью функций.
# Кто хочет посложней - добавляем очки и барабан.

import random
from random import randint

words = ['черепаха', 'бисер', 'манишка']
questions = ['Какое животное дало название распространенному в Древнем Риме способу боевого построения?',
             'Предмет, совершенно не интересующий свиней?',
             'Как называется белый нагрудник на мужской сорочке?']
result = False
question = 0

def computer_question(): #генерируем вопрос компьютера из списка questions
    global question
    question = random.randint(0, len(questions)-1)
    print(questions[question])
    for i in range(0, len(words[question])):
        i = '*'
        print(i, end=' ')
    return question

def participant_response(): #запрашиваем ответ пользователя, сравниваем с выбором компьютера
    while result == False:
        answer = input('Введите ваш ответ с маленькой буквы: ')
        if answer != words[question]:
            print('Подумайте ещё!')
        else:
            print('Вы абсолютно правы!')
            return result == True

computer_question()
print("\n")
participant_response()