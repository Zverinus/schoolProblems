from math import ceil


def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, ceil(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


array = [int(input()) for i in range(20)]
new_array = [i for i in array if is_prime(i)]

print(new_array)
