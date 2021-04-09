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


def main():
    print("\n".join([f"{i + 1}. {j}" for i, j in enumerate(find_prime_nums(int(input("Первое число: ")),
                                                                           int(input("Последнее число: "))))]))


if __name__ == '__main__':
    main()
