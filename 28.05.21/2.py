def to_base(num: int, base: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted_num = ""
    while num > 0:
        num, ind = divmod(num, base)
        converted_num += alphabet[ind]
    return converted_num[::-1]


num = to_base(7 ** 2 + 49 ** 4 - 21, 14)
print(num.count('A'), num.count('0'))
