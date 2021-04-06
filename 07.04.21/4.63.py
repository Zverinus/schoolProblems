def main():
    num = input("Введите число:")
    print("Все цифры числа различны" if len(set(num)) == len(num) else "Не все цифры различны")


if __name__ == '__main__':
    main()
