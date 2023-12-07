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


def hexagon_function(center: tuple, side: float, angle: int):
    hexagon = Hexagon()
    hexagon.set_coord(*center)
    hexagon.set_hex_side(side)
    hexagon.set_hex_angle(angle)
    print(f'Шестиугольник с центром в точке {hexagon.get_coord()}, стороной равной {hexagon.get_hex_side()} '
          f'и повёрнут относительно ценра на {hexagon.get_hex_angle()} градусов')


if __name__ == '__main__':
    hexagon_function(center=(4, 5), side=6, angle=45)
