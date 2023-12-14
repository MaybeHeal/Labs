import lab5_classes as l5c
import random


def hero_creator(count):
    hero_list = list()
    for i in range(count):
        hero_list.append(l5c.Hero())
    return hero_list


def warrior_team_creator(count, hero_list):
    warrior_team_list = dict()
    for i in hero_list:
        warrior_team_list[i.unit_team_id] = list()

    for unit in range(count):
        hero = random.choice(hero_list)
        warrior = l5c.Warrior()
        warrior_team_list[hero.unit_team_id].append(warrior)
        hero.add_warrior_in_team(warrior)
    return warrior_team_list


def main_scenario():
    hero_list = hero_creator(3)
    warrior_team_list = warrior_team_creator(15, hero_list=hero_list)

    for hero in hero_list:
        print(f'Численность команды Героя (id: {hero.unit_id}): {len(l5c.Unit.hero_team_list[hero.unit_team_id])}')

    warrior_team_size_list = dict()
    for key, value in warrior_team_list.items():
        warrior_team_size_list[key] = len(value)

    max_team_size = max(warrior_team_size_list.values())
    for key, value in warrior_team_size_list.items():
        if value == max_team_size:
            hero_list[key].level_up(value)

    random.choice(warrior_team_list[0]).following_hero(hero_list[0])


def hexagon_function(center: tuple, side: float, angle: int):
    hexagon = l5c.Hexagon()
    hexagon.set_coord(*center)
    hexagon.set_hex_side(side)
    hexagon.set_hex_angle(angle)
    print(f'Шестиугольник с центром в точке {hexagon.get_coord()}, стороной равной {hexagon.get_hex_side()} '
          f'и повёрнут относительно ценра на {hexagon.get_hex_angle()} градусов')


if __name__ == '__main__':
    main_scenario()
    hexagon_function(center=(4, 5), side=6, angle=45)
