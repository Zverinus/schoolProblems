nums = list(filter(lambda x: len([i for i in range(2, x // 2 + 1) if x % i == 0]) > 15, range(12356, 76436)))
print(len(nums), nums[-1])
