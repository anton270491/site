print ("Привет, перед вами проект №7 (угадай чисто от 1 до 50) 'Путь к успеху'!")

"""импортируем модуль, который будет имитировать вашего противника — им станет компьютер"""
import random

while True:
    """ любая переменная = range (50) - эта функция даём возможность модую random выбрать любое случайное число от 0 до 50"""
    possible_actions = range(50)
    number = random.choice(possible_actions)

    while True:
        user = int(input("Угадайте число от 0 и до 50 : "))

        if user == number:
            print("Вы угадали! Поздравляю Вас!")
            break
        if user < number:
            print ("выше")
        if user > number:
            print("ниже")

    q = str(input("Сыграем ещё разок? (да\нет) : "))
    if q == "да":
        print("Ура!!!! Мы будем играть ещё!!!")
    else:
        print("Ну и ладно, бог вам судья!")
        break
