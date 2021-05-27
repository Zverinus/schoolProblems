def to_base(num: int, base: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted_num = ""
    while num > 0:
        num, ind = divmod(num, base)
        converted_num += alphabet[ind]
    return converted_num[::-1]


nums = {base: len([i for i in to_base(456, base) if int(i) % 2 != 0]) for base in range(2, 11)}
print(max(nums, key=lambda x: (nums[x], x)))
