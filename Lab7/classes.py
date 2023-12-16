from db import DataBase


class Employee:
    table = 'employee'

    def __init__(self, firstname: str, secondname: str, age: int, department_id: int = None):
        self.firstname = firstname
        self.secondname = secondname
        self.age = age
        self.department_id = department_id
        self.id = DataBase().add_item(self.table, ('firstname', 'secondname', 'age'),
                                      (self.firstname, self.secondname, self.age))
        if self.department_id is not None:
            self.add_in_department(self.department_id)

    def __str__(self):
        emp = DataBase().get_item(self.table, self.id)
        return (f'id: {emp['id']}, Имя: {emp['firstname']}, Фамилия: {emp['secondname']}, Возраст: {emp['age']}, '
                f'Отдел: {self.department_id}')

    def add_in_department(self, department_id: int):
        self.department_id = department_id
        db = DataBase()
        db.update_item(self.table, self.id, 'department_id', self.department_id)
        Department.update_employee_number()


class Department:
    table = 'department'

    def __init__(self, department_name: str, direction: str):
        self.department_name = department_name
        self.direction = direction
        self.employee_number = 0
        self.id = DataBase().add_item(self.table, ('department_name', 'direction', 'employee_number'),
                                      (self.department_name, self.direction, self.employee_number))

    @classmethod
    def update_employee_number(cls):
        db = DataBase()
        deps = db.get_all_items(cls.table)
        for item in deps:
            emp_count = db.get_item_count(Employee.table, 'department_id', item['id'])
            db.update_item(cls.table, item['id'], 'employee_number', emp_count)

    def __str__(self):
        dep = DataBase().get_item(self.table, self.id)
        return (f'id: {dep['id']}, Отдел: {dep['department_name']}, Направление: {dep['direction']}, '
                f'Количество сотрудников: {dep['employee_number']}')


class Edition:
    table = 'edition'

    def __init__(self, title: str, circulation: int, page_count: int):
        self.title = title
        self.circulation = circulation
        self.page_count = page_count
        self.id = DataBase().add_item(self.table, ('title', 'circulation', 'page_count'),
                                      (self.title, self.circulation, self.page_count))

    def __str__(self):
        ed = DataBase().get_item(self.table, self.id)
        return (f'id: {ed['id']}, Название: {ed['title']}, Тираж: {ed['circulation']}, '
                f'Количество страниц: {ed['page_count']}')


if __name__ == '__main__':
    pass
