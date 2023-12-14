class Nikola:
    def __init__(self, name, age):
        self.__firstname = 'Николай'
        if name.title() != 'Николай':
            self.__firstname = f'Я не {name.title()}, а Николай'
        self.__age = age

    def __setattr__(self, key, value):
        if key.split('_Nikola')[-1] not in ['__firstname', '__age']:
            print(f'Невозможно создать атрибут {key}')
        else:
            object.__setattr__(self, key, value)

    def __str__(self):
        return f'Имя: {self.__firstname}; Возраст: {self.__age}'


class RealString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        res = 0
        if isinstance(other, RealString):
            res = len(other.string)
        elif isinstance(other, str):
            res = len(other)
        return len(self.string) == res

    def __lt__(self, other):
        res = 0
        if isinstance(other, RealString):
            res = len(other.string)
        elif isinstance(other, str):
            res = len(other)
        return len(self.string) < res

    def __le__(self, other):
        res = 0
        if isinstance(other, RealString):
            res = len(other.string)
        elif isinstance(other, str):
            res = len(other)
        return len(self.string) <= res


def task_nikola():
    a = Nikola('николай', 12)
    b = Nikola('Крокозябра', 454)
    a.ff = 123
    print(f'{a}\n{b}')


def task_real_string():
    s1 = RealString('qwer')
    s2 = RealString('reqw2')
    s3 = 'qwere'
    print(s1 == s2)
    print(s1 <= s2)
    print(s1 < s2)
    print(s1 == s3)
    print(s1 <= s3)
    print(s1 < s3)


if __name__ == '__main__':
    task_nikola()
    task_real_string()
