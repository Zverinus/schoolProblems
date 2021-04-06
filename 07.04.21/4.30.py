from math import prod


def main():
    num = input("Введите число: ")
    digit_sum = sum(map(int, list(num)))
    print("Сумма цифр является двузначным числом" if len(str(digit_sum)) == 2
          else "Сумма цифр не является двузначным числом")
    digit_prod = prod(map(int, list(num)))
    print("Произведение цифр является трехзначным числом" if len(str(digit_prod)) == 3
          else "Произведение цифр не является трехзначным числом")
    print("Произведение цифр больше самого числа" if digit_prod > int(num)
          else "Произведение цифр меньше самого числа")
    print("Сумма цифр кратна 5" if digit_sum % 5 == 0 else "Сумма цифр не кратна 5")
    print("Сумма цифр кратна самому числу" if digit_sum % int(num) == 0 else "Сумма цифр не кратна самому числу")


if __name__ == '__main__':
    main()
