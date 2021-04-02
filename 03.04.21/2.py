def main():
    num, value = int(input("Номер элемента: ")), int(input("Значение: "))
    if num == 1:
        c = value * 2 ** 0.5
        h = c / 2
        s = c * h / 2
        print(c, h, s)
    elif num == 2:
        a = value / 2 ** 0.5
        h = value / 2
        s = value * h / 2
        print(a, h, s)
    elif num == 3:
        c = value * 2
        a = c / 2 ** 0.5
        s = c * value / 2
        print(a, c, s)
    elif num == 4:
        h = value ** 0.5
        c = 2 * h
        a = c / 2 ** 0.5
        print(a, c, h)


if __name__ == '__main__':
    main()
