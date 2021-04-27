nums = list(filter(lambda x: len([i for i in range(2, x // 2 + 1) if x % i == 0]) > 20, range(23561, 64355)))
print(len(nums), nums[0])
