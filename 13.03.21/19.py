def main():
    num = input()
    sums = sorted([str(int(num[i]) + int(num[i + 1])) for i in range(len(num) - 1)], key=lambda x: int(x), reverse=True)
    print(''.join(sums))


if __name__ == '__main__':
    main()
