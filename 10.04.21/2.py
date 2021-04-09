from typing import List


def find_prime_nums(start: int, end: int) -> List[int]:
    a = [0, 0] + [i for i in range(2, end + 1)]
    prime_nums = []
    i = 2
    while i <= end:
        if a[i] != 0:
            prime_nums.append(a[i])
            for j in range(i, end + 1, i):
                a[j] = 0
        i += 1
    ind = start
    while ind not in prime_nums:
        ind += 1
    return prime_nums[prime_nums.index(ind):]


def get_suitable(start: int, end: int) -> dict:
    result = {}
    prime_nums = find_prime_nums(2, end)
    for num in range(start, end + 1):
        for j in prime_nums:
            divisor = num / j
            if divisor < 2:
                break
            if int(divisor) == divisor:
                if int(divisor) in prime_nums and j != int(divisor):
                    result[num] = int(abs(j - divisor))
                    break
        print(result)
    return result


def main():
    suitable = get_suitable(int(input("Первое число: ")), int(input("Последнее число: ")))
    print(f"Кол-во подходящих чисел: {len(suitable)}")
    if suitable:
        print(min(suitable, key=lambda x: (-suitable[x], x)))


if __name__ == '__main__':
    main()
