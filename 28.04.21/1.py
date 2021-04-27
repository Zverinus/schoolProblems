def to_base(num: int, base: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted_num = ""
    while num > 0:
        num, ind = divmod(num, base)
        converted_num += alphabet[ind]
    return converted_num[::-1]


nums = [i for i in range(3712, 8433) if bin(i)[-1] == to_base(i, 4)[-1] and (i % 13 == 0 or i % 14 == 0 or i % 15 == 0)]
print(len(nums), nums[0])
