def main():
    coefficients = get_coefficients(2, ['A', 'B', 'C'])
    d = coefficients[0][0] * coefficients[1][1] - coefficients[1][0] * coefficients[0][1]
    try:
        print(f"x = {get_x(coefficients, d):.2f}\ny = {get_y(coefficients, d):.2f}")
    except ZeroDivisionError:
        print('Неверные коэффициенты!')


def get_coefficients(number: int, letters: list) -> list:
    return [tuple(map(float, [input(f'Введите {letter}{num}: ')
                              for letter in letters])) for num in range(1, number + 1)]


def get_x(coefficients: list, d: float) -> float:
    return (coefficients[0][2] * coefficients[1][1] - coefficients[1][2] * coefficients[0][2]) / d


def get_y(coefficients: list, d: float) -> float:
    return (coefficients[0][0] * coefficients[1][2] - coefficients[1][0] * coefficients[0][2]) / d


if __name__ == '__main__':
    main()
