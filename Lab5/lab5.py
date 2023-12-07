import random


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


def hero_creator(count):
    hero_list = list()
    for i in range(count):
        hero_list.append(Hero())
    return hero_list


def warrior_team_creator(count, hero_list):
    warrior_team_list = dict()
    for i in hero_list:
        warrior_team_list[i.unit_team_id] = list()

    for unit in range(count):
        hero = random.choice(hero_list)
        warrior = Warrior()
        warrior_team_list[hero.unit_team_id].append(warrior)
        hero.add_warrior_in_team(warrior)
    return warrior_team_list


def main_scenario():
    hero_list = hero_creator(3)
    warrior_team_list = warrior_team_creator(15, hero_list=hero_list)

    warrior_team_size_list = dict()
    for key, value in warrior_team_list.items():
        warrior_team_size_list[key] = len(value)

    max_team_size = max(warrior_team_size_list.values())
    for key, value in warrior_team_size_list.items():
        if value == max_team_size:
            hero_list[key].level_up(value)

    random.choice(warrior_team_list[0]).following_hero(hero_list[0])


if __name__ == '__main__':
    main_scenario()
