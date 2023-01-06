import time
import random
class Player:

    hunger = 50
    sleep = 50
    leisure = 50
    money = 0
    age = 5
    day = 360
    day_in_scool = 0
    chcoll_class = 1
    place_of_work = "Без работы"
    post = ""
    education = "Без образования"
    rep = 0
    car = "Без машины"
    home = "Живет с родителями"

    def __init__(self,name,country):
        self.name = name
        self.country = country

    def work(self):
        if self.place_of_work == "Без работы":
            if self.age >= 14 and self.age < 18:
                print("С 14 лет вам доступные работы:\nРазносить почту\nВыгул собак\nПромоутер")
                choice = input("Выберете профессию: ")
                if choice == "Разносить почту":
                    print("Обычный день, почтальона + 500 рублей")
                    self.money += 500
                    self.sleep -= 20
                elif choice == "Выгул собак":
                    print("Взял поводок, вывел собаку , завел домой и так целый день + 700 рублей")
                    self.money += 700
                    self.sleep -= 30
                elif choice == "Промоутер":
                    print("Стоял весь день у торгового центра + 400 рублей")
                    self.money += 400
                    self.sleep -= 10
                else:
                    print("не корректный ввод")
                    time.sleep(1)
                    self.work()

            elif self.age >= 18:
                print("С 18 лет вам доступны работы:\nПолиция\nВрач\nУчитель\nПожарный\nАртист\nДепутат")
                choice = input("Выберете профессию: ")
                if choice == "Полиция":
                    self.place_of_work = "Полиция"
                    self.post = "Рядовой"
                elif choice == "Врач":
                    self.place_of_work = "Больница"
                    self.post = 'Младший мед персонал'
                elif choice == "Учитель":
                    self.place_of_work = "Школа"
                    self.post = "Учитель начальных классов"
                elif choice == "Пожарный":
                    self.place_of_work = "Пожарная часть"
                    self.post = "Пожарный"
                elif choice == "Артист":
                    self.place_of_work = "Улица"
                    self.post = "Музыкант в переходе"
                elif choice == "Депутат":
                    if self.chcoll_class > 9 and self.age > 21:
                        self.place_of_work = "Местный отдел партии"
                        self.post = 'Помощьник депутата'
                    else:
                        print("Ты не можешь работать депутатом! не достаточно опыта")
                else:
                    print("Не корректный ввод")
                    time.sleep(1)
                    self.work()

            else:
                print("Ты еще слишком маленький")
        elif self.place_of_work == "Полиция":
            self.money += 1500
        elif self.place_of_work == "Врач":
            self.money += 1000
        elif self.place_of_work == "Учитель":
            self.money += 700
        elif self.place_of_work == "Пожарный":
            self.money += 1300
        elif self.place_of_work == "Артист":
            self.money += random.randint(1,4000)
        elif self.place_of_work == "Депутат":
            self.money += 5000
    def sleeping(self):
        pass

    def entertainment(self):
        pass

    def eat(self):
        pass

    def study(self):
        pass

    def shop(self):
        pass

    def print_info(self):
        print("\n"*50)
        print("Сытость: {}\nБодрость: {}\nДосуг: {}\nДеньги : {} рублей\nВозраст: {} лет"
              "\nДней прошло: {} день(ей)\nМесто работы: {}\nОброзование: {}\nРепутация: {}\nМашина: {}"
              "\nКвартира: {}".format(self.hunger,
                                      self.sleep,self.leisure,self.money,self.age,
                                      self.day,self.place_of_work,self.education,self.rep,self.car,self.home))
    def step_day(self):
        self.day += 1
        if self.day == 365:
            self.day = 1
            self.age += 1
            print("У тебя день рождения,пришли гости и принесли подарки")
            self.sleep += 100
            self.money += 5000
            self.hunger += 100
            self.leisure += 100

        self.sleep -= 10
        self.hunger -= 10
        self.leisure -= 10
    def step_chool(self):
        self.day_in_scool += 1

        if self.chcoll_class == 9 and self.age > 16:
            print("ты закончил 9 классов поздравляю")
            self.education = "Среднее не полное"

        elif self.day_in_scool == 15 and self.age == 8:
            self.day_in_scool = 1
            self.chcoll_class = 2

        elif self.day_in_scool == 15 and self.age == 9:
            self.day_in_scool = 1
            self.chcoll_class = 3

        elif self.day_in_scool == 15 and self.age == 10:
            self.day_in_scool = 1
            self.chcoll_class = 4

        elif self.day_in_scool == 15 and self.age == 11:
            self.day_in_scool = 1
            self.chcoll_class = 4

        elif self.day_in_scool == 15 and self.age == 12:
            self.day_in_scool = 1
            self.chcoll_class = 5

        elif self.day_in_scool == 15 and self.age == 13:
            self.day_in_scool = 1
            self.chcoll_class = 6

        elif self.day_in_scool == 15 and self.age == 14:
            self.day_in_scool = 1
            self.chcoll_class = 7

        elif self.day_in_scool == 15 and self.age == 15:
            self.day_in_scool = 1
            self.chcoll_class = 8

        elif self.day_in_scool == 15 and self.age == 16:
            self.day_in_scool = 1
            self.chcoll_class = 9

def choice_pl(name):
    time.sleep(1)
    print("\n"*3)
    choice = int(input("Выберете действие:\n1-Пойти поесть\n2-Пойти поспать\n3-Пойти гулять"
                       "\n4-Пойти учиться\n5-Пойти работать\n6-Пойти в магазин\n>>>"))
    if choice == 1:
        print("\n" * 3)
        if name.age < 18:
            print("Ты взял из холодильника родителей еду + 30 к сытости")
            name.hunger += 30
            time.sleep(2)
        else:
            print("Для того что бы поесть нужно заработать! еда стоит 300 рублей")
            if name.money >=300:
                print("Ты поел + 30 к сытости\nНо потратил 300 рублей")
                name.hunger += 30
                name.money -= 300
            else:
                print("Денег не хватило иди на работу")
        name.step_day()
        time.sleep(1)
        name.print_info()
        choice_pl(name)
    elif choice == 2:
        print("ТЫ пошел спать")
        name.sleep += 50
        name.step_day()
        time.sleep(1)
        name.print_info()
        choice_pl(name)

    elif choice == 3:
        print("Ты пошел на прогулку с друзьями")
        name.leisure += 60
        name.step_day()
        time.sleep(1)
        name.print_info()
        choice_pl(name)
    elif choice == 4:
        if name.age >= 7:
            if name.day_in_scool == 1 and name.chcoll_class == 1:
                print("Теперь ты можешь пойти учиться в первый класс!")
                name.step_chool()
            else:
                name.step_chool()


        name.step_day()
        time.sleep(1)
        name.print_info()
        choice_pl(name)
    elif choice == 5:
        name.work()
        name.step_day()
        time.sleep(1)
        name.print_info()
        choice_pl(name)
    elif choice == 6:
        name.step_day()
        time.sleep(1)
        name.print_info()
        choice_pl(name)
    else:
        print("Не корректный ввод")
        choice_pl(name)

def mainMenu(name,country):
    print("Добро пожаловать в симулятор жизни!")
    name = Player(name,country)
    name.print_info()
    time.sleep(3)
    print("\n"*15)
    choice_pl(name)

name = input("Введите имя вашего персонажа: ")
country = input("Введите старну рождения вашего персонажа: ")
mainMenu(name,country)