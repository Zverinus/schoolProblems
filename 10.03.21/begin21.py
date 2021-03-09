from begin20 import get_points, get_distance
from functools import reduce


def main():
    points = get_points(3, ['x', 'y'])
    print(f'Площадь фигуры: {get_square(points)}')


def get_square(points: list) -> float:
    sides = [get_distance(points[i], points[i + 1]) for i in range(len(points) - 1)]\
            + [get_distance(points[0], points[-1])]
    semiperimeter = sum(sides) / 2
    return (semiperimeter * reduce(lambda x, y: x * y, [semiperimeter - side for side in sides])) ** 0.5


if __name__ == '__main__':
    main()
