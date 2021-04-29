def to_base(num: int, base: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted_num = ""
    while num > 0:
        num, ind = divmod(num, base)
        converted_num += alphabet[ind]
    return converted_num[::-1]


nums = [i for i in range(int('1000000', 7), int('6666666', 7)) if to_base(i, 3)[-1] == '2'
        and to_base(i, 8)[-1] != '3' and to_base(i, 12) != '5']
print(len(nums), nums[-1])
