def main():
    description = ""
    num = int(input())
    if num == 0:
        description += "нулевое"
    elif num < 0:
        description += "отрицательное"
    else:
        description += "положительное"
    if num % 2 == 0 and num != 0:
        description += " четное"
    elif num % 2 == 1:
        description += " нечетное"
    description += " число"
    print(description)


if __name__ == '__main__':
    main()
