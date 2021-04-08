def main():
    print(f'Кол-во четных цифр: {len(list(filter(lambda x: int(x) % 2 == 0, input("Введите число: "))))}')


if __name__ == '__main__':
    main()
