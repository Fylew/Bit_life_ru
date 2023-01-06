import time
class Player:

    hunger = 50
    sleep = 50
    leisure = 50
    money = 0
    age = 5
    day = 1
    day_in_scool = 0
    chcoll_class = 1
    place_of_work = "Без работы"
    education = "Без образования"
    rep = 0
    car = "Без машины"
    home = "Живет с родителями"

    def __init__(self,name,country):
        self.name = name
        self.country = country

    def work(self):
        if self.place_of_work == "Без работы":
            if self.age == 14:
                print("С 14 лет вам доступные работы:\nРазносить почту\nВыгул собак\nПромоутер")
            elif self.age == 18:
                print("С 18 лет вам доступны работы:\nПолиция\nВрач\nУчитель\nПожарный\nАртист\nДепутат")
        else:
            self.money += 1000

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
              "\nДней прошло: {}день(ей)\nМесто работы: {}\nОброзование: {}\nРепутация: {}\nМашина: {}"
              "\nКвартира: {}".format(self.hunger,
                                      self.sleep,self.leisure,self.money,self.age,
                                      self.day,self.place_of_work,self.education,self.rep,self.car,self.home))
    def step_day(self):
        self.day += 1
        if self.day == 365:
            self.day = 1
            self.age += 1
        self.sleep -= 20
        self.hunger -= 10
        self.leisure -= 10

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
        name.print_info()
        choice_pl(name)
    elif choice == 2:
        print("ТЫ пошел спать")
        name.sleep += 50
        name.step_day()
        name.print_info()
        choice_pl(name)
    elif choice == 3:
        print("Ты пошел на прогулку с друзьями")
        name.leisure += 30
        name.step_day()
        name.print_info()
        choice_pl(name)
    elif choice == 4:
        if name.age > 6:
            if name.day_in_scool == 1 and name.chcoll_class == 1:
                print("Теперь ты можешь пойти учиться в первый класс!")
                

        name.step_day()
        name.print_info()
        choice_pl(name)
    elif choice == 5:
        name.step_day()
        name.print_info()
        choice_pl(name)
    elif choice == 6:
        name.step_day()
        name.print_info()
        choice_pl(name)
    else:
        print("Не корректный ввод")
        choice_pl(name)

def mainMenu():
    print("Добро пожаловать в симулятор жизни!")
    name = input("Введите имя вашего персонажа: ")
    country = input("Введите старну рождения вашего персонажа: ")
    name = Player(name,country)
    name.print_info()
    time.sleep(3)
    print("\n"*15)
    choice_pl(name)

mainMenu()