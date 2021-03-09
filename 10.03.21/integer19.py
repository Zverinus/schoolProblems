def main():
    n = int(input())
    print(f"Кол-во полных минут: {n // 60 % 1440}")


if __name__ == '__main__':
    main()
