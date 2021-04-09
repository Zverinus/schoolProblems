def get_suitable(start: int, end: int) -> dict:
    result = {}
    for i in range(start, end + 1):
        num = i
        divisors = []
        for j in range(2, i):
            divisor = num / j
            if divisor < 2:
                break
            if int(divisor) != divisor:
                continue
            else:
                if len(divisors) >= 3:
                    break
                else:
                    divisors.append(j)
                    num = divisor
        if len(divisors) == 3:
            result[i] = max(divisors)
    return result


def main():
    suitable = get_suitable(int(input("Первое число: ")), int(input("Последнее число: ")))
    print("\n".join([f"{key}: {value}" for key, value in suitable.items()]))


if __name__ == '__main__':
    main()
