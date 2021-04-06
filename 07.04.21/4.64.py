def main():
    num = input("Введите число: ")
    print("Число счастливое" if sum(map(int, list(num[:3]))) == sum(map(int, list(num[-3:]))) else "Число несчастливое")


if __name__ == '__main__':
    main()
