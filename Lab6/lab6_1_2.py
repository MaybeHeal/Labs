class SuperStr(str):
    def is_repeatance(self, string):
        if str == type(string):
            string_set = {self[i:i + len(string)] for i in range(0, len(self), len(string))}
            if len(string_set) == 1 and list(string_set)[0] == string:
                return True
            else:
                return False
        else:
            return False

    def is_palindrom(self):
        if self == self[::-1]:
            return True
        else:
            return False


def task():
    s = SuperStr('123123123123')
    print(s.is_repeatance('123'))  # True
    print(s.is_repeatance('123123'))  # True
    print(s.is_repeatance('123123123123'))  # True
    print(s.is_repeatance('12312'))  # False
    print(s.is_repeatance(123))  # False
    print(s.is_palindrom())  # False
    print(s)  # 123123123123 (строка)
    print(int(s))  # 123123123123 (целое число)
    print(s + 'qwe')  # 123123123123qwe
    p = SuperStr('123_321')
    print(p.is_palindrom())  # True


if __name__ == '__main__':
    task()
