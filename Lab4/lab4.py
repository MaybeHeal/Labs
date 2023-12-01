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

    def fire_person(self):
        print(self.__first_name, self.__second_name, 'вы уволены')
        self.__del__()


def persons():
    person1 = Person('Вася', 'Пупкин', 3)
    person2 = Person('Гадя', 'Петрович', 1)
    person3 = Person('Олег', 'Иванов', 2)
    person_list = [person1, person2, person3]
    person_qualification_list = []
    for person in person_list:
        person_qualification_list.append(person.person_qualification)
    for key, qualification in enumerate(person_qualification_list):
        if qualification == min(person_qualification_list):
            person_list[key].fire_person()
    input('Нажмите Enter для продолжения')


# Задание 4:
class TriangleChecker:
    def __init__(self):
        self.__side_a = 0
        self.__side_b = 0
        self.__side_c = 0

    def is_triangle(self):
        ab_sum = self.__side_a + self.__side_b
        bc_sum = self.__side_b + self.__side_c
        ca_sum = self.__side_c + self.__side_c
        if ab_sum > self.__side_c and bc_sum > self.__side_a and ca_sum > self.__side_b:
            print('Ура, можно построить треугольник!')
        else:
            print('Жаль, но из этого треугольник не сделать.')

    @property
    def side_a_value(self):
        return self.__side_a

    @side_a_value.setter
    def side_a_value(self, count):
        while True:
            try:
                if float(count) < 0:
                    print('С отрицательными числами ничего не выйдет!')
                else:
                    self.__side_a = float(count)
                    break
            except:
                print('Нужно вводить только числа!')
            count = input('Введите длину стороны a: ')

    @property
    def side_b_value(self):
        return self.__side_b

    @side_b_value.setter
    def side_b_value(self, count):
        while True:
            try:
                if float(count) < 0:
                    print('С отрицательными числами ничего не выйдет!')
                else:
                    self.__side_b = float(count)
                    break
            except:
                print('Нужно вводить только числа!')
            count = input('Введите длину стороны b: ')

    @property
    def side_c_value(self):
        return self.__side_c

    @side_c_value.setter
    def side_c_value(self, count):
        while True:
            try:
                if float(count) < 0:
                    print('С отрицательными числами ничего не выйдет!')
                else:
                    self.__side_c = float(count)
                    break
            except:
                print('Нужно вводить только числа!')
            count = input('Введите длину стороны c: ')


def dose_a_triangle_exist():
    triangle = TriangleChecker()

    triangle.side_a_value = input('Введите длину стороны a: ')
    triangle.side_b_value = input('Введите длину стороны b: ')
    triangle.side_c_value = input('Введите длину стороны c: ')

    triangle.is_triangle()


if __name__ == '__main__':
    give_me_a_soda()
    warrior_fight()
    persons()
    dose_a_triangle_exist()
