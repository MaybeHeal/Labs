from classes import *


def task():
    worker1 = Employee('Олег', 'Иванович', 39)
    dep1 = Department('Отдел печати', 'Подготовка и печать бумажной продукции')
    worker2 = Employee('Максим', 'Владимирович', 27, department_id=dep1.id)
    worker1.add_in_department(dep1.id)
    ed1 = Edition('Программирование на Python', 10000, 250)
    print(worker1)
    print(worker2)
    print(dep1)
    print(ed1)


if __name__ == '__main__':
    task()
