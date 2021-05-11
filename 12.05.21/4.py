nums = [i for i in range(1871, 9198) if i % 9 in (2, 4) and len(str(i)) != len(hex(i)) - 2]
print(len(nums), nums[0])
