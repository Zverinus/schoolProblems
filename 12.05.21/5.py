nums = list(filter(lambda x: len([i for i in range(2, x // 2 + 1) if x % i == 0]) > 25, range(35612, 57355)))
print(len(nums), nums[0])
