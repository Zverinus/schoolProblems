def main():
    x, y = int(input("x: ")), int(input("y: "))
    if x <= y <= 2 - x ** 2 and y >= 0:
        print("Принадлежит")
    else:
        print("Не принадлежит")


if __name__ == '__main__':
    main()
