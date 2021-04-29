def to_base(num: int, base: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted_num = ""
    while num > 0:
        num, ind = divmod(num, base)
        converted_num += alphabet[ind]
    return converted_num[::-1]


nums = [i for i in range(1000, 10000) if len(to_base(i, 4)) == 6 and i % 3 != 0 and i % 17 != 0 and i % 19 != 0]
print(nums)
