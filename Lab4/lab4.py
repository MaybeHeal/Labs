import random


# Задание 1
class Soda:
    def __init__(self, supplement):
        self.supplement = supplement

    def show_my_drink(self):
        if self.supplement == '':
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.supplement}')


def give_me_a_soda():
    supplement = input('Выберите добавку, если необходимо: ')
    my_soda = Soda(supplement=supplement)
    my_soda.show_my_drink()


# Задание 2
class Warrior:
    def __init__(self, name='Иван'):
        self.__name = name
        self.__health = 100

    def take_damage(self):
        self.warrior_health = self.warrior_health - 20
        print(f'Воин {self.__name} получил 20 урона')

    @property
    def warrior_health(self):
        return self.__health

    @warrior_health.setter
    def warrior_health(self, count):
        self.__health = count

    @property
    def warrior_name(self):
        return self.__name

    @warrior_name.setter
    def warrior_name(self, name):
        self.__name = name


def warrior_fight():
    warrior1 = Warrior('Вяся')
    warrior2 = Warrior('Олег')
    while True:
        warrior = random.choice([warrior1, warrior2])
        warrior.take_damage()
        print(f'Воин {warrior.warrior_name} имеет {warrior.warrior_health} здоровья')
        if warrior.warrior_health == 0:
            print(f'Воин {warrior.warrior_name} проиграл')
            break


# Задание 3:
class Person:
    def __init__(self, first_name, second_name, qualification=1):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__qualification = qualification

    def __del__(self):
        print(f'До свидания, мистер {self.__first_name} {self.__second_name}')

    def person_info(self):
        return f'Имя специалиста: {self.__first_name} {self.__second_name}\nКвалификация: {self.person_qualification}'

    @property
    def person_qualification(self):
        return self.__qualification

    @person_qualification.setter
    def person_qualification(self, count):
        self.__qualification = count


# def persons():
#     person1 = Person('Вася', 'Пупкин', 3)
#     person2 = Person('Гадя', 'Петрович', 1)
#     person3 = Person('Олег', 'Молодой', 2)
#     person_list = [person1.person_qualification, person2.person_qualification, person3.person_qualification]
#     print(min(enumerate(person_list)))
#     input()


if __name__ == '__main__':
    give_me_a_soda()
    warrior_fight()
    # persons()
