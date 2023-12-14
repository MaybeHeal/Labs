class Unit:
    unit_list = dict()
    hero_team_list = dict()

    def __init__(self):
        self.__u_id = 0
        self.__team_id = None
        if self.__u_id in Unit.unit_list:
            self.__u_id = max(Unit.unit_list.keys()) + 1
            Unit.unit_list[self.__u_id] = self
        else:
            Unit.unit_list[self.__u_id] = self

    @property
    def unit_id(self):
        return self.__u_id

    @property
    def unit_team_id(self):
        return self.__team_id

    @unit_team_id.setter
    def unit_team_id(self, count):
        self.__team_id = count


class Hero(Unit):
    def __init__(self):
        super().__init__()
        self.__lvl = 0
        self.unit_team_id = 0
        if self.unit_team_id in Unit.hero_team_list:
            self.unit_team_id = max(Unit.hero_team_list.keys()) + 1
            Unit.hero_team_list[self.unit_team_id] = [self]
        else:
            Unit.hero_team_list[self.unit_team_id] = [self]

    @property
    def level(self):
        return self.__lvl

    @level.setter
    def level(self, count):
        self.__lvl = count

    def level_up(self, count):
        self.__lvl += count
        print(f'Уровень Героя (id: {self.unit_id}) повышен до {self.level}')

    def add_warrior_in_team(self, warrior):
        Unit.hero_team_list[self.unit_team_id].append(warrior)
        warrior.unit_team_id = self.unit_team_id

    def team_size(self):
        return len(Unit.hero_team_list[self.unit_team_id])


class Warrior(Unit):
    def following_hero(self, hero):
        if hero.unit_team_id == self.unit_team_id:
            print(f'Воин (id: {self.unit_id}) следует за Героем (id: {hero.unit_id})')
        else:
            print('Данные юниты находятся в разных командах')


class Dot:
    coord = (0, 0)

    def set_coord(self, x, y):
        self.coord = (x, y)

    def get_coord(self):
        return self.coord

    def get_x(self):
        return self.coord[0]

    def get_y(self):
        return self.coord[1]


class Side(Dot):
    a = 0

    def set_hex_side(self, count):
        self.a = count

    def get_hex_side(self):
        return self.a


class Hexagon(Side):
    hex_angle = 0

    def set_hex_angle(self, count):
        self.hex_angle = count

    def get_hex_angle(self):
        return self.hex_angle
