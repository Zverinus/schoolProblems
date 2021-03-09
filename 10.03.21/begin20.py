def main():
    points = get_points(2, ['x', 'y'])
    print(f'Расстояние: {get_distance(*points):.2f}')


def get_points(number: int, letters: list) -> list:
    return [tuple(map(float, [input(f'Введите {letter}{num}: ')
                              for letter in letters])) for num in range(1, number + 1)]


def get_distance(point1: tuple, point2: tuple) -> float:
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


if __name__ == '__main__':
    main()
