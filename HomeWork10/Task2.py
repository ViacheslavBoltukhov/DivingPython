'''
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
одиночестве, Артём решил провести необычное исследование. Для этого он
реализовал модель человека и модель дома.
Человек может (должны быть такие методы):
● есть (+ сытость, − еда);
● работать (− сытость, + деньги);
● играть (− сытость);
● ходить в магазин за едой (+ еда, − деньги);
● прожить один день (выбирает одно действие согласно описанному ниже
приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):
● имя,
● степень сытости (изначально 50),
● дом.
В доме есть:
● холодильник с едой (изначально 50 еды),
● тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.
Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6.
2. Если сытость < 20, то нужно поесть.
3. Иначе, если еды в доме < 10, то сходить в магазин.
4. Иначе, если денег в доме < 50, то работать.
5. Иначе, если кубик равен 1, то работать.
6. Иначе, если кубик равен 2, то поесть.
7. Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.
Реализуйте такую программу и создайте двух людей, живущих в одном доме.
Проверьте работу программы несколько раз.
'''

import random


class Human:
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety

    def eat(self):
        self.satiety += 10
        print(f'{self.name} поел. Сытость: {self.satiety}')

    def work(self):
        self.satiety -= 10
        print(f'{self.name} поработал. Сытость: {self.satiety}')

    def play(self):
        self.satiety -= 10
        print(f'{self.name} поиграл. Сытость: {self.satiety}')


class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def buy_food(self):
        self.food += 10
        self.money -= 10
        print('Куплена еда')

    def earn_money(self):
        self.money += 10
        print('Заработаны деньги')


human1 = Human('Максим')
human2 = Human('Артем')
house = House()

for day in range(1, 366):
    print(f'\nДень {day}:')
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)

    if human1.satiety < 20:
        human1.eat()
    elif house.food < 10:
        house.buy_food()
    elif house.money < 50:
        house.earn_money()
    elif number1 == 1:
        human1.work()
    elif number1 == 2:
        human1.eat()
    else:
        human1.play()

    if human2.satiety < 20:
        human2.eat()
    elif house.food < 10:
        house.buy_food()
    elif house.money < 50:
        house.earn_money()
    elif number2 == 1:
        human2.work()
    elif number2 == 2:
        human2.eat()
    else:
        human2.play()

    if human1.satiety <= 0 and human2.satiety <= 0:
        print('Оба умерли от голода.')
        break
    elif human1.satiety <= 0:
        print(f'{human1.name} умер от голода.')
        break
    elif human2.satiety <= 0:
        print(f'{human2.name} умер от голода.')
        break