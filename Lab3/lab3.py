import random
import string
import pickle


def string_generator():
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(489))
    return random_string


def task1():
    with open('task1.txt', mode='w', encoding='utf-8') as file:
        file.write(string_generator())

    try:
        with open('task1.txt', mode='r', encoding='utf-8') as file:
            copied_string = ''
            k = ' '
            while k != '':
                k = file.read(100)
                copied_string += k
    except FileNotFoundError:
        print("Невозможно открыть файл")

    with open('copied_file.txt', mode='w', encoding='utf-8') as file:
        file.write(copied_string)


def task2():
    this_is_string = input('Введите любое предложение:')
    separated_string = this_is_string.split(' ')
    with open('task2.txt', mode='w+', encoding='utf-8') as file:
        file.writelines(f'{word}\n' for word in separated_string)


def task3():
    d = {"house": "дом", "car": "машина",
         "tree": "дерево", "road": "дорога",
         "river": "река"}
    with open('task3.bin', mode='wb') as file:
        for key in d:
            pickle.dump((key, d[key]), file)

    with open('task3.bin', mode='rb') as file:
        # Не очень понял как мне определить точку выхода из цикла в бинарном виде,
        # поэтому просто по ошибке вылетаем с цикла, знаю что не правильно написано, но работает
        try:
            while True:
                a = pickle.load(file)
                print(a)
        except:
            pass


if __name__ == '__main__':
    task1()
    task2()
    task3()
    # Задание 4 в lab2.py
