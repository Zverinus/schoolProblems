nums = list(filter(lambda x: sum([i for i in range(2, x // 2 + 1) if x % i == 0]) > 40 and x % 5 != 1, range(123, 1151)))
print(len(nums), nums[-1] - nums[0])
