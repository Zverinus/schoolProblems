nums = [i for i in range(2495, 7084) if hex(i)[-2:] in ('1a', '1f') and i % 5 != 0 and i % 9 != 0]
print(len(nums), nums[0])
